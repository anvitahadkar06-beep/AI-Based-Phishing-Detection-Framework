import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ScanURL from "./pages/ScanURL";
import History from "./pages/History";
import Reports from "./pages/Reports";
import Layout from "./components/Layout";

function App() {
  return (
    <BrowserRouter>

    <ToastContainer />

      <Routes>

        {/* Login Page */}
        <Route path="/" element={<Login />} />

        <Route element={<Layout />}>

        {/* Dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* URL Scanner */}
        <Route path="/scan" element={<ScanURL />} />

        {/* Scan History */}
        <Route path="/history" element={<History />} />

        {/* Reports */}
        <Route path="/reports" element={<Reports />} />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;
