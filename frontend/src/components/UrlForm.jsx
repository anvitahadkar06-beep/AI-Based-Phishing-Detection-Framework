import { useState } from "react";
import { predictURL } from "../services/api";
import Loader from "./Loader";
import ResultCard from "./ResultCard";

function UrlForm() {

    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleSubmit = async () => {

        if (!url.trim()) {
            alert("Please enter a URL.");
            return;
        }

        try {

            setLoading(true);

            const response = await predictURL(url);

            setResult(response.data);
            alert("Analysis Complete!");

        } catch (error) {

            console.error(error);
            alert("Backend Offline");

        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="url-form">

            <input
                type="text"
                placeholder="https://example.com"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />

            <button onClick={handleSubmit}>
                Analyze URL
            </button>
            {
    !loading && !result &&

    <div
        style={{
            marginTop:"40px",
            color:"#94a3b8"
        }}
    >

        🛡 Enter a website URL above to begin phishing analysis.

    </div>
}
            {loading && <Loader />}

            {result && <ResultCard result={result} />}


        </div>

    );
}

export default UrlForm;