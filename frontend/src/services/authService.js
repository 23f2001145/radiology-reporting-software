import api from "../api/axios";

async function sendLoginRequest(formData) {
    
    const result = api.post(
        "/auth/token",
        formData
    );
    return result;
}

export default sendLoginRequest;