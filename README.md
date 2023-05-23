# SQL-DataPullStrategy-MultipleDatabases
 A data pull strategy to pull data from multiple databases into pandas dataframe in an easy, flexible & secure way.
 I hope this helps to anyone reading this, I've used this many times to:
 - Build scripts for automation & data analysis purposes that're simply not possible with just one SQL query querying a single database.
 - Ease my process to only deal with the URIs for once
 - Securely share my code with others

## Description
This is an open-source Python script for flexible data extraction from different databases. It uses Python's `pandas` library and the `psycopg2-binary` package for database connectivity and querying. The script employs the Strategy design pattern, allowing you to quickly and easily switch between different database sources. This script can serve as a base or complement for creating more complex scripts for data analysis or software development.

## Installation
1. Clone the repository: `git clone https://github.com/Safakan/SQL-DataPullStrategy-MultipleDatabases.git` or by using the GitHub Desktop app.
2. Install the required dependencies: `pip install pandas psycopg2-binary python-dotenv` (ideally in a virtual environment).
    - Note: If updates to these packages cause this code to break, you can still install the specific versions of the packages listed in the `requirements.txt` file.
3. Create a .env file in the directory and specify your database URIs as shown in the .env.example file.

## Usage
- Modify the subclasses & names based on your needs.
- To use this script, create an instance of one of the subclasses and use the `pull_data` method with your custom SQL query for it to return a DataFrame.
- Check out the main.py file for detailed examples before you use.



## Limitations
Currently, this script is specifically designed to work with PostgreSQL databases due to the connection string format and the use of the psycopg2-binary package. This package is a PostgreSQL adapter for Python, and therefore the script may not work properly with other types of databases (like MySQL, SQLite, etc.) without modification.

If you want to adapt this script to other databases, you might need to use other connection libraries (like pyodbc for SQL Server, mysql-connector-python for MySQL, sqlite3 for SQLite, etc.) and adjust the connection string format to the specific requirements of these databases.

The URI format for connecting to a PostgreSQL database usually follows the pattern: postgresql://user:password@localhost:5432/mydatabase. Other databases may have different URI formats, which would need to be reflected in your .env file and in how you use the read_sql function.

This is a simplification for the purpose of demonstrating a strategy pattern and not intended to be a one-size-fits-all solution. Always adapt your database interactions to your specific needs and security considerations.

## License
This project is licensed under the [MIT License](LICENSE).
