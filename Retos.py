import pandas as pd
pd.set_option('display.max_rows', None)
empleados=pd.read_csv("./empleados.csv")

#1 Filtrar empleados que solo sean analistas 1

data1= empleados.loc[empleados['cargo']== "analista1"].head(40)
print(data1)
print("\n")

#2 Filtrar empleados que solo sean analistas 2

data2= empleados.loc[empleados['cargo']== "analista2"].head(40)
print(data2)
print("\n")

#3 Filtrar empleados en general que tengan menos de 30 años

data3= empleados[empleados["edad"]<30]
print(data3)
print("\n")

#4 Filtrar empleados en general que tengan mas de 50 años

data4= empleados[empleados["edad"]>50]
print(data4)
print("\n")

#5 ¿Cuál es el promedio de salario de un analista 1?
data5= data1['salario'].mean()
print("El salario promedio de el cargo analista 1 es: ",round(data5,0))
print("\n")

#6 ¿Cuál es el promedio de salario de un analista 2?
data6= data2['salario'].mean()
print("El salario promedio de el cargo analista 2 es: ",round(data6,0))
print("\n")

#7 Filtrar empleados cuyo porcentaje de deducción sea mayor al 10%

data7= empleados.loc[empleados['porcentajeDeduccion']>10].head(40)
print(data7)
print("\n")

#8 Cambiar todos los datos nan por el valor 0

data8= empleados.fillna({"cargo":0,"salario":0,"porcentajeDeduccion":0,"edad":0})
print(data8)
print("\n")

#9 Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0
data9= empleados.fillna({"nombres":"Default","cargo":"sin cargo","edad":0})
print(data9)
print("\n")

#10 