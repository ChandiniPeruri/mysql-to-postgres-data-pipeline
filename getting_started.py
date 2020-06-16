"""this is the driver program"""
import sys
from config import DB_DETAILS

def main():
    print(len(sys.argv))
    if(len(sys.argv)<2):
        print("Usage: python <filename> <env>")
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)
if __name__ == '__main__':
    main()
