# Cashier Project

## Table of Content
1. Project Description
2. How it works
3. Test Case
4. Credits

## Project Description
This project aims to make a cashier self-service program. Some of the initial features requested are:
* Create an ID transaction
* Add item (item name, item amount, item price)
* Update item
* Delete Item
* Reset the transaction
* Check the order list
* Calculate the total price
* and Discount features

But while making the program, I decided to develop it using a dictionary that stores data on product names and prices. So that the customer only needs to add the item name and the number of items, then the price will be automatically added. Because of that, I choose a cafe or restaurant to be used as an example for this program because there are fewer menus and prices that have to be made in the dictionary rather than supermarkets.

I built the program based on the customer journey. From that, I develop some features to accommodate the customer journey when want to order something.
In short, this is the customer journey flow:

<img src="https://github.com/dzakiyma/cashier/assets/137891087/040ab8b3-5ddf-458a-be54-acc2cf22e894" width=450>

## How it works
* Download all files into one local directory.
* Open initiate.py and run it.
* The program will be starting and you just have to follow the instructions of the program.
* In the program, have some features to control your input so that the Error will never happen and the program can finish perfectly.

## Test Case
1. Add item
* add items for the first time.
  
  <img src="https://github.com/dzakiyma/cashier/assets/137891087/b1440a6f-9ab5-47d5-ab3f-ac8b30aa18c7" width=250> 
  
* The order resume will show up, when the customer doesn't wanna confirm the order then the program will offer some options.

  <img src="https://github.com/dzakiyma/cashier/assets/137891087/3c6e28bc-16af-40cb-a32c-dc8ff4930f28" width=250>

* Add another item.
  
  <img src="https://github.com/dzakiyma/cashier/assets/137891087/0586d5c1-1eb8-4fa6-a1c5-dbe3dad35df6" width=250>
  
  In case the customer adds the same item already added before, the amount just will be calculated. Example: Chicken Katsu already added 2 portions, then the customer adds Chicken Katsu again 1 portion. At the order resume, the Chicken Katsu amount is updated to 3 portions.

2. Delete Item
   
    <img src="https://github.com/dzakiyma/cashier/assets/137891087/9e1f2a13-90a4-4fe8-9194-a0b0249dac11" width=250>
  
    The customer can delete items when they want. After the item is deleted, the program will offer some options again.
  
3. Cancel order

    <img src="https://github.com/dzakiyma/cashier/assets/137891087/74cc24b8-5466-4dc3-af53-0bce32d5e29b" width=250>
    
    When the customer decided to cancel their order, the program will remove all of items, and the order has been canceled.

4. Finish Order

    <img src="https://github.com/dzakiyma/cashier/assets/137891087/534194eb-64ab-4690-a28b-6b3f0fabfab7" width=250>
  
    After the customer confirms their order, the program will resume the order and calculate the bill. If the order bill meets the criteria, the customer will get a discount as much as specified in the discount term.

# Credits
This project was created to fulfill the assignment from Pacmann Academy.


 


