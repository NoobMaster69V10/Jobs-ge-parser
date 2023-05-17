from database import DataBase

db = DataBase('job.db')


def average_salary_counter():
    lst = []

    for salary in db.all_salary():
        lst.append(str(list(salary)[0]).split(' ')[0])

    all_salary_lst = []
    for e in lst:
        if e.isnumeric():
            all_salary_lst.append(int(e))

    if len(all_salary_lst) == 0:
        print('Column of salary is clear, please add something... ')
    else:
        average_salary = sum(all_salary_lst) / len(all_salary_lst)
        print(average_salary)
