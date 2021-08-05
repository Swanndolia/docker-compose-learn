from model.db import DB

class userModel():
    def __init__(self):
        self.conn = DB.connect()

    def fetch_all_user(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS user(id int(11), name char(45));
            SELECT * from user
            """
        )
        rows = self.conn.fetchall()
        return rows

    def add_user(self, data):
        self.conn.execute(
            f"""
            insert into user(id_user, nom_user)values("{data.get('id')}", "{data.get('nom')}");
            """
        )

    def delete_user(self, id):
        self.conn.execute(
            f"""
            delete from user where id_user = {id};
            """
        )

    def update_user(self, id):
        self.conn.execute(
            f"""
            select * from user where id_user = {id};
            """
        )
