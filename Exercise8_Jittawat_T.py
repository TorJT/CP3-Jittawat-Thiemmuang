print("Welcome, please enter your username and password")

usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "tor1836" and passwordInput == "1836":
    print("-login succeeded-")
    print("-Welcome to TShop-")

    print("Product list")
    print('''
    1. Book   100 baht
    2. Pen    20 baht
    3. Pencil 15 baht
    4. ruler  10 baht
    5. eraser 5 baht
    ''')
    productSelected = int(input("please select product>> "))
    if productSelected == 1:
        productName = "Book"
        productPrice = 100
    elif productSelected == 2:
        productName = "Pen"
        productPrice = 20
    elif productSelected == 3:
        productName = "Pencil"
        productPrice = 15
    elif productSelected == 4:
        productName = "ruler"
        productPrice = 10
    elif productSelected == 5:
        productName = "eraser"
        productPrice = 5
    print("Product you selected: ", productName, ":", productPrice, "baht")
    qtySelected = int(input("please select QTY: "))
    print("Summary: ", productName, ":", qtySelected, "x", productPrice, "=", productPrice*qtySelected, "Baht")

else:
    print("Your username or password is incorrect")