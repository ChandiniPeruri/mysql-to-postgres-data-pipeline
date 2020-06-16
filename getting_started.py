"""this is the driver program"""
import sys
from config import DB_DETAILS
from utils import get_tables


def main():
    if len(sys.argv) < 2:
        print("Usage: python <filename> <env>")
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list.txt')
    for table in tables['table_name']:
        print(table)


if __name__ == '__main__':
    main()
