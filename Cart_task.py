a = input("Welcome to the Online store.\n what is your name ? ")
b = ("Welcome,")
print (a,b)
product=["rice", "fruits", "vegetables", "shampoo", "dal"]
catagory=[{"kohinoor": 50, "Indiagate": 40, "dawaat": 60, "sungold": 40},
				{"apple": 20, "banana": 30, "orange": 50, "watermelon": 10},
				{"potato": 30, "tomato": 30, "brinjal": 30, "chilly": 20, "pumpkin": 20},
				{"Loreal": 60, "Pantene": 60, "Head & Soulder": 75},
				{"urad dal": 65, "masoor dal": 85, "channa dal": 40}]
cart=[]
price=[]
qnt=[]
while(1):
  x=input("press y to add items to your Shopping cart or press x to exit")
  if x=="x":
    break
  if x=="y":
    print("Available products are :")
    for i in product:
      print(i)
    p=input("Enter the product name")
    indx=product.index(p)
    for i,j in catagory[indx].items():
      print(i,":",j)
    item=input("enter the catagory name")
    qnty=int(input("How many??"))
    cart.append(item)
    price.append(catagory[indx][item]*qnty)
    qnt.append(qnty)
print(cart,price)
print("----------INVOICE----------")
for i in range(len(cart)):
    print(qnt[i],"*",cart[i],"price =",price[i])
print("Total amount : ",sum(price))