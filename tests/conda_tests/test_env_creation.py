import os
import sys
import subprocess
import pytest
import logging

# Configure logging for detailed output
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", force=True)
logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

ENV_NAME = "test_env1"
PYTHON_VERSION = "3.9"
INVALID_ENV_NAMES = [
    "env with space",  # Spaces are not allowed
    "env/name",        # Slashes are not allowed
    "env#test",        # Special characters (#) are not allowed
]

CLONE_ENV_NAME = "test_env_clone"
EXPORT_FILE = "environment.yml"

def run_command(command):
    """Helper function to execute shell commands and log output."""
    logging.info(f"Executing command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    stdout, stderr = result.stdout.strip(), result.stderr.strip()
    
    if stdout:
        logging.info(f"Command Output:\n{stdout}")
    if stderr:
        logging.error(f"Command Error:\n{stderr}")
    
    return stdout, stderr

def environment_exists(env_name):
    """Check if a Conda environment exists."""
    stdout, _ = run_command("conda env list")
    return env_name in stdout

#-----------------------------------------------------------------------------
# Tests defenition Section. Test are ran in order of appearance.
#-----------------------------------------------------------------------------

def test_conda_installed():
    """Test Conda is installed."""
    stdout, stderr = run_command("conda --version")
    
    assert "conda" in stdout.lower(), f"Unexpected output for Conda version check: {stdout}"

@pytest.mark.parametrize("env_name, python_version", [
    (ENV_NAME, PYTHON_VERSION)
    ])
def test_create_conda_environment(env_name, python_version):
    """Test Conda environment creation."""
    logging.info(f"Creating Conda environment: {env_name} with Python {python_version}")
    create_cmd = f"conda create --name {env_name} python={python_version} -y"
    stdout, stderr = run_command(create_cmd)
    
    assert any(word in stdout.lower() for word in ["done", "created"]), f"Environment creation failed: {stderr}"
    assert environment_exists(ENV_NAME), f"Environment '{ENV_NAME}' does not exist after creation!"    

@pytest.mark.parametrize("env_name", [
    (ENV_NAME)
    ])
def test_check_environment_exists(env_name):
    """Test Conda environment existence."""
    logging.info(f"Checking if environment '{ENV_NAME}' exists.")
    list_cmd = "conda env list"
    stdout, _ = run_command(list_cmd)
    
    assert environment_exists(env_name), f"Environment '{ENV_NAME}' not found in Conda env list."

@pytest.mark.parametrize("env_name", [
    (ENV_NAME)
    ])
def test_activate_environment(env_name):
    """Test Conda environment activation."""
    logging.info(f"Activating Conda environment: {ENV_NAME}")
    activate_cmd = f"conda activate {ENV_NAME}"
    stdout, stderr = run_command(activate_cmd)
    
    assert any(keyword in stdout or keyword in stderr.lower() for keyword in [ENV_NAME, "activate"]), f"Failed to activate environment: {stderr}"

def test_remove_conda_environment():
    """Test Remove Conda environment."""
    logging.info(f"Removing Conda environment: {ENV_NAME}")

    if environment_exists(ENV_NAME):
        remove_cmd = f"conda remove --name {ENV_NAME} --all -y"
        stdout, stderr = run_command(remove_cmd)
        assert "removed" in stdout.lower() or "delete" in stdout.lower(), f"Failed to remove environment: {stderr}"
    else:
        pytest.skip(f"Skipping removal: Environment '{ENV_NAME}' does not exist.")

@pytest.mark.parametrize("invalid_env_name", INVALID_ENV_NAMES)
def test_invalid_conda_environment_creation(invalid_env_name):
    """Test Negative. Create Conda environments with invalid names."""
    create_cmd = f"conda create --name {invalid_env_name} python={PYTHON_VERSION} -y"
    stdout, stderr = run_command(create_cmd)

    # Conda should return an error message
    assert "error" in stderr.lower() or "invalid" in stderr.lower(), f"Conda accepted invalid env name: {invalid_env_name}"

@pytest.mark.order(1)
def test_create_conda_env():
    """Test Conda environment creation."""
    logging.info(f"Creating Conda environment: {ENV_NAME} with Python {PYTHON_VERSION}")
    create_cmd = f"conda create --name {ENV_NAME} python={PYTHON_VERSION} -y"
    stdout, stderr = run_command(create_cmd)
    
    assert any(word in stdout.lower() for word in ["done", "created"]), f"Environment creation failed: {stderr}"
    assert environment_exists(ENV_NAME), f"Environment '{ENV_NAME}' does not exist after creation!"    

@pytest.mark.order(2)
def test_export_environment():
    """Test exporting an environment to a YAML file."""
    assert environment_exists(ENV_NAME), f"Environment '{ENV_NAME}' does not exist!"
    
    export_cmd = f"conda env export --name {ENV_NAME} > {EXPORT_FILE}"
    stdout, stderr = run_command(export_cmd)
    
    assert os.path.exists(EXPORT_FILE), f"Export failed: {stderr}"
    assert "dependencies" in open(EXPORT_FILE).read(), "Exported file does not contain environment data"

@pytest.mark.order(3)
def test_recreate_environment():
    """Test recreating an environment from an export file."""
    assert os.path.exists(EXPORT_FILE), f"Export file '{EXPORT_FILE}' not found!"

    recreate_cmd = f"conda env create -f {EXPORT_FILE}"
    stdout, stderr = run_command(recreate_cmd)

    assert environment_exists(ENV_NAME), f"Failed to recreate environment from {EXPORT_FILE}: {stderr}"

@pytest.mark.order(4)
def test_clone_environment():
    """Test cloning an existing environment."""
    assert environment_exists(ENV_NAME), f"Environment '{ENV_NAME}' does not exist!"
    
    clone_cmd = f"conda create --name {CLONE_ENV_NAME} --clone {ENV_NAME} -y"
    stdout, stderr = run_command(clone_cmd)

    assert environment_exists(CLONE_ENV_NAME), f"Failed to clone environment '{ENV_NAME}': {stderr}"

@pytest.mark.order(5)
def test_list_environments():
    """Test listing Conda environments."""
    list_cmd = "conda env list"
    stdout, stderr = run_command(list_cmd)

    assert ENV_NAME in stdout, f"'{ENV_NAME}' not found in Conda environment list!"
    assert CLONE_ENV_NAME in stdout, f"'{CLONE_ENV_NAME}' not found in Conda environment list!"

