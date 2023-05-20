import time
import requests
from bs4 import BeautifulSoup
from database import DataBase
from job import Job

from selenium import webdriver

from selenium.webdriver.common.by import By


def add_info_to_db(quantity):

    driver = webdriver.Chrome()

    driver.get("https://jobs.ge")

    category_btn = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div[2]/div[1]')

    category_btn.click()

    it_category = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div[2]/div[1]/select/option[11]')

    it_category.click()

    trs = driver.find_elements(By.XPATH, '//*[@id="job_list_table"]/tbody/tr')

    my_current_url = driver.current_url

    cycle_count = 0
    if quantity == 'all':
        cycle_count = len(trs) + 1
    elif int(quantity) > len(trs):
        print('Invalid quantity of jobs')
    else:
        cycle_count = int(quantity) + 2

    for i in range(2, cycle_count):
        driver.get(my_current_url)

        name_btn = driver.find_element(By.XPATH, f'//*[@id="job_list_table"]/tbody/tr[{i}]/td[2]/a[1]')
        name_btn.click()

        name = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/b').text

        description = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[4]/td').text

        company = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[2]/td/b').text

        date = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[1]').text

        deadline = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[2]').text

        description_2 = description.split()

        salary = None

        email = None

        for j in range(len(description_2)):
            if 'ლარ' in description_2[j] and description_2[j - 1].isnumeric() or '₾' in description_2[j] or '$' in \
                    description_2[j]:
                salary = description_2[j - 1] + ' ' + description_2[j]
                break
            else:
                salary = None

        for e in description_2:
            if '@' in e:
                email = e
                break
            else:
                email = None

        info = Job(name, description, company, date, deadline, salary, email)

        db = DataBase('job.db')
        db.add_job(info)

    time.sleep(5)
