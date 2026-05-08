import os

REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    ".gitignore"
]


def scan_project(project_path):
    report = {}

    for file in REQUIRED_FILES:
        file_path = os.path.join(project_path, file)
        report[file] = os.path.exists(file_path)

    github_workflow = os.path.exists(
        os.path.join(project_path, ".github", "workflows")
    )

    report["GitHub Actions"] = github_workflow

    return report