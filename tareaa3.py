#ejercicio 
def merge(listaA,listaB):
        return sorted(listaA+listaB, key=lambda x: x['nombre'])
listaA = [ {"nombre": "manzana", "precio": 1.2},{"nombre": "pera", "precio": 1.9}]
listaB = [{"nombre": "uva ", " precio ": 1.7},{"nombre": "sandia  ", " precio ": 1.0}]
resultado = merge(listaA,listaB)
print("lista fusionada y ordenada :")
for fruta in resultado:
 print(fruta)
