import pytest
from conda_commands import CONDA_COMMANDS, run_command

FAKE_ENV = "fake_env"
INVALID_PACKAGE = "invalid_package"
CONFLICTING_PACKAGES = ["tensorflow", "pytorch"]
PROBLEMATIC_PACKAGE = "problematic-package"
PYTHON_VERSION = "3.9"
INVALID_ENV_NAMES = ["env with space", "env/name", "env#test"]

@pytest.mark.order(1)
def test_install_invalid_package():
    """Test attempting to install an invalid package."""
    stdout, stderr = run_command(CONDA_COMMANDS["install_package"](INVALID_PACKAGE))
    assert "package not found" in stderr.lower() or "invalid" in stderr.lower(), f"Unexpected response: {stderr}"

@pytest.mark.order(2)
def test_simulate_network_failure():
    """Test network failure during package installation."""
    stdout, stderr = run_command("conda install numpy -y --override-channels --channel fake_channel")
    assert "failed" in stderr.lower() or "could not find" in stderr.lower(), f"Unexpected response: {stderr}"

@pytest.mark.order(3)
def test_simulate_network_failure():
    """Test network failure during package installation."""
    stdout, stderr = run_command("conda install numpy -y --override-channels --channel fake_channel")

    expected_errors = ["failed", "could not find", "unavailableinvalidchannel", "http 404 not found"]
    assert any(error in stderr.lower() for error in expected_errors), f"Unexpected response: {stderr}"

