import { FaBell, FaUserCircle } from "react-icons/fa";
import "../styles/navbar.css";

function Navbar() {

  return (

    <header className="navbar">

      <div className="navbar-title">
        AI Phishing Detection System
      </div>


      <div className="navbar-actions">

        <FaBell className="nav-icon" />

        <div className="user-profile">
          <FaUserCircle className="nav-icon" />
          <span>Admin</span>
        </div>

      </div>

    </header>

  );

}

export default Navbar;