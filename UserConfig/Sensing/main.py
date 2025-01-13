# standard imports
from time import sleep

# local imports
from utilities.mqtt_out import publish
from hardware.ICs.sht40 import SHT40
from hardware.ICs.bmp280_wrapper import BMP280

# sensing loop
while True:
    sleep(1)
    publish( {"machine": "MachineNameHere"} | SHT40.get_TRH() | BMP280.get_P() )
    
