class ParkingGarage:

    def __init__(self, ticket=10, parking_spaces=10, current_ticket={}):
        self.ticket = ticket
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        


    def take_ticket(self):
            user_input = input(f' Welcome! there are {self.parking_spaces} spaces available. Do you want to park?[y]/[n] ').lower()
            if user_input == 'y':
                last_name = input('What is your last Name? ')
                license_number = int(input("Enter your Liscene Plate number"))
                self.current_ticket[last_name]= license_number
                # print("Please Enter and dont lose your ticket!!!")
                self.parking_spaces -= 1
                self.ticket -= 1
                
            else:
                 print('Please Exit Garage. ')
            




    def pay_for_parking(self):
        while True:
            user_input = input(f"Daily charge is $25 are you ready yo pay? [y]/[n] ").lower()
            if user_input == 'y':
                to_delete = input("what is your last name")
                del self.current_ticket[to_delete]
                print('Thank you, you have 15 min to leave garage')
                self.parking_spaces += 1
                self.ticket += 1
            else:
                print(f'Invalid entry please enter  : [y] or [n]')
            break


    def leave_garage(self):
        print(f"Ticket Paid Have a nice day!")
       


self=ParkingGarage(10)

print(self.take_ticket())
print(self.current_ticket)
print(self.pay_for_parking())
print(self.leave_garage())
# print(self.parking_spaces)


# print(self.current_ticket)
# self.current_ticket = ["trevino"]
# print(self.current_ticket)
# self.current_ticket[] = license