# use the following link to update version of setup tools (must be 21)

https://www.versioneye.com/python/setuptools/21.0.0

_____________________________________________________________________________________

# sensor_development

-------------------------------------------------------------------------------------


Initial Configuration:
http://www.seeedstudio.com/wiki/Intel%C2%AE_Edison_and_Grove_IoT_Starter_Kit_Powered_by_AWS
-------------------------------------------------------------------------------------

AWS IoT Policy Configuration: note, my-rule = myRule, and always remember to copy paste our own ans
http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html
-------------------------------------------------------------------------------------

Install Screen:
$ wget https://ftp.gnu.org/gnu/screen/screen-4.3.1.tar.gz

$ tar -zxvf screen-4.3.1.tar.gz

$ cd screen-4.3.1

$ ./configure

$ make

$ make install

$ export PATH=$PATH:/usr/local/bin/

$ cd ~
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

src/gz all http://repo.opkg.net/edison/repo/all

src/gz edison http://repo.opkg.net/edison/repo/edison

src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32

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

board11 IP address: 10.251.213.151

board12 IP address: 10.251.221.208

testboard IP address: 10.251.27.138

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


