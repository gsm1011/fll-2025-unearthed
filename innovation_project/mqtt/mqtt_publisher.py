import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime, timezone
import random

# MQTT Broker settings
BROKER = "localhost"  # Change to your broker address (e.g., "mqtt.example.com")
PORT = 1883
TOPIC = "fll/test"
USERNAME = "shumin"  # Set your MQTT username
PASSWORD = "825123"  # Set your MQTT password
SENSOR_IDS = [
    "6925363e7334c80d5937216d",
    "6923a28b1d4808907442eac9",  # monalisa
    "69228248ad44d08d8b6f5e45",  # pot
    "6922812df7da00e341b087fc",  # warrior
    "69210013cf6a217cc0a7ed82",  # pot
    "6920fe70db7b39ab0d18ca45",  # warrior
]
LATITUDE = 34.017250  # Optional latitude
LONGITUDE = -118.289141  # Optional longitude

# Callback when connected to broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        error_messages = {
            1: "Connection refused - incorrect protocol version",
            2: "Connection refused - invalid client identifier",
            3: "Connection refused - server unavailable",
            4: "Connection refused - bad username or password",
            5: "Connection refused - not authorized"
        }
        print(f"Failed to connect, return code {rc}: {error_messages.get(rc, 'Unknown error')}")
        print("\nTroubleshooting:")
        print("- Check your USERNAME and PASSWORD are correct")
        print("- Verify your broker address and port")
        print("- Make sure your user has permission to connect")
        print("- Try connecting without credentials first (comment out username_pw_set line)")

# Callback when message is published
def on_publish(client, userdata, mid, properties=None):
    print(f"Message {mid} published")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Set username and password
client.username_pw_set(USERNAME, PASSWORD)

try:
    # Connect to broker
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    
    # Wait for connection
    time.sleep(1)
    
    # Publish messages: perform 10 rounds; in each round publish one message per sensor
    for i in range(100):
        for sensor_id in SENSOR_IDS:
            print(f"Fake data for SENSOR_ID: {sensor_id}")
            # generate random sensor values within requested ranges and round to 2 decimals
            temperature = round(random.uniform(20.0, 25.0), 2)            # 20..25
            humidity = round(random.uniform(50.0, 70.0), 2)               # 50..70
            movement_x = round(random.uniform(0.01, 0.1), 2)              # 0.01..0.1
            movement_y = round(random.uniform(0.01, 0.1), 2)              # 0.01..0.1
            movement_z = round(random.uniform(0.01, 0.1), 2)              # 0.01..0.1

            message = {
                "sensor_id": sensor_id,  # Required
                "temperature": temperature,              # Required (in Celsius)
                "humidity": humidity,
                "latitude": LATITUDE,
                "longitude": LONGITUDE,
                "movement_x": movement_x,
                "movement_y": movement_y,
                "movement_z": movement_z,
            }

            # Publish as JSON string
            result = client.publish(TOPIC, json.dumps(message))

            # Or publish plain text
            # result = client.publish(TOPIC, f"Message {i}")

            print(f"Publishing: {message}")
            time.sleep(10)
    
    # Keep connection alive briefly to ensure all messages are sent
    time.sleep(1)
    
except Exception as e:
    print(f"Error: {e}")
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected from broker")