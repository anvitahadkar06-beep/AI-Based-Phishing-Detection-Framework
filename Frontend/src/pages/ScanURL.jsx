import { useState } from "react";
import { FaSearch, FaShieldAlt } from "react-icons/fa";
import { toast } from "react-toastify";
import API from "../services/api";
import "../styles/scanURL.css";

function ScanURL() {
  const [inputUrl, setInputUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleScan = async () => {
    if (!inputUrl.trim()) {
      toast.warning("Please enter a URL.");
      return;
    }

    try {
      new URL(inputUrl);
    } catch {
      toast.error("Please enter a valid URL.");
      return;
    }

    setLoading(true);
    setResult(null);
    setProgress(0);

    const timer = setInterval(() => {
      setProgress((old) => {
        if (old >= 90) {
          clearInterval(timer);
          return 90;
        }
        return old + 10;
      });
    }, 300);

    try {
      const response = await API.post("/predict", {
        url: inputUrl,
      });

      clearInterval(timer);
      setProgress(100);

      setTimeout(() => {
        setResult(response.data);
        saveToHistory(response.data);
        setLoading(false);
      }, 500);
    } catch (error) {
      clearInterval(timer);
      setLoading(false);

      if (error.response) {
        toast.error(error.response.data.error || "Prediction failed");
      } else {
        toast.error("Cannot connect to Flask backend");
      }
    }
  };

  const saveToHistory = (data) => {
    const history =
      JSON.parse(localStorage.getItem("scanHistory")) || [];

    const newRecord = {
      url: inputUrl,
      prediction: data.prediction,
      confidence: data.confidence,
      risk: data.risk,
      date: new Date().toLocaleString(),
    };

    localStorage.setItem(
      "scanHistory",
      JSON.stringify([newRecord, ...history])
    );
  };

  return (
    <div className="scan-container">
      <h1>
        <FaShieldAlt /> AI URL Security Scanner
      </h1>

      <p>Machine Learning Based Phishing Detection Analysis</p>

      <div className="scan-box">
        <input
          type="text"
          placeholder="https://example.com"
          value={inputUrl}
          onChange={(e) => setInputUrl(e.target.value)}
        />

        <button onClick={handleScan}>
          <FaSearch /> Scan
        </button>
      </div>

      {loading && (
        <div className="scanner">
          <div className="loader"></div>

          <h3>Analyzing URL...</h3>

          <div className="progress">
            <div
              className="progress-value"
              style={{
                width: `${progress}%`,
              }}
            ></div>
          </div>

          <p>
            Checking URL Features...
            <br />
            Running AI Model...
            <br />
            Evaluating Security...
          </p>
        </div>
      )}

      {result && (
        <div className="result-card">
          <h2>Security Analysis Report</h2>

          <div className="risk-meter">
            <div className="circle">{result.confidence}%</div>
            <p>Confidence Score</p>
          </div>

          <div className="result-details">
            <p>
              <strong>Status:</strong>{" "}
              <span
                className={
                  result.prediction === "PHISHING"
                    ? "danger"
                    : "safe"
                }
              >
                {result.prediction}
              </span>
            </p>

            <p>
              <strong>Risk Level:</strong> {result.risk}
            </p>

            <p>
              <strong>Confidence:</strong> {result.confidence}%
            </p>

            {result.trusted !== undefined && (
              <p>
                <strong>Trusted:</strong>{" "}
                {result.trusted ? "Yes ✅" : "No ❌"}
              </p>
            )}
          </div>

          {result.reasons && result.reasons.length > 0 && (
            <div className="security-checks">
              <h3>Reasons</h3>

              <ul>
                {result.reasons.map((reason, index) => (
                  <li key={index}>✔ {reason}</li>
                ))}
              </ul>
            </div>
          )}

          <div className="security-checks">
            <h3>Security Checks</h3>

            <ul>
              <li>✔ URL Feature Extraction</li>
              <li>✔ Machine Learning Prediction</li>
              <li>✔ Rule-Based Detection</li>
              <li>✔ Domain Reputation Analysis</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default ScanURL;