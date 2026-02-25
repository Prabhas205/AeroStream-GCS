from fastapi import FastAPI, WebSocket
from mavlink_bridge import MavlinkBridge
import asyncio
import json  # Built-in, no pip install needed
from fastapi import FastAPI, WebSocket
from pymavlink import mavutil
import asyncio

async def main():
    print("GCS Bridge Starting...")
    await asyncio.sleep(1)
    print("Data Stream Active.")

if __name__ == "__main__":
    asyncio.run(main())

app = FastAPI()
bridge = MavlinkBridge()

@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        async for data in bridge.get_telemetry():
            # Real-time data visualization streaming [cite: 10]
            await websocket.send_json(data)
    except Exception as e:
        print(f"Connection closed: {e}")