#List to keep track of the kinds of pizzas you sell
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
#list to keep track of how much each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]
#variable to Find the length of the toppings list
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#zip to combine the two lists prices and toppings into a list called pizzas
pizzas = list(zip(prices, toppings))

print(pizzas)

#Sort pizzas so that the pizzas with the lowest prices are at the start
#of the list.
pizzas.sort()

#Store the first element of pizzas in a variable called cheapest_pizza.
cheapest_pizza = pizzas[0]

#Store the last element of pizzas in a variable called priciest_pizza.
priciest_pizza = pizzas[-1]

#store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizzas[:4]

print(three_cheapest)

#It counts the number of occurrences of $2 in the prices list,
#and stores the result in a variable called num_two_dollar_slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
