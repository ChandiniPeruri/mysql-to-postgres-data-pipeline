import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode as ec
from config import DB_DETAILS
import psycopg2

""" get_tables method returns tables from the table list file
    parameter: string
    return: list
"""


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')


def load_db_details(env: str) -> dict:
    return DB_DETAILS[env]


def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name)
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print("error")
    return connection


def get_pg_connection(db_host, db_name, db_user, db_pass):
    target_db = DB_DETAILS['dev']['TARGET_DB']
    connection = psycopg2.connect(
        f'dbname={target_db["DB_NAME"]} user = {target_db["DB_USER"]} host ={target_db["DB_HOST"]} password ={target_db["DB_PASS"]}')
    return connection


def get_db_connection(db_type, db_host, db_name, db_user, db_pass):
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_pass=db_pass
                                          )
        return connection
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass
                                       )
        return connection