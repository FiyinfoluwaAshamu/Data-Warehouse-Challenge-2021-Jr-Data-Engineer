#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import psycopg2
import configparser
from src.api import API
from helper.db_management import DBManagement
logging.basicConfig(format="%(asctime)s %(name)s %(levelname)-10s %(message)s")
LOG = logging.getLogger("ETL")
LOG.setLevel(os.environ.get("LOG_LEVEL", logging.DEBUG))

##############################################################################
LOG.info("init parameters")
#############################################################################

api_client = API()
db_client = DBManagement()


query = """
    SELECT EXISTS (
       SELECT * FROM information_schema.tables
       WHERE  table_schema = 'project'
       AND    table_name   = '{}'
       );
"""

def _create_db(cur):
    """

    Parameters
    ----------
    cur : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    db_client.create_database(cur, db='projects')


def get_data_to_table(cur, table)-> list:
    """

    Parameters
    ----------
    cur : TYPE
        DESCRIPTION.
    table : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    #table="users"
    user_data = api_client._get_api_information(endpoint=table)
    # add a validation to first check the table before recareting it. The query to check the validation is above
    
    db_client.create_tables(cur, table)
    
    
    #export data into the table
    if len(user_data) > 0:
        db_client.insert_statement(cur, user_data, table)
    
    return user_data





def main():
    config = configparser.ConfigParser()
    config.read('db.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['db'].values()))
    cur = conn.cursor()
    _create_db(cur)
    
    endpoint_names = ['users', 'messages']
    for i in endpoint_names:
        get_data_to_table(cur, i)
    
    
if __name__ == '__main__':
    main()