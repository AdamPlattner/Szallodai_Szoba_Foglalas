# Szállodai Szoba Foglalás

A terminal-based hotel room booking system built in Python, developed as a university OOP assignment at **Gábor Dénes Egyetem**.

**Author:** Plattner Ádám Gergely

---

## About

This project was created as a graded assignment for an Object-Oriented Programming course. The goal was to design and implement a working system using core OOP principles: abstraction, inheritance, and encapsulation.

The system simulates a hotel's room management, allowing users to book and cancel rooms, view availability and pricing, and save their bookings to a file.

---

## Features

- Book and cancel hotel rooms by room number
- View all rooms and available rooms
- View room prices
- Save confirmed bookings to a text file
- Pre-loaded demo rooms and reservations on startup

---

## Room Types

The system uses an abstract base class `Room` with three concrete types:

| Type | Class | Price |
|------|-------|-------|
| Single Room | `SingleRoom` | 25,000 Ft |
| Double Room | `DoubleRoom` | 55,000 Ft |
| Suite | `Suite` | 100,000 Ft |

---

## Project Structure

```
├── FoglaloRendszer.py   # Main entry point, menu loop
├── Szalloda.py          # Hotel class (manages rooms and bookings)
├── Szoba.py             # Abstract base class Room (ABC)
├── EgyagyasSzoba.py     # SingleRoom (inherits Room)
├── KetagyasSzoba.py     # DoubleRoom (inherits Room)
├── Lakosztaly.py        # Suite (inherits Room)
├── Foglalas.py          # Reservation class
└── adatok.txt           # Sample data file
```

---

## How to Run

Requires Python 3.x — no external dependencies.

```bash
python FoglaloRendszer.py
```

Then follow the on-screen menu:
```
1. Foglalás       – Book a room
2. Szoba Lista    – List all / available rooms
3. Ár Lista       – View prices
4. Lemondás       – Cancel a booking
5. Véglegesítés   – Save bookings to file
6. Kilépés        – Exit
```

---

## OOP Concepts Demonstrated

- **Abstract base class** (`Room` using Python's `abc` module)
- **Inheritance** (SingleRoom, DoubleRoom, Suite all extend Room)
- **Encapsulation** (room state managed through methods)
- **Composition** (Hotel contains a list of Room objects)
