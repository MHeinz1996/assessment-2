from inventory import Inventory
from customer import Customer

class Blockbuster:
    def __init__(self) -> None:
        self.customers = Customer.all_customers()
        self.inventory = Inventory.all_inventory()

    def view_inventory(self):
        print(f"\nCurrent inventory:\n------------------")
        for movie in self.inventory:
            print(movie)

    def customer_rented_videos(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                print(customer)

    def add_customer(self, customer_data):
        new_customer = Customer(customer_data['id'],customer_data['account_type'],customer_data['first_name'],customer_data['last_name'],customer_data['current_video_rentals'])
        self.customers.append(new_customer)
        print(f"\nCustomer {new_customer.id}: {new_customer.first_name} {new_customer.last_name} ({new_customer.account_type}) has been added.")

        for x in self.customers:
            print(x)

    def rent_video(self):
        print(f"\nInput Customer ID for customer renting a video:\n")
        for customer in self.customers:
            print(f"Customer {customer.id} - {customer.first_name} {customer.last_name}")
        
        # Ensure valid user input
        validity = False
        while validity != True:
            customer_id = input("\n> ")
            if customer_id.isdigit() == False:
                print(f"\nInvalid input, please select from options 1-{len(self.customers)}.")
            elif int(customer_id) == 0 or int(customer_id) > len(self.customers):
                print(f"\nInvalid input, please select from options 1-{len(self.customers)}.")
            else:
                validity = True
        
        for customer in self.customers:
            videos = 'videos'
            if customer.id == customer_id:
                # Make movie titles easier to work with
                if len(customer.current_video_rentals) != 0:
                    rentals = customer.current_video_rentals.split('/')
                else:
                    rentals = []
                
                account_type = customer.account_type
                amount_of_rentals = 0
                restricted = False

                # Set account type rules
                if account_type == 'sx':
                    amount_of_rentals = 1
                elif account_type == 'px':
                    amount_of_rentals = 3
                elif account_type == 'sf':
                    amount_of_rentals = 1
                    restricted = True
                else:
                    amount_of_rentals = 3
                    restricted = True

                if len(rentals) == 1:
                    videos = 'video'

                print(f"\nCustomer {customer.first_name} {customer.last_name} has a {account_type} account.\nThey currently have {len(rentals)} {videos} checked out.")

                if len(rentals) < amount_of_rentals:
                    print(f"\nPlease enter the title of the movie that {customer.first_name} {customer.last_name} would like to check out:")
                    self.view_inventory()
                    
                    validity = False
                    while validity != True:
                        movie = input("\n> ")
                        for title in self.inventory:
                            if movie == title.title:
                                validity = True
                                break
                        if validity == False:
                            print(f"\nTitle entered does not match any of the listed titles. Please enter the title again (case sensitive).")

                    for title in self.inventory:
                        if movie == title.title:
                            if restricted == False:
                                if title.copies_available != '0':
                                    if len(customer.current_video_rentals) > 0:
                                        customer.current_video_rentals+= f"/{title.title}" # Update customer current video rentals
                                    else:
                                        customer.current_video_rentals+= f"{title.title}" # Update customer current video rentals
                                    title.copies_available = str(int(title.copies_available)-1) # Update inventory
                                    print(f"\n {customer.first_name} {customer.last_name} successfully rented {title.title} ({title.release_year})")
                                else:
                                    print(f"\nSorry, there are no more copies of {movie} available at this time.")
                            elif restricted == True and title.rating == 'R':
                                print(f"\n{customer.first_name} {customer.last_name} has a family account.\nThey cannot rent 'R' rated movies.")
                    

                else: # Does not let someone rent a movie if they are already at their limit per their account type
                    print(f"\n{customer.first_name} {customer.last_name} is already at their max amount of rentals.")
                    print(len(rentals))
    
    def return_video(self):
        print(f"\nInput Customer ID for customer returning a video:\n")
        for customer in self.customers:
            print(f"Customer {customer.id} - {customer.first_name} {customer.last_name}")
        
        # Ensure valid user input
        validity = False
        while validity != True:
            customer_id = input("\n> ")
            if customer_id.isdigit() == False:
                print(f"\nInvalid input, please select from options 1-{len(self.customers)}.")
            elif int(customer_id) == 0 or int(customer_id) > len(self.customers):
                print(f"\nInvalid input, please select from options 1-{len(self.customers)}.")
            else:
                validity = True

        for customer in self.customers:
            if customer_id == customer.id:
                print(customer)
            
                rentals = customer.current_video_rentals.split('/')
                
                print(f"\nWhich movie is {customer.first_name} {customer.last_name} returning (title name)?")

                validity = False
                while validity != True:
                    movie = input("\n> ")
                    for i, title in enumerate(rentals):
                        if movie == title:
                            validity = True
                            rentals.pop(i) # Remove title from rental list
                            print(f"\n {customer.first_name} {customer.last_name} returned {title}.")
                            break
                    if validity == False:
                        print(f"\nTitle entered does not match any of the listed titles. Please enter the title again (case sensitive).")

                # Update inventory
                for title in self.inventory:
                    if movie == title.title:
                        title.copies_available = str(int(title.copies_available)+1)

                # Update customer's current video rentals         
                for i, title in enumerate(rentals):
                    rentals[i]= title + '/'

                customer.current_video_rentals = ''.join(rentals)