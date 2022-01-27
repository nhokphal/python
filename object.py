
# define clas
class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity # store value
        self.passengers = [] # empty list
    def add_passengers(self, name):
        if not self.add_seat():
            return False # return false
        self.passengers.append(name) # adding value to empty list in passengers
        return True
    def add_seat(self):
        return self.capacity - len(self.passengers) # basically convert value in name or already append in
        # passengers and minus capacity which is 3

flight = Flight(3)

people = ["Harry", "Ron", "Herminone", "Ginny"]

for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"added {person} to flight successfully")
    else:
        print(f"no avaible seats for {person}")
