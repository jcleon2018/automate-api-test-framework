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
@pytest.mark.parametrize("invalid_env_name", INVALID_ENV_NAMES)
def test_invalid_conda_environment_creation(invalid_env_name):
    """Test invalid Conda environment names."""
    stdout, stderr = run_command(CONDA_COMMANDS["create"](invalid_env_name, PYTHON_VERSION))
    assert "error" in stderr.lower() or "invalid" in stderr.lower(), f"Conda accepted invalid env name: {invalid_env_name}"
