class Star_Cinema:
    __hall_list = []

    def entry_hall(self, obj):
        self.__hall_list.append(obj)
    

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
    
    def entry_show(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        self.show_list.append((id, movie_name, time))

        arr = []
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                col.append(0)
            arr.append(col)
        index = len(self.seats)
        self.seats[index+1] = arr

    def book_seats(self, seat_id, seat_list):
        print('\n')
        if seat_id in self.seats:
            seat_layout = self.seats[seat_id]
            for row, col in seat_list:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if seat_layout[row][col] == 0:
                        seat_layout[row][col] = 1
                        print(f"Seat ({row}, {col}) booked successfully.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print("Invalid seat number.")
        else:
            print("Invalid Seat ID.")
        print('\n')

    def view_show_list(self):
        print('\nShow Lists:')
        for show in self.show_list:
            print(show)
        print('\n')

    def view_available_seats(self, seat_id):
        if seat_id in self.seats:
            print('\nAvailable Seats:')
            for s in self.seats[seat_id]:
                print(s)
            print('\n')
        else:
            print("\nInvalid Seat ID\n")


hall1 = Hall(rows=5, cols=5, hall_no=1)
hall1.entry_show('101', 'Movie1', '08:00 pm')
hall1.entry_show('102', 'Movie1', '10:00 pm')
hall1.entry_show('103', 'Movie3', '12:00 am')
# hall1.book_seats(2, [(2, 1)])
# hall1.book_seats(1, [(1, 1)])
# hall1.view_available_seats(2)

while True:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    take_input = input('Enter Option: ')
    if take_input == '4':
        break
    elif take_input == '1':
        hall1.view_show_list()
    elif take_input == '2':
        id = input('Enter Seat ID: ')
        hall1.view_available_seats(int(id))
    elif take_input == '3':
        id = input('Show ID: ')
        row = input('Enter Seat Row: ')
        col = input('Enter Seat Col: ')
        hall1.book_seats(int(id), [(int(row), int(col))])
