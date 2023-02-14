import pandas as pd

empleados=pd.read_csv("./empleados.csv")

#print (empleados)


filtro=empleados.head(10)
#print (filtro)
#print ("\n")

filtro2=empleados.head(10)["nombres"]
#print(filtro2)
#print ("\n")

filtro3= empleados.tail(5)[["nombres","salario"]]
#print(filtro3)
#print ("\n")

filtro4= empleados.head(20).describe()
#print(round(filtro4,2))
#print ("\n")

#Filtrando por condiciones logicas

filtroEdad=empleados[empleados["edad"]<30].head(20)

print(filtroEdad)

dataLimpia= filtroEdad.dropna()
print("\n")
print(dataLimpia)

dataLimpia["cargo"]=empleados.replace(['analista2'],"practicante comfama")
print (dataLimpia)
print("\n")