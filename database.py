import sqlite3


class DataBase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs(
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                company TEXT,
                date TEXT,
                deadline TEXT,
                salary REAL,
                email TEXT
            )
        ''')
        self.conn.commit()

    def add_job(self, job_info):
        self.cursor.execute(
            '''INSERT INTO jobs(name, description, company, date, deadline, salary, email) VALUES (?, ?, ?, ?, ?, ?, 
            ?)''',
            (job_info.name, job_info.description, job_info.company, job_info.date, job_info.deadline, job_info.salary,
             job_info.email))
        self.conn.commit()

    def clear_table(self):
        self.cursor.execute('''
            DELETE FROM jobs
        ''')
        self.conn.commit()

    def all_salary(self):
        self.cursor.execute('''
            SELECT salary FROM jobs;
        ''')
        return self.cursor.fetchall()
