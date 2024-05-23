from Szoba import Room


class SingleRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.append("single bed")

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"A {self.number} szoba sikeresen lefoglalva.")
        else:
            print("A szoba már le van foglalva.")

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
            print("A szoba most nincs lefoglalva.")
        else:
            print("A szoba nincs lefoglalva.")

    def __str__(self):
        return f"{self.number}"

 # lknfljndfslfnm,