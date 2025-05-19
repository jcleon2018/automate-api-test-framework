import pytest
import logging
from conda_commands import CONDA_COMMANDS, run_command

# Packages to test
PACKAGE_SINGLE = "numpy"
PACKAGE_MULTIPLE = ["pandas", "scikit-learn"]

@pytest.mark.order(1)
def test_search_package():
    """Test searching for a package before installing."""
    stdout, stderr = run_command(CONDA_COMMANDS["search_package"](PACKAGE_SINGLE))
    assert PACKAGE_SINGLE in stdout, f"Package '{PACKAGE_SINGLE}' not found!"

@pytest.mark.order(2)
def test_install_package():
    """Test installing a single package."""
    stdout, stderr = run_command(CONDA_COMMANDS["install_package"](PACKAGE_SINGLE))
    assert "installed" in stdout.lower(), f"Failed to install '{PACKAGE_SINGLE}': {stderr}"

@pytest.mark.order(3)
def test_install_multiple_packages():
    """Test installing multiple packages simultaneously."""
    stdout, stderr = run_command(CONDA_COMMANDS["install_package"](" ".join(PACKAGE_MULTIPLE)))
    for package in PACKAGE_MULTIPLE:
        assert package in stdout, f"Package '{package}' was not installed!"

@pytest.mark.order(4)
def test_verify_package_version():
    """Test verifying installed package version."""
    stdout, stderr = run_command(CONDA_COMMANDS["list_package"](PACKAGE_SINGLE))
    assert PACKAGE_SINGLE in stdout, f"Package '{PACKAGE_SINGLE}' is not installed!"

@pytest.mark.order(5)
def test_uninstall_package():
    """Test uninstalling a package and confirming removal."""
    stdout, stderr = run_command(CONDA_COMMANDS["uninstall_package"](PACKAGE_SINGLE))
    
    # Verify removal using `conda list`
    stdout, _ = run_command(CONDA_COMMANDS["list_package"](PACKAGE_SINGLE))
    assert PACKAGE_SINGLE not in stdout, f"Package '{PACKAGE_SINGLE}' was not removed!"

@pytest.mark.order(6)
def test_check_package_integrity():
    """Test checking package integrity."""
    stdout, stderr = run_command(CONDA_COMMANDS["check_integrity"])
    assert "@" in stdout, "Package integrity listing is incorrect!"
