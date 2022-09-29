
# How many total messages are being sent every day?
query1="""SELECT to_char(createdAt, "YYYY-MM-DD"), COUNT(message) as totalmsg
FROM message_service
WHERE message IS NOT NULL
Group by 1
"""

cur.execute(query1)

cur.fetchall()

# Are there any users that did not receive any message?
query2="""SELECT to_char(createdAt, "YYYY-MM-DD"), Id
FROM message_service as ms 
JOIN user_service as us ON ms.Id = as.Id
WHERE message IS NULL
Group by 1
"""
cur.execute(query2)

# How many active subscriptions do we have today?
query3="""SELECT to_char(createdAt, "YYYY-MM-DD"), COUNT(status) as NumactiveUser
FROM subscription_service
WHERE status = 'Active'
Group by 1
"""
cur.execute(query3)

# Are there users sending messages without an active subscription?
query4="""SELECT senderId
FROM subscription_service as ss
JOIN message_service as ms ON ss.user_id = ms.Id
WHERE status = 'Inactive'AND message IS NOT NULL
"""

cur.execute(query4)
# How much is the average subscription amount (sum amount subscriptions/count subscriptions) breakdown by year/month (format YYYY-MM)?
query5="""SELECT to_char(createdAt, 'YYYY-MM'), SUM(AMOUNT)/COUNT(*) as avg_sub_amount
from subscription_service
group by 1
order by 1
"""

cur.execute(query5)