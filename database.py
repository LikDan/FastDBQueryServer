from urllib.parse import urlparse

import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self, conn) -> None:
        result = urlparse(conn)
        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        port = result.port
        self.connection = psycopg2.connect(
            database=database,
            user=username,
            password=password,
            host=hostname,
            port=port
        )

    @staticmethod
    def fetch(cursor):
        try:
            return cursor.fetchall()
        except Exception as ex:
            print(str(ex))
            return ["no rows"]

    def execute(self, query):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(query)
            records = Database.fetch(cursor)
            if records.__len__() == 1:
                records = records[0]
            self.connection.commit()
            return records
        except Exception as ex:
            self.connection.rollback()
            raise ex
        finally:
            cursor.close()
