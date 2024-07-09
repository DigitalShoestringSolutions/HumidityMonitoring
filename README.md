# Relative Humidity, Temperature and Pressure monitoring solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/HumidityMonitoring`
- Open the downloaded folder `cd HumidityMonitoring`

### Configure & Assemble
- Edit the config file to set machine name `nano UserConfig/Sensing/main.py`
- Check the recipe contains the Service Modules you desire `nano recipe.txt`
- Assemble the Service Modules `ServiceModules/Asssembly/get_service_modules.sh`

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser

![image](https://github.com/DigitalShoestringSolutions/HumidityMonitoring/assets/51968582/f25fa0a5-1ede-4509-813b-4811b7263210)
