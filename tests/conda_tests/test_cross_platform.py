import os
import pytest
import platform
from conda_commands import CONDA_COMMANDS, run_command, environment_exists

ENV_NAME = "test_env"
PYTHON_VERSION = "3.9"

# Define supported platforms
SUPPORTED_PLATFORMS = ["Linux", "Windows", "Darwin"]  # Darwin = macOS


##----------------------------------------------------------------------------
## Test needs to e ran in different OS platform
##----------------------------------------------------------------------------
@pytest.mark.parametrize("os_name", SUPPORTED_PLATFORMS)
@pytest.mark.order(1)
def test_create_conda_env(os_name):
    """Test Conda environment creation across different OS platforms."""
    current_os = platform.system()
    
    if current_os != os_name:
        pytest.skip(f"Skipping test for {os_name}: Running on {current_os}")

    stdout, stderr = run_command(CONDA_COMMANDS["create"](ENV_NAME, PYTHON_VERSION))
    assert environment_exists(ENV_NAME), f"Failed to create environment on {os_name}: {stderr}"



DOCKERFILE_CONTENT = """\
FROM continuumio/miniconda3
RUN conda create --name test_env python=3.9 -y
SHELL ["conda", "run", "-n", "test_env", "/bin/bash", "-c"]
"""
@pytest.mark.order(3)
def test_conda_inside_docker():
    """Test Conda setup in a containerized environment."""
    pytest.skip(f"Skipping Docker Test as this requires to be installed.")
    with open("Dockerfile", "w") as f:
        f.write(DOCKERFILE_CONTENT)

    os.system("docker build -t conda_test .")
    stdout = os.popen("docker run --rm conda_test python --version").read()

    assert "3.9" in stdout, "Python version mismatch in Docker!"
