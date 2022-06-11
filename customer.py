import csv

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals) -> None:
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    def __str__(self) -> str:
        rentals = self.current_video_rentals.split('/')
        print(f"\nCustomer {self.id}: {self.first_name} {self.last_name} ({self.account_type})\n--------------")
        for movie in rentals:
            print(movie)
        return ''


    @staticmethod
    def all_customers():
        # return contents of student.csv
        customers = []

        with open('data/customers.csv', newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            for row in csv_reader:
                customers.append(Customer(**dict(row)))
            file.close()
        
        return customers