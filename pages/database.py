from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "exalted-ability-417323:us-east4:ash247",
        "pymysql",
        user="ash247",
        password="120304",
        db="StreamlitChatLogs"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# Test the connection
with pool.connect() as conn:
    # Execute a simple query to test the connection
    result = conn.execute("SELECT 1")
    for row in result:
        print(row)  # This should print (1,)

print("Connection test completed.")