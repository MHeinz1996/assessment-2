import csv

class Inventory:
    def __init__(self,id,title,rating,release_year,copies_available) -> None:
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def __str__(self) -> str:
        copies = 'copies'
        if self.copies_available == '1':
            copies = 'copy'
        return f"{self.title} ({self.release_year}) - {self.copies_available} {copies} available."

    @staticmethod
    def all_inventory():
        # return contents of student.csv
        inventory = []

        with open('data/inventory.csv', newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            for row in csv_reader:
                inventory.append(Inventory(**dict(row)))
            file.close()
        
        return inventory

# a_new_hope = Inventory('1234','Star Wars - A New Hope','PG','1977','1')
# print(a_new_hope)