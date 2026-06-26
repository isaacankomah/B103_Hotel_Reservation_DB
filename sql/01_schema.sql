-- Hotel Reservation Database schema.
-- We will build this step by step and explain each table before finalizing it.

CREATE DATABASE hotel_reservation_db;
USE hotel_reservation_db;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE RoomTypes (
    room_type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(200),
    base_price DECIMAL(10, 2) NOT NULL,
    max_guests INT NOT NULL
);

CREATE TABLE Rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    room_status VARCHAR(20) DEFAULT 'Available',

    FOREIGN KEY (room_type_id) REFERENCES RoomTypes(room_type_id),
    CHECK (room_status IN ('Available', 'Occupied', 'Maintenance'))
);

CREATE TABLE Staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE Bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    staff_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    number_of_guests INT NOT NULL,
    booking_status VARCHAR(20) DEFAULT 'Confirmed',

    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id),

    CHECK (check_out_date > check_in_date),
    CHECK (number_of_guests > 0),
    CHECK (booking_status IN ('Confirmed', 'Checked In', 'Checked Out', 'Cancelled'))
);

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT UNIQUE NOT NULL,
    payment_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'Paid',

    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),

    CHECK (amount > 0),
    CHECK (payment_method IN ('Cash', 'Card', 'Mobile Money', 'Bank Transfer')),
    CHECK (payment_status IN ('Paid', 'Pending', 'Refunded'))
);