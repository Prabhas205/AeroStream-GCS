import React, { useEffect, useState } from 'react';
import { connectTelemetry } from '../services/websocket';

const Dashboard = () => {
    const [stats, setStats] = useState({ alt: 0, heading: 0, velocity: 0 });

    useEffect(() => {
        const ws = connectTelemetry((data) => {
            if (data.mavpackettype === 'VFR_HUD') {
                setStats({
                    alt: data.alt,
                    heading: data.heading,
                    velocity: data.airspeed
                });
            }
        });
        return () => ws.close();
    }, []);

    return (
        <div className="p-6 bg-slate-900 text-white grid grid-cols-3 gap-4">
            <div className="border p-4"><h3>Altitude</h3><p>{stats.alt}m</p></div>
            <div className="border p-4"><h3>Heading</h3><p>{stats.heading}°</p></div>
            <div className="border p-4"><h3>Velocity</h3><p>{stats.velocity}m/s</p></div>
        </div>
    );
};

export default Dashboard;