"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


CUSTOMERS_DATA_PATH = 'north_data/customers_data.csv'
EMPLOYEES_DATA_PATH = 'north_data/employees_data.csv'
ORDERS_DATA_PATH = 'north_data/orders_data.csv'
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='123qwe')

try:
    with conn:
        with conn.cursor() as cur:
            with open(CUSTOMERS_DATA_PATH, 'r', encoding='utf8') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (line['customer_id'], line['company_name'], line['contact_name']))

            with open(EMPLOYEES_DATA_PATH, 'r', encoding='utf8') as file:
                reader = csv.DictReader(file)
                employee_id = 0
                for line in reader:
                    employee_id += 1
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee_id, line['first_name'], line['last_name'], line['title'], line['birth_date'], line['notes']))

            with open(ORDERS_DATA_PATH, 'r', encoding='utf8') as file:
                reader = csv.DictReader(file)
                for line in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (line['order_id'], line['customer_id'], line['employee_id'], line['order_date'], line['ship_city']))

finally:
    conn.close()
