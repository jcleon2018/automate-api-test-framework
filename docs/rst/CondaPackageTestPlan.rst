=========================
Conda Package Test Plan.
========================

This document outlines test cases for validating Conda functionality across various workflows, including cross-platform compatibility, error handling, logging, package installation, and environment management.

----------------------
Test Files & Test Cases
----------------------

**1. test_cross_platform.py**
    
    - Test: Validate environment creation across OS platforms
    - Test: Automate Conda setup inside a containerized environment (Skipped)

**2. test_env_creation.py**
    
    - Test: Verify Conda is installed
    - Test: Create a Conda environment 
    - Test: Check if environment exists 
    - Test: Activate environment 
    - Test: De-activate environment 
    - Test: Export environment 
    - Test: Recreate environment 
    - Test: Clone environment 
    - Test: List available environments 
    - Test: Remove Conda environment 

**3. test_error_handling.py**
    
    - Test: Attempt installing an invalid package 
    - Test: Validate invalid environment names 

**4. test_logging.py**
    
    - Test: Measure installation time for large packages 
    - Test: Capture installation logs 
    - Test: Generate a test execution report in JSON format 

**5. test_package_install.py**
    
    - Test: Search for a package 
    - Test: Install a package 
    - Test: Install multiple packages 
    - Test: Verify installed package version 
    - Test: Uninstall a package 
    - Test: Check package integrity 

**6. test_conda_env_switch.py**
    
    - Test: Switch between environments 
    - Test: Remove a specific environment 

===========================
Execution Steps for Testing
===========================

------------
Setup Steps
------------

1. **Initialize Pipenv and Install Dependencies**
   ::
       pipenv install

   This ensures all dependencies listed in `Pipfile` are installed into the Pipenv-managed virtual environment.

2. **Activate the Virtual Environment**
   ::
       pipenv shell

   Alternatively, run commands directly using:
   ::
       pipenv run <command>

--------------------
Running Pytest Tests
--------------------

**Run Tests Without Verbosity**
   ::
       pipenv run pytest tests/conda_tests

**Run Tests With Verbosity**
   ::
       pipenv run pytest -v tests/conda_tests

**Generate JSON Test Report**
   ::
       pipenv run pytest --json-report --json-report-file=tests/conda_tests/installation_report.json

-------------------------------
One-Liner Execution for All Steps
-------------------------------

To run everything in a **single command**, including verbose output and structured reporting:
   ::
       pipenv run pytest -v --json-report --json-report-file=tests/conda_tests/installation_report.json


------------------------
Expected Test Outcomes
------------------------

**Cross-Platform Validation:** Ensure consistency across Linux, Windows, and MacOS.  
**Environment Management:** Proper handling of creation, activation, export, cloning, and deletion.  
**Error Resilience:** Conda should fail gracefully and provide meaningful error messages.  
**Logging & Reporting:** Test execution should generate structured logs for debugging.  
**Package Management:** Seamless installation, verification, and removal of dependencies.  
**Environment Switching:** Validate smooth transitions between Conda environments.  
