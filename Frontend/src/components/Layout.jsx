import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
import "../styles/layout.css";

function Layout() {
  return (
    <div className="dashboard-layout">

      <Sidebar />
      <div className="dashboard-area">
        <Navbar />

      <main className="main-content">
        <Outlet />
      </main>

    </div>
    </div>
  );
}

export default Layout;