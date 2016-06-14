import pyupm_th02 as upmth02

th02_sensor = upmth02.TH02()

print(th02_sensor.getStatus())
print(th02_sensor.name())
print("Humidity", th02_sensor.getHumidity())
print("Temperature", th02_sensor.getTemperature())
