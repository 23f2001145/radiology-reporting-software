import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createPatient } from "../services/patientService";

function PatientCreatePage() {
    const navigate = useNavigate();

    const [patientName, setPatientName] = useState("");
    const [dob, setDob] = useState("");
    const [gender, setGender] = useState("M");

    async function handleSubmit(e) {
        e.preventDefault();

        try {
            const payload = {
                patient_name: patientName,
                dob,
                gender,
            };

            await createPatient(payload);

            alert("Patient created successfully!");
            navigate("/patients");
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.detail ??
                "Failed to create patient."
            );
        }
    }

    return (
        <>
            <h1>Add Patient</h1>

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
                    Add Patient
                </button>

                <button
                    type="button"
                    onClick={() => navigate("/patients")}
                    style={{ marginLeft: "10px" }}
                >
                    Cancel
                </button>
            </form>
        </>
    );
}

export default PatientCreatePage;