#Manages actuator control signals, possibly triggered by user commands or automated scripts.
  
import RPi.GPIO as GPIO

class ActuatorController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.setup_actuators()

    def setup_actuators(self):
        # Setup GPIO pins for actuators, like lights, fans, etc.
        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Define GPIO pin numbers for actuators
        self.light_pin = 18
        
        # Setup GPIO pins
        GPIO.setup(self.light_pin, GPIO.OUT)
        
        # Initial state for actuators
        GPIO.output(self.light_pin, GPIO.LOW)

    def control_actuators(self, command):
        print(f"Executing command: {command}")
        
        if command == "toggle_light":
            current_state = GPIO.input(self.light_pin)
            GPIO.output(self.light_pin, not current_state)
            print(f"Light turned {'on' if not current_state else 'off'}")
        
        elif command == "turn_on_fan":
            # GPIO.output(fan_pin, GPIO.HIGH)
            print("Fan turned on")
        
        elif command == "turn_off_fan":
            # GPIO.output(fan_pin, GPIO.LOW)
            print("Fan turned off")

    def cleanup(self):
        # Reset GPIO settings
        GPIO.cleanup()
    
    def on_mqtt_message(self, client, userdata, msg):
        """
        Handle incoming MQTT messages related to actuators.
        This method should be connected to the MQTT client's on_message handler.
        """
        # Decode message payload and send to control_actuators
        command = msg.payload.decode('utf-8')
        self.control_actuators(command)