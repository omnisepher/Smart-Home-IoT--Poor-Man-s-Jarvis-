// const rpio = require('rpio');
// rpio.open(7,rpio.OUTPUT,rpio.LOW);
// console.log("Pin 7 is currently " + (rpio.read(7) ? 'high' : 'low'));


// for(var i=0;i<5;i++){
//     console.log('lel');
//     rpio.write(7,rpio.HIGH);
//     rpio.sleep(1);

//     rpio.write(7,rpio.LOW);
//     rpio.msleep(500);
// }
let {
    PythonShell
} = require('python-shell')

var temperature = 0;
var humidity = 0;

PythonShell.run('dht22.py', null, (err, results) => {
    if (err) throw err;
    temperature = results[0];
    humidity = results[1];
    console.log('Temperature is ' + temperature + ' Celcius and Humidity is ' + humidity + '%');
})


console.log('Temperature is ' + temperature + ' Celcius and Humidity is ' + humidity + '%');