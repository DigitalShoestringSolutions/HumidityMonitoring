# Relative Humidity, Temperature and Pressure monitoring solution

- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/HumidityMonitoring`
- Open the downloaded folder `cd HumidityMonitoring`
- Edit the config file to set machine name `nano UserConfig/Sensing/main.py`
- Assemble the Service Modules `ServiceModules/Asssembly/get_service_modules.sh`
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`
- View the dashboard: nevigate to `localhost:3000` in a web browser
