-- SQL-команды для создания таблиц
CREATE TABLE customers
(
    customer_id varchar(5) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
);

CREATE TABLE employees
(
    employee_id smallserial PRIMARY KEY,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders
(
    order_id smallserial PRIMARY KEY,
    customer_id varchar(100) REFERENCES customers(customer_id) NOT NULL,
    employee_id smallserial REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(100)
);
