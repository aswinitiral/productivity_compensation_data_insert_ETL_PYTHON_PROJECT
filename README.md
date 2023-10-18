# productivity_compensation_data_insert_ETL_PYTHON_PROJECT

## About DataSet
Productivity and Hourly Compensation (1948-2021)
Year by year data for net productivity per hour worked and hourly compensation.
This dataset provides insight into the productivity and hourly compensation trends in the United States from 1948 to 2021.
It includes data on both overall compensation and compensation specifically for production and nonsupervisory workers.

## Project: CSV to PostgreSQL Database
## Overview
This project provides a Python script for extracting data from a CSV file and inserting it into a PostgreSQL database. This can be particularly useful when you have large datasets in CSV format that you want to analyze or work with using a relational database.
## Prerequisites
Before running the script, make sure you have the following installed:
Python (version 3.x)
psycopg2 library (install using pip install psycopg2)
PostgreSQL database server

## Usage
_____________________________________________________________________________________________________________________________________________________________
#### Database Configuration:
Create a PostgreSQL database.
Update the database connection details (host, port, username, password, and database name) in the script.
#### CSV File:
Place the CSV file you want to import in the same directory as the script.
Update the csv_file_path variable in the script with the correct file name.
#### Run the Script:
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the command: python script_name.py
#### Monitor Progress:
The script will print progress messages as it extracts data from the CSV file and inserts it into the database.
#### Verify Data:
Connect to your PostgreSQL database and verify that the data has been successfully inserted.

## Script Details
The Python script (script_name.py) uses the csv and psycopg2 libraries to read the CSV file and interact with the PostgreSQL database. It follows these steps:
_______________________________________________________________________________________________________________________________________________________________
#### Establish Database Connection:
Connect to the PostgreSQL database using the provided credentials.
#### Read CSV File:
Read the data from the CSV file into a Python data structure (e.g., list of dictionaries).
#### Insert Data into Database:
Loop through the data and insert each row into the specified PostgreSQL table.
#### Close Database Connection:
Close the connection to the database after the data insertion is complete.

## Notes
Ensure that the CSV file has a header row that corresponds to the columns in the PostgreSQL table.
Customize the script according to your specific database schema and CSV file structure.
Happy coding!
