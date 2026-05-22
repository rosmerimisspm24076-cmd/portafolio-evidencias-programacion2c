"""
estas programando el sistema de una pequeña tienda.debes manipular el inventario de productos disponibles
1.inicia una lista de productos que contenga:"leche","pan","huevos","manzanas"
2.te ha llegado un camion con nuevos productos:"arroz","frijol" y "aceite".agregando todos a la lista usando un solo metodo
3.te das cuenta que el "pan"esat vencido.encuentra el indice del "pan" usando .index
"""

productos=["leche","pan","huevos","manzanas" ]
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("pan"))
productos.sort()
print(productos)
if "leche" in