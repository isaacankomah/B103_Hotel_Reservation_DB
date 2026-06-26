-- Sample data for the hotel reservation database.
-- Add records only after the schema is complete.

USE hotel_reservation_db;

INSERT INTO RoomTypes (type_name, description, base_price, max_guests) VALUES
('Single', 'A room for one guest with one single bed', 80.00, 1),
('Double', 'A room for two guests with one double bed', 120.00, 2),
('Deluxe', 'A larger room with premium facilities', 180.00, 3),
('Suite', 'A luxury room with separate living space', 300.00, 4);

INSERT INTO Rooms (room_number, room_type_id, floor_number, room_status) VALUES
('101', 1, 1, 'Available'),
('102', 1, 1, 'Maintenance'),
('201', 2, 2, 'Available'),
('202', 2, 2, 'Occupied'),
('301', 3, 3, 'Available'),
('401', 4, 4, 'Available');

INSERT INTO Customers (first_name, last_name, email, phone, address) VALUES
('Kwame', 'Mensah', 'kwame.mensah@example.com', '0241112233', 'Accra, Ghana'),
('Ama', 'Boateng', 'ama.boateng@example.com', '0204445566', 'Kumasi, Ghana'),
('Kofi', 'Owusu', 'kofi.owusu@example.com', '0267778899', 'Takoradi, Ghana'),
('Abena', 'Asante', 'abena.asante@example.com', '0551234567', 'Cape Coast, Ghana');

INSERT INTO Staff (first_name, last_name, role, email, phone) VALUES
('Daniel', 'Agyeman', 'Receptionist', 'daniel.agyeman@hotel.com', '0302221111'),
('Linda', 'Osei', 'Booking Officer', 'linda.osei@hotel.com', '0302223333'),
('Michael', 'Addo', 'Manager', 'michael.addo@hotel.com', '0302225555');

INSERT INTO Bookings (
    customer_id,
    room_id,
    staff_id,
    check_in_date,
    check_out_date,
    number_of_guests,
    booking_status
) VALUES
(1, 1, 1, '2026-07-01', '2026-07-03', 1, 'Confirmed'),
(2, 3, 2, '2026-07-05', '2026-07-08', 2, 'Confirmed'),
(3, 5, 1, '2026-07-10', '2026-07-12', 3, 'Checked In'),
(4, 6, 3, '2026-07-15', '2026-07-20', 4, 'Confirmed'),
(1, 4, 2, '2026-07-22', '2026-07-25', 2, 'Cancelled');

INSERT INTO Payments (
    booking_id,
    payment_date,
    amount,
    payment_method,
    payment_status
) VALUES
(1, '2026-06-25', 160.00, 'Mobile Money', 'Paid'),
(2, '2026-06-26', 360.00, 'Card', 'Paid'),
(3, '2026-07-10', 360.00, 'Cash', 'Paid'),
(4, '2026-07-12', 1500.00, 'Bank Transfer', 'Pending'),
(5, '2026-07-18', 360.00, 'Card', 'Refunded');
