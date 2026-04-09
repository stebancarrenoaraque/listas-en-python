edades = ["14" , "15" , "14" , "16" , "14"]
musica = ["vallenato", "rock" , "pop" , "reggeton" , "hip hop"]
import math
# promedio edades
promedio = sum(int(edad) for edad in edades) / len(edades)
print("el promedio de edades es: " + str (promedio))

#mayores de 15
mayores=[edad for edad in edades if int(edad) > 15]
print("edades > 15: "+str(mayores))

#fans del rock
fans_rock=[genero for genero in musica if genero=="rock"]
print("fans del rock: "+str(fans_rock))