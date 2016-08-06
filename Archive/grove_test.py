from datetime import datetime
import pyupm_grove as grove

temp = grove.GroveTemp(0)
celsius = temp.value()
fahrenheit = celsius * 9.0/5.0 + 32.0;
print "Celsius:", celsius 
print "Fahrenheit:", fahrenheit 
print datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
