class pizza:
    def __init__(self,toppings,ingredients,size):
        self.toppings= toppings
        self.ingredients = ingredients
        self.size = size
    


    def change_size(self,new_size):
        self.size= new_size




food=pizza('cheese and pepperoni','Dough','16inch')



print(food.toppings)
print(food.ingredients)
food.change_size('24inch')
print(food.size)

