# {{cookiecutter.repo_name}}

{{cookiecutter.project_short_description}}

## Recommended Development Steps

### Create a Virtual Environment for the Project

Virtual environments (venvs) let you install dependencies separately from other projects to help avoid dependency conflicts. It is recommended to create one for each project. After using either method below to create the virtual environment, VSCode should automatically detect and activate the virtual environment for the project going forward.

#### Through VSCode

With the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed, open the Command Pallete with Ctrl+Shift+P, search for "Python: Create Environment...", select the "Venv" option, and select your Python interpreter (the first option will probably be correct). This will create virtual environment folder as a hidden file called `.venv` in your project.

#### Through the Terminal

Navigate to your project directory, open a terminal there, and run the following commands:

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate the virtual environment

```bash
# For macOS/Linux
source venv/bin/activate

# For Windows
.\venv\Scripts\activate
```

### Install Development Tools for the Project

We recommend creating and activating a venv for the project from the section above first. Inside of your new repo folder venv, install the development tools optional dependency group (`dev`) with:

```bash
pip install --group dev
```

This installs useful development tools that this repo template uses, like `pre-commit` for automated actions on commit, `flake8` for linting, and `sphinx` for building the documentation pages.

#### Pre-commit Setup

Once you install the dev tools, you need to install the pre-commit hooks for them to function with:

```bash
pre-commit install
```

On `git commit`, these installed hooks will run, checking the code and not allowing the commit to succeed until issues are fixed.

These hooks can be run at any time manually with:

```bash
# Only on staged files
pre-commit run

# All files
pre-commit run --all-files
```

See `pre-commit run --help` for more running options that are available.

## Running Unit Tests

Unit tests are run with the `pytest` tool, installed as part of the `dev` optional dependency group (`pip install --group dev`). To execute the unit tests for the project, simply run the following command from the root directory of the project:

```bash
pytest
```
