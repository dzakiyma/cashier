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

But while making the program, I decided to develop it using a database that stores data on product names and prices. So that the customer only needs to add the item name and the number of items, then the price will be automatically added. Because of that, I choose a cafe or restaurant to be used as an example for this program because there are fewer menus and prices that have to be made in the database rather than supermarkets.

I built the program based on the customer journey. From that, I develop some features to accommodate the customer journey when want to order something.
In short, this is the customer journey flow:

<img src="https://github.com/dzakiyma/cashier/assets/137891087/040ab8b3-5ddf-458a-be54-acc2cf22e894" width=500>

## How it works
At very first, you can start the whole cashier program by call method: Welcome.start() 

![image](https://github.com/dzakiyma/cashier/assets/137891087/879217ad-bc97-43c7-9176-0eb8b1647093)

The block code above will show you the menu and its price, so you can get a reference when inputting the order item. Every input will be checked, whether it meets the input criteria or not, so no errors will appear. For this case, I used many while looping so the input variable will be looped until the input is as expected.
for example:

![image](https://github.com/dzakiyma/cashier/assets/137891087/f4b6030d-434f-424e-a75c-24a11ddc1881)

The input expected is only 'yes' or 'no'. If you input other words, the program will be looping until your input meets the criteria. And finally, this method will generate an instance of the Customer class. 

Customer class has some methods, there are add_item(), edit_item(), cancel_order(), calculate_bill() and check_transaction_history(). After the object class is created in Welcome.start(), it will go to calculate_bill() which will show the resume of the order and you can confirm the order or not.
The output:

![image](https://github.com/dzakiyma/cashier/assets/137891087/43b4183d-486c-46e3-a55f-75096e8f3ccc)

if you don't want to confirm this order, you will be offered an option to add items, delete items or cancel the order, or even back to finish the order. This is the code:

![image](https://github.com/dzakiyma/cashier/assets/137891087/003f1c5c-03e7-40cc-88f8-92ae89ddfc6c)

Those codes prevent customers insert the not expected input. So it will be a loop.

In add_item() you will input the new item you want to add and its amount. If you input the item which already in your order list, the program just will sum the amount of that item.






<<<<<<< HEAD
=======

>>>>>>> 0f817320e9fd7fb6c72aea48ee2198b003671c14
