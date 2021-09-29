# Admin interacts with our system
class Admin():
    def __init__(self, name, email, password, phone):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone

    def reset_password(self):
        pass

    def modify_service_on_floor(self, floor_name):
        pass

    def change_display_settings(self):
        pass

    def send_notifications(self):
        pass

    def on_off_elevator(self, elevator_number):
        pass


class Elevator(object):

    # Initializes a new Elevator object
    def __init__(self, num_floors, starting_floor):
        # Total number of floors accessible by the elevator
        self.num_floors = num_floors
        # Current floor number
        self.current_floor = starting_floor
        # An unordered set of floor numbers that have been requested
        self.requested_floors = set()
        # An ordered list of floors that have been visited
        self.visited_floors = []
        # Number of floors traveled since the elevator was started
        self.num_floors_traveled = 0

    # Registers a request to visit a specific floor
    def request_floor(self, floor):
        self.requested_floors.add(floor)

    # Allocate elevators
    def allocate_elevators(self):
        pass

    # Computes number of floors passed when traveling from the current floor to
    # the given floor (including the given floor itself)
    def get_floor_difference(self, floor):
        return abs(self.current_floor - floor)

    # Travels to the given floor to pick up or drop off passengers
    def visit_floor(self, floor):
        self.num_floors_traveled += self.get_floor_difference(floor)
        self.current_floor = floor
        self.visited_floors.append(self.current_floor)
        # discard() will not raise an exception if floor does not exist
        self.requested_floors.discard(self.current_floor)

    # Starts elevator and travels computed route according to current requests
    def travel(self):
        # Visit next closest requested floor until all requested floors have
        # been visited
        while len(self.requested_floors) != 0:
            closest_floor = min(
                self.requested_floors, key=self.get_floor_difference)
            self.visit_floor(closest_floor)
