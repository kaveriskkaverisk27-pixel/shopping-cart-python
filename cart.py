        
# Create a Cart class to manage products in a shopping cart.
# The class should have:
# productname
# price
# quantity
# Create the following methods:
# display() – Display product details.
# Calculate the total price using:
# price × quantity
# discount() – If the total price is above ₹1000, give a 10% discount.
# Create an object and display the product details, total price, discount, and final amount.


# total=0
# discount=0
# class Cart:
#     def __init__(self,product_name,price,quantity):
#         self.product_name=product_name
#         self.price=price
#         self.quantity=quantity
#     def display(self):
#             global total,discount
#             total=self.price*self.quantity
#             print(f"your product details \nproduct name: {self.product_name}\nprice:{self.price}\nquantity:{self.quantity}")
#             print("============================")
#             print(f"claculator:{total}")
#             if total>1000:
#                  discount=total*10/100
#                  print(f"your discount is:{discount}")
#                  print("============================")
#             else:
#                  print("no discount")
#      
#        print(f"so your final amount is:{total-discount}")
                 
# ob1=Cart("lehanga",3400,1)
# ob1.display()