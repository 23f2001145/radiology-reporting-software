import api from "../api/axios";

export async function getPatients() {
    const response = await api.get(
        '/patients'
    );
    return response.data;
}

export async function createPatient(patientData) {
    const response = await api.post("/patients", patientData);
    return response.data;
}

export async function getPatient(patientId) {
    const response = await api.get(`/patients/${patientId}`);
    return response.data;
}

export async function updatePatient(patientId, patientData) {
    const response = await api.patch(
        `/patients/${patientId}`,
        patientData
    );

    return response.data;
}

export async function deactivatePatient(patientId) {
    const response = await api.patch(`/patients/${patientId}/deactivate`);
    return response.data;
}