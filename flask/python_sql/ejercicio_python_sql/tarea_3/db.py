
import psycopg2

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection()

        if self.connection:
            print("Database connected successfully!")
            self.cursor = self.connection.cursor()


    def create_connection(self):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                options="-c search_path=lyfter_car_rental"
            )
            return connection

        except Exception as error:
            print("Error connecting to the database:", error)
            return None


    def execute_query(self, query, *args):
        try:
            self.cursor.execute(query, args)
            return "Query executed"

        except Exception as error:
            raise Exception("Error executing query:", error)


    def fetchall(self, query, *args):
        try:
            self.cursor.execute(query, args)
            results = self.cursor.fetchall()

            return results

        except Exception as error:
            raise Exception("Error fetching all:", error)


    def commit(self):
        try:
            self.connection.commit()
            return "Query committed"
        
        except Exception as error:
            raise Exception ("Error committing query to database:", error)

    def rollback(self):
        try:
            self.connection.rollback()
            return "Query rolled back"
        
        except Exception as error:
            raise Exception ("Error rolling back query:", error)


    def close_connection(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        print("Connection closed")


db_manager = PgManager(
    db_name='postgres',
    user='postgres',
    password='xyz0138',
    host='localhost'
)

