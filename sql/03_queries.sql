-- Demonstration queries for the hotel reservation database.
-- This file will include CRUD, joins, aggregations, and useful filters.
USE hotel_reservation_db;
-- Query 1: View all customers
SELECT *
FROM Customers;

-- Query 2: View all bookings with customer, room, and staff details
SELECT
    b.booking_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    r.room_number,
    rt.type_name AS room_type,
    CONCAT(s.first_name, ' ', s.last_name) AS handled_by,
    b.check_in_date,
    b.check_out_date,
    b.number_of_guests,
    b.booking_status
FROM Bookings b
JOIN Customers c ON b.customer_id = c.customer_id
JOIN Rooms r ON b.room_id = r.room_id
JOIN RoomTypes rt ON r.room_type_id = rt.room_type_id
JOIN Staff s ON b.staff_id = s.staff_id;

-- Query 3: Find rooms that are currently available
SELECT
    r.room_id,
    r.room_number,
    rt.type_name AS room_type,
    rt.base_price,
    r.floor_number
FROM Rooms r
JOIN RoomTypes rt ON r.room_type_id = rt.room_type_id
WHERE r.room_status = 'Available';

-- Query 4: Calculate total paid revenue
SELECT
    SUM(amount) AS total_paid_revenue
FROM Payments
WHERE payment_status = 'Paid';

-- Query 5: Count bookings by room type
SELECT
    rt.type_name AS room_type,
    COUNT(b.booking_id) AS total_bookings
FROM RoomTypes rt
JOIN Rooms r ON rt.room_type_id = r.room_type_id
JOIN Bookings b ON r.room_id = b.room_id
GROUP BY rt.type_name;

-- Query 6: Update a booking status
UPDATE Bookings
SET booking_status = 'Checked In'
WHERE booking_id = 1;

-- Query 7: Insert a new customer
INSERT INTO Customers (first_name, last_name, email, phone, address)
VALUES ('Yaw', 'Appiah', 'yaw.appiah@example.com', '0279998888', 'Tema, Ghana');

-- Query 8: Delete a customer record
DELETE FROM Customers
WHERE email = 'yaw.appiah@example.com';
