# Python language feature set

## Basic features

- [Hello world](com/inbravo/core/HelloWorld.py)
- [Hello world using Jupitor Notebook](com/inbravo/core/HelloWorld.ipynb)
- [Data types](com/inbravo/core/DataTypeTest.py)
- [Variable types](com/inbravo/core/VariableTest.py)
- [Why intendation matters in Python](com/inbravo/core/IntendationTest.py)
- [Main function](com/inbravo/core/MainFunctionTest.py)

## Data Structures

- [Tuples](com/inbravo/core/TupleTest.py)
- [Sets](com/inbravo/core/SetTest.py)

## String handling

- [Formatted Strings](com/inbravo/string/FString.py)

## System

- [Operating system information](com/inbravo/system/OSInfo.py)

## PySpark

- [Calculate gross income of a super marker](com/inbravo/dbx/super-market/Gross_Income.ipynb)

## Build and Packaging

The provided [pyproject.toml](pyproject.toml) file is a configuration file for a Python project. It defines metadata and dependencies for the project. Here's a review and guidance on how to use it:

### Ensure Python version 3.9 or higher is installed on your system:

```
python --version
```

### Create and activate a virtual environment to isolate dependencies:

```
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### Install Dependencies:

If the project has dependencies (not shown in this excerpt), they would typically be listed in a [tool.poetry.dependencies] or [build-system] section. Install them using a tool like pip or poetry:

```
pip install .
```

### Run the Project:

If the project has an entry point (e.g., a script or module to execute), you can run it. For example

```
python -m pfs
```

### Build and Publish (Optional):

To build the project into a distributable format (e.g., a wheel or source distribution), use a build tool like build:

```
pip install build
python -m build
```

### Publish (Optional):

To publish the package to PyPI, use twine

```
pip install twine
twine upload dist/*
```
