import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", force=True)
logger = logging.getLogger()

def run_command(command):
    """Execute shell commands and return output."""
    logger.info(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    stdout, stderr = result.stdout.strip(), result.stderr.strip()

    if stdout:
        logger.info(f"Output:\n{stdout}")
    if stderr:
        logger.error(f"Error:\n{stderr}")

    return stdout, stderr

def environment_exists(env_name):
    """Check if a Conda environment exists."""
    stdout, _ = run_command(CONDA_COMMANDS["list_envs"])
    return env_name in stdout

CONDA_COMMANDS = {
    # Environment Management
    "list_envs": "conda env list",
    "check_installed": "conda --version",
    "create": lambda env, py_ver: f"conda create --name {env} python={py_ver} -y",
    "activate": lambda env: f"conda activate {env}",
    "deactivate": lambda: "conda deactivate",  # Added deactivate command
    "init": lambda: "conda init",  # Added init command
    "remove": lambda env: f"conda remove --name {env} --all -y",
    "clone": lambda source, target: f"conda create --name {target} --clone {source} -y",
    "update_env": lambda env: f"conda env update --name {env}",

    # Environment Export & Recreation
    "export": lambda env, file: f"conda env export --name {env} > {file}",
    "recreate": lambda file: f"conda env create -f {file}",

    # Conda Cleanup & Info
    "clean_all": "conda clean --all -y",
    "info": "conda info",

    # Package Management
    "search_package": lambda package: f"conda search {package}",
    "install_package": lambda package: f"conda install {package} -y",
    "uninstall_package": lambda package: f"conda remove {package} -y",
    "list_package": lambda package: f"conda list {package}",
    "check_integrity": "conda list --explicit",
    "update_package": lambda package: f"conda update {package} -y",
}
