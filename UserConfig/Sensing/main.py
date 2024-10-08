# standard imports
from time import sleep

# local imports
from utilities.mqtt_out import publish
from hardware.ICs.sht40 import SHT40
from hardware.ICs.bmp280_wrapper import BMP280

# setup sensors and models
mysht40 = SHT40()
mybmp280 = BMP280()

# sensing loop
while True:
    sleep(1)
    publish( {"machine": "MachineNameHere"} | mysht40.get_TRH() | mybmp280.get_P() )