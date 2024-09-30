# Proyecto FIME - Funciones y Operaciones Interactivas

Bienvenido al proyecto **FIME**, una aplicación web interactiva creada con **Streamlit**. Esta página ofrece una serie de funciones que permiten realizar cálculos comunes, como la suma de números, el cálculo de áreas, operaciones con listas, y más, todo con un enfoque sencillo y práctico.

## Características

El proyecto incluye las siguientes funcionalidades:

1. **Saludo**: Genera un saludo personalizado.
2. **Suma de dos números**: Permite sumar dos números, ya sean enteros o decimales.
3. **Área de un triángulo**: Calcula el área de un triángulo dado la base y la altura.
4. **Calculadora de descuentos**: Calcula el precio final de un producto considerando descuentos e impuestos.
5. **Suma de una lista de números**: Suma todos los números de una lista.
6. **Costo por producto**: Calcula el costo total de un producto según su cantidad y precio unitario.
7. **Números pares e impares**: Clasifica una lista de números en pares e impares.
8. **Multiplicación de una lista de números**: Multiplica todos los números en una lista.
9. **Información personal**: Permite ingresar y mostrar información personal clave-valor.
10. **Calculadora flexible**: Realiza operaciones aritméticas como suma, resta, multiplicación y división.

## Instalación

1. Clona este repositorio a tu máquina local:
   ```bash
   git clone https://github.com/tuusuario/fime-proyecto.git
   ```
2. Instala las dependencias necesarias (si no tienes `Streamlit` instalado):
   ```bash
   pip install streamlit
   ```

3. Ejecuta el servidor de **Streamlit**:
   ```bash
   streamlit run stream.py
   ```

## Estructura de Archivos

- **funciones.py**: Contiene las definiciones de las funciones de lógica que son llamadas por la interfaz de Streamlit.
- **stream.py**: El archivo principal de la aplicación donde se integra la lógica de las funciones con la interfaz de usuario utilizando **Streamlit**.

## Funciones Principales

### 1. `saludar(nombre: str) -> str`
   Retorna un saludo personalizado:
   ```python
   def saludar(nombre: str) -> str:
       return f"Hola {nombre}"
   ```

### 2. `sumar(a: int|float, b: int|float) -> int|float`
   Suma dos números:
   ```python
   def sumar(a: int | float, b: int | float) -> int | float:
       return a + b
   ```

### 3. `calcular_area_triangulo(base: float, altura: float) -> float`
   Calcula el área de un triángulo:
   ```python
   def calcular_area_triangulo(base: float, altura: float) -> float:
       return (base * altura) / 2
   ```

### 4. `calcular_precio_final(precio: int|float, descuento=0.10, impuesto=0.16) -> int|float`
   Calcula el precio final de un producto aplicando descuento e impuestos:
   ```python
   def calcular_precio_final(precio: int | float, descuento=10, impuesto=16) -> int | float:
       desc = precio - (precio * (descuento / 100))
       total = desc + (desc * (impuesto / 100))
       return total
   ```

### 5. `sumar_lista(*nums: list[int|float]) -> int|float`
   Suma los valores de una lista de números:
   ```python
   def sumar_lista(*nums: list | int) -> list | int:
       suma = 0
       for i in range(len(nums)):
           suma = suma + nums[i]
       return suma
   ```

### 6. `producto(nombre: str, cantidad=1, precio=10) -> str`
   Calcula el costo total de un producto según la cantidad:
   ```python
   def producto(nombre: str, cantidad=1, precio=10) -> int | float | str:
       precio_total = precio * cantidad
       return f"El total a pagar por {cantidad} {nombre} es {precio_total}"
   ```

### 7. `numeros_pares_e_impares(*nums: list[int|float]) -> str`
   Clasifica los números en pares e impares:
   ```python
   def numeros_pares_e_impares(*nums):
       element_par = []
       element_impar = []
       numeros = []
       for i in nums:
           numeros.append(i)
       for num in range(len(numeros)):
           if numeros[num] % 2 == 0:
               element_par.append(numeros[num])
           else:
               element_impar.append(numeros[num])
       return f"Lista pares{element_par}\nLista impares{element_impar}"
   ```

### 8. `multiplicar_todos(*nums: list[int|float]) -> int|float`
   Multiplica todos los números de una lista:
   ```python
   def multiplicar_todos(*nums):
       numeros = []
       for i in nums:
           numeros.append(i)
       mult_nums = 1
       for num in numeros:
           mult_nums = mult_nums * num
       return mult_nums if len(numeros) >= 1 else 1
   ```

### 9. `informacion_personal(**datos: dict[str, int]) -> str`
   Recibe varios datos de una persona (clave-valor):
   ```python
   def informacion_personal(**datos: str | int) -> str:
       datos_completos = ""
       for clave, valor in datos.items():
           datos_completos += f"{clave}: {valor}\n"
       return datos_completos
   ```

### 10. `calculadora_flexible(a: int|float, b: int|float, op="Suma") -> str`
   Realiza varias operaciones matemáticas en base a la opción elegida:
   ```python
   def calculadora_flexible(a: int | float, b: int | float, op="Suma") -> str:
       match op:
           case "Suma":
               return f"Resultado de la suma {a + b}"
           case "Resta":
               return f"Resultado de la resta {a - b}"
           case "Multiplicación":
               return f"Resultado de la multiplicación {a * b}"
           case "División":
               if a and b != 0:
                   return f"Resultado de la division {a / b}"
               else:
                   return "Error, división por cero"
           case _:
               return "Elige una operación válida"
   ```

## Contacto

Si tienes problemas con la página o quieres contribuir al proyecto, no dudes en ponerte en contacto con nosotros. Para reportar errores, puedes enviar un correo electrónico a:

- **Correo de contacto**: fimefun5@gmail.com

