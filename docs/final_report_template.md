# Hotel Reservation Database Management System

Gisma University of Applied Sciences

School of Computer Science

Module: B103 Databases & Big Data

Assessment Title: Individual Project

Student Name: Isaac Ankomah

Student ID: GH1056979

GitHub Repository: https://github.com/isaacankomah/B103_Hotel_Reservation_DB

Video Demonstration Link: [Add your video link here after recording]

## 1. Introduction

Write this section in your own words.

Cover these points:

- the project is a hotel reservation database system
- the problem it solves
- why a relational database is suitable
- the main operations the system supports

Suggested structure:

Paragraph 1: Introduce the hotel reservation problem.

Paragraph 2: Explain the aim of the database.

Paragraph 3: Briefly mention the main tables and operations.

## 2. System Design

Write this section in your own words.

Include the ER diagram from `diagrams/er_diagram.mmd` or an exported image of the diagram.

Explain these entities:

- Customers
- RoomTypes
- Rooms
- Staff
- Bookings
- Payments

Explain these relationships:

- One customer can make many bookings.
- One room type can describe many rooms.
- One room can be used in many bookings over time.
- One staff member can handle many bookings.
- One booking has one payment.

Also explain that the design reduces duplication by storing room category information in `RoomTypes` instead of repeating it inside every room record.

## 3. Implementation

Write this section in your own words.

Mention that the database was implemented using SQL and split into three files:

- `01_schema.sql`
- `02_sample_data.sql`
- `03_queries.sql`

Explain:

- primary keys uniquely identify rows
- foreign keys connect related tables
- unique constraints prevent duplicate emails and room numbers
- check constraints restrict invalid values
- default values make common statuses easier to manage

Use examples from the schema:

- `customer_id` is the primary key in `Customers`
- `room_type_id` is a foreign key in `Rooms`
- `booking_id` is a foreign key in `Payments`
- `check_out_date > check_in_date` prevents invalid booking dates
- `amount > 0` prevents invalid payment amounts

## 4. Results

Write this section in your own words.

Use the query screenshots from the `screenshots/` folder.

Recommended screenshots:

1. `query_1_customers.png`
2. `query_2_booking_details.png`
3. `query_3_available_rooms.png`
4. `query_4_total_paid_revenue.png`
5. `query_5_bookings_by_room_type.png`
6. `query_6_updated_booking_status.png`
7. `query_7_inserted_customer.png`
8. `query_8_customer_deleted.png`

For each screenshot, explain what the query proves.

Example explanation pattern:

The booking details query joins five tables: `Bookings`, `Customers`, `Rooms`, `RoomTypes`, and `Staff`. This shows that the database can combine related records and produce readable booking information instead of only displaying ID numbers.

## 5. Challenges and Solutions

Write this section in your own words.

Possible points to discuss:

- inserting data in the correct order because of foreign keys
- separating `RoomTypes` from `Rooms` to avoid repeated data
- designing queries that show both simple and advanced SQL operations
- using constraints to prevent invalid data

Keep this section honest. Use challenges you understand and can explain in your video.

## 6. Conclusion and Future Work

Write this section in your own words.

Conclusion points:

- the database stores hotel reservation information in a structured way
- it supports bookings, room availability checks, payment records, and revenue queries
- relationships and constraints help keep data consistent

Future work ideas:

- add hotel branches
- support multiple payments per booking
- add room cleaning or maintenance scheduling
- improve room availability checks by date range
- add user roles for administrators and reception staff

## References

Use Harvard referencing style if you include external sources.

Possible references:

MySQL. n.d. MySQL Documentation. Available at: https://dev.mysql.com/doc/

Lucidchart. n.d. What is an Entity Relationship Diagram? Available at: https://www.lucidchart.com/pages/er-diagrams
