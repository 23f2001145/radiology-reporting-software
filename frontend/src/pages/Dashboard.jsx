import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { getReports } from "../services/reportService";

function Dashboard() {
    const { logout } = useAuth();
    const navigate = useNavigate();

    const [reports, setReports] = useState([]);

    useEffect(() => {
        async function loadReports() {
            try {
                const data = await getReports();
                setReports(data);
            } catch (error) {
                console.error(error);
            }
        }

        loadReports();
    }, []);

    function handleLogout() {
        logout();
        navigate("/login");
    }

    function handleNewReport() {
        navigate("/report");
    }

    return (
        <>
            <h1>Dashboard</h1>

            <button onClick={handleNewReport}>
                New Report
            </button>

            <button onClick={handleLogout}>
                Logout
            </button>

            <h2>Saved Reports</h2>

            <table border="1" cellPadding="8">
                <thead>
                    <tr>
                        <th>Report ID</th>
                        <th>Patient</th>
                        <th>Status</th>
                        <th>Created</th>
                        <th>Actions</th>
                    </tr>
                </thead>

                <tbody>
                    {reports.map((report) => (
                        <tr key={report.id}>
                            <td>{report.id}</td>
                            <td>{report.patient_name}</td>
                            <td>{report.status}</td>
                            <td>
                                {new Date(report.creation_time).toLocaleString()}
                            </td>
                            <td>
                                <button onClick={() => navigate(`/report/${report.id}`)}>
                                    Open
                                </button>
                            </td>
                        </tr>
                    ))}

                    {reports.length === 0 && (
                        <tr>
                            <td colSpan="5">
                                No reports found.
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </>
    );
}

export default Dashboard;