var sys = require('sys')
var exec = require('child_process').exec;

function puts(error, stdout, stderr) { sys.puts(stdout) }

var recursive = function () {
    exec("python /home/root/executable/sensor_development/run_temp_v2.py temp_board12 status_board12 board12 1 1 1", puts);
    console.log("Updating Temperature at:");
    var date = new Date();
    console.log(date);
    setTimeout(recursive, 15000);
}
recursive();
