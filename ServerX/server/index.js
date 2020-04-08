const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// import * as sens from './pyths/sensory.js'

const app = express();

app.use(bodyParser.json());
app.use(cors());

const sensor = require('./routes/sensor');

app.use('/',sensor);

if(process.env.NODE_ENV == 'production'){
    app.use(express.static(__dirname + '/public'));

    app.get(/.*/,(req,res) => res.sendFile(__dirname + '/public/index.html'));
}

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});