function ResultCard({ result }) {

    const safe = result.prediction === "LEGITIMATE";

    return (

        <div
            style={{
                marginTop: "30px",
                background: "#ffffff",
                color: "#111827",
                borderRadius: "16px",
                padding: "25px",
                boxShadow: "0 10px 30px rgba(0,0,0,0.25)",
                textAlign: "left"
            }}
        >

            <h2
                style={{
                    color: safe ? "#16a34a" : "#dc2626",
                    marginBottom: "20px"
                }}
            >
                {safe ? "🟢 SAFE" : "🔴 PHISHING"}
            </h2>

            <p><strong>🌐 URL:</strong> {result.url}</p>

            <p><strong>🎯 Confidence:</strong> {result.confidence}%</p>
            <div
    style={{
        width: "100%",
        height: "12px",
        background: "#e5e7eb",
        borderRadius: "10px",
        overflow: "hidden",
        marginBottom: "20px"
    }}
>
    <div
        style={{
            width: `${result.confidence}%`,
            height: "100%",
            background:
                result.prediction === "LEGITIMATE"
                    ? "#16a34a"
                    : "#dc2626",
            transition: "width 0.5s ease"
        }}
    />
</div>

            <div style={{ margin: "15px 0" }}>
    <strong>⚠ Risk: </strong>

    <span
        style={{
            background:
                result.risk === "LOW"
                    ? "#16a34a"
                    : result.risk === "MEDIUM"
                    ? "#f59e0b"
                    : "#dc2626",
            color: "white",
            padding: "6px 12px",
            borderRadius: "20px",
            fontSize: "14px",
            marginLeft: "8px"
        }}
    >
        {result.risk}
    </span>
</div>

<div style={{ marginBottom: "20px" }}>
    <strong>🛡 Trusted: </strong>

    <span
        style={{
            background: result.trusted ? "#16a34a" : "#dc2626",
            color: "white",
            padding: "6px 12px",
            borderRadius: "20px",
            fontSize: "14px",
            marginLeft: "8px"
        }}
    >
        {result.trusted ? "YES" : "NO"}
    </span>
</div>

            <hr style={{ margin: "20px 0" }} />

            <h3>Reasons</h3>

            <ul>
                {result.reasons.map((reason, index) => (
                    <li
    key={index}
    style={{
        marginBottom: "10px",
        listStyle: "none"
    }}
>
    ✅ {reason}
</li>
                ))}
            </ul>

        </div>

    );

}

export default ResultCard;