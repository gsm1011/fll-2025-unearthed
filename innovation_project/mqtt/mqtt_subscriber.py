import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker settings
BROKER = "localhost"  # Change to your broker address
PORT = 1883
TOPIC = "fll/test"
USERNAME = "shumin"  # Set your MQTT username
PASSWORD = "825123"  # Set your MQTT password
USE_AUTH = True  # Set to False if no authentication needed

# Callback when connected to broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✓ Connected to MQTT Broker!")
        print(f"Subscribing to topic: {TOPIC}")
        client.subscribe(TOPIC)
        print("Waiting for messages... (Press Ctrl+C to exit)\n")
    else:
        error_messages = {
            1: "Incorrect protocol version",
            2: "Invalid client identifier",
            3: "Server unavailable",
            4: "Bad username or password",
            5: "Not authorized"
        }
        print(f"✗ Failed to connect, return code {rc}: {error_messages.get(rc, 'Unknown error')}")

# Callback when subscribed to topic
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"✓ Successfully subscribed (QoS: {granted_qos[0]})")

# Callback when message is received
def on_message(client, userdata, msg):
    print(f"\n--- Message Received ---")
    print(f"Topic: {msg.topic}")
    print(f"QoS: {msg.qos}")
    print(f"Retain: {msg.retain}")
    
    # Try to parse as JSON
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Payload (JSON):")
        print(json.dumps(payload, indent=2))
    except:
        # If not JSON, print as plain text
        print(f"Payload: {msg.payload.decode()}")
    
    print("-" * 24)

# Callback when disconnected
def on_disconnect(client, userdata, rc, properties=None):
    if rc == 0:
        print("\n✓ Disconnected gracefully")
    else:
        print(f"\n✗ Unexpected disconnection (code: {rc})")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_disconnect = on_disconnect

# Set username and password if authentication is enabled
if USE_AUTH and USERNAME and PASSWORD:
    client.username_pw_set(USERNAME, PASSWORD)

try:
    print(f"Connecting to broker {BROKER}:{PORT}...")
    
    # Connect to broker
    client.connect(BROKER, PORT, 60)
    
    # Start the loop to process callbacks
    client.loop_forever()
    
except KeyboardInterrupt:
    print("\n\nShutting down subscriber...")
    client.disconnect()
    print("Subscriber stopped")
    
except ConnectionRefusedError:
    print("✗ Connection refused - broker may not be running")
    print("Check if Docker container is running: docker ps")
    
except Exception as e:
    print(f"✗ Error: {e}")
    
finally:
    client.loop_stop()