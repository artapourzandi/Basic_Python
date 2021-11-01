""" class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = point(10, 13)

print(p.x)
print(p.y)
print(p) """

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.cap():
            return False
        else: self.passengers.append(name)
        return True


    def cap(self):
        return self.capacity - len(self.passengers)



flight = Flight(3)

names = ["Nasi", "Vala", "Ahmad", "Omid", "Jamshid"]

for n in names:
    if flight.add_passenger(n):
        print(f"Passenger {n} is added to the list.")
    else: print(f"passenger {n} could not be added. cap reached")


print(flight.passengers)