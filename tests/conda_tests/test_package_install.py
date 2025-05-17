import subprocess
import pytest

# Packages to test
PACKAGE_SINGLE = "numpy"
PACKAGE_MULTIPLE = ["pandas", "scikit-learn"]

def run_command(command):
    """Execute shell commands and return output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

@pytest.mark.order(1)
def test_search_package():
    """Test searching for a package before installing."""
    search_cmd = f"conda search {PACKAGE_SINGLE}"
    stdout, stderr, returncode = run_command(search_cmd)

    assert returncode == 0, f"Failed to search package '{PACKAGE_SINGLE}': {stderr}"
    assert PACKAGE_SINGLE in stdout, f"Package '{PACKAGE_SINGLE}' not found!"

@pytest.mark.order(2)
def test_install_package():
    """Test installing a single package."""
    install_cmd = f"conda install {PACKAGE_SINGLE} -y"
    stdout, stderr, returncode = run_command(install_cmd)

    assert returncode == 0, f"Failed to install package '{PACKAGE_SINGLE}': {stderr}"
    assert PACKAGE_SINGLE in stdout, f"Installation did not report '{PACKAGE_SINGLE}'!"

@pytest.mark.order(3)
def test_install_multiple_packages():
    """Test installing multiple packages simultaneously."""
    install_cmd = f"conda install {' '.join(PACKAGE_MULTIPLE)} -y"
    stdout, stderr, returncode = run_command(install_cmd)

    assert returncode == 0, f"Failed to install multiple packages: {stderr}"
    for package in PACKAGE_MULTIPLE:
        assert package in stdout, f"Package '{package}' was not installed!"

@pytest.mark.order(4)
def test_verify_package_version():
    """Test verifying installed package version."""
    version_cmd = f"conda list {PACKAGE_SINGLE}"
    stdout, stderr, returncode = run_command(version_cmd)

    assert returncode == 0, f"Failed to list package '{PACKAGE_SINGLE}': {stderr}"
    assert PACKAGE_SINGLE in stdout, f"Package '{PACKAGE_SINGLE}' is not installed!"

@pytest.mark.order(5)
def test_uninstall_package():
    """Test uninstalling a package and confirming removal."""
    uninstall_cmd = f"conda uninstall {PACKAGE_SINGLE} -y"
    stdout, stderr, returncode = run_command(uninstall_cmd)

    assert returncode == 0, f"Failed to uninstall package '{PACKAGE_SINGLE}': {stderr}"

    # Verify removal
    list_cmd = f"conda list {PACKAGE_SINGLE}"
    stdout, stderr, returncode = run_command(list_cmd)
    assert PACKAGE_SINGLE not in stdout, f"Package '{PACKAGE_SINGLE}' was not removed!"

@pytest.mark.order(6)
def test_check_package_integrity():
    """Test checking package integrity."""
    integrity_cmd = "conda list --explicit"
    stdout, stderr, returncode = run_command(integrity_cmd)

    assert returncode == 0, f"Failed to check package integrity: {stderr}"
    assert "@" in stdout, "Package integrity listing is incorrect!"

