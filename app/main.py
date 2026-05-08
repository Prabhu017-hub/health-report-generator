import os

from scanner import scan_project
from analyzer import calculate_health
from report_generator import generate_markdown


PROJECT_PATH = "sample_project"


os.makedirs("reports", exist_ok=True)


scan_result = scan_project(PROJECT_PATH)


health_result = calculate_health(scan_result)


markdown_report = generate_markdown(
    scan_result,
    health_result
)


report_path = "reports/health_report.md"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(markdown_report)


print("Health report generated successfully")
print(f"Report saved at: {report_path}")