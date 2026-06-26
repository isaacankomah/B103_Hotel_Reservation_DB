# B103 Hotel Reservation Database Project

This workspace is for building a hotel reservation relational database system.

## Project Structure

- `sql/01_schema.sql` - database tables, keys, relationships, and constraints.
- `sql/02_sample_data.sql` - sample records for testing the database.
- `sql/03_queries.sql` - CRUD and analytical queries for the demonstration.
- `docs/report_outline.md` - report structure to complete in your own words.
- `docs/video_demo_plan.md` - short plan for a 3 to 5 minute screen recording.
- `diagrams/` - ER diagram files or exported images.
- `screenshots/` - query output screenshots for the report.
- `outputs/query_results.md` - generated query results for checking the database logic.
- `tools/generate_query_outputs.py` - local verification helper used when MySQL is unavailable.

## Chosen Domain

Hotel Reservation System.

The system stores hotel customers, room types, rooms, staff, bookings, and payments.

## Running the Project

Use `docs/run_instructions.md` to run the SQL files in MySQL Workbench.

If MySQL is unavailable in the terminal, run the local verification helper:

```bash
python tools/generate_query_outputs.py
```
