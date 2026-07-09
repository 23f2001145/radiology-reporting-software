import { BrowserRouter, Routes, Route} from "react-router-dom"
import NewReportPage from "../pages/NewReportPage"

function AppRoutes(){
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/report" element={<NewReportPage />}></Route>
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default AppRoutes