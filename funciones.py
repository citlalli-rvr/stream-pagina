
#funcion saludo
def saludar(nombre:str)->str:
    return f"Hola {nombre}"



#suma de dos numeros
def sumar(a:int|float, b:int|float)->int|float:
    return a+b



#area de un triangulo 
def calcular_area_triangulo(base:float,altura:float)->float:
    return (base*altura)/2

#calculadora de descuento
def calcular_precio_final(precio:int|float,descuento=.10, impuesto=.16)->int|float:
    desc=precio-(precio * (descuento/100))
    total=desc+(desc*(impuesto/100))
    return total


#suma de lista
def sumar_lista(*nums:list|int)->list|int:
    suma=0
    for i in range (len(nums)): 
        suma=suma+nums[i]
    return suma

    
#valores predeterminados 
def producto(nombre:str,cantidad=1, precio=10)->int|float|str:
    precio_total=precio*cantidad
    return f"El total a pagar por {cantidad} {nombre} es {precio_total} "


#numeros pares e impares
def numeros_pares_e_impares(*nums):
    element_par=[]
    element_impar=[]
    numeros=[]

    for i in nums:
         numeros.append(i)

    for num in range (len(numeros)): #de esta forma num adquiere el valor de la longitud y no el valor de cada elemento 
        if numeros[num] %2==0:
            element_par.append(numeros[num])
    
        else:
            element_impar.append(numeros[num])
    return f"Lista pares{element_par}\nLista impares{element_impar}"



#multiplicacion con *args
def multiplicar_todos(*nums):#una tupla que alamacena mi lista ingresada, tengo que accesar a mi lista para poder realizar operaciones con c/elemento
    numeros=[]
    for i in  nums:#nums es una tupla, al intentar sumarle +1 estamos tratando de realizar una operacion con esta(ERROR)
        numeros.append(i) 

    mult_nums=1     

    for num in numeros: #num adquiere el valor de cada elemento de numeros
        mult_nums=mult_nums*num

    if len(numeros)>=1:
             return mult_nums
    else:
             return 1  

#informacion de una persona 
def informacion_personal(**datos:str|int):#indicamos que tipo de dato utilizara ** indica que es una funcion que recibe clave-valor
    datos_completos="" #almacen de los datos clave-valor
    for clave, valor in datos.items():
         datos_completos= datos_completos+ f"{clave}: {valor}\n"
    return datos_completos
       
        

def calculadora_flexible(a:int|float, b:int|float, op="Suma")->int|float|str:
     match op:
          case "Suma" :
               return f"Resultado de la suma {a+b}"
          case "Resta" :
               return f"Resultado de la resta {a-b}"
          case "Multiplicación" :
               return f"Resultado de la multiplicación {a*b}"
          case "División":
               if a and b !=0:
                return f"Resultado de la division {a/b}"
               else:
                    "Error, división por cero"
          case _ :
               return "Elige una operación valida"
               
            
     
     
     



  


             

              
    