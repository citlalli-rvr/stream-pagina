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
# stream.py - Aplicación Web Interactiva con Streamlit

Este archivo, **stream.py**, es el núcleo de la aplicación web interactiva desarrollada con **Streamlit**. La aplicación permite a los usuarios realizar cálculos comunes y obtener resultados instantáneos en una interfaz amigable. Este archivo conecta la lógica de las funciones con la interfaz gráfica, permitiendo que los usuarios interactúen de manera dinámica.

## Estructura de `stream.py`

El archivo está diseñado para ser modular y fácil de navegar. Está dividido en las siguientes secciones principales:

1. **Título y encabezados**
2. **Introducción y contenido informativo**
3. **Menú lateral para seleccionar operaciones**
4. **Implementación de las funciones seleccionadas**
5. **Formulario de contacto**

## Sección 1: Título y Encabezados

Al iniciar la aplicación, se presenta el título de la página junto con una breve introducción. Esta sección se incluye dentro de un `container` de **Streamlit**, lo que facilita la organización y el diseño del contenido.

```python
st.title("FIME")
email_contact="fimefun5@gmail.com"

with st.container():
    st.header("Hola, Somos FIME👋")
    st.subheader("Creamos esta página priorizando tu comodidad, esperamos tengas una excelente experiencia")
```

Aquí se define el título principal y un correo de contacto para los usuarios en caso de que necesiten soporte.

## Sección 2: Introducción y Columnas Informativas

En esta sección, se divide la página en dos columnas: una para explicar el propósito de la página y la otra para ofrecer información de ayuda en caso de que los usuarios encuentren dificultades.

```python
with st.container():
    st.write("---")
    text_column, error_column = st.columns(2)
    with text_column:
        st.header("Te contamos más...")
        st.write(
            """Al navegar por esta página notarás una barra lateral que te permite visualizar un menú, 
            podrás seleccionar la operación que desees acorde a tus necesidades."""
        )
    with error_column:
        st.header("¿La página está presentando dificultades?")
        st.write("En caso de experimentar algún problema con nuestras funciones no dudes en enviarnos un correo.")
```

## Sección 3: Barra Lateral de Selección

En esta parte, se crea una **barra lateral** con el widget `selectbox` de **Streamlit** que permite a los usuarios elegir una de las múltiples funciones disponibles. Cada opción llama a una función específica previamente definida en `funciones.py`.

```python
st.sidebar.title("Explora nuestros ejercicios")
opcion = st.sidebar.selectbox("Selecciona una opción: ", [
    "Saludo",
    "Suma dos números",
    "Área de un triángulo",
    "Calculadora de descuento",
    "Suma una lista de números",
    "Calcular costo por mi producto",
    "Números pares e impares",
    "Multiplicación de una lista de números",
    "Darme a conocer",
    "Calculadora flexible"
])
```

## Sección 4: Implementación de las Funciones Seleccionadas

Dependiendo de la opción seleccionada en la barra lateral, la aplicación ejecuta diferentes bloques de código que corresponden a las funciones definidas en `funciones.py`. El código usa la estructura `match-case` (equivalente a `switch-case`) para ejecutar la lógica adecuada según la selección del usuario.

Por ejemplo, en el caso de seleccionar "Suma dos números":

```python
match opcion:
    case "Saludo":
        nombre = st.text_input("Ingresa tu nombre")
        st.write(fn.saludar(nombre))

    case "Suma dos números":
        a = st.number_input("Ingresa el primer número: ")
        b = st.number_input("Ingresa el segundo número: ")
        st.write(f"El resultado de la suma es {fn.sumar(a, b)}")
```

Cada función es llamada dinámicamente según la opción seleccionada, permitiendo una experiencia interactiva. Por ejemplo:

- **Saludo**: Solicita un nombre y muestra un saludo.
- **Suma dos números**: Permite al usuario ingresar dos números y los suma.
- **Calculadora flexible**: Realiza una operación elegida por el usuario (suma, resta, multiplicación o división).

En el caso de "Multiplicación de una lista de números", se utiliza un botón para activar la operación después de ingresar los números:

```python
case "Multiplicación de una lista de números":
    numeros = []
    cantidad_nums = st.number_input("¿Cuántos números deseas multiplicar?", min_value=0)
    for i in range(int(cantidad_nums)):
        numero = st.number_input(f"Ingresa el número {i+1}", key=f"num_{i}")
        numeros.append(numero)
    if st.button("Multiplicar"):
        st.write(f"El resultado de la multiplicación es {fn.multiplicar_todos(*numeros)}")
```

## Sección 5: Formulario de Contacto

Al final de la página, se incluye un formulario de contacto creado con un formulario HTML. Permite a los usuarios enviar un mensaje por correo electrónico en caso de problemas o consultas.

```python
with st.container():
    st.write("------")
    st.header("Contáctanos")
    st.write("Recuerda comentar las dificultades presentadas por nuestra página")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
     <input type="text" name="name" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu correo" required>
     <textarea name="message" placeholder="Detalles de su problema"></textarea>
     <button type="submit">Enviar</button>
    </form>"""
```

Se utiliza `st.markdown` para insertar el formulario HTML en la página con `unsafe_allow_html=True` para permitir la inserción de código HTML.

## Uso

1. Ejecuta la aplicación con el siguiente comando:
   ```bash
   streamlit run stream.py
   ```

2. La aplicación se abrirá en tu navegador web predeterminado. Selecciona una opción desde la barra lateral para realizar operaciones.

## Funcionalidades Incluidas

1. **Saludo personalizado**
2. **Operaciones matemáticas**: Suma, multiplicación, área de triángulo, calculadora de descuentos, etc.
3. **Operaciones avanzadas con listas**: Clasificación de números pares e impares, suma de listas y multiplicación.
4. **Formulario de contacto** para consultas o problemas técnicos.

## Personalización

Puedes añadir más operaciones o modificar las existentes simplemente agregando más funciones en `funciones.py` y ampliando el menú de selección en la barra lateral de `stream.py`.



## Contacto

Si tienes problemas con la página o quieres contribuir al proyecto, no dudes en ponerte en contacto con nosotros. Para reportar errores, puedes enviar un correo electrónico a:

- **Correo de contacto**: fimefun5@gmail.com

