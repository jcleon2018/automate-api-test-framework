import pytest
import os
import logging
from conda_commands import CONDA_COMMANDS, run_command, environment_exists

ENV_NAME = "test_env1"
PYTHON_VERSION = "3.9"
CLONE_ENV_NAME = "test_env_clone"
EXPORT_FILE = "environment.yml"
INVALID_ENV_NAMES = ["env with space", "env/name", "env#test"]

@pytest.mark.order(1)
def test_conda_installed():
    """Test Conda is installed."""
    stdout, stderr = run_command(CONDA_COMMANDS["check_installed"])
    assert "conda" in stdout.lower(), f"Unexpected output for Conda version check: {stdout}"

@pytest.mark.order(2)
def test_create_conda_environment():
    """Test Conda environment creation."""
    if not environment_exists(ENV_NAME):
        stdout, stderr = run_command(CONDA_COMMANDS["create"](ENV_NAME, PYTHON_VERSION))
        assert "done" in stdout.lower() or "created" in stdout.lower(), f"Environment creation failed: {stderr}"
    assert environment_exists(ENV_NAME), f"'{ENV_NAME}' does not exist after creation!"

@pytest.mark.order(3)
def test_check_environment_exists():
    """Test Conda environment existence."""
    stdout, _ = run_command(CONDA_COMMANDS["list_envs"])
    assert environment_exists(ENV_NAME), f"'{ENV_NAME}' not found in Conda env list."

@pytest.mark.order(4)
def test_activate_environment():
    """Test Conda environment activation."""
    stdout, stderr = run_command(CONDA_COMMANDS["activate"](ENV_NAME))
    assert "activate" in stderr.lower(), f"Failed to activate '{ENV_NAME}': {stderr}"

@pytest.mark.order(6)
def test_export_environment():
    """Test exporting an environment to a YAML file."""
    assert environment_exists(ENV_NAME), f"'{ENV_NAME}' does not exist!"
    run_command(CONDA_COMMANDS["export"](ENV_NAME, EXPORT_FILE))
    assert os.path.exists(EXPORT_FILE), "Export failed!"

@pytest.mark.order(7)
def test_recreate_environment():
    """Test recreating an environment from an export file."""
    assert os.path.exists(EXPORT_FILE), "Export file not found!"
    run_command(CONDA_COMMANDS["recreate"](EXPORT_FILE))
    assert environment_exists(ENV_NAME), "Failed to recreate environment!"

@pytest.mark.order(8)
def test_clone_environment():
    """Test cloning an existing environment."""
    assert environment_exists(ENV_NAME), f"'{ENV_NAME}' does not exist!"
    run_command(CONDA_COMMANDS["clone"](ENV_NAME, CLONE_ENV_NAME))
    assert environment_exists(CLONE_ENV_NAME), "Failed to clone environment!"

@pytest.mark.order(9)
def test_list_environments():
    """Test listing Conda environments."""
    stdout, _ = run_command(CONDA_COMMANDS["list_envs"])
    assert ENV_NAME in stdout, f"'{ENV_NAME}' not found!"
    assert CLONE_ENV_NAME in stdout, f"'{CLONE_ENV_NAME}' not found!"

@pytest.mark.order(10)
def test_remove_conda_environment():
    """Test removing Conda environments."""
    if environment_exists(ENV_NAME):
        run_command(CONDA_COMMANDS["remove"](ENV_NAME))
        assert not environment_exists(ENV_NAME), "Environment not removed!"

    if environment_exists(CLONE_ENV_NAME):
        run_command(CONDA_COMMANDS["remove"](CLONE_ENV_NAME))
        assert not environment_exists(CLONE_ENV_NAME), "Clone environment not removed!"

