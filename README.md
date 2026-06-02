# Python Package Template

A comprehensive [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating professional Python projects. Designed for SIMCODES-ISU.

## Features

* **Modern Structure:** `src/` layout for better packaging.
* **Testing:** Pre-configured for `pytest`.
* **Documentation:** Ready-to-build Sphinx docs looking good out of the box with `sphinx-rtd-theme`.
* **CI/CD:** GitHub Actions workflows for automated testing and linting.
* **Quality Control:** Pre-commit hooks for naming validation.

## How to Use the Template

The end goal will be to create a GitHub repository from the template. 

### 1. Create the GitHub Repository

Start by going to [SIMCODES@ISU](https://github.com/SIMCODES-ISU)
and clicking on the "New Repository" button. Provide:

- repository name
- description
- and choose the visibility

Leave everything else disabled (we don't want GitHub to generate any files).

### 2. Populate the Local Repository

Next, we need to locally create the repository from this template. To do this first install the Cookiecutter tool (if it's not already installed) to be available for your user account. We recommend using a virtual environment. In the directory where you want the virtual environment to live run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install cookiecutter
```

Then run `cookiecutter`, telling it to use the SIMCODES-ISU template:

```bash
cookiecutter gh:simcodes-isu/python-package-template
```

Cookiecutter will then proceed to ask you to provide the following information:

- full name
- email
- repo_name (use whatever you called it on GitHub)
- package_name (this will be the name used in Python import statements)
- project_short_description (use whatever you put on GitHub)
- version (default of 0.1.0 is fine)

The result will be a directory named whatever you provided for `repo_name`. The directory will NOT yet be a git repository, nor will it be synched to GitHub.

### 3. Set the Local Repository to Track the GitHub Repository

A local git repository is created as part of the template generation process. Now we need to tell this repository to track the GitHub repository from step 1:

```bash
# <repo_name> is whatever you called it in step 1
git remote add origin https://github.com/SIMCODES-ISU/<repo_name>.git

git push -u origin main
```

## Recommended Next Steps

### Create a CODEOWNERS file

Add a line like

```
* @mentor1
```

where `@mentor1` is the GitHub username of the mentor in charge of the project. You can add multiple GitHub usernames on the same line if there are multiple mentors.

### Modify the GitHub Settings

We suggest going to your repo's settings and applying the following settings:

General Settings:
- Enable "Automatically delete head branches"

Under rules create a new ruleset to protect the main branch. Recommended 
settings:
- Name "Protect Main"
- Target branches "default"
- Restrict deletions (should be on by default)
- Require a pull request before merging
  - Set required approvals to "number of mentors" plus one.
  - Set "Dismiss stale pull request approvals when new commits are pushed"
  - Set required review from Code Owners
  - Require approval of the most recent reviewable push
- Require status checks to pass (requires that CI/CD has run once)
  - Require branches to be up to date before merging

### Follow Steps in README.md

Check the `README.md` file in your new project and follow any steps there.
