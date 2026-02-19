# Python Language Feature Set

## Python Script/Class/Module
- [Class](com/inbravo/struct/book.py) | [Module](com/inbravo/struct/library_utils.py) | [Script](com/inbravo/struct/main_app.py)

## Basic Features

- [Hello World](com/inbravo/core/HelloWorld.py)
- [Hello World using Jupyter Notebook](com/inbravo/core/HelloWorld.ipynb)
- [Data Types](com/inbravo/core/DataTypeTest.py)
- [Variable Types](com/inbravo/core/VariableTest.py)
- [Why Indentation Matters in Python](com/inbravo/core/IntendationTest.py)
- [Main Function](com/inbravo/core/MainFunctionTest.py)

## Built-in data types
- [List](com/inbravo/core/List.py)

## File Operations

- [SHUtils Examples ("shell utilities", sh standing for Shell)](com/inbravo/file/SHUtil_Test.py)
- [Get File Metadata](com/inbravo/file/File_Meta_Data.py)
- [Get Count of Files in a Folder](com/inbravo/file/SAS_File_Counter.py)
- [Fetche all hyperlinks from a given URL and checks their validity](com/inbravo/file/URL_Validator.py)

## Data Structures

- [Tuples](com/inbravo/core/TupleTest.py)
- [Sets](com/inbravo/core/SetTest.py)

## String Handling

- [Formatted Strings](com/inbravo/string/FString.py)

## Regular Expressions

- [Regular Expressions Based String Splitting](com/inbravo/regexp/Reg_Exp_Utils.py)

## System

- [Operating System Information](com/inbravo/system/OSInfo.py)
- [Find the Library Version in Environment](com/inbravo/system/LibVersion.py)

## Matplotlib

- [Create a Two-Dimensional Graph](com/inbravo/matplot/Graph_Test.py)

## PySpark

- [Calculate Gross Income of a Supermarket](com/inbravo/dbx/super-market/Gross_Income.ipynb)

## Virtual Environment (VENV) (Optional)

1. Install Python: `brew install python@3.11`
2. Install PIP: `pip3.11 install uv`
3. Create a virtual environment in the downloaded codebase: `python3.11 -m venv .venv`
4. Install dependencies: `pip install -r requirements.txt`
5. Activate the virtual environment: `source .venv/bin/activate`

## Run Ollama (Optional)

1. To run the 8b LLM: `ollama run llama3:8b`
2. To stop: `/bye`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
