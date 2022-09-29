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
g
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
    user_data = api_client._get_api_information(endpoint=table)

    
    db_client.create_tables(cur, table)
    
    
    #export data into the table
    if len(user_data) > 0:
        db_client.insert_statement(cur, user_data, table)
    
    return user_data


def _create_data_modelling_tables(cur):
    """

    Parameters
    ----------
    cur : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    #create table if not exists
    db_client.create_data_table(cur)
    
    #insert into table
    db_client.insert_data_table(cur)
    
    


def main():
    config = configparser.ConfigParser()
    config.read('db.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['db'].values()))
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    _create_db(cur)
    conn.close()

    # connect to project database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['new_db'].values()))
    cur = conn.cursor()
    endpoint_names = ['users', 'messages']
    for i in endpoint_names:
        get_data_to_table(cur,i)
    
    _create_data_modelling_tables(cur)
    conn.commit()
    conn.close()
    
    
if __name__ == '__main__':
    main()