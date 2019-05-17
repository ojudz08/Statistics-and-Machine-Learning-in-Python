# File I/O

# SQL (SQLite)

import pandas as pd
import sqlite3

db_filename = os.path.join(tmpdir, "users.db")

# Connect
conn = sqlite3.connect(db_filename)


# Creating tables with pandas
url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read.csv(url)

salary.to_sql("salary", conn, if_exists="replace")


# Push modifications
cur = conn.cursor()
values = (100, 14000, 5, 'Bachelor', 'N')
cur.execute("insert into salary values (?, ?, ?, ?, ?)", values)


# Reading results into a pandas DataFrame
salary_sql = pd.read_sql_query("select * from salary;", conn)
print(salary_sql.head())

pd.read_sql_query("select * from salary;", conn).tail()
pd.read_sql_query('select * from salary where salary > 25000;', conn)
pd.read_sql_query('select * salary where experience = 16;', conn)
pd.read_sql_query('select * from salary where education="Master";', conn)