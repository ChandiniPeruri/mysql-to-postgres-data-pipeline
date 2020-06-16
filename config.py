""" config.py is used to store information related to environment"""
import os
DB_DETAILS ={
    'dev':{
        'SOURCE_DB':{
            'DB_TYPE': 'mysql',
            'DB_HOST': '34.72.33.3',
            'DB_NAME': 'retail',
            'DB_USER': os.environ.get("SOURCE_DB_USER"),
            'DB_PASS': os.environ.get("SOURCE_DB_PASS")
        },
        'TARGET_DB':{
            'DB_TYPE': 'postgresql',
            'DB_HOST': '34.72.33.3',
            'DB_NAME': 'pg_retail_dwh',
            'DB_USER': os.environ.get("TARGET_DB_USER"),
            'DB_PASS': os.environ.get("TARGET_DB_PASS")
        }
    }
}