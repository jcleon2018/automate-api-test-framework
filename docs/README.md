# Sphinx Python Documentation

## Overview

This directory provides a template to generate package documentation.

## Documentation Structure

```
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── Makefile
│   ├── README.md
│   ├── rst
│   │   ├── Specification.rst
│   │   └── TestPlan.rst
│   └── _static
│       ├── fig_1.jpeg
│       ├── fig_2.jpeg
│       ├── fig_3.jpeg
│       └── solidfire.jpeg
```

## Gerating Documentation.

1. Running sphinx-apidoc. The tool outputs the generated documentation to docs/rst
uses ../util as the targeted directory to be documented.
Command below documents the source and becomes static after run.

   * `../ntap-test/docs$ sphinx-apidoc -o docs/rst ../util`

2. Running make file to build the documentationa

   * `../ntap-test/docs$ make html`
```
├── docs
│   ├── _build
│   │   ├── doctrees
│   │   └── html
│   ├── conf.py
│   ├── index.rst
│   ├── Makefile
│   ├── README.md
│   ├── request_response.log
│   ├── rst
│   │   ├── modules.rst
│   │   ├── Specification.rst
│   │   ├── TestPlan.rst
│   │   ├── util.chess.rst
│   │   └── util.rst
│   └── _static
│       ├── fig_1.jpeg
│       ├── fig_2.jpeg
│       ├── fig_3.jpeg
│       └── solidfire.jpeg
```

3. Running clean to delete build files
   * `../ntap-test/docs$ make clean`



