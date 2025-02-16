--  Retrieve the names and email addresses of all customers from the “Customers” table.
SELECT Name; Email
FROM Customers;

-- Select the product names and prices from the “Products” table where the price is greater than $50.
SELECT ProductName, price
FROM Products
WHERE Price > 50;

-- Filter the orders table to show only those orders that were placed after January 1, 2023, and are in the “Shipped” status.
SELECT *
FROM Orders
WHERE OrderDate > '2023-01-01' AND Status = 'Shipped';

-- Use a subquery to find products whose unit price is greater than the average unit price of all products.
SELECT ProductName, Price
FROM Products
WHERE Price > (
    SELECT AVG(Price)
    FROM Products
);

-- Calculate the total number of employees in each department from the “Employees” table.
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department;


SQL


