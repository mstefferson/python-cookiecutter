# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

1. Make sure you have Poetry installed. If not, you can install it by following the instructions in the [Poetry documentation](https://python-poetry.org/docs/#installation).

2. Clone the repository and navigate to the project directory:

3. Initialize the Poetry environment and install the project dependencies:

```bash
poetry install
```

This command will create a virtual environment for the project and install all the required dependencies specified in the `pyproject.toml` file.

## Installing Additional Packages

To install additional packages in your project, you can use the following Poetry commands:

- To install a package as a main dependency:

```bash
poetry add <package-name>
```

- To install a package as a development dependency:

```bash
poetry add --dev <package-name>
```

Replace `<package-name>` with the name of the package you want to install.

Poetry will automatically update the `pyproject.toml` file and the `poetry.lock` file to include the newly installed packages.

Note: you should commit the `poetry.lock` file to version control.

## Using pre-commit

This project uses pre-commit to automatically check and format the code before each commit. It best to run run everything in a poetry shell. To enable pre-commit, run the following command:

```bash
poetry shell
pre-commit install
```

## Usage

TODO: Add usage instructions

## Testing

```bash
poetry run pytest
```

## Code Quality

This project uses various tools to ensure code quality and consistency:

- Flakeheaven: A wrapper around Flake8 with additional plugins for linting and code style enforcement.
- Mypy: A static type checker for Python.
- Black: An opinionated code formatter.
- isort: A utility to sort and organize imports.

To run these tools, use the following commands:

```bash
poetry run flakeheaven
poetry run mypy .
poetry run black .
poetry run isort .
```

## License

{{cookiecutter.open_source_license}}
