import re
import sys

# These variables are injected by Cookiecutter before the script runs
MODULE_NAME = "{{ cookiecutter.package_name }}"
REPO_NAME = "{{ cookiecutter.repo_name }}"


def validate_module_name(module_name):
    """
    Ensures the package name is valid Python:
    - Must start with a letter (usually lowercase).
    - Can only contain letters, numbers, and underscores.
    - NO dashes allowed.
    """
    module_regex = r"^[a-z][a-z0-9_]+$"
    if not re.match(module_regex, module_name):
        print(f"\nERROR: The package name '{module_name}' is invalid!")
        print("  - It must be lowercase.")
        print(
            "  - It cannot contain dashes/hyphens (use underscores instead)."
        )
        print("  - It cannot start with a number.")
        print(f"  > Suggestion: Try '{module_name.replace('-', '_').lower()}'")
        # Exit with status 1 to stop the generation
        sys.exit(1)


def validate_repo_name(repo_name):
    """
    Ensures the repo name (folder name) doesn't have weird characters.
    """
    # Allow alphanumeric, dashes, and underscores
    repo_regex = r"^[a-zA-Z0-9-_]+$"
    if not re.match(repo_regex, repo_name):
        print(
            f"\nERROR: The repository name '{repo_name}' contains illegal characters."
        )
        print("  - Please use only letters, numbers, dashes, and underscores.")
        sys.exit(1)


if __name__ == "__main__":
    validate_module_name(MODULE_NAME)
    validate_repo_name(REPO_NAME)
