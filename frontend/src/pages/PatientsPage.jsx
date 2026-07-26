import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getPatients, deactivatePatient } from "../services/patientService";

function PatientsPage() {
    const [patients, setPatients] = useState([]);

    const navigate = useNavigate();

    useEffect(() => {
        loadPatients();
    }, []);

    async function loadPatients() {
        try {
            const data = await getPatients();
            setPatients(data);
        } catch (error) {
            console.error(error);
        }
    }

    function handleEdit(patientId) {
        navigate(`/patients/edit/${patientId}`);
    }

    async function handleDeactivate(patientId) {
        const confirmed = window.confirm(
            "Are you sure you want to deactivate this patient?"
        );

        if (!confirmed) {
            return;
        }

        try {
            await deactivatePatient(patientId);

            alert("Patient deactivated successfully!");

            loadPatients();
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.detail ??
                "Failed to deactivate patient."
            );
        }
    }

    return (
        <>
            <h2>Patients</h2>

            <button onClick={() => navigate("/patients/new")}>
                Add Patient
            </button>

            <br />
            <br />

            <table border="1" cellPadding="8">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>DOB</th>
                        <th>Gender</th>
                        <th>Actions</th>
                    </tr>
                </thead>

                <tbody>
                    {patients.map((patient) => (
                        <tr key={patient.id}>
                            <td>{patient.patient_name}</td>
                            <td>{patient.dob}</td>
                            <td>{patient.gender}</td>
                            <td>
                                <button onClick={()=>handleEdit(patient.id)}>
                                    Edit
                                </button>

                                <button
                                    onClick={() => handleDeactivate(patient.id)}
                                    style={{ marginLeft: "8px" }}
                                >
                                    Deactivate
                                </button>
                            </td>
                        </tr>
                    ))}

                    {patients.length === 0 && (
                        <tr>
                            <td colSpan="4">
                                No patients found.
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </>
    );
}

export default PatientsPage;