import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getReport, updateReport } from "../services/reportService";

function ReportEditPage() {
    const { reportId } = useParams();
    const navigate = useNavigate();

    const [report, setReport] = useState(null);
    const [patientName, setPatientName] = useState("");
    const [status, setStatus] = useState("");

    useEffect(() => {
        async function loadReport() {
            try {
                const data = await getReport(reportId);

                setPatientName(data.patient_name);
                setStatus(data.status);

                const structuredReport = {};

                data.sections.forEach((section) => {
                    structuredReport[section.section_type] = section.content;
                });

                setReport(structuredReport);
            } catch (error) {
                console.error(error);
                alert("Failed to load report.");
                navigate("/dashboard");
            }
        }

        loadReport();
    }, [reportId, navigate]);

    async function handleSave() {
        try {
            const payload = {
                status: "draft",
                sections: [
                    {
                        section_type: "findings",
                        content: report.findings,
                    },
                    {
                        section_type: "impression",
                        content: report.impression,
                    },
                    {
                        section_type: "advice",
                        content: report.advice,
                    },
                ],
            };

            await updateReport(reportId, payload);

            alert("Report updated successfully!");
            navigate("/dashboard");
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.detail ??
                "Failed to update report."
            );
        }
    }

    async function handleFinalize() {
        try {
            const payload = {
                status: "finalized",
                sections: [
                    {
                        section_type: "findings",
                        content: report.findings,
                    },
                    {
                        section_type: "impression",
                        content: report.impression,
                    },
                    {
                        section_type: "advice",
                        content: report.advice,
                    },
                ],
            };

            await updateReport(reportId, payload);
            setStatus("finalized");

            alert("Report finalized successfully!");
            navigate("/dashboard");
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.detail ??
                "Failed to finalize report."
            );
        }
    }

    if (!report) {
        return <h2>Loading...</h2>;
    }

    return (
        <>
            <h1>View Report</h1>

            <p>
                <strong>Patient:</strong> {patientName}
            </p>

            <p>
                <strong>Status:</strong> {status.charAt(0).toUpperCase() + status.slice(1)}
            </p>

            <h3>Findings</h3>
            <textarea
                value={report.findings ?? ""}
                onChange={(e) =>
                    setReport({
                        ...report,
                        findings: e.target.value,
                    })
                }
            />

            <h3>Impression</h3>
            <textarea
                value={report.impression ?? ""}
                onChange={(e) =>
                    setReport({
                        ...report,
                        impression: e.target.value,
                    })
                }
            />

            <h3>Advice</h3>
            <textarea
                value={report.advice ?? ""}
                onChange={(e) =>
                    setReport({
                        ...report,
                        advice: e.target.value,
                    })
                }
            />

            <br />
            <br />

            <button 
                onClick={handleSave}
                disabled={status === "finalized"}
            >
                Save Changes
            </button>

            <button
                onClick={handleFinalize}
                disabled={status === "finalized"}
                style={{ marginLeft: "10px" }}
            >
                Finalize Report
            </button>
        </>
    );
}

export default ReportEditPage;