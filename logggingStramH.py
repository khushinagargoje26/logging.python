# Assignment
# create a project and add logging to it
# stocks=[]
# order the products from the stocks and proceed with the payment
# check if the product is available in the stock , if no display log message
# check if payment is successful or not , and display log messages accordingly

import logging 
logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',level=logging.DEBUG)

stock=[{ "name": "Apple", "price": 174.23, "volume": 1500000},
    { "name": "OpenAi", "price": 2804.23, "volume": 1200000},
    { "name": "Tesla", "price": 692.12, "volume": 1800000},
    {"name": "Amazon", "price": 3330.12, "volume": 1000000},
    { "name": "Microsoft Corporation", "price": 289.67, "volume": 1400000}]

def display():
    print("\nAvailable Stocks:")
    for i, j in enumerate(stock,1):
         print(f"{i}. {j['name']} - Price: ${j['price']} - Available: {j['volume']} units")


def find_stock(productname):
    for i in stock:
        if i["name"].lower()== productname.lower():
            return i 
          
    logging.error("product is not avaiable")

    


def payment(amount):
    payment_status=input(f"total amount is ${amount}. proceed with payment?(yes?no):").lower()
    if payment_status=="yes":
         logging.info("Payment Successful!")
         return True
    else:
         logging.error("Payement Failed!")
         return False
while True:
    display()
    productname = input("Enter the stock name you want to buy (or type 'exit' to quit): ")
    
    if productname.lower() == "exit":
        logging.info("Exiting the program.")
        break

    
    try:
        quantity = int(input("Enter quantity: "))
        
    except ValueError:
        logging.error("Invalid quantity. Please enter a valid number.")
        continue
    
    
    
    product=find_stock(productname)
    if product:
        if product['volume']>=quantity:
            logging.debug(f"product {productname} is available.")
            total_price=product['price']*quantity
            if payment(total_price):
                product["volume"]=product["volume"]-quantity
                logging.info(f"Successfully Purchaased {quantity} units of {productname}")
            else:
                logging.error("payment failed .")
        else:
            logging.error("limited stocks available")
    else:
        logging.error("product is not available")


