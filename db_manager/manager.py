import sqlite3

class ConnectDB(object):
    
    def __init__(self, db_name = "db.sqlite3") -> None:
        self.db_name = db_name
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except e:
            raise e

    def close(self):
        if self.conn:
            self.conn.close()
    
    def commit(self):
        if self.conn:
            self.conn.commit()
