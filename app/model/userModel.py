from model.db import DB

class userModel():
    def __init__(self):
        self.conn = DB.connect()

    def create_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS user (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(45) NOT NULL, PRIMARY KEY ( id ))
            """
        )

    def fetch_all_user(self):
        self.conn.execute(
            """
            SELECT * from user
            """
        )
        rows = self.conn.fetchall()
        return rows

    def add_user(self, data):
        self.conn.execute(
            f"""
            insert into user(id, name)values("{data.get('id')}", "{data.get('nom')}");
            """
        )

    def delete_user(self, id):
        self.conn.execute(
            f"""
            delete from user where id = {id};
            """
        )

    def update_user(self, id):
        self.conn.execute(
            f"""
            select * from user where id = {id};
            """
        )
