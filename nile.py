# Nile Project - Eden Ehm

#Assumptions:
    #Users must have an account to purchase anything. If they don't have an existing account, they must create one.
    #Nile is an exclusive online shopping community.  Users must login or create an account first in order to view the items for sale.
    #Users have two chances to correctly log in.
    #User login is whatever the use considers their first and last name to be and is not case sensitive.
    #There are no pictures of the items, just descriptions.
    #Users can buy multiple items or multiples of one item.
    #Nile has only 2 of each item in stock.
    #There is only one shopper shopping on Nile at any given time.  Two people cannot shop simultaneously.
    #Items are in the category assigned by Nile and items cannot be in two categories.

#Read in Account and Products Data
accounts = open('accounts.csv')
accountsread = accounts.read()

products = open('products.csv', encoding = 'utf8', errors = 'replace')
productsread = products.read()

#Sort Products Data by Type and item
shirt1 = productsread[:367]
shirt2 = productsread[367:811]
shirt3 = productsread[811:1301]
shirt4 = productsread[1301:1709]
shirt5 = productsread[1709:2254]

pants1 = productsread[2254:2739]
pants2 = productsread[2739:3287]
pants3 = productsread[3287:3592]
pants4 = productsread[3592:3910]
pants5 = productsread[3910:4222]

sweater1 = productsread[4222:4645]
sweater2 = productsread[4645:4919]
sweater3 = productsread[4919:5277]
sweater4 = productsread[5277:5592]
sweater5 = productsread[5592:5865]

jewelry1 = productsread[5865:6209]
jewelry2 = productsread[6209:6506]
jewelry3 = productsread[6506:6757]
jewelry4 = productsread[6757:7076]
jewelry5 = productsread[7076:7425]

fs1 = productsread[7425:8097]
fs2 = productsread[8097:9020]
fs3 = productsread[9020:9775]
fs4 = productsread[9775:10700]
fs5 = productsread[10700:11611]

#User Accounts With Account Info
bobsmith1 = accountsread[44:105]
maysnell2 = accountsread[105:207]
tombanks3 = accountsread[207:290]
shellyambers4 = accountsread[290:]

#Welcome Message
print('Welcome to Nile!  The longest online shopping experience in the world!')
print('Nile is just for people who work with and/or love technology.  Please log in.\n')

#Login
useraccounts = list()
useraccounts.append('bob smith')
useraccounts.append('may snell')
useraccounts.append('tom banks')
useraccounts.append('shelly ambers')

def faillogin():
    while True:
        existing = input('Do you have an existing Nile account?''\n')
        if existing == "Yes" or existing == "Y" or existing == "yes" or existing == "y" or existing == "YES":
            logintwo()
            break
        if existing == "No" or existing == "N" or existing == "no" or existing == "n" or existing == "NO":
            create = input('Would you like to create a Nile account?''\n')
            if create == "Yes" or create == "Y" or create == "yes" or create == "y" or create == "YES":
                while len(useraccounts) > 1:
                    newacct = input('Please enter your first and last name. This will be your username.''\n')
                    useraccounts.append(newacct)
                    print('Welcome,',newacct.title(),' Your Nile account has been created and you have been logged in.\n')
                    break
                break
            if create == "No" or create == "N" or create == "no" or create == "NO" or create == "n":
                print('We are sorry you do not wish to create a Nile account. Goodbye!')
                exit()
            else:
                print('Invalid answer.  Please only answer "yes" or "no."')
                continue
        else:
            print('Invalid answer.  Please only answer "yes" or "no."')
            continue

def login():
    while True:
        user = input('Please log in using your first and last name\n') #chance 1 to login correctly
        user = user.lower()
        if user in useraccounts:
            print('Welcome,',user.title(),'.\n')
            break
        else:
            print('No user found.')
            faillogin()
            break

def logintwo():
    while True:
        user = input('Please log in using your first and last name\n') #chance 2 to login correctly
        user = user.lower()
        if user in useraccounts:
            print('Welcome,',user.title(),'.\n')
            break
        else:
            print('Second failed login attempt. For your account security, Nile is closing.  Try logging in again later.  Goodbye!')
            exit()

login()

#Create Empty Cart
cart = list()

#Pick a Category, Display Items, and Shop that Category
def shop():
    while True:
        categories = ['shirts' , 'pants' , 'sweaters' , 'jewelry' , 'fun stuff', 'checkout']
        print('\n''The product categories are Shirts, Pants, Sweaters, Jewelry, and Fun Stuff.')
        cat = input('What category would you like to shop?  Please enter a category or type "checkout" to proceed to checkout.''\n')
        cat = cat.lower()
        if cat in categories:
            if cat == "shirts" or cat == "shirt":
                print('\n''Sorry, there are no photos of the shirts.  Just descriptions.''\n')
                print(shirt1,'\n')
                print(shirt2,'\n')
                print(shirt3,'\n')
                print(shirt4,'\n')
                print(shirt5,'\n')
                shirtorder()
            if cat == "pants" or cat == "pant":
                print('\n''Sorry, there are no photos of the pants.  Just descriptions.''\n')
                print(pants1,'\n')
                print(pants2,'\n')
                print(pants3,'\n')
                print(pants4,'\n')
                print(pants5,'\n')
                pantsorder()
            if cat == "sweaters" or cat == "sweater":
                print('\n''Sorry, there are no photos of sweaters.  Just descriptions.''\n')
                print(sweater1,'\n')
                print(sweater2,'\n')
                print(sweater3,'\n')
                print(sweater4,'\n')
                print(sweater5,'\n')
                sweaterorder()
            if cat == "jewelry" or cat == "jewel":
                print('\n''Sorry, there are no photos of jewelry.  Just descriptions.''\n')
                print(jewelry1,'\n')
                print(jewelry2,'\n')
                print(jewelry3,'\n')
                print(jewelry4,'\n')
                print(jewelry5,'\n')
                jewelryorder()
            if cat == "fun stuff" or cat == "fun" or cat == "stuff" or cat == "funstuff":
                print('\n''Sorry, there are no photos of fun stuff items.  Just descriptions.''\n')
                print(fs1,'\n')
                print(fs2,'\n')
                print(fs3,'\n')
                print(fs4,'\n')
                print(fs5,'\n')
                funorder()
            if cat == "checkout" or cat == "Checkout" or cat == "check out" or cat == "Check out":
                break
            break
        else:
            print('That category does not exist. Please type in your selected category again.')
            continue

#Shirts Order
def shirtorder():
    shirtitem = input('Please type in the name of the shirt you would like to purchase.''\n')
    numbershirt = input('How many would you like to purchase? Please enter a whole numerical value.''\n')
    try:
        numbershirt = float(numbershirt)
        if numbershirt > 2:
            print('We are sorry, but there are only 2', shirtitem, 'in stock.')
            yesornoshirt = input('Would you like to order fewer of that shirt? Please answer "yes" or "no."''\n')
            if yesornoshirt == "yes" or yesornoshirt == "y" or yesornoshirt == "Y" or yesornoshirt == "Yes":
                numbershirt = input('How many would you like to purchase?''\n')
                try:
                    numbershirt = int(numbershirt)
                    if numbershirt == 2:
                        cart.append(shirtitem)
                        cart.append(shirtitem)
                        print('Cart updated with', numbershirt, shirtitem)
                        print('Cart:', cart)
                        shop()
                    if numbershirt == 1:
                        cart.append(shirtitem)
                        print('Cart updated with', numbershirt, shirtitem)
                        print('Cart:', cart)
                        shop()
                    if numbershirt == 0:
                        print('None added to cart.')
                        shop()
                    if numbershirt < 0:
                        print('Invalid number of shirts. Please try again.')
                        shirtorder()
                except:
                    print('Please enter only a numeric value. Do not enter any letters, punctuation, or special characters.')
                    shirtorder()
            if yesornoshirt == "n" or yesornoshirt == "no" or yesornoshirt == "No" or yesornoshirt == "N":
                print('None have been added to your cart.')
                shop()
            try:
                yesornoshirt = float(yesornoshirt)
                yesornoshirt = int(yesornoshirt)
            except:
                print('Please answer only "yes" or "no."')
                shirtorder()
        if numbershirt == 2:
            cart.append(shirtitem)
            cart.append(shirtitem)
            print('Cart updated with', numbershirt, shirtitem)
            print('Cart:', cart)
            shop()
        if numbershirt == 1:
            cart.append(shirtitem)
            print('Cart updated with', numbershirt, shirtitem)
            print('Cart:', cart)
            shop()
        if numbershirt == 0:
            print('None added to cart.')
            shop()
        if numbershirt < 0:
            print('Invalid number of shirts. Please try again.')
            shirtorder()
    except:
        print('Please enter only a whole numeric value. Do not enter any letters, punctuation, or special characters.')
        shirtorder()

#Pants Order
def pantsorder():
    pantsitem = input('Please type in the name of the pants you would like to purchase.''\n')
    numberpants = input('How many would you like to purchase? Please enter a whole numerical value.''\n')
    try:
        numberpants = float(numberpants)
        if numberpants > 2:
            print('We are sorry, but there are only 2', pantsitem, 'in stock.')
            yesornopants= input('Would you like to order fewer of those pants? Please answer "yes" or "no."''\n')
            if yesornopants == "yes" or yesornopants == "y" or yesornopants == "Y" or yesornopants == "Yes":
                numberpants = input('How many would you like to purchase?''\n')
                try:
                    numberpants = int(numberpants)
                    if numberpants == 2:
                        cart.append(pantsitem)
                        cart.append(pantsitem)
                        print('Cart updated with', numberpants, pantsitem)
                        print('Cart:', cart)
                        shop()
                    if numberpants == 1:
                        cart.append(pantsitem)
                        print('Cart updated with', numberpants, pantsitem)
                        print('Cart:', cart)
                        shop()
                    if numberpants == 0:
                        print('None added to cart.')
                        shop()
                    if numberpants < 0:
                        print('Invalid number of pants. Please try again.')
                        pantsorder()
                except:
                    print('Please enter only a numeric value. Do not enter any letters, punctuation, or special characters.')
                    pantsorder()
            if yesornopants == "n" or yesornopants == "no" or yesornopants == "No" or yesornopants == "N":
                print('None have been added to your cart.')
                shop()
            try:
                yesornopants = float(yesornopants)
                yesornopants = int(yesornopants)
            except:
                print('Please answer only "yes" or "no."')
                pantsorder()
        if numberpants == 2:
            cart.append(pantsitem)
            cart.append(pantsitem)
            print('Cart updated with', numberpants, pantsitem)
            print('Cart:', cart)
            shop()
        if numberpants == 1:
            cart.append(pantsitem)
            print('Cart updated with', numberpants, pantsitem)
            print('Cart:', cart)
            shop()
        if numberpants == 0:
            print('None added to cart.')
            shop()
        if numberpants < 0:
            print('Invalid number of pants. Please try again.')
            pantsorder()
    except:
        print('Please enter only a whole numeric value. Do not enter any letters, punctuation, or special characters.')
        pantsorder()

#Sweater Order
def sweaterorder():
    sweateritem = input('Please type in the name of the sweater you would like to purchase.''\n')
    numbersweater = input('How many would you like to purchase? Please enter a whole numerical value.''\n')
    try:
        numbersweater = float(numbersweater)
        if numbersweater > 2:
            print('We are sorry, but there are only 2', sweateritem, 'in stock.')
            yesornosweater = input('Would you like to order fewer of that sweater? Please answer "yes" or "no."''\n')
            if yesornosweater == "yes" or yesornosweater == "y" or yesornossweater == "Y" or yesornosweater == "Yes":
                numbersweater = input('How many would you like to purchase?''\n')
                try:
                    numbersweater = int(numbersweater)
                    if numbersweater == 2:
                        cart.append(sweateritem)
                        cart.append(sweateritem)
                        print('Cart updated with', numbersweater, sweateritem)
                        print('Cart:', cart)
                        shop()
                    if numbersweater == 1:
                        cart.append(sweateritem)
                        print('Cart updated with', numbersweater, sweateritem)
                        print('Cart:', cart)
                        shop()
                    if numbersweater == 0:
                        print('None added to cart.')
                        shop()
                    if numbersweater < 0:
                        print('Invalid number of sweaters. Please try again.')
                        sweaterorder()
                except:
                    print('Please enter only a numeric value. Do not enter any letters, punctuation, or special characters.')
                    sweaterorder()
            if yesornosweater == "n" or yesornosweater == "no" or yesornosweater == "No" or yesornosweater == "N":
                print('None have been added to your cart.')
                shop()
            try:
                yesornosweater = float(yesornosweater)
                yesornosweater = int(yesornosweater)
            except:
                print('Please answer only "yes" or "no."')
                sweaterorder()
        if numbersweater == 2:
            cart.append(sweateritem)
            cart.append(sweateritem)
            print('Cart updated with', numbersweater, sweateritem)
            print('Cart:', cart)
            shop()
        if numbersweater == 1:
            cart.append(sweateritem)
            print('Cart updated with', numbersweater, sweateritem)
            print('Cart:', cart)
            shop()
        if numbersweater == 0:
            print('None added to cart.')
            shop()
        if numbersweater < 0:
            print('Invalid number of sweaters. Please try again.')
            sweaterorder()
    except:
        print('Please enter only a whole numeric value. Do not enter any letters, punctuation, or special characters.')
        sweaterorder()

#Jewelry Order
def jewelryorder():
    jewelryitem = input('Please type in the name of the jewelry you would like to purchase.''\n')
    numberjewelry = input('How many would you like to purchase? Please enter a whole numerical value.''\n')
    try:
        numberjewelry = float(numberjewelry)
        if numberjewelry > 2:
            print('We are sorry, but there are only 2', jewelryitem, 'in stock.')
            yesornojewelry = input('Would you like to order fewer of that jewelry? Please answer "yes" or "no."''\n')
            if yesornojewelry == "yes" or yesornojewelry == "y" or yesornojewelry == "Y" or yesornojewelry == "Yes":
                numberjewelry = input('How many would you like to purchase?''\n')
                try:
                    numberjewelry = int(numberjewelry)
                    if numberjewelry == 2:
                        cart.append(jewelryitem)
                        cart.append(jewelryitem)
                        print('Cart updated with', numberjewelry, jewelryitem)
                        print('Cart:', cart)
                        shop()
                    if numberjewelry == 1:
                        cart.append(jewelryitem)
                        print('Cart updated with', numberjewelry, jewelryitem)
                        print('Cart:', cart)
                        shop()
                    if numberjewelry == 0:
                        print('None added to cart.')
                        shop()
                    if numberjewelry < 0:
                        print('Invalid number of jewelry. Please try again.')
                        jewelryorder()
                except:
                    print('Please enter only a numeric value. Do not enter any letters, punctuation, or special characters.')
                    jewelryorder()
            if yesornojewelry == "n" or yesornojewelry == "no" or yesornojewelry == "No" or yesornojewelry == "N":
                print('None have been added to your cart.')
                shop()
            try:
                yesornojewelry = float(yesornojewelry)
                yesornojewelry = int(yesornojewelry)
            except:
                print('Please answer only "yes" or "no."')
                jewelryorder()
        if numberjewelry == 2:
            cart.append(jewelryitem)
            cart.append(jewelryitem)
            print('Cart updated with', numberjewelry, jewelryitem)
            print('Cart:', cart)
            shop()
        if numberjewelry == 1:
            cart.append(jewelryitem)
            print('Cart updated with', numberjewelry, jewelryitem)
            print('Cart:', cart)
            shop()
        if numberjewelry == 0:
            print('None added to cart.')
            shop()
        if numberjewelry < 0:
            print('Invalid number of jewelry. Please try again.')
            jewelryrder()
    except:
        print('Please enter only a whole numeric value. Do not enter any letters, punctuation, or special characters.')
        jewelryorder()

#Fun Stuff Order
def funorder():
    funitem = input('Please type in the name of the fun stuff item you would like to purchase.''\n')
    numberfun = input('How many would you like to purchase? Please enter a whole numerical value.''\n')
    try:
        numberfun = float(numberfun)
        if numberfun > 2:
            print('We are sorry, but there are only 2', funitem, 'in stock.')
            yesornofun = input('Would you like to order fewer of that fun stuff item? Please answer "yes" or "no."''\n')
            if yesornofun == "yes" or yesornofun == "y" or yesornofun == "Y" or yesornofun== "Yes":
                numberfun = input('How many would you like to purchase?''\n')
                try:
                    numberfun = int(numberfun)
                    if numberfun == 2:
                        cart.append(funitem)
                        cart.append(funitem)
                        print('Cart updated with', numberfun, funitem)
                        print('Cart:', cart)
                        shop()
                    if numberfun == 1:
                        cart.append(funitem)
                        print('Cart updated with', numberfun, funitem)
                        print('Cart:', cart)
                        shop()
                    if numberfun == 0:
                        print('None added to cart.')
                        shop()
                    if numberfun < 0:
                        print('Invalid number of fun stuff items. Please try again.')
                        funorder()
                except:
                    print('Please enter only a numeric value. Do not enter any letters, punctuation, or special characters.')
                    funorder()
            if yesornofun == "n" or yesornofun == "no" or yesornofun == "No" or yesornofun == "N":
                print('None have been added to your cart.')
                shop()
            try:
                yesornofun = float(yesornofun)
                yesornofun = int(yesornofun)
            except:
                print('Please answer only "yes" or "no."')
                funorder()
        if numberfun == 2:
            cart.append(funitem)
            cart.append(funitem)
            print('Cart updated with', numberfun, funitem)
            print('Cart:', cart)
            shop()
        if numberfun == 1:
            cart.append(funitem)
            print('Cart updated with', numberfun, funitem)
            print('Cart:', cart)
            shop()
        if numberfun == 0:
            print('None added to cart.')
            shop()
        if numberfun < 0:
            print('Invalid number of fun stuff items. Please try again.')
            funorder()
    except:
        print('Please enter only a whole numeric value. Do not enter any letters, punctuation, or special characters.')
        funorder()

shop()

#Keep Shopping or Checkout
def cartcheck():
    more = input('\n''Would you like to order another item before finalizing your shopping cart?''\n')
    more = more.lower()
    if more == "yes" or more == "y" or more == "Y" or more == "Yes" or more == "YES" or more == "YEs" or more == "YeS" or more == "yES" or more == "yeS" or more == "yEs":
        shop()
    if more == "no" or more == "n" or more == "N" or more == "No" or more == "NO" or more == "nO":
        print('Continuing to checkout.''\n')
    else:
        print('Invalid answer.  Please only answer "yes" or "no."')
        cartcheck()

cartcheck()

#Check Out
print('Below is a summary of your order. Please review it for correctness.')
print(cart)
if len(cart) == 0:
    print("There are no items in your cart. Please shop with Nile again soon!  Goodbye!")
    exit()
if len(cart) > 0:
    print('Is your order summary correct?')
    while True:
        correct = input('Please answer "yes" or "no."''\n')
        if correct == "yes" or correct == "y" or correct == "Y" or correct == "Yes" or correct == "YES" or correct == "YEs" or correct == "YeS" or correct == "yES" or correct == "yeS" or correct == "yEs":
            print('Continuing to checkout.\n')
            break
        if correct == "no" or correct == "n" or correct == "N" or correct == "No" or correct == "NO" or correct == "nO":
            print('We are sorry for the error.  To be sure we have your order right, please create your order again.\n')
            cart = list()
            shop()
        try:
            correct = float(correct)
            correct = int(correct)
        except:
            print('Invalid answer.  Is your order summary correct?')
            continue

#Identify Top Items Purchased
counts = dict()
items = productsread
for item in items:
    counts[item] = counts.get(item,0)+1
    #print(counts)

#Credit Card Authorization
ccnumber = input('Nile only accepts credit cards. Please enter your credit card number.  Please enter only numbers.\n')
import random
authorization = random.randint(0,2)
if authorization < 1:
    print('Thank you for your payment.  Your order has been placed and your items will be shipped today.\n')
    print('Other people who purchased what you did also purchased the "Silver Tone Sliced Dark Pink Agate Crystal Edged Pendant Necklace" and the "Coeur Sauvage Necklace Pendant."\n')
    print('Thank you for shopping on Nile!  Goodbye!')
    exit()
if authorization >= 1:
    print('We are sorry, but there is a problem with your credit card and your order has been cancelled.\n')
    exit()
