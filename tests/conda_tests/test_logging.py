import pytest
import time
import json
import logging
from conda_commands import CONDA_COMMANDS, run_command, logger

INSTALLATION_REPORT = {}

@pytest.mark.order(1)
def test_installation_time():
    """Measure installation time for large packages like TensorFlow."""
    start_time = time.time()
    
    stdout, stderr = run_command(CONDA_COMMANDS["install_package"]("tensorflow"))

    end_time = time.time()
    duration = end_time - start_time
    INSTALLATION_REPORT["tensorflow_installation_time"] = duration

    assert "installed" in stdout.lower(), f"TensorFlow installation failed: {stderr}"
    logger.info(f"TensorFlow installation took {duration:.2f} seconds.")

@pytest.mark.order(3)
def test_capture_installation_logs():
    """Capture installation logs to analyze failures."""
    stdout, stderr = run_command(CONDA_COMMANDS["install_package"]("tensorflow"))

    INSTALLATION_REPORT["tensorflow_install_logs"] = {"stdout": stdout, "stderr": stderr}

    assert "installed" in stdout.lower(), f"TensorFlow installation failed: {stderr}"

@pytest.mark.order(4)
def test_generate_execution_report():
    """Generate a test execution report in JSON format."""
    with open("installation_report.json", "w") as report_file:
        json.dump(INSTALLATION_REPORT, report_file, indent=4)

    logger.info("Installation report generated.")
    assert True, "Test report successfully created."
