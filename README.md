# Hotel Reservation Database Management System

## Project Overview

This repository contains a relational SQL database project for the B103 Databases & Big Data individual assessment.

The project models a hotel reservation system that stores and manages:

- customers
- room types
- rooms
- staff members
- bookings
- payments

The database demonstrates table design, primary keys, foreign keys, constraints, sample data, CRUD operations, joins, filtering, grouping, and aggregation.

## Student Details

- Student name: Isaac Ankomah
- Student ID: GH1056979
- Module: B103 Databases & Big Data
- Project title: Hotel Reservation Database Management System

## Repository Structure

```text
B103_Hotel_Reservation_DB/
|-- diagrams/
|   `-- er_diagram.mmd
|-- docs/
|   |-- design_notes.md
|   |-- final_report_template.md
|   |-- report_outline.md
|   |-- run_instructions.md
|   |-- sample_report_guide.md
|   |-- submission_checklist.md
|   `-- video_demo_plan.md
|-- outputs/
|   `-- query_results.md
|-- screenshots/
|   `-- query output images
|-- sql/
|   |-- 01_schema.sql
|   |-- 02_sample_data.sql
|   `-- 03_queries.sql
`-- tools/
    `-- generate_query_outputs.py
```

## SQL Files

Run the SQL files in this order:

1. `sql/01_schema.sql` - creates the database and tables.
2. `sql/02_sample_data.sql` - inserts sample data.
3. `sql/03_queries.sql` - demonstrates CRUD and analytical queries.

## Database Design Summary

The database uses six main tables:

| Table | Purpose |
|---|---|
| `Customers` | Stores hotel guest details. |
| `RoomTypes` | Stores room categories, prices, and guest capacity. |
| `Rooms` | Stores individual room records. |
| `Staff` | Stores staff members who manage bookings. |
| `Bookings` | Connects customers, rooms, and staff for each reservation. |
| `Payments` | Stores payment details for each booking. |

## Key Relationships

- One customer can make many bookings.
- One room type can describe many rooms.
- One room can appear in many bookings over time.
- One staff member can handle many bookings.
- One booking has one payment record.

## How to Run

Use MySQL Workbench or another MySQL-compatible tool.

1. Open `sql/01_schema.sql` and run it.
2. Open `sql/02_sample_data.sql` and run it.
3. Open `sql/03_queries.sql` and run each query one by one.

Detailed instructions are in `docs/run_instructions.md`.

## Verification Outputs

The terminal environment used during development did not have MySQL installed, so a local Python verification helper was added:

```bash
python tools/generate_query_outputs.py
```

This helper creates readable verification outputs in:

- `outputs/query_results.md`
- `screenshots/`

The official SQL submission files remain in the `sql/` folder.
