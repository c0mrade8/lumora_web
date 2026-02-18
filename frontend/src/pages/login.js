import React, { useState} from "react";
import axios from "axios";
const Login = () => {
    const[nickname, setNickname] = useState("");

    const handleGuestLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/auth/anonymous/", {display_name: nickname});

            localStorage.setItem("access_token", response.data.tokens.access);
            localStorage.setItem("refresh_token", response.data.refresh);
            localStorage.setItem("user_id", response.data.user.id);
            localStorage.setItem("expires_at", response.data.expires_at);
            alert(`Welcome, ${response.data.user.display_name}! Session started.`);
            window.location.href = "/dashboard";
        } catch (error) {
            console.error("Login failed:", error);
        }
    };
    return (
        <div className="login-container">
      <form onSubmit={handleGuestLogin}>
        <h2>Enter the Safe Space</h2>
        <input 
          type="text" 
          placeholder="Choose a nickname..." 
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
          required 
        />
        <button type="submit">Start 48h Session</button>
      </form>
    </div>
  );
};

export default Login;
