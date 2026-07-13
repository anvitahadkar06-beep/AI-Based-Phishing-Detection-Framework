import "./App.css";

import Navbar from "./components/Navbar";
import UrlForm from "./components/UrlForm";

function App() {

  return (

    <div className="app">

      <Navbar />

      <main>

        <h1>🛡️ AI-Based Phishing Detection</h1>

        <p>
  Instantly analyze websites using Machine Learning and rule-based detection.
        </p>

        <UrlForm />

      </main>

    </div>

  );

}

export default App;