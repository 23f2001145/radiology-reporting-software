import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getPatient, updatePatient } from "../services/patientService";

function PatientEditPage() {
    const { patientId } = useParams();
    const navigate = useNavigate();

    const [patientName, setPatientName] = useState("");
    const [dob, setDob] = useState("");
    const [gender, setGender] = useState("M");

    useEffect(() => {
        async function loadPatient() {
            try {
                const patient = await getPatient(patientId);

                setPatientName(patient.patient_name);
                setDob(patient.dob);
                setGender(patient.gender);
            } catch (error) {
                console.error(error);
                alert("Failed to load patient.");
                navigate("/patients");
            }
        }

        loadPatient();
    }, [patientId, navigate]);

    async function handleSubmit(e) {
        e.preventDefault();

        try {
            const payload = {
                patient_name: patientName,
                dob,
                gender,
            };

            await updatePatient(patientId, payload);

            alert("Patient updated successfully!");
            navigate("/patients");
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.detail ??
                "Failed to update patient."
            );
        }
    }

    return (
        <>
            <h1>Edit Patient</h1>

            <form onSubmit={handleSubmit}>
                <div>
                    <label>Patient Name</label>
                    <br />
                    <input
                        type="text"
                        value={patientName}
                        onChange={(e) => setPatientName(e.target.value)}
                    />
                </div>

                <br />

                <div>
                    <label>Date of Birth</label>
                    <br />
                    <input
                        type="date"
                        value={dob}
                        onChange={(e) => setDob(e.target.value)}
                    />
                </div>

                <br />

                <div>
                    <label>Gender</label>
                    <br />
                    <select
                        value={gender}
                        onChange={(e) => setGender(e.target.value)}
                    >
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                    </select>
                </div>

                <br />

                <button type="submit">
                    Save Changes
                </button>
            </form>
        </>
    );
}

export default PatientEditPage;