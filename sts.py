import socket
from time import sleep
from sense_hat import SenseHat
# Development
#from sense_emu import SenseHat
from datetime import datetime

## CONFIG
port = 1337
tick = 5 # In seconds


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sense = SenseHat()
sense.clear()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  #message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  signalk = '{"updates":[{"$source":"RaspiSenseHAT.Environment","timestamp":"'+ str(datetime.now()) +'","values":[{"path":"environment.temperature","value": '+ str(t) +'},{"path":"environment.relativeHumidity","value": '+ str(h) +'},{"path":"environment.pressure","value": '+ str(p) +'}]}]}'

  # Display the scrolling message
  #print(signalk)
  sock.sendto(signalk.encode('utf-8'), ('127.0.0.1', port))
  sleep(tick)
