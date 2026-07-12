import { useState } from "react";
import { useNavigate } from "react-router-dom";

import "../styles/login.css";


function Login(){

const [email,setEmail] = useState("");
const [password,setPassword] = useState("");

const navigate = useNavigate();


const handleLogin = (e)=>{

e.preventDefault();

if(email && password){

navigate("/dashboard");

}

};


return (

<div className="login-container">


<div className="login-card">


<h1>
PhishGuard AI
</h1>


<p>
AI Based Phishing Detection System
</p>



<form onSubmit={handleLogin}>


<input

type="email"

placeholder="Email"

value={email}

onChange={(e)=>setEmail(e.target.value)}

/>



<input

type="password"

placeholder="Password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

/>



<button type="submit">

Login

</button>


</form>


</div>


</div>

);

}


export default Login;