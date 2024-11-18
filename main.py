from mqtt_client import MQTTClient
from sensor_controller import SensorController
from actuator_controller import ActuatorController

def main():
    # Initialize MQTT Client
    mqtt_client = MQTTClient()
    
    # Start MQTT Client
    mqtt_client.start()

    # Initialize Sensor Controller
    sensor_ctrl = SensorController(mqtt_client)
    
    # Initialize Actuator Controller
    actuator_ctrl = ActuatorController(mqtt_client)
    
    # Main loop to manage system
    try:
        while True:
            sensor_data = sensor_ctrl.read_sensors()
            if sensor_data:
                mqtt_client.publish_sensor_data(sensor_data)
    except KeyboardInterrupt:
        print("Shutting down...")
        mqtt_client.stop()

if __name__ == "__main__":
    main()