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
        self.customers.append(new_customer) # Add new customer to customer list
        print(f"\nCustomer {new_customer.id}: {new_customer.first_name} {new_customer.last_name} ({new_customer.account_type}) has been added.")

    def rent_video(self):
        print(f"\nInput Customer ID for customer renting a video:\n")
        # Displays a list of customers for the user to choose from
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
        
        # Cycles through all customers in the list
        for customer in self.customers:
            videos = 'videos' # Used for string formatting purposes

            if customer.id == customer_id:
                # Make movie titles easier to work with
                if len(customer.current_video_rentals) != 0:
                    # Split rented movies into a list of the movie titles
                    rentals = customer.current_video_rentals.split('/')
                else:
                    # If customer doesn't have any movies checked out, initialize an empty list
                    rentals = []
                
                # Declaring variables to help with logic
                account_type = customer.account_type
                amount_of_rentals = 0
                restricted = False  # If a customer has a family account, this will turn to True

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

                # For output string formatting
                if len(rentals) == 1:
                    videos = 'video'

                print(f"\nCustomer {customer.first_name} {customer.last_name} has a {account_type} account.\nThey currently have {len(rentals)} {videos} checked out.")

                # Checks if customer has not reached their rental limit yet
                if len(rentals) < amount_of_rentals:
                    print(f"\nPlease enter the title of the movie that {customer.first_name} {customer.last_name} would like to check out:")
                    
                    # Prints out a list of movies to pick from
                    self.view_inventory()
                    
                    # Validates user input
                    validity = False
                    while validity != True:
                        movie = input("\n> ")
                        for title in self.inventory:
                            if movie == title.title:
                                validity = True
                                break
                        if validity == False:
                            print(f"\nTitle entered does not match any of the listed titles. Please enter the title again (case sensitive).")

                    # Cycles through all movies in inventory
                    for title in self.inventory:
                        if movie == title.title: # Checks to see if user input matches a movie in the inventory
                            if restricted == False: # Logic for customer that does not have a family account
                                if title.copies_available != '0': # Does not let user rent a movie that isn't available
                                    if len(customer.current_video_rentals) > 0:
                                        customer.current_video_rentals+= f"/{title.title}" # Update customer current video rentals
                                    else:
                                        customer.current_video_rentals+= f"{title.title}" # Update customer current video rentals
                                    title.copies_available = str(int(title.copies_available)-1) # Update inventory
                                    print(f"\n{customer.first_name} {customer.last_name} successfully rented {title.title} ({title.release_year})")
                                
                                else: # Prints if customer trys to rent a movie that has no available copies
                                    print(f"\nSorry, there are no more copies of {movie} available at this time.")
                            
                            elif restricted == True and title.rating == 'R': # Prints if a customer tries to rent an R-rated movie with a family account
                                print(f"\n{customer.first_name} {customer.last_name} has a family account.\nThey cannot rent 'R' rated movies.")
                            
                            else: # Customer has a restriced account, rents a movie that is not rated 'R'
                                if title.copies_available != '0': # Does not let user rent a movie that isn't available
                                    if len(customer.current_video_rentals) > 0:
                                        customer.current_video_rentals+= f"/{title.title}" # Update customer current video rentals
                                    else:
                                        customer.current_video_rentals+= f"{title.title}" # Update customer current video rentals
                                    title.copies_available = str(int(title.copies_available)-1) # Update inventory
                                    print(f"\n{customer.first_name} {customer.last_name} successfully rented {title.title} ({title.release_year})")
                                
                                else: # Prints if customer trys to rent a movie that has no available copies
                                    print(f"\nSorry, there are no more copies of {movie} available at this time.")
                
                else: # Does not let someone rent a movie if they are already at their limit per their account type
                    print(f"\n{customer.first_name} {customer.last_name} is already at their rental limit.")
                    print(len(rentals))
    
    def return_video(self):
        print(f"\nInput Customer ID for customer returning a video:\n")
        
        # Provides user a list of customers to select from
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
                # Shows what movies that customer currently has rented
                print(customer)
            
                # Splits movies into a list of titles
                rentals = customer.current_video_rentals.split('/')
                
                print(f"\nWhich movie is {customer.first_name} {customer.last_name} returning (title name)?")

                # Verifies user input
                validity = False
                while validity != True:
                    movie = input("\n> ")
                    for i, title in enumerate(rentals):
                        if movie == title:
                            validity = True
                            rentals.pop(i) # Remove title from rental list
                            print(f"\n{customer.first_name} {customer.last_name} returned {title}.")
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

                # Update customer object's current video rentals
                customer.current_video_rentals = ''.join(rentals)