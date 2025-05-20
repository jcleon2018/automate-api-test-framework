# Conda Automation Testing Framework

## Project Overview
This repository contains an **automated Conda package management framework**, designed to validate **environment creation, package installation, error handling, and cross-platform compatibility** using `pytest`. The framework ensures that Conda environments function correctly across **Linux, Windows, and macOS**.

## Intended Goals
- **Automate Conda environment creation** and validation.
- **Ensure cross-platform compatibility** by testing Conda commands on multiple OS.
- **Verify package installation and integrity** for different dependencies.
- **Capture installation logs and execution reports** for debugging.
- **Improve maintainability and scalability** for Conda testing.

**NOTE** there is addtional details of the test plan. See docs/rst folder 
---

## Project Structure

![Directory Image](../../docs/rst/images/condateststruc.png))

## Running Conda Tests

### **Execute Tests with Pytest**
Run all Conda tests:
```bash
pytest conda_tests/ -v --html=reports/conda_test_report.html

