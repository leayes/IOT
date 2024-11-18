#Handles data collection from sensors and sends data to MQTT broker.

import random
import Adafruit_DHT  

class SensorController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.temperature_sensor_pin = 4  

    def read_sensors(self):
        """
        Reads data from connected sensors. In this example, it reads:
        - Temperature and humidity from a DHT sensor.
        - Simulated lighting level.
        """
        humidity, temperature = self.read_temperature_humidity()

        lighting = random.randint(0, 100)
        
        sensor_data = {
            "temperature": temperature if temperature is not None else "N/A",
            "humidity": humidity if humidity is not None else "N/A",
            "lighting": lighting
        }
        
        # Publish sensor data to MQTT
        self.publish_sensor_data(sensor_data)
        return sensor_data

    def read_temperature_humidity(self):
        """
        Reads temperature and humidity data from a DHT sensor.
        Returns a tuple of (humidity, temperature).
        If the reading fails, returns (None, None).
        """
        # Use Adafruit_DHT library for reading DHT sensors.
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.temperature_sensor_pin)
        if humidity is None or temperature is None:
            print("Failed to retrieve data from humidity sensor")
        return humidity, temperature
            
    def publish_sensor_data(self, sensor_data):
        """
        Publishes sensor data to the MQTT broker under the `home/sensors` topic.
        """
        message_payload = f"Temperature: {sensor_data['temperature']}, " \
                          f"Humidity: {sensor_data['humidity']}, " \
                          f"Lighting: {sensor_data['lighting']}"
        self.mqtt_client.publish("home/sensors/data", message_payload)
        print("Published sensor data:", message_payload)