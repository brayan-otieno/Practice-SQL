-- Create the orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    Total DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Students(CustomerID)
);

-- Insert data into the orders table
INSERT INTO Orders (OrderID, CustomerID, OrderDate, Total)
VALUES (1, 101, '2025-01-15', 250.00);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Total)
VALUES (2, 102, '2025-01-15', 150.50);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Total)
VALUES (3, 103, '2025-01-16', 300.75);

-- Retrieve All Orders Placed on a Specific Date
SELECT * FROM Orders
WHERE OrderDate = '2025-01-15';

-- Retrieve Orders for a Specific Customer, Including the Customer’s Name and Emai
SELECT Orders.OrderID, Orders.OrderDate, Orders.Total, Students.Name, Students.Email
FROM Orders
JOIN Students ON Orders.CustomerID = Students.CustomerID
WHERE Orders.CustomerID = 101;

--  Update Data in the Orders Table
UPDATE Orders
SET Total = 175.00
WHERE OrderID = 2;

-- Delete Data from the Orders Table
DELETE FROM Orders
WHERE OrderID = 1;


