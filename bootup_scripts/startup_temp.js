var sys = require('sys')
var exec = require('child_process').exec;

function puts(error, stdout, stderr) { sys.puts(stdout) }

var recursive = function () {
    exec("python /home/root/sensor_development/Archive/run_temp_v2.py temp_ed<board #> status_ed1 edison<board #> 1 3 300", puts);
    console.log("Updating Temperature at:");
    var date = new Date();
    console.log(date);
    setTimeout(recursive, 900000);
}
recursive();

##used to be 12 60 900000, no Archive, run_temp_v3.py
