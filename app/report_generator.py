from datetime import datetime


def generate_markdown(scan_data, health_data):
    report = "# Automated Bootstrap Health Report\n\n"

    report += f"Generated On: {datetime.now()}\n\n"

    report += "## Scan Results\n\n"

    for item, status in scan_data.items():
        symbol = "✅" if status else "❌"
        report += f"- {symbol} {item}\n"

    report += "\n## Health Summary\n\n"
    report += f"- Health Score: {health_data['score']}%\n"
    report += f"- Status: {health_data['status']}\n"

    return report