"""Generate verification outputs for the hotel reservation database.

This script uses Python's built-in SQLite engine to verify the same table
relationships and query logic used in the MySQL project files. The submitted
SQL files remain MySQL-compatible; this script is only for local checking and
creating readable outputs when MySQL is unavailable in the terminal.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
SCREENSHOT_DIR = ROOT / "screenshots"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE Customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20),
            address VARCHAR(150),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE RoomTypes (
            room_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name VARCHAR(50) UNIQUE NOT NULL,
            description VARCHAR(200),
            base_price DECIMAL(10, 2) NOT NULL,
            max_guests INT NOT NULL
        );

        CREATE TABLE Rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number VARCHAR(10) UNIQUE NOT NULL,
            room_type_id INT NOT NULL,
            floor_number INT NOT NULL,
            room_status VARCHAR(20) DEFAULT 'Available',

            FOREIGN KEY (room_type_id) REFERENCES RoomTypes(room_type_id),
            CHECK (room_status IN ('Available', 'Occupied', 'Maintenance'))
        );

        CREATE TABLE Staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            role VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20)
        );

        CREATE TABLE Bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        """
    )


def insert_sample_data(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
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
        """
    )


def fetch_rows(conn: sqlite3.Connection, sql: str) -> tuple[list[str], list[tuple[object, ...]]]:
    cur = conn.execute(sql)
    headers = [description[0] for description in cur.description]
    rows = cur.fetchall()
    return headers, rows


def format_table(headers: list[str], rows: list[tuple[object, ...]]) -> str:
    values = [[str(value) if value is not None else "" for value in row] for row in rows]
    widths = [
        max(len(header), *(len(row[index]) for row in values)) if values else len(header)
        for index, header in enumerate(headers)
    ]
    border = "+-" + "-+-".join("-" * width for width in widths) + "-+"
    header_line = "| " + " | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)) + " |"
    body = [
        "| " + " | ".join(row[index].ljust(widths[index]) for index in range(len(headers))) + " |"
        for row in values
    ]
    return "\n".join([border, header_line, border, *body, border])


def render_png(title: str, table_text: str, filename: str) -> None:
    font_path = Path("C:/Windows/Fonts/consola.ttf")
    if font_path.exists():
        title_font = ImageFont.truetype(str(font_path), 22)
        body_font = ImageFont.truetype(str(font_path), 16)
    else:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    lines = [title, ""] + table_text.splitlines()
    dummy = Image.new("RGB", (1, 1), "white")
    draw = ImageDraw.Draw(dummy)
    line_metrics = [draw.textbbox((0, 0), line, font=title_font if index == 0 else body_font) for index, line in enumerate(lines)]
    widths = [bbox[2] - bbox[0] for bbox in line_metrics]
    heights = [bbox[3] - bbox[1] for bbox in line_metrics]
    padding = 24
    line_gap = 8
    image_width = max(widths) + (padding * 2)
    image_height = sum(heights) + (line_gap * (len(lines) - 1)) + (padding * 2)

    image = Image.new("RGB", (image_width, image_height), "#ffffff")
    draw = ImageDraw.Draw(image)
    y = padding
    for index, line in enumerate(lines):
        font = title_font if index == 0 else body_font
        fill = "#111827" if index == 0 else "#1f2937"
        draw.text((padding, y), line, font=font, fill=fill)
        y += heights[index] + line_gap

    image.save(SCREENSHOT_DIR / filename)


def add_result(
    sections: list[str],
    conn: sqlite3.Connection,
    title: str,
    sql: str,
    png_name: str,
) -> None:
    headers, rows = fetch_rows(conn, sql)
    table = format_table(headers, rows)
    sections.append(f"## {title}\n\n```text\n{table}\n```\n")
    render_png(title, table, png_name)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    SCREENSHOT_DIR.mkdir(exist_ok=True)

    conn = connect()
    create_schema(conn)
    insert_sample_data(conn)

    sections = [
        "# Query Results\n",
        "Generated from the hotel reservation sample dataset for verification.\n",
    ]

    add_result(
        sections,
        conn,
        "Query 1 - View all customers",
        "SELECT customer_id, first_name, last_name, email, phone, address FROM Customers;",
        "query_1_customers.png",
    )
    add_result(
        sections,
        conn,
        "Query 2 - Booking details with customer, room, and staff",
        """
        SELECT
            b.booking_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            r.room_number,
            rt.type_name AS room_type,
            s.first_name || ' ' || s.last_name AS handled_by,
            b.check_in_date,
            b.check_out_date,
            b.number_of_guests,
            b.booking_status
        FROM Bookings b
        JOIN Customers c ON b.customer_id = c.customer_id
        JOIN Rooms r ON b.room_id = r.room_id
        JOIN RoomTypes rt ON r.room_type_id = rt.room_type_id
        JOIN Staff s ON b.staff_id = s.staff_id;
        """,
        "query_2_booking_details.png",
    )
    add_result(
        sections,
        conn,
        "Query 3 - Available rooms",
        """
        SELECT
            r.room_id,
            r.room_number,
            rt.type_name AS room_type,
            printf('%.2f', rt.base_price) AS base_price,
            r.floor_number
        FROM Rooms r
        JOIN RoomTypes rt ON r.room_type_id = rt.room_type_id
        WHERE r.room_status = 'Available';
        """,
        "query_3_available_rooms.png",
    )
    add_result(
        sections,
        conn,
        "Query 4 - Total paid revenue",
        """
        SELECT
            printf('%.2f', SUM(amount)) AS total_paid_revenue
        FROM Payments
        WHERE payment_status = 'Paid';
        """,
        "query_4_total_paid_revenue.png",
    )
    add_result(
        sections,
        conn,
        "Query 5 - Bookings by room type",
        """
        SELECT
            rt.type_name AS room_type,
            COUNT(b.booking_id) AS total_bookings
        FROM RoomTypes rt
        JOIN Rooms r ON rt.room_type_id = r.room_type_id
        JOIN Bookings b ON r.room_id = b.room_id
        GROUP BY rt.type_name;
        """,
        "query_5_bookings_by_room_type.png",
    )

    conn.execute("UPDATE Bookings SET booking_status = 'Checked In' WHERE booking_id = 1;")
    add_result(
        sections,
        conn,
        "Query 6 - Updated booking status",
        "SELECT booking_id, booking_status FROM Bookings WHERE booking_id = 1;",
        "query_6_updated_booking_status.png",
    )

    conn.execute(
        """
        INSERT INTO Customers (first_name, last_name, email, phone, address)
        VALUES ('Yaw', 'Appiah', 'yaw.appiah@example.com', '0279998888', 'Tema, Ghana');
        """
    )
    add_result(
        sections,
        conn,
        "Query 7 - Inserted customer",
        "SELECT customer_id, first_name, last_name, email, phone, address FROM Customers WHERE email = 'yaw.appiah@example.com';",
        "query_7_inserted_customer.png",
    )

    conn.execute("DELETE FROM Customers WHERE email = 'yaw.appiah@example.com';")
    add_result(
        sections,
        conn,
        "Query 8 - Customer deleted",
        """
        SELECT
            CASE
                WHEN COUNT(*) = 0 THEN 'Customer deleted successfully'
                ELSE 'Customer still exists'
            END AS delete_result
        FROM Customers
        WHERE email = 'yaw.appiah@example.com';
        """,
        "query_8_customer_deleted.png",
    )

    (OUTPUT_DIR / "query_results.md").write_text("\n".join(sections), encoding="utf-8")
    print(f"Wrote {(OUTPUT_DIR / 'query_results.md')}")
    print(f"Wrote PNG outputs to {SCREENSHOT_DIR}")


if __name__ == "__main__":
    main()
