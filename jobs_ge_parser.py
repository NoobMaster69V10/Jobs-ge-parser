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

    my_current_url = driver.current_url

    response = requests.get(my_current_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'job_list_table'})

    soup_2 = BeautifulSoup(str(table), 'html.parser')

    trs = soup_2.find_all('tr')

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

        response = requests.get(driver.current_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': 'dtable'})

        soup_2 = BeautifulSoup(str(table), 'html.parser')

        trs = soup_2.find_all('tr')
        name = trs[0].td.b.text.strip()

        description = trs[3].td.text.strip()
        if trs[1].td.b.a is None:
            company = trs[1].td.b.text.strip()
        else:
            company = trs[1].td.b.a.text.strip()

        date = trs[2].td.b.text.strip()

        soup_3 = BeautifulSoup(str(trs[2]), 'html.parser')

        bs = soup_3.find_all('b')
        deadline = bs[1].text.strip()

        description_2 = trs[3].td.text.strip().split(' ')

        salary = None

        email = None

        for j in range(len(description_2)):
            if 'ლარ' in description_2[j] and description_2[j - 1].isnumeric() or '₾' in description_2[j] or '$' in \
                    description_2[j]:
                salary = description_2[j - 1] + ' ' + description_2[j]
                break
            else:
                salary = None

        for j in range(len(description_2)):
            if '@' in description_2[j]:
                email = description_2[j]
                break
            else:
                email = None

        info = Job(name, description, company, date, deadline, salary, email)

        db = DataBase('job.db')
        db.add_job(info)

    time.sleep(5)
