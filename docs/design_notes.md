# Design Notes

## Selected Domain

Hotel Reservation System.

## Main Goal

The database should help a hotel manage rooms, customers, bookings, staff, and payments.

## Initial Entities

1. Customer - a guest who makes a booking.
2. RoomType - category of room, such as Single, Double, Deluxe, or Suite.
3. Room - an individual room in the hotel.
4. Staff - hotel employee who handles bookings.
5. Booking - reservation made by a customer for a room.
6. Payment - payment made for a booking.

## Initial Relationships

- One customer can make many bookings.
- One room can appear in many bookings over time.
- One room type can describe many rooms.
- One staff member can handle many bookings.
- One booking can have one payment.

## Why This Scope Works

This scope is small enough to finish quickly, but it still demonstrates primary keys,
foreign keys, constraints, normalization, joins, aggregations, and realistic business logic.
