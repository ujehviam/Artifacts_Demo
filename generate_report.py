import json

report = {
    "status": "success",
    "metrics": {
        "accuracy": 0.93,
        "loss": 0.12
    }
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Report generated.")