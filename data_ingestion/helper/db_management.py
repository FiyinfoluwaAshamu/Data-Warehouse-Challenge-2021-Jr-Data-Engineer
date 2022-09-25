import json
import psycopg2
import configparser
from helper.sql_queries import SqlQueries

config = configparser.ConfigParser()
config.read('db.cfg')


class DBManagement:
    def __str__(self):
        pass

    def create_database(self, cur, db):
        """
        Returns
        -------
        cur : TYPE
            DESCRIPTION.
        conn : TYPE
        - Creates and connects tothe db
        - Returns the connection and cursor to db
        """
    
        # connect to default database
    
        # create database with UTF8 encoding
        cur.execute(f"DROP DATABASE IF EXISTS {db} WITH (FORCE)")

        cur.execute(f"CREATE DATABASE {db} WITH ENCODING 'utf8' TEMPLATE template0")

    
    
    def drop_tables(self, cur, table):
        """

        Parameters
        ----------
        cur : TYPE
            DESCRIPTION.
        table : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
 
        query = SqlQueries.drop_table.format(table)
        cur.execute(query)


    
    def create_tables(self, cur, table):
        """

        Parameters
        ----------
        cur : TYPE
            DESCRIPTION.
        table : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        query = SqlQueries.create_staging_user.format(table)
        cur.execute(query)


    def insert_statement(self, cur, data, table):
        """

        Parameters
        ----------
        cur : TYPE
            DESCRIPTION.
        data : TYPE
            DESCRIPTION.
        table : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        # Export the data to db
        for row in data:
            # print(row)
            cur.execute(SqlQueries.insert_data.format(table), [json.dumps(row)])


    def create_message_service(self, cur, data, table):
        """

        Parameters
        ----------
        cur : TYPE
            DESCRIPTION.
        data : TYPE
            DESCRIPTION.
        table : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        cur.execute(SqlQueries.messsage_service)



    def create_data_table(self, cur):
        """

        Parameters
        ----------
        cur : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        for queries in SqlQueries.create_data_table:
            cur.execute(queries)



    def insert_data_table(self, cur):
        cur.execute(SqlQueries.user_service)
        data = cur.fetchall()
        for row in data:
            id, firstName, lastName, address, city, country, zipCode, email, profile, subscription = row
            domain = email.split('@')[1]
            gender = profile.get("gender")
            isSmoking = profile.get("isSmoking")
            profession = profile.get("profession")
            income = profile.get("income")
            #for user service
            selected_list = [ id, address, city, country, zipCode, domain, gender, isSmoking, profession, income]
            cur.execute(SqlQueries.insert_user_service, selected_list)
            if len(subscription) > 0:
                for sub in subscription:
                    createdAt = sub.get("createdAt")
                    startDate = sub.get("startDate")
                    endDate = sub.get("endDate")
                    status = sub.get("status")
                    amount = sub.get("amount")
                    selected_list = [id, createdAt, startDate, endDate, status, amount]
               
                  
            
                    #for subscription service
        
                    cur.execute(SqlQueries.insert_subscription_service, selected_list) 
        