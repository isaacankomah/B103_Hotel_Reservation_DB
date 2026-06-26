# Run Instructions

Use MySQL Workbench, phpMyAdmin, or another MySQL-compatible tool.

## Order

Run the SQL files in this order:

1. `sql/01_schema.sql`
2. `sql/02_sample_data.sql`
3. `sql/03_queries.sql`

## In MySQL Workbench

1. Open MySQL Workbench.
2. Connect to your local MySQL server.
3. Open `sql/01_schema.sql`.
4. Click the lightning/run button.
5. Open `sql/02_sample_data.sql` and run it.
6. Open `sql/03_queries.sql`.
7. Run each query one by one so you can screenshot and explain the output.

## Suggested Screenshots

Take screenshots for:

- all customers
- booking details with customer, room, and staff names
- available rooms
- total paid revenue
- booking count by room type
- update query result
- insert query result
- delete query result
