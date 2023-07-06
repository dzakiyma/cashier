from tabulate import tabulate
from datetime import datetime

class Welcome:
    """
    This class have a main function, it's to create an instance
    which will be processed in the child class later.
    """
    
    def start():
        '''
        In this method you will enter your name as first.
        And the program will show you the menu, 
        so you can pick your order and create an instance.
        '''
        name_input = input("Enter your name\t: ")
        while True:
            if name_input != '':
                break
            else:
                print("Please enter your name first.")
                name_input = input("Enter your name\t: ")
        print('')
        print(f'Welcome! {name_input}')
        menu_list = [[a, b] for a, b in Customer.menu_price.items()] 
        #list of lists menu to show in tabulate format
        print(tabulate(menu_list, headers=['Menu', 'Price(Rp)'], tablefmt='pretty'))
        
        order = []  #List to save your ordered items.
        order_amount = []  #List to save your number of ordered items.
        
        question = input('Do you want to order? (Yes/No) :').lower()
        
        #Validate the question input that must be 'yes' or 'no'.
        if question == 'no':
            print("Thank You, Have a nice day!")
            pass
        while question != 'yes' and question != 'no':
            question = input("Please only insert 'yes' or 'no' :").lower()
        
        while question == 'yes':
            menu_items = [keys for keys, value in Customer.menu_price.items()]
            items_input = input('Insert your items\t: ')
            if items_input not in menu_items:
                while items_input not in menu_items:
                    print('')
                    print("The item not available in menu,please select another items available in menu.\n(Case sensitive)")
                    items_input = input('Insert your items\t: ')                 
            amount_input = input('Insert the amount\t: ')
            
            #Validate the amount_input that must be a number.
            while True:
                try:
                    value_check = int(amount_input)
                    if type(value_check) is int:
                        amount_input = value_check      
                        break  
                except ValueError:
                    print('Please insert item amount in number.')
                    amount_input = input('Insert the amount\t: ') 
                    
            #Save the order details.
            if items_input in order:
                i = order.index(items_input)
                order[i] = items_input
                order_amount[i] = order_amount[i] + amount_input
            elif items_input not in order:        
                order.append(items_input)
                order_amount.append(amount_input) 
            
            #Confirmation whether wanna order again or no, and validating the input.
            question = input('Do you want to order again? (Yes/No) :').lower()  
            while question != 'yes' and question != 'no':
                question = input("Please only insert 'yes' or 'no' :").lower()
            if question == 'no':
                customer1 = Customer(name_input, order, order_amount)
                customer1.calculate_bill()
                break
            
#--------------------------------------------------------------------------------------------------------------------#

class Customer(Welcome):
    """
    This is Child class of 'Welcome'.
    The instance that created before in Welcome.start()
    will be used here as object and will be processed.
    """
    #transaction_data is to save the order history from customer.
    transaction_data = [["ID Transaction", "Customer Name", "Ordered Menu", "Amounts", "Total Bill", "Date Time"]]
    menu_price = {
        '------Main------': '',
        'Finger Chicken' : 42_000,
        'Chicken Grilled' : 43_000,
        'Chicken Katsu' : 42_000,
        'Chicken Marsala' : 47_000,
        'Chicken Prame' : 40_000,
        '~' : '',
        '-----Drinks-----' : '',
        'Lemon Tea' : 23_000,
        'Lychee Tea' : 24_000,
        'Green Tea' : 27_000,
        'Vanilla Cream' : 34_000,
        'Chocolate Cream' : 32_000,
        'Coffee' : 32_000,
        'Caramel Coffee' : 32_000,
        '~' : '',
        '-----Snacks-----' : '',
        'Sushi Roll' : 27_000,
        'French Fries' : 25_000,
        'Potato Wedges' : 26_000,
        'Onion Ring' : 20_000,
        'Cupcake' : 22_000,
        'Donuts Choco' : 27_000
    }
    
    def __init__(self, name, order, order_amount):
        self.name = name
        self.items = order
        self.num_of_items = order_amount
        self.final_bill = [] #List to save the final bill after (if there any) calculate discount.
        self.id_transaksi = datetime.today().strftime("%m%d%H%M") + '-' + self.name[:2].lower()
        self.transaction_data.append([self.id_transaksi, 
                                      self.name,
                                      self.items,
                                      self.num_of_items,
                                      self.final_bill,
                                      datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                                    ])          
        self.ordered_items = {} #Dict. to save the data of the ordered items and the amounts.
        
        for i in range(0, len(self.items)):
            self.ordered_items.update({self.items[i] : self.num_of_items[i]})
       
    def add_item(self):
        """
        Method for add some items, besides you have added in Welcome.start() at first.
        """
        new_item = input("Enter the items you want to add\t: ")
        menu_items = [keys for keys, value in Customer.menu_price.items()]
        
        #Check input are available in menu_items or not.
        while new_item not in menu_items:
            print("Please only insert item which avaliable in menu.\n(Case Sensitive)")
            new_item = input("Enter the items you want to add\t: ")
            
        items_total = input("Enter the amount of the items\t: ")
        #Vaidate input must be in a number.
        while items_total:
            try:
                value_check = int(items_total)
                if type(value_check) is int:
                    items_total = value_check      
                    break  
            except ValueError:
                print('Please insert the item amount in number.')
                items_total = input('Insert the amount\t: ')
        
        #Check whether new item already in order list or not.
        if new_item in self.items:
            i = self.items.index(new_item)
            self.items[i] = new_item
            self.num_of_items[i] = self.num_of_items[i] + items_total
            self.ordered_items.update({self.items[i] : self.num_of_items[i]})  
        elif new_item not in self.items:   
            self.items.append(new_item)
            self.num_of_items.append(items_total)
            update_items = {new_item : items_total} #This dict used for update the ordered_items.
            self.ordered_items.update(update_items)
        
        add_confirmation = input("Do you want to add another items?\t(yes/no): ").lower()
        if add_confirmation == 'yes':
            self.add_item()
        elif add_confirmation == 'no':       
            self.calculate_bill()       
        else:
            while add_confirmation != 'no' and add_confirmation != 'yes':
                print("Please insert only with 'yes' or 'no'.")
                add_confirmation = input("Do you want to add another items?(yes/no)\t: ").lower()
                if add_confirmation == 'yes':
                    self.add_item()
                    break
            else:
                self.calculate_bill()
            
    def edit_item(self):
        """
        This method have a function to edit your ordered items,
        By delete the item you want to first then offer an option,
        whether you add items, or delete another items or cancel order or finish your order.
        """
        
        deleted_item = input("Choose the item you want to delete or replace\t: ")
        print('')
        #Check whether input already in order list or not.
        while True:
            if deleted_item not in self.items:
                print("You're not order this item yet.")
                deleted_item = input("Choose the item you want to delete or replace from order list\t: ")
            elif deleted_item in self.items:
                i = self.items.index(deleted_item)
                self.items.remove(self.items[i])
                break
            
        print(f"{deleted_item} has been deleted from your order. Then :\n")
        print("1. Add another items?\n2. Delete another items?\n3. Cancel order?\n4. Finish order?")
        
        edit_confirmation = input("Please insert the number of your choice?. (1/2/3/4)\t: ").lower()              
        while edit_confirmation != '1' or edit_confirmation != '2' or edit_confirmation != '3' or edit_confirmation != '4':    
            if edit_confirmation == '1':
                self.add_item()
                break
            elif edit_confirmation == '2':
                self.edit_item()
                break
            elif edit_confirmation == '3':
                self.cancel_order() 
                break      
            elif edit_confirmation == '4':
                self.calculate_bill()
                break
            else:
                edit_confirmation = input("Please insert the number of your choice?. (1/2/3)\t: ").lower()
        
    def cancel_order(self):
        """
        This method will cancel your order and 
        the transaction wouldn't be recorded or saved at self.transaction_data dict.
        """
        for i in range(1, len(self.transaction_data)):
            if self.transaction_data[i][0] == self.id_transaksi:
                del self.transaction_data[i]   
        
                
        print(f"ID transaksi\t:  {self.id_transaksi}")
        print(f"Nama Customer\t:  {self.name}")
        
        #Delete value in customer attributes.
        self.items = ' '
        self.num_of_items = ' '
        self.id_transaksi = ' '
        self.ordered_items = {}
        
        print('')
        print(f"Your order has been canceled.")
        self.calculate_bill()
        
    def calculate_bill(self):
        """
        This method will calculate total bill of the order.
        Include whether your order qualified to get discount or not,
        and you will be asked to confirm the order or will change the order.
        """
        
        bill_list = []  #List to save the bill of each ordered items to facilitate calculation.
        item_amounts = []  #List to save the number of each ordered items to facilitate calculation.
        item_price = []  #List to save the price of each ordered items to facilitate calculation.
       
        #2 variables below are used for ease the calculation of the bill by calculate each of item_amounts and item_price.
        menu_items = [keys for keys, value in self.menu_price.items()]  #List of all items in the menu.
        menu_items_ordered = [value for value in menu_items if value in self.items] #List of items in the menu which also in your order items.
        
        print('-'*52)
        print(f'ID transaksi\t:{self.id_transaksi}')
        print(f"Nama Customer\t:{self.name}")
        
        for i in range(0, len(menu_items_ordered)):
            bill_per_items = self.menu_price[menu_items_ordered[i]] * self.ordered_items[menu_items_ordered[i]]
            ordered_items_amount = self.ordered_items[menu_items_ordered[i]]
            price_list = self.menu_price[menu_items_ordered[i]]
            
            bill_list.append(bill_per_items)
            item_amounts.append(ordered_items_amount)
            item_price.append(price_list)           
            
        order_resume = [menu_items_ordered, item_price, item_amounts, bill_list] 
        total_bill = sum(bill_list) #The calculation result of the bill.
        
        #The conditions to qualify the discount term on your order.
        if total_bill > 500_000:
            total_bill = sum(bill_list) * 0.90
        elif total_bill > 300_000:
            total_bill = sum(bill_list) * 0.92
        elif total_bill > 200_000:
            total_bill = sum(bill_list) * 0.95
            
        print(tabulate(zip(*order_resume), 
                       headers = ['Items', 'Price per items', 'Amounts', 'Bill'], 
                       tablefmt='fancy_grid')) #Show the order resume before you confirm it or will change the order.
        print('-'*52)
        
        if sum(bill_list) > 500_000:
            print(f"Price total :\t  Rp {int(sum(bill_list))}")
            print(f"Discount 10% :\t Rp {int(sum(bill_list) * 0.1)}")
            print('-'*52)     
            print(f"Total bill :\t  Rp {int(total_bill)}")
        elif sum(bill_list) > 300_000:
            print(f"Price total :\t  Rp {int(sum(bill_list))}")
            print(f"Discount 8% :\t  Rp {int(sum(bill_list) * 0.08)}")
            print('-'*52)     
            print(f"Total bill :\t  Rp {int(total_bill)}")
        elif sum(bill_list) > 200_000:
            print(f"Price total :\t Rp {int(sum(bill_list))}")
            print(f"Discount 5% :\t Rp {int(sum(bill_list) * 0.05)}")
            print('-'*52)     
            print(f"Total bill :\t  Rp {int(total_bill)}")
        else:
            print(f"Price total :\t Rp {int(sum(bill_list))}")
            print(f"Discount - :\t\t -")
            print('-'*52)     
            print(f"Total bill :\t  Rp {int(total_bill)}")
        
        order_confirmation = input("Do you want to confirm this order? (yes/no)\t: ")
        
        while order_confirmation != 'yes' or order_confirmation != 'no':          
            if order_confirmation == 'yes':
                print('-'*52)
                if int(total_bill) == 0:
                    print("Thank you, Have a nice day!") 
                else:
                    print(f"Your order confirmed, Thankyou {self.name}!")
                    print(f"Order id\t: {self.id_transaksi}")
                    print(f"Total bill\t: Rp {int(total_bill)}")
                    print(f"Please complete the payment and enjoy your foods!")
                self.final_bill.append(int(total_bill))      
                break  
            elif order_confirmation == 'no':
                print('-'*52)
                print("1. Add items?\n2. Delete/Edit items?\n3. Cancel order?\n4. Finish order?")
                question = input("Please insert the number of your choice. (1/2/3/4)\t: ")
                if question == '1':
                    self.add_item()
                    break
                elif question == '2':
                    self.edit_item()
                    break
                elif question == '3':
                    self.cancel_order()
                    break
                elif question == '4':
                    self.calculate_bill()
                    break     
                else:
                    question = input("Please insert the number of your choice. (1/2/3/4)\t: ")
                    
            order_confirmation = input("Do you want to confirm this order? (yes/no)?\t: ")
                    
    def check_transaction_history():
        """This method for show all of the transaction made."""
        print(tabulate(Customer.transaction_data, headers='firstrow', tablefmt='fancy_grid'))