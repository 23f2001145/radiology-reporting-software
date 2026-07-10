import { createContext, useContext, useState } from "react";
import sendLoginRequest from "../services/authService";

const AuthContext = createContext();

export function AuthProvider({children}){
    const [isAuthenticated, setisAuthenticated] = useState(
        () => {
            return Boolean(localStorage.getItem("access_token"));
        }
    );

    async function login(email, password) {
        const formData = new URLSearchParams();
        formData.append("username", email);
        formData.append("password", password);

        try{
            const response = await sendLoginRequest(formData);
            localStorage.setItem("access_token", response.data.access_token);
            setisAuthenticated(true);          
        }
        catch(error) {
            console.error(error);
            throw error;
        }
    }

    function logout(){
        localStorage.removeItem("access_token");
        setisAuthenticated(false);
    }

    return (
        <AuthContext.Provider
            value={{isAuthenticated, login, logout}}
        >
            {children}
        </AuthContext.Provider>
    )
}

export function useAuth(){
    return useContext(AuthContext);
}