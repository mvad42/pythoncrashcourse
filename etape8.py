pizzas = ['hawaii','hawaienne',"à l'ananas"]
for pizza in pizzas:
    print(f"J'aime beaucoup la pizza {pizza}")
print("\nJ'aime beaucoup les pizzas.")

pizzamis=pizzas[:]
print(pizzas)
print(pizzamis)
pizzas.append('tomate')
pizzamis.append('sandwich')
print(pizzas)
print(pizzamis)