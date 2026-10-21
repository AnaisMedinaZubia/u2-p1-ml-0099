import numpy as np

califas=np.array([60,70,90])
print(" ------------  ej 1 imprimir califas --------")
print(califas) # imprime la lista de califas
print(type(califas)) # muestra el tipo de arreglo
print(" ---------------- ej 2 dmensiones de un Array -----------------")
califas=np.array(60)
print(califas)
print("dimenciones :", califas.ndim)
print("------------- ej 2 dimensiones de un array -----------")
califas=np.array([
    [60,70,90],
    [50,80,98]
    ]) # un arreglo de dimensiones es como una tabla en excel
print(califas)
print("dimensiones :", califas.ndim)
print("------------- ej 3 dimensiones de un array -----------")
califas=np.array([
    [
    [60,70,90],
    [50,80,98]
    ],
    [
    [60,70,90],
    [50,80,98]
    ]
]) # un arreglo de dimensiones es como una tabla en excel
print(califas)
print("dimensiones :", califas.ndim)