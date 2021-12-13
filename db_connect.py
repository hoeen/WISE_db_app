# import psycopg2
# import csv 

class wise_connect:
    def __init__(self):
        self.host = 'arjuna.db.elephantsql.com'
        self.user = 'zhduuuid'
        self.password = 'Spw4jaiW6cv1xOyZN6FlaJ1SojO_9fck'
        self.database = 'zhduuuid'

    def connect(self):
        import psycopg2
        connection = psycopg2.connect(
            host = self.host,
            user = self.user,
            password = self.password, 
            database = self.database, 
        )
        return connection

