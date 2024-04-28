class CakeShop():
    def __init__(self):
        
        self.prices = {
            'Chocolate Cake': 2000,
            'Pineapple Cake': 1800,
            'Strawberry Cake': 1900,
        }
    
    def CakePrice(self, cake_type):
        return self.prices.get(cake_type, 0)
    
class Cake(CakeShop):
    def Shop(self, cake_type, quantity):
        if quantity <= 0:
            print("Please Enter number greater than 0")
        else:
            per_cake = self.CakePrice(cake_type)
            total_price = per_cake * quantity
            
            print("Total price:", total_price)
    
while True:
    obj = Cake()
    
    userinput = int(input('''
                      1 Chocolate
                      2 Pineappale
                      3 Strawberry 
                      4 Exit
                      '''))
    
    if userinput == 1:
        quan = int(input("How many Chocolate cakes do you want?"))
        obj.Shop('Chocolate Cake', quan)
        
    elif userinput == 2:
        quan1 = int(input("How many Pineapple cakes do you want?"))
        obj.Shop('Pineapple Cake', quan1)
    
    elif userinput == 3:
        quan2 = int(input("How many Strawberry cakes do you want?"))
        obj.Shop('Strawberry Cake', quan2)
    
    else:
        break