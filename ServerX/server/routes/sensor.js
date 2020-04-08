const express = require('express');
const mongodb = require('mongodb');
const axios = require('axios');

const router = express.Router();

const uri = "mongodb+srv://serverxadmin:789789@serverx-95ayk.mongodb.net/test?retryWrites=true"
const pyURL = 'http://127.0.0.1:5555'


// router.get('/', async (req,res) => {
//     const conn = await conndb("test");
//     res.send(await conn.find({}).toArray());
// });

//  Temperature and Humidity
router.get('/TAH', async (req, res) => {
    await axios.get(pyURL.concat("/TAH")).then((response) => {
        // console.log(`Humidity ${hum} and Temperature ${temp}`);
        res.status(201).send(response.data);
    })
});

router.post('/TAH', async (req, res) => {
    await axios.post(pyURL.concat("/TAH"),{
        "set" : req.body.comm
    }).then((response) => {
        res.status(201).send(response.data);
    })
});

//  Gas 
router.get('/gas', async (req, res) => {
    await axios.get(pyURL+"/gas").then((response) => {
        // console.log(response);
        res.status(201).send(response.data);
    })
});

router.post('/gas', async (req, res) => {
    await axios.post(pyURL.concat("/gas"), {
        "set": req.body.comm
    }).then((response) => {
        res.status(201).send(response.data);
    })
});

//  Light
router.get('/light', async (req, res) => {
    await axios.get(pyURL + "/light").then((response) => {
        // console.log(response);
        res.status(201).send(response.data);
    })
});

router.post('/light', async (req, res) => {
    await axios.post(pyURL.concat("/light"), {
        "set": req.body.comm,
        "auto": req.body.auto,
        "thresh": req.body.thresh
    }).then((response) => {
        res.status(201).send(response.data);
    })
});



router.post('/', async (req,res) => {
    const conn = await conndb("test");
    await conn.insertOne({
        temp: req.body.temp,
        light: req.body.light,
        gas: req.body.gas,
        created: new Date()
    });
    res.status(201).send();
})

async function conndb(coll){
    const client = await mongodb.MongoClient.connect(uri,{useNewUrlParser:true});

    return client.db('serverHome').collection(coll);
}

module.exports = router;