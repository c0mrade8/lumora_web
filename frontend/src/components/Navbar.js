import React, { useEffect, useState } from 'react';

const Navbar = () => {
    const [timeLeft, setTimeLeft] = useState('');

    useEffect(() => {
        const expiry = localStorage.getItem('expires_at');
        if (!expiry) return;

        const interval = setInterval(() => {
            const now = new Date();
            const end = new Date(expiry);
            const diff = end - now;

            if (diff <= 0) {
                setTimeLeft('Session Expired');
                clearInterval(interval);
                // Optional: Force logout here
            } else {
                const hours = Math.floor(diff / (1000 * 60 * 60));
                const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                setTimeLeft(`${hours}h ${mins}m left`);
            }
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    return (
        <nav style={{ display: 'flex', justifyContent: 'space-between', padding: '1rem', background: '#fff' }}>
            <h2>🌿 WellnessSpace</h2>
            {timeLeft && <span style={{ color: '#76a19f' }}>{timeLeft}</span>}
        </nav>
    );
};

export default Navbar;