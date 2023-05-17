import jobs_ge_parser
import average_salary
from datetime import date
from job import Job
from database import DataBase
import cleardb

db = DataBase('job.db')
user_input = input('Choose action: 1. Add info to db from "jobs.ge",  2. Add info to db manually, 3. Get average '
                   'salary, 4. Clear db >>> ')

if user_input == '1':
    user_second_input = input('Enter quantity of jobs you want to add (all/your input) >>> ')
    jobs_ge_parser.add_info_to_db(user_second_input)

elif user_input == '2':
    name = input("Enter job's name >>> ")
    description = input("Write job's description >>> ")
    company = input("Enter company name >>> ")
    date = str(date.today())
    deadline = input("Enter job's deadline >>> ")
    salary = input("Enter job's salary >>> ")
    email = input("Enter your email >>> ")
    jb = Job(name, description, company, date, deadline, salary, email)
    db.add_job(jb)

elif user_input == '3':
    average_salary.average_salary_counter()

elif user_input == '4':
    cleardb.clear_db()
