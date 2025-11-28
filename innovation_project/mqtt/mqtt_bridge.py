import paho.mqtt.client as mqtt
import requests
import json
import time
from datetime import datetime

# MQTT Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "fll/test"  # Use "#" to subscribe to all topics
MQTT_USERNAME = "shumin"
MQTT_PASSWORD = "825123"
USE_MQTT_AUTH = True

# HTTP Configuration
APP_ID = "691d5eaae10f8e3ac6decd42"
HTTP_ENDPOINT = f"https://base44.app/api/apps/{APP_ID}/functions/ingestSensorData"
HTTP_METHOD = "POST"  # POST, PUT, or GET
HTTP_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer arch_SPBHPmHiaNzfNRBIfMmmSy4gZbONqNZT"  # Optional: Add your auth token
}
HTTP_TIMEOUT = 10  # seconds

# Bridge Configuration
INCLUDE_METADATA = False  # Include topic, timestamp in HTTP payload
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # seconds

def forward_to_http(topic, payload, qos, retain):
    """Forward MQTT message to HTTP endpoint"""
    
    # Prepare the payload
    try:
        # Try to parse as JSON
        message_data = json.loads(payload)
    except:
        # If not JSON, send as string
        message_data = payload
    
    # Add metadata if enabled
    if INCLUDE_METADATA:
        http_payload = {
            "topic": topic,
            "payload": message_data,
            "qos": qos,
            "retain": retain,
            "timestamp": datetime.now().isoformat()
        }
    else:
        http_payload = message_data
    
    # Send to HTTP endpoint with retry logic
    for attempt in range(RETRY_ATTEMPTS):
        try:
            print(f"\n→ Forwarding to HTTP endpoint (attempt {attempt + 1}/{RETRY_ATTEMPTS})")
            print(f"  Topic: {topic}")
            print(f"  Payload: {json.dumps(http_payload, indent=2)}")
            
            if HTTP_METHOD == "POST":
                response = requests.post(
                    HTTP_ENDPOINT,
                    json=http_payload,
                    headers=HTTP_HEADERS,
                    timeout=HTTP_TIMEOUT
                )
            elif HTTP_METHOD == "PUT":
                response = requests.put(
                    HTTP_ENDPOINT,
                    json=http_payload,
                    headers=HTTP_HEADERS,
                    timeout=HTTP_TIMEOUT
                )
            elif HTTP_METHOD == "GET":
                response = requests.get(
                    HTTP_ENDPOINT,
                    params=http_payload,
                    headers=HTTP_HEADERS,
                    timeout=HTTP_TIMEOUT
                )
            
            response.raise_for_status()
            print(f"✓ HTTP {response.status_code}: Message forwarded successfully")
            print(f"  Response: {response.text[:200]}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"✗ HTTP Error (attempt {attempt + 1}/{RETRY_ATTEMPTS}): {e}")
            if attempt < RETRY_ATTEMPTS - 1:
                print(f"  Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"  Failed to forward message after {RETRY_ATTEMPTS} attempts")
                return False

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✓ Connected to MQTT Broker!")
        print(f"  Broker: {MQTT_BROKER}:{MQTT_PORT}")
        print(f"  Subscribing to: {MQTT_TOPIC}")
        client.subscribe(MQTT_TOPIC)
        print(f"\n✓ MQTT to HTTP Bridge Active")
        print(f"  HTTP Endpoint: {HTTP_ENDPOINT}")
        print(f"  Waiting for messages...\n")
    else:
        error_messages = {
            1: "Incorrect protocol version",
            2: "Invalid client identifier",
            3: "Server unavailable",
            4: "Bad username or password",
            5: "Not authorized"
        }
        print(f"✗ Failed to connect: {error_messages.get(rc, 'Unknown error')}")

def on_message(client, userdata, msg):
    print(f"\n{'='*50}")
    print(f"📨 MQTT Message Received")
    print(f"{'='*50}")
    forward_to_http(msg.topic, msg.payload.decode(), msg.qos, msg.retain)

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"✓ Subscribed successfully (QoS: {granted_qos[0]})")

def on_disconnect(client, userdata, rc, properties=None):
    if rc == 0:
        print("\n✓ Disconnected from MQTT broker")
    else:
        print(f"\n✗ Unexpected disconnection (code: {rc})")
        print("  Attempting to reconnect...")

# Create MQTT client
print("Starting MQTT to HTTP Bridge...")
print(f"MQTT: {MQTT_BROKER}:{MQTT_PORT} → HTTP: {HTTP_ENDPOINT}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect

# Enable automatic reconnection
client.reconnect_delay_set(min_delay=1, max_delay=120)

# Set authentication if enabled
if USE_MQTT_AUTH:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

try:
    # Connect to MQTT broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    # Start loop
    client.loop_forever()
    
except KeyboardInterrupt:
    print("\n\nShutting down bridge...")
    client.disconnect()
    print("Bridge stopped")
    
except Exception as e:
    print(f"✗ Error: {e}")
    
finally:
    client.loop_stop()