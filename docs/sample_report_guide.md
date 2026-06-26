# Sample Report Guide

Important: Do not submit this wording unchanged. Use it to understand what each
section should contain, then rewrite the final report in your own words.

# Hotel Reservation Database Management System

## First Page

Student name: [Your full name]

Student ID: [Your student ID]

Module: B103 Databases & Big Data

Project title: Hotel Reservation Database Management System

GitHub repository: https://github.com/isaacankomah/B103_Hotel_Reservation_DB

Video demonstration link: [Add your video link after recording]

## 1. Introduction

This project designs and implements a relational database system for a hotel
reservation environment. Hotels need to manage customers, rooms, bookings,
staff members, and payments in an organized way. Without a structured database,
records can become duplicated, inconsistent, or difficult to search.

The main objective of this project is to create a SQL database that stores hotel
reservation data and supports useful operations such as adding customers,
checking available rooms, recording bookings, updating booking status, and
calculating revenue. The chosen domain is suitable for a relational database
because it contains clear relationships between entities. For example, a
customer can make many bookings, a room can be booked many times over different
dates, and each booking can have one related payment.

## 2. System Design

The database contains six main entities: Customers, RoomTypes, Rooms, Staff,
Bookings, and Payments.

The Customers table stores guest information such as name, email, phone number,
and address. The RoomTypes table stores categories of rooms, including the base
price and maximum number of guests. The Rooms table stores individual hotel
rooms and links each room to a room type. The Staff table stores employees who
handle bookings. The Bookings table connects customers, rooms, and staff
members. The Payments table records payment information for each booking.

The main relationships are:

- One customer can make many bookings.
- One room type can describe many rooms.
- One room can be used in many bookings over time.
- One staff member can handle many bookings.
- One booking has one payment record.

The design avoids unnecessary duplication by separating room type details from
individual room records. This means that information such as base price and
maximum guests is stored once in the RoomTypes table instead of being repeated
for every room.

## 3. Implementation

The database was implemented using SQL. The schema file creates the database
and defines all tables, primary keys, foreign keys, unique constraints, default
values, and check constraints.

Each table has a primary key to uniquely identify records. For example,
customer_id identifies each customer, room_id identifies each room, and
booking_id identifies each booking. Foreign keys are used to enforce
relationships between tables. For example, the Bookings table contains
customer_id, room_id, and staff_id, which reference the Customers, Rooms, and
Staff tables.

Constraints were added to improve data quality. The email fields in Customers
and Staff are unique so the same email cannot be entered twice. The booking
date constraint checks that the check-out date is after the check-in date. The
payment amount must be greater than zero, and fields such as booking_status and
payment_method are limited to valid values.

Sample data was inserted into the database to demonstrate how the system works.
The sample data includes room types, rooms, customers, staff, bookings, and
payments.

## 4. Results

Several SQL queries were created to demonstrate the functionality of the
database.

The first query displays all customers. This confirms that customer records are
stored correctly.

The second query joins Bookings, Customers, Rooms, RoomTypes, and Staff. This is
important because it shows complete booking information in a readable format
instead of only showing ID numbers.

The third query lists available rooms by joining Rooms and RoomTypes and
filtering records where room_status is Available.

The fourth query calculates total paid revenue using the SUM function and only
includes payments with the status Paid.

The fifth query counts bookings by room type using COUNT and GROUP BY. This
helps the hotel understand which room types are booked more often.

The final queries demonstrate CRUD operations. A booking status is updated, a
new customer is inserted, and then that customer is deleted using the unique
email address.

These results show that the database supports storage, retrieval, updates,
deletions, joins, filtering, and aggregation.

## 5. Challenges and Solutions

One challenge was deciding the correct order for creating and inserting data
into tables. Since some tables depend on others through foreign keys, the parent
tables must be created and filled first. For example, RoomTypes must exist
before Rooms can reference them, and Customers, Rooms, and Staff must exist
before Bookings can be inserted.

Another challenge was avoiding duplicated information. Room type details could
have been stored directly in the Rooms table, but this would repeat the same
price and guest limit many times. The solution was to create a separate
RoomTypes table and link Rooms to it using a foreign key.

A further challenge was making the demonstration queries realistic. The
solution was to include both simple queries and more advanced queries involving
joins, aggregations, updates, inserts, and deletes.

## 6. Conclusion and Future Work

The project successfully implements a relational database for managing hotel
reservations. It stores customers, rooms, staff, bookings, and payments in a
structured way. The use of primary keys, foreign keys, unique constraints, and
check constraints helps maintain data accuracy and consistency.

The database also supports useful hotel operations such as checking room
availability, viewing booking details, calculating revenue, and analyzing
bookings by room type.

Future improvements could include adding a table for hotel branches, supporting
multiple payments for one booking, tracking room cleaning status, and adding a
date-based availability query that checks whether a room is free for a specific
period.

## References

MySQL Documentation. Available at: https://dev.mysql.com/doc/

Lucidchart. Entity Relationship Diagram Tutorial. Available at:
https://www.lucidchart.com/pages/er-diagrams
