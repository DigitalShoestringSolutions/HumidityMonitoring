# Relative Humidity, Temperature and Pressure monitoring solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/HumidityMonitoring`
- Open the downloaded folder `cd HumidityMonitoring`

### Configure & Assemble
- Edit the config file to set machine name `nano UserConfig/Sensing/main.py`
- Check the recipe contains the Service Modules you desire `nano recipe.txt`
- Assemble the Service Modules `ServiceModules/Asssembly/get_service_modules.sh`
- Restart to apply the settings to the downloaded Service Modules

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser

![image](https://github.com/user-attachments/assets/ef3972aa-4e11-4208-b141-6587e39b842b)

![image](https://github.com/user-attachments/assets/406bf5cc-232b-4abd-83ff-c64687bcb410)


### Additional Sensing Nodes
The default collection of Service Modules creates an independent system, complete with communications controller, database and dashboard hosting. If in your deployment environment you would like to expand an existing sytem by adding more sensors connected over the network, the Solution can be built in a simplified configuration that only gathers data and sends it to the master pi. 

- In `recipe.txt`, remove the Service Modules that are not required:
    - MQTTBroker
    - AWSRelay
    - Timeseries
    - Grafana
      
- In `UserConfig/Sensing/main.py`, Add `, broker="xxx.xxx.xxx.xxx"` to the end of the `publish` function to send the data to the master pi. Hence ideally your master pi will have a static IP address. For example the last line could become:
    - `publish( {"machine": "StoreRoom"} | mysht40.get_TRH() | mybmp280.get_P(), broker="192.168.59.50" )`
