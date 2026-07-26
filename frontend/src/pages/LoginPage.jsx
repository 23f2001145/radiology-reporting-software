import { useState } from "react";
import { useNavigate } from "react-router-dom"
import { useAuth } from "../contexts/AuthContext";

function LoginPage(){
    const navigate = useNavigate();
    const { login } = useAuth();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function handleLogin(event){
        event.preventDefault();
        try{
            await login(email, password)
            navigate('/dashboard') 
        }
        catch(error) {
            console.error(error);
        }
    }
    return(
        <>
            <form onSubmit={handleLogin}>
                Email : 
                <input type="email" value={email} onChange={(e)=>setEmail(e.target.value)}></input>
                Password : 
                <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)}></input>
                <input type="submit"></input>
            </form>
        </>
    )
}

export default LoginPage;