from pathlib import Path

import toml


def get_version() -> str:
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    pyproject_content = toml.load(pyproject_path)
    version = pyproject_content["tool"]["poetry"]["version"]
    return str(version)


__version__ = get_version()
