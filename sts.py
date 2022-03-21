import socket
from time import sleep
from sense_hat import SenseHat
# Development
#from sense_emu import SenseHat
from datetime import datetime

## CONFIG
port = 1337
tick = 1 # In seconds
debug = False

# Bootstrapping sensor
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sense = SenseHat()
sense.clear()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()


  # convert units to SignalK standards
  # C to Kelvin
  t = t + 273.15
  # millibar to pascal
  p = p * 100

  ## Paths
  # Temp Path
  t_path = "environment.inside.temperature"
  # pressure path
  p_path = "environment.inside.pressure"
  # humidity path
  h_path = "environment.inside.relativeHumidity"
  
  # Create the message
  signalk = '{"updates":[{"$source":"RaspiSenseHAT.Environment","timestamp":"'+ str(datetime.now()) +'","values":[{"path":"' + t_path + '","value": '+ str(t) +'},{"path":"' + h_path + '","value": '+ str(h) +'},{"path":"' + p_path + '","value": '+ str(p) +'}]}]}'

  if debug:
    print(signalk)

  # Send message via UDP
  sock.sendto(signalk.encode('utf-8'), ('127.0.0.1', port))
  sleep(tick)
