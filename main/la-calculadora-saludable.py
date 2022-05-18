
#Esta linea es un comentario


def sexo():
  sexo=input("Escriba su sexo [m] ó [f]: ")
  if(sexo=="m"):
    return sexo
  elif(sexo=="f"): 
    return sexo
  else:
    print("Error")

def peso_ideal(sexo,altura):
  if(sexo=="m"):
    peso=56.2+1.41*(altura/2.54-60)
    print(f"El peso ideal es: ", peso)
  elif(sexo=="f"):
    peso=553.1+1.36*(altura/2.54-60)
    print(f"El peso ideal es: ", peso)
  else:
    print("el parametro solo puedes ser m o f")

def calorias_quemadas():
  tiempo=int(input("Digitar el tiempo de actividad en minutos"))
  peso=float(input("Digitar su peso en kilogramos"))
  opciones=int(input("opciones \n 1.caminar \n 2.tennis \n 3.montar en biciclenta \n 4.correr \n 5.nadar \n"))
  if(opciones==1):
    MET=2
    c_quemadas=(tiempo*MET*peso)/200
    print("resultado calorias quemadas por caminar:",c_quemadas)

  elif(opciones==2):
    MET=5
    c_quemadas=(tiempo*MET*peso)/200
    print("resultado calorias quemadas por tennis:",c_quemadas)

  elif(opciones==3):
    MET=14
    c_quemadas=(tiempo*MET*peso)/200
    print("resultado calorias quemadas por montar bicicleta:",c_quemadas)

  elif(opciones==4):
    MET=6
    c_quemadas=(tiempo*MET*peso)/200
    print("resultado calorias quemadas por correr:",c_quemadas)

  elif(opciones==5):
    MET=9.8
    c_quemadas=(tiempo*MET*peso)/200
    print("resultado calorias quemadas por nadar:",c_quemadas)
  else:("opcion no valida")

def porcentaje_de_grasa_corporal(sexo, edad, peso, altura):
    if sexo == 'f':
        pgc = 1.20 * (peso/altura) + 0.23 * edad - 5.4
        print(f'El porcentaje de grasa corporal: {pgc}')
    elif sexo == 'm':
        pgc = 1.20 * (peso/altura) + (0.23 * edad) - 16.2
        print(f'El porcentaje de grasa corporal: {pgc}')

def tasa_metabolica_basal(sex,peso,edad,altura):
    print(sex)
    if sex == 'm':
        TMB = 13.397*peso + 4.799*edad - 5.677*altura + 88.362
        print(f'La tasa metabolica basal es: {TMB}')

    elif sex == 'f':
        TMB = 9.247*peso + edad*3.098 - 4.330*altura + 447.593
        print(f'La tasa metabolica basal es: {TMB}')

def calculadora_saludable():
  opcion=int(input("----OPCIONES---- \n 1.Peso ideal \n 2.Calorias quemadas \n 3.Porcentaje Grasa Corporal \n 4. tasa metabolica basal \n")) #aqui vamos, colocar las siguientes opciones
  if (opcion==1):
    sex=sexo()
    altura=float(input("Digitar su altura en centimetros: "))
    peso_ideal(sex,altura)
  elif (opcion==2):
    calorias_quemadas()

  elif (opcion==3):
    sex = sexo()
    edad=int(input("Digitar su edad en años"))
    peso=float(input("Digitar su peso en Kg"))
    altura=float(input("Digitar su altura en metros"))
    porcentaje_de_grasa_corporal(sex, edad, peso, altura)

  elif (opcion==4):
    sex = sexo()
    edad=int(input("Digitar su edad en años"))
    peso=float(input("Digitar su peso en Kg"))
    altura=float(input("Digitar su altura en centimetros"))
    tasa_metabolica_basal(sex,peso,edad,altura)
  else:print("opcion invalida")

calculadora_saludable ()
