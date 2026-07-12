import { NavLink } from "react-router-dom";
import "../styles/sidebar.css";

import {
  FaHome,
  FaSearch,
  FaHistory,
  FaChartBar,
  FaCog,
  FaShieldAlt
} from "react-icons/fa";


function Sidebar() {

  return (

    <aside className="sidebar">

      <div className="logo">
        <FaShieldAlt />
        <h2>PhishGuard AI</h2>
      </div>


      <nav>

        <NavLink to="/dashboard">
          <FaHome />
          Dashboard
        </NavLink>


        <NavLink to="/scan">
          <FaSearch />
          Scan URL
        </NavLink>


        <NavLink to="/history">
          <FaHistory />
          History
        </NavLink>


        <NavLink to="/reports">
          <FaChartBar />
          Reports
        </NavLink>


        <NavLink to="/settings">
          <FaCog />
          Settings
        </NavLink>

      </nav>


    </aside>

  );

}

export default Sidebar;