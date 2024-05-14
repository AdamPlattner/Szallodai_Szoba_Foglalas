# Reservation.py

import uuid


class Reservation:
    def __init__(self, room, start_date, end_date):
        self.id = str(uuid.uuid4())
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    def is_valid(self):
        if not self.room.is_booked:
            return self.start_date < self.end_date
        return False
