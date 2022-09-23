class SqlQueries:
    create_staging_user = ("""
    CREATE TABLE IF NOT EXISTS {} (
    	id serial NOT NULL PRIMARY KEY,
    	info json NOT NULL
       );

            """)

    insert_data = ("""
         INSERT INTO {} (
                    data
                    ) VALUES(%s);
 """)
 
 
    message_service = (
     """CREATE TABLE message_service AS (
         WITH raw_data AS (
           SELECT  
                info::json->'createdAt' as createdAt,
                info::json->'receiverId' as receiverId,
                info::json->'id' as id,
                info::json->'senderId' as senderId
           FROM messages
     )
         SELECT createdAt, receiverId, id, senderId
         FROM raw_data)"""
 )

    user_service = (""" WITH raw_data AS (
          SELECT  
               info::json->'id' as id,
               info::json->'firstName' as firstName,
               info::json->'lastName' as lastName,
               info::json->'address' as address,
               info::json->'city' as city,
               info::json->'country' as country,
               info::json->'zipCode' as zipCode,
               info::json->'birthDate' as birthDate,
               info::json->'email' as email,
               info::json->'profile' as profile,
               info::json->'subscription' as subscription
          FROM users
    )
        SELECT id, firstName, lastName, address, city, country, zipCode, email, profile, subscription
        FROM raw_data"""

)
    
    create_user_service = ("""
       CREATE TABLE IF NOT EXISTS user_service (
       	id INTEGER NOT NULL PRIMARY KEY,
        address VARCHAR(100), 
        city VARCHAR(50), 
        country VARCHAR(50), 
        zipCode VARCHAR(50), 
        domain VARCHAR(50), 
        gender VARCHAR(10), 
        isSmoking BOOLEAN, 
        profession VARCHAR(100), 
        income DECIMAL(10,2)
          );

           """)
           
           
    create_subscription_service = ("""
       CREATE TABLE IF NOT EXISTS subscription_service (
          id serial NOT NULL PRIMARY KEY,
       	user_id INTEGER NOT NULL,
        createdAt TIMESTAMP, 
        startDate TIMESTAMP, 
        endDate TIMESTAMP, 
        status VARCHAR(50), 
        amount DECIMAL(10,2)
          );

           """)
           
           
    insert_user_service = (
        """
        INSERT INTO user_service(
            id, address, city, country, zipCode, domain, gender, isSmoking, profession, income
            ) VALUES(
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
        
        """
        )
                
                
           
    insert_subscription_service = (
        """
        INSERT INTO subscription_service(
            user_id, createdAt, startDate, endDate, status
            ) VALUES(
                %s, %s, %s, %s, %s
                )
        
        """
        )
        
    create_data_table =[create_user_service, create_subscription_service, message_service]