import api from "../api/axios";

async function getPatients() {
    const response = await api.get(
        '/patients'
    );
    return response.data;
}

export default getPatients