# Relative Humidity, Temperature and Pressure monitoring solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/HumidityMonitoring`
- Open the downloaded folder `cd HumidityMonitoring`

### Configure & Assemble
- Edit the config file to set machine name `nano Config/Sensing/main.py`
- Check the recipe contains the Modules you desire `nano recipe.txt`
- Assemble the Modules `Modules/Asssembly/get_modules.sh`
- Restart to apply the settings to the downloaded Modules

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboards: navigate to `localhost:3000` in a web browser:

![image](https://github.com/user-attachments/assets/87c6c741-8b0f-47b2-8376-9b4b64879a4a)

![image](https://github.com/user-attachments/assets/732c5968-577d-4385-862f-1f04d62e768d)

### Additional Sensing Nodes
The default collection of Modules creates an independent system, complete with communications controller, database and dashboard hosting. If in your deployment environment you would like to expand an existing sytem by adding more sensors connected over the network, the Solution can be built in a simplified configuration that only gathers data and sends it to the master pi. 

- In `recipe.txt`, remove the Modules that are not required:
    - MQTTBroker
    - AWSRelay
    - Timeseries
    - Grafana
      
- In `Config/Sensing/main.py`, Add `, broker="xxx.xxx.xxx.xxx"` to the end of the `publish` function to send the data to the master pi. Hence ideally your master pi will have a static IP address. For example the last line could become:
    - `publish( {"machine": "StoreRoom"} | mysht40.get_TRH() | mybmp280.get_P(), broker="192.168.59.50" )`
