import pytest
import subprocess

ENV_NAMES = ["test_env1", "test_env2"]
PYTHON_VERSION = "3.9"

def run_command(command):
    """Execute shell commands and return output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def environment_exists(env_name):
    """Check if a Conda environment exists."""
    stdout, _, _ = run_command("conda env list")
    return env_name in stdout

# Define Conda actions in a reusable dictionary
CONDA_COMMANDS = {
    "create": lambda env: f"conda create --name {env} python={PYTHON_VERSION} -y",
    "activate": lambda env: f"bash -c 'source ~/.bashrc && conda activate {env}'",
    "remove": lambda env: f"conda env remove --name {env} -y",
}

@pytest.fixture(scope="module", autouse=True)
def setup_test_environments():
    """Setup: Ensure test environments exist before running tests."""
    for env_name in ENV_NAMES:
        if not environment_exists(env_name):
            stdout, stderr, returncode = run_command(CONDA_COMMANDS["create"](env_name))
            assert returncode == 0, f"Failed to create '{env_name}': {stderr}"
            print(f"Environment '{env_name}' created successfully!")

@pytest.mark.parametrize("env_name", ENV_NAMES)
def test_switch_environment(env_name):
    """Test switching between Conda environments."""
    assert environment_exists(env_name), f"Skipping activation: '{env_name}' does not exist."

    stdout, stderr, returncode = run_command(CONDA_COMMANDS["activate"](env_name))
    assert returncode == 0, f"Failed to activate '{env_name}': {stderr}"

@pytest.mark.parametrize("env_name", ENV_NAMES)
def test_remove_conda_environment(env_name):
    """Cleanup: Remove test environments after tests."""
    if environment_exists(env_name):
        stdout, stderr, returncode = run_command(CONDA_COMMANDS["remove"](env_name))
        assert returncode == 0, f"Failed to remove '{env_name}': {stderr}"

