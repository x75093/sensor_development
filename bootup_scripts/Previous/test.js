const exec = require('child_process').exec;
const child = exec('python /home/root/executable/sensor_development/run_temp_v1.py temperature status_table board12 5',
		    setInterval(function() {console.log("Hello");}, 1000),	
    function(error, stdout, stderr) {
        console.log("Script Executed")
	console.log("Updating temperature")
	if (error !== null) {
            console.log("Error");
        }
});
