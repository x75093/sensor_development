var sys = require('sys')
var exec = require('child_process').exec;

function puts(error, stdout, stderr) { sys.puts(stdout) }

var recursive = function () {
    exec("python /home/root/sensor_development/run_temp_v3.py temp_ed<board #> status_ed1 edison<board #> 12 60", puts);
    console.log("Updating Temperature at:");
    var date = new Date();
    console.log(date);
    setTimeout(recursive, 900000);
}
recursive();
