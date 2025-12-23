frutas = ['maça', 'banana', 'laranja']
print(frutas)

frutas.append("Melancia")
print(frutas)

frutas.remove("Melancia")
print(frutas)

frutas[0] = 'melancia'
print(frutas)

frutas.insert(0, 'maca')
print(frutas)

frutas.pop(1)
print(frutas)


frutas.sort()
print(frutas)

print(frutas.index("banana"))

frutas2 = frutas.copy()
print(frutas2)