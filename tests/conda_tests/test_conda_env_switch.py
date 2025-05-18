import pytest
import logging
from conda_commands import CONDA_COMMANDS, run_command, environment_exists

ENV_NAMES = ["test_env1", "test_env2"]
PYTHON_VERSION = "3.9"

@pytest.fixture(scope="module", autouse=True)
def setup_test_environments():
    """Setup: Ensure test environments exist before running tests."""
    for env_name in ENV_NAMES:
        if not environment_exists(env_name):
            stdout, stderr = run_command(CONDA_COMMANDS["create"](env_name, PYTHON_VERSION))
            assert environment_exists(env_name), f"Failed to create '{env_name}': {stderr}"
            logging.info(f"Environment '{env_name}' created successfully!")

@pytest.mark.parametrize("env_name", ENV_NAMES)
def test_switch_environment(env_name):
    """Test switching between Conda environments."""
    assert environment_exists(env_name), f"Skipping activation: '{env_name}' does not exist."

    stdout, stderr = run_command(CONDA_COMMANDS["activate"](env_name))
    assert "activate" in stderr.lower(), f"Failed to activate '{env_name}': {stderr}"

@pytest.mark.parametrize("env_name", ENV_NAMES)
def test_remove_conda_environment(env_name):
    """Cleanup: Remove test environments after tests."""
    if environment_exists(env_name):
        stdout, stderr = run_command(CONDA_COMMANDS["remove"](env_name))
        assert "removed" in stdout.lower() or "delete" in stdout.lower(), f"Failed to remove '{env_name}': {stderr}"

