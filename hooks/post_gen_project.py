import subprocess


def initialize_git_repo():
    """
    Initializes the git repo after initial project creation from the template.

    NOTE: ``post_gen_project`` hooks execute from the root directory of the
    generated project.
    """
    subprocess.run(["git", "init"])

    # Ensure the primary branch name is 'main' for CI/CD
    subprocess.run(["git", "branch", "-M", "main"])

    # Stages all non-staged files for commit
    subprocess.run(["git", "add", "-A"])

    # Commits the staged files
    subprocess.run(
        ["git", "commit", "-m", "Created from cookiecutter project template"]
    )


if __name__ == "__main__":
    initialize_git_repo()
