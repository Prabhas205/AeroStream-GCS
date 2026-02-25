from pymavlink import mavutil
import asyncio

class MavlinkBridge:
    def __init__(self, connection_str='udpin:localhost:14550'):
        # Establish low-latency UDP connection [cite: 11, 13]
        self.master = mavutil.mavlink_connection(connection_str)

    async def get_telemetry(self):
        """Asynchronously listen for MAVLink packets."""
        while True:
            # Non-blocking wait for specific telemetry types [cite: 10]
            msg = self.master.recv_match(type=['VFR_HUD', 'GLOBAL_POSITION_INT', 'HEARTBEAT'], blocking=False)
            if msg:
                yield msg.to_dict()
            await asyncio.sleep(0.05) # 20Hz update frequency