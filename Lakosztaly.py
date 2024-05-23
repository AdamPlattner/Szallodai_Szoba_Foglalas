from Szoba import Room


class Suite(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.append(["double bed", "minibar", "jacuzzi", "sauna"])

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
        else:
            print("A szoba már le van foglalva.")

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
        else:
            print("A szoba nincs lefoglalva.")

    def __str__(self):
        return f"{self.number}"
