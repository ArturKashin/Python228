import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из базы данных")
        return []

    def add_post(self, name, author, text):
        try:
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (name, author, text,))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return True

    def get_post(self):
        try:
            self.__cur.execute(f"SELECT id, name, author, text FROM posts")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи за БД " + str(e))

    def get_post_id(self, post_id):
        try:
            self.__cur.execute(f"SELECT name, author, text FROM posts WHERE id = {post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи за БД" + str(e))
        return False, False, False
