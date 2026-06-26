# Query Results

Generated from the hotel reservation sample dataset for verification.

## Query 1 - View all customers

```text
+-------------+------------+-----------+--------------------------+------------+-------------------+
| customer_id | first_name | last_name | email                    | phone      | address           |
+-------------+------------+-----------+--------------------------+------------+-------------------+
| 1           | Kwame      | Mensah    | kwame.mensah@example.com | 0241112233 | Accra, Ghana      |
| 2           | Ama        | Boateng   | ama.boateng@example.com  | 0204445566 | Kumasi, Ghana     |
| 3           | Kofi       | Owusu     | kofi.owusu@example.com   | 0267778899 | Takoradi, Ghana   |
| 4           | Abena      | Asante    | abena.asante@example.com | 0551234567 | Cape Coast, Ghana |
+-------------+------------+-----------+--------------------------+------------+-------------------+
```

## Query 2 - Booking details with customer, room, and staff

```text
+------------+---------------+-------------+-----------+----------------+---------------+----------------+------------------+----------------+
| booking_id | customer_name | room_number | room_type | handled_by     | check_in_date | check_out_date | number_of_guests | booking_status |
+------------+---------------+-------------+-----------+----------------+---------------+----------------+------------------+----------------+
| 1          | Kwame Mensah  | 101         | Single    | Daniel Agyeman | 2026-07-01    | 2026-07-03     | 1                | Confirmed      |
| 2          | Ama Boateng   | 201         | Double    | Linda Osei     | 2026-07-05    | 2026-07-08     | 2                | Confirmed      |
| 3          | Kofi Owusu    | 301         | Deluxe    | Daniel Agyeman | 2026-07-10    | 2026-07-12     | 3                | Checked In     |
| 4          | Abena Asante  | 401         | Suite     | Michael Addo   | 2026-07-15    | 2026-07-20     | 4                | Confirmed      |
| 5          | Kwame Mensah  | 202         | Double    | Linda Osei     | 2026-07-22    | 2026-07-25     | 2                | Cancelled      |
+------------+---------------+-------------+-----------+----------------+---------------+----------------+------------------+----------------+
```

## Query 3 - Available rooms

```text
+---------+-------------+-----------+------------+--------------+
| room_id | room_number | room_type | base_price | floor_number |
+---------+-------------+-----------+------------+--------------+
| 1       | 101         | Single    | 80.00      | 1            |
| 3       | 201         | Double    | 120.00     | 2            |
| 5       | 301         | Deluxe    | 180.00     | 3            |
| 6       | 401         | Suite     | 300.00     | 4            |
+---------+-------------+-----------+------------+--------------+
```

## Query 4 - Total paid revenue

```text
+--------------------+
| total_paid_revenue |
+--------------------+
| 880.00             |
+--------------------+
```

## Query 5 - Bookings by room type

```text
+-----------+----------------+
| room_type | total_bookings |
+-----------+----------------+
| Deluxe    | 1              |
| Double    | 2              |
| Single    | 1              |
| Suite     | 1              |
+-----------+----------------+
```

## Query 6 - Updated booking status

```text
+------------+----------------+
| booking_id | booking_status |
+------------+----------------+
| 1          | Checked In     |
+------------+----------------+
```

## Query 7 - Inserted customer

```text
+-------------+------------+-----------+------------------------+------------+-------------+
| customer_id | first_name | last_name | email                  | phone      | address     |
+-------------+------------+-----------+------------------------+------------+-------------+
| 5           | Yaw        | Appiah    | yaw.appiah@example.com | 0279998888 | Tema, Ghana |
+-------------+------------+-----------+------------------------+------------+-------------+
```

## Query 8 - Customer deleted

```text
+-------------------------------+
| delete_result                 |
+-------------------------------+
| Customer deleted successfully |
+-------------------------------+
```
