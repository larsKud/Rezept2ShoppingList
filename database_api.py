import json
import os
import pathlib
import sqlite3
import sys
import pandas as pd

from utils import load_json

# create database
def create_database(path: str = 'database.db'):
    con = sqlite3.connect(path)
    cur = con.cursor()
    query_str = ""
    config = load_json('dataconfig.json')
    for table in config.keys():
        table_name =config[table]['table_name']
        columns = config[table_name]['columns']
        for q in columns[:-1]:    
            query_str += f"{str(q[0])} {str(q[1])}, " 

        query_str += f"{str(columns[-1][0])} {str(columns[-1][1])}"
        cur.execute(f"CREATE TABLE {table_name}({query_str})")

# query database


# add entry to database
def add_entry_to_db(table: str, entry: dict, id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    if entry['id'] == -1:
        entry['id'] = get_next_id('items')
    temp = f"{entry["id"], entry["name"], entry["category"], entry["unit"]}"
    query_str = f"INSERT INTO {table} VALUES {temp};"
    print(query_str)
    cur.execute(query_str)
    con.commit()

# update entry to database
def update_entry(table: str, entry: pd.DataFrame):
    pass

# delete entry to database

# add category
def add_category(category: str):
    pass

def get_all_categories():
    pass

def get_categories_with_order() -> dict:
    pass

def get_next_id(table: str):
    query_string = f"SELECT MAX(id) FROM {table};"
    res = run_query_on_db(query_string)
    if res[0][0] is None:
        return 0
    else:
        return res[0][0] + 1

def run_query_on_db(query: str, db: str = "database.db"):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    con.commit()
    return res

if __name__ == "__main__":
    #create_database()
    entry = {
        'id': -1,
        'name': 'Karotten',
        'category': 'Gemuese',
        'unit': 1
    }

    add_entry_to_db('items', entry, -1)
    print(get_next_id("items"))