from model.db import DB


class ArticleModel():
    def __init__(self):
        self.conn = DB.connect()

    def fetch_all_article(self):
        self.conn.execute(
            """
            SELECT * from article
            """
        )
        rows = self.conn.fetchall()
        return rows

    def add_article(self, data):
        self.conn.execute(
            f"""
            insert into article(id_article, nom_article, prix_achat, volume)values("{data.get('id')}", "{data.get('nom')}", "{data.get('prix')}", "{data.get('volume')}");
            """
        )

    def delete_article(self, id):
        self.conn.execute(
            f"""
            delete from article where id_article = {id};
            """
        )

    def update_article(self, id):
        self.conn.execute(
            f"""
            select * from article where id_article = {id};
            """
        )
