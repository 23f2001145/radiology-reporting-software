import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext"

function Dashboard(){
    const { logout } = useAuth();
    const navigate = useNavigate();

    function handleLogout(){
        logout();
        navigate('/login');
    }

    return (
        <>
            <button onClick={handleLogout}>logout</button>
        </>
    )
}

export default Dashboard;