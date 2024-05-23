import uuid


class Reservation:
    def __init__(self, room, start_date, duration):
        self.id = str(uuid.uuid4())
        self.room = room
        self.start_date = start_date
        self.duration = duration

    def is_valid(self):
        if not self.room.is_booked:
            return True
        return False
