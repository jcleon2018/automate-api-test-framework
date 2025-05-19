import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pytest Execution Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2C3E50; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #3498DB; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Pytest Execution Report</h1>
    <table>
        <tr><th>Test Name</th><th>Outcome</th><th>Duration (s)</th></tr>
        {rows}
    </table>
</body>
</html>
"""

def json_to_html(json_file, output_file):
    """Convert JSON test report to HTML table format."""
    with open(json_file, "r") as file:
        report = json.load(file)

    rows = ""
    for test in report.get("tests", []):
        test_name = test.get("nodeid", "Unknown")
        outcome = test.get("outcome", "Unknown")
        duration = test.get("call", {}).get("duration", "N/A")
        rows += f"<tr><td>{test_name}</td><td>{outcome}</td><td>{duration:.2f}</td></tr>\n"

    html_content = HTML_TEMPLATE.format(rows=rows)

    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"HTML report generated: {output_file}")

# Convert JSON report to HTML
json_to_html("tests/conda_tests/test_report.json", "tests/conda_tests/test_report.html")

