create table products (
    product_id NUMERIC(50) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	category VARCHAR(50) NOT NULL,
	price DECIMAL(50) NOT NULL
);
insert into products (product_id, name, category, price) values (123, 'Smartphone', 'Electronics', 599.99);
insert into products (product_id, name, category, price) values (456, 'Phone_Case', 'Accessories', 19.99);
insert into products (product_id, name, category, price) values (789, 'Iphone', 'Electronics', 1299.99);
insert into products (product_id, name, category, price) values (101, 'Headphones', 'Accessories', 99.99);
insert into products (product_id, name, category, price) values (202, 'Smartwatch', 'Electronics', 299.99);

