# SQL-DataPullStrategy-MultipleSources
 A data pull strategy to pull data from multiple databases into pandas dataframe in an easy & secure way..

## Description
This is an open-source Python script for flexible data extraction from different databases. It uses Python's `pandas` library and the `psycopg2-binary` package for database connectivity and querying. The script employs the Strategy design pattern, allowing you to quickly and easily switch between different database sources. This script can serve as a base or complement for creating more complex scripts for data analysis or software development.

## Installation
1. Clone the repository: `git clone https://github.com/Safakan/SQL-DataPullStrategy-MultipleDatabases.git` or by using the GitHub Desktop app.
2. Install the required dependencies: `pip install pandas psycopg2-binary python-dotenv` (ideally in a virtual environment).
    - Note: If updates to these packages cause this code to break, you can still install the specific versions of the packages listed in the `requirements.txt` file.
3. Create a .env file in the directory and specify your database URIs as shown in the .env.example file.

## Usage
To use this script, create an instance of one of the subclasses and use the `pull_data` method with your custom SQL query. This method returns a DataFrame.
More detailed explanation & examples are showned in the code itself.
Example:

```python
pulldata_Production1().pull_data('enter_your_query_or_function_here')
```
## License
This project is licensed under the [MIT License](LICENSE).
