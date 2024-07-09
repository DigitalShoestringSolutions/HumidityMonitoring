# Relative Humidity, Temperature and Pressure monitoring solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/HumidityMonitoring`
- Open the downloaded folder `cd HumidityMonitoring`

### Configure
- Edit the config file to set machine name `nano UserConfig/Sensing/main.py`

### Assemble
- Check the recipe contains the Service Modules you desire `nano recipe.txt`
- Assemble the Service Modules `ServiceModules/Asssembly/get_service_modules.sh`

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`
- View the dashboard: navigate to `localhost:3000` in a web browser
