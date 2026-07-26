import { BrowserRouter, Routes, Route} from "react-router-dom"
import LoginPage from "../pages/LoginPage"
import Dashboard from "../pages/Dashboard"
import ProtectedRoute from "../components/ProtectedRoute"
import NewReportPage from "../pages/NewReportPage"
import ReportEditPage from "../pages/ReportEditPage"
import PatientsPage from "../pages/PatientsPage"
import PatientEditPage from "../pages/PatientEditPage"
import PatientCreatePage from "../pages/PatientCreatePage"

function AppRoutes(){
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/login" element={
                        <LoginPage />
                    }></Route>

                    <Route path="/report" element={
                        <ProtectedRoute>
                            <NewReportPage />
                        </ProtectedRoute>
                    }></Route>

                    <Route path="/report/:reportId" element={
                        <ProtectedRoute>
                            <ReportEditPage />
                        </ProtectedRoute>
                    }></Route>

                    <Route path="/dashboard" element={
                        <ProtectedRoute>
                            <Dashboard />
                        </ProtectedRoute>
                    }></Route>

                    <Route path="/patients" element={
                        <ProtectedRoute>
                            <PatientsPage />
                        </ProtectedRoute>
                    }></Route>

                    <Route path="/patients/edit/:patientId" element={
                        <ProtectedRoute>
                            <PatientEditPage />
                        </ProtectedRoute>
                    }></Route>

                    <Route path="/patients/new" element={
                        <ProtectedRoute>
                            <PatientCreatePage />
                        </ProtectedRoute>
                    }></Route>

                </Routes>
            </BrowserRouter>
        </>
    )
}

export default AppRoutes;   