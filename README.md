# sensor_development

Install Mako:
$ pip install Mako

-------------------------------------------------------------------------------------

Install Boto:
$ pip install boto3

-------------------------------------------------------------------------------------

Install Github:
Note: If you get the error Unknown package 'git', add this repo to the feeds

$ vi /etc/opkg/base-feeds.conf

src all     http://iotdk.intel.com/repos/2.0/iotdk/all

src x86 http://iotdk.intel.com/repos/2.0/iotdk/x86

src i586    http://iotdk.intel.com/repos/2.0/iotdk/i586


$ opkg update

$ opkg install git

-------------------------------------------------------------------------------------

Install nodejs

$ npm init

$ npm install --save aws-iot-device-sdk

$ touch main.js

$ vi myfile.js

Copy to file

setInterval( function() {
    console.log("Hello");
}, 1000);


To execute file

$ node myfile.js

-------------------------------------------------------------------------------------

board 12 IP address: 10.251.217.90

-------------------------------------------------------------------------------------
Setup Password to enable ssh 

configure_edison --setup

1. Configure Edison: Device Password
Enter a new password (leave empty to abort)
This will be used to connect to the access point and login to the device.
Password: <insert password>

2. Configure Edison: Device Name
Give this Edison a unique name.
This will be used for the access point SSID and mDNS address.
Make it at least five characters long (leave empty to skip):(insert device name)

3. Do you want to set up wifi? [Y or N]: Y
Select SSID number
Password

4. ssh root@(IP address)
Enter device password

-------------------------------------------------------------------------------------
Setup automatic files

1. cd /etc/
2. mkdir init.d
3. vi some_file_name.sh
4. root@edison chmod +x /etc/init.d/some_file_name.sh
5. update-rc.d startup_test.sh defaults

Adding system startup for /etc/init.d/startup_test.sh.

**This Doesn't work for simple example

2nd option (works)
http://shawnhymel.com/792/run-a-script-on-edison-boot/

3rd options (works)
http://www.tektyte.com/docs/docpages/edison-reference/runonstartup.html

-------------------------------------------------------------------------------------
Commmand to create table 
python create_temperature_table_v1.py temperature_table_v1
