Before doing anything, make sure amazon account is set to N. Virginia (Tab at top right) so that when you're working to aws configure the board, the policy documents actually show up and attach correctly.
_____________________________________________________________________________________

# sensor_development

-------------------------------------------------------------------------------------

Initial Configuration:
http://www.seeedstudio.com/wiki/Intel%C2%AE_Edison_and_Grove_IoT_Starter_Kit_Powered_by_AWS
http://wiki.seeedstudio.com/wiki/Grove_IoT_Starter_Kits_Powered_by_AWS

basically follow through all the steps until it tells you to Use MQTT to subscribe and publish to AWS. 
then follow our steps below for nodejs folder

-------------------------------------------------------------------------------------

AWS IoT Policy Configuration: note, my-rule = myRule, and always remember to copy paste our own ans
http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html

once you hit the confusing page about PassRole permissions, go to Pat K's document edit_db.txt in dynamodb folder

-------------------------------------------------------------------------------------

Create tables: go to document called "initiate_temperature_humidity_table_v2.txt" in general folder

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
PIP INSTALL AWSCLI

NOTE: In order to avoid 'egg_command' error when trying to "$ pip install awscli", you might need to delete the first 3 src lines in the above /etc/opkg file.

Check version: 
$ easy_install --version

if setuptools is not 21.0.0, 

# use the following link to update version of setup tools (must be 21)

https://www.versioneye.com/python/setuptools/21.0.0

Grab this line to update setuptools:
$ pip install https://pypi.python.org/packages/15/b7/a76624e5a3b18c8c1c8d33a5240b34cdabb08aef2da44b536a8b53ba1a45/setuptools-21.0.0-py2.py3-none-any.whl

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
Board IP Addresses 

See NETS1_Data document: 
https://docs.google.com/spreadsheets/d/1yq63MRy-mdnHkPO6iLynhxMXbEqtH9t-1t9vsIxglp8/edit?ts=57a50931#gid=0
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


