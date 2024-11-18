#Contains configuration variables for the system.


# MQTT Configuration
MQTT_BROKER_ADDRESS = "192.168.1.100"    
MQTT_BROKER_PORT = 1883                        
MQTT_KEEPALIVE_INTERVAL = 60                   
MQTT_SENSOR_TOPIC = "home/sensors/data"
MQTT_COMMANDS_TOPIC = "home/commands"

# GPIO Configuration

ACTUATOR_LIGHT_PIN = 18             
SENSOR_TEMPERATURE_PIN = 4          
DHT_SENSOR_TYPE = 'DHT22'           

# Sensor Polling Interval
SENSOR_POLL_INTERVAL = 10            

# Debugging
DEBUG_MODE = True                    # Set to True for verbose debug output

# Authentication 
MQTT_USER = "leayeseid" 
