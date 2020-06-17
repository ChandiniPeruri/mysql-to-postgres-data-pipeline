"""this is the driver program"""
import sys
from config import DB_DETAILS
from util import get_tables
from read import read_table


def main():
    if len(sys.argv) < 2:
        print("Usage: python <filename> <env>")
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list.txt')
    for table in tables['table_name']:
        print(f'Reading data for table {table}')
        data, column_names = read_table(db_details, table)
        print(data)
        print(column_names)
        print(f'Loading data for table {table}')
        

if __name__ == '__main__':
    main()
