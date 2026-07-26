import { BrowserRouter, Routes, Route} from "react-router-dom"
import LoginPage from "../pages/LoginPage"
import Dashboard from "../pages/Dashboard"
import ProtectedRoute from "../components/ProtectedRoute"
import NewReportPage from "../pages/NewReportPage"
import ReportEditPage from "../pages/ReportEditPage"

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

                </Routes>
            </BrowserRouter>
        </>
    )
}

export default AppRoutes;   