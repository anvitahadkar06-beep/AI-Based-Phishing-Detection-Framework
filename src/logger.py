import csv
import os
from datetime import datetime

LOG_PATH = "data/logs/scan_history.csv"


def log_scan(result):

    os.makedirs("data/logs", exist_ok=True)

    file_exists = os.path.exists(LOG_PATH)

    with open(LOG_PATH, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "URL",
                "Prediction",
                "Confidence",
                "Risk",
                "Trusted",
                "RuleScore"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            result["url"],
            result["prediction"],
            result["confidence"],
            result["risk"],
            result["trusted"],
            result["rule_score"]
        ])