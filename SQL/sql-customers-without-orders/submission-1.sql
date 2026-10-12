-- Write your query below
SELECT name
FROM customers 
WHERE customers.id NOT IN (
    SELECT customer_id 
    FROM orders
);