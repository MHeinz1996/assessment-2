from blockbuster import Blockbuster
from inventory import Inventory
from customer import Customer

# Function used to test user input validity
def valid(options, user_input):
    
    if user_input.isdigit() == False: # If user input is anything other than a number, return false
        return False
    elif int(user_input) == 0 or int(user_input) > options: # If user input is not one of the options listed, return false
        return False
    else:
        return True


blockbuster = Blockbuster()

print("\n== Welcome to Blockbuster! ==")

mode = None
while(mode != '6'):
    mode = input("\nWhat would you like to do?\n1. View store video inventory\n2. View customer rented videos\n3. Add a new customer\n4. Rent video\n5. Return video\n6. Exit\n\n> ")

    if mode == '1': # View store video inventory

        Blockbuster.view_inventory(blockbuster)

    elif mode == '2': # View customer rented videos

        print(f"\nEnter the ID of the customer you would like to view:\n")
        for customer in blockbuster.customers:
            print(f"Customer {customer.id} - {customer.first_name} {customer.last_name}")
        
        validity = False
        while validity != True:
            customer_id = input("\n> ")
            if valid(len(blockbuster.customers), customer_id):
                validity = True
            else:
                print(f"\nInvalid input, please select from options 1-{len(blockbuster.customers)}.")

        Blockbuster.customer_rented_videos(blockbuster, customer_id)

    elif mode == '3': # Add a new customer

        customer_data = {'id': str(len(blockbuster.customers)+1)} # This ensures that every new entry has a new ID
        customer_data['first_name'] = input("\nFirst name: ")
        customer_data['last_name'] = input("Last name: ")

        validity = False
        while validity != True: # Ensures user enters a valid input
            account_type = input("\nSelect account type:\n\n1. Standard account: max 1 rental out at a time\n2. Premium account: max 3 rentals out at a time\n3. standard family account: max 1 rental out at a time AND can not rent any 'R' rated movies\n4. premium family account: max 3 rentals out at a time AND can not rent any 'R' rated movies\n\n> ")
            if valid(4, account_type):
                validity = True
            else:
                print(f"\nInvalid input, please select from options 1-4.")

        # Convert user input to proper account type
        if account_type == '1':
            customer_data['account_type'] = 'sx'
        elif account_type == '2':
            customer_data['account_type'] = 'px'
        elif account_type == '3':
            customer_data['account_type'] = 'sf'
        else:
            customer_data['account_type'] = 'pf'                
        
        # New users should not have an initial video list
        customer_data['current_video_rentals'] = '' 

        Blockbuster.add_customer(blockbuster, customer_data)

    elif mode == '4': # Rent video
        Blockbuster.rent_video(blockbuster)
    elif mode == '5': # Return video
        Blockbuster.return_video(blockbuster)
    elif mode == '6': # Exit
        print("\nGoodbye!")
    else:   # If input is not 1-6
        print("\nInvalid input, please select from options 1-6.")