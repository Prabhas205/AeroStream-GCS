export const connectTelemetry = (onMessage) => {
    const socket = new WebSocket('ws://localhost:8000/ws/telemetry');
    socket.onmessage = (event) => onMessage(JSON.parse(event.data));
    return socket;
};