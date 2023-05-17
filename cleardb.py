from database import DataBase


def clear_db():
    db = DataBase('job.db')
    db.clear_table()
