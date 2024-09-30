import streamlit as st
import funciones as fn

#definir el nombre de la pagina 

st.title("FIME")
email_contact="fimefun5@gmail.com"

#poner todo dentro de un streamlit with
#empleabilidad de container para seccionar

with st.container():
    st.header("Hola, Somos FIME👋")
    st.subheader("Creamos esta pagina priorizando tu comodidad, esperamos tengas una excelente experiencia")
    
    
#introducción
with st.container():
    st.write("---")
    #creacion de columnas 
    text_column,error_column= st.columns(2)
    with text_column:
        st.header("Te contamos más...")
        st.write(
            """Al navegar por esta pagina notarás una barra lateral que te permite visualizar un menú, podrás seleccionar la operacion que desees acorde a tus necesidades.
            """
            )
    with error_column:
        st.header("¿La página está presentando dificultades?")
        st.write("En caso de experimentar algun problema con nuestras funciones no dudes en enviarnos un correo, el proceso lo encontrarás al final de esta sección.")
    
#Barra lateral    
st.sidebar.title("Explora nuestros ejercicios")
st.sidebar.write("Te ofrecemos diversas opciones que te resultaran interesantes y sobre todo sencillas de implementar")
opcion=st.sidebar.selectbox("Selecciona una opción: ",
                     [
                         "Saludo",
                         "Suma dos números",
                         "Área de un triángulo",
                         "Calculadora de descuento",
                         "Suma una lista de numeros",
                         "Calcular costo por mi producto",
                         "Números pares e impares",
                         "Multiplicación de una lista de números",
                         "Darme a conocer",
                         "Calculadora flexible"

                     ]
)

match opcion:
    case "Saludo":
        nombre= st.text_input("Ingresa tu nombre")
        st.write(fn.saludar(nombre))

    case "Suma dos números":
        a=st.number_input("Ingresa el primer número: ")
        b=st.number_input("Ingresa el segundo número: ")
        st.write(f"El resultado de la suma es {fn.sumar(a,b)}")

    case "Área de un triángulo":
        base=st.number_input("Ingresa la base: ")
        altura=st.number_input("Ingresa la altura: ")
        st.write(f"El área del triángulo es {fn.calcular_area_triangulo(base,altura)} ")    

    case "Calculadora de descuento":  
        precio=st.number_input("Ingresa el precio de tu producto: ")
        descuento=st.number_input("Ingresa el descuento aplicado: ",value=10)
        impuesto=st.number_input("Ingresa el impuesto aplicado: ",value=16)
        st.write(f"El pago total a pagar de tu producto es {fn.calcular_precio_final(precio,descuento,impuesto)}")

    case  "Suma una lista de numeros":
        numeros=[]
        cantidad_nums=int(st.number_input("¿cuántos números conformarán tu lista? "))

        for i in range(cantidad_nums):
            numero=st.number_input(f"Ingresa el número {i+1}",key=f"num_{i}")
            numeros.append(numero)
        
        st.write(f"La suma de tu lista es {fn.sumar_lista(*numeros)}")   

    case "Calcular costo por mi producto":
        nombre=st.text_input("Ingresa el nombre del producto: ")
        cantidad=st.number_input("Ingresa la cantidad de unidades: ", value=1)
        precio=st.number_input("Ingresa el precio por unidad: ",value=10)
        st.write(fn.producto(nombre,cantidad,precio))

    case  "Números pares e impares":
        numeros=[]
        cantidad_nums=int(st.number_input("¿cuántos números conformarán tu lista? "))

        for i in range(cantidad_nums):
            numero=st.number_input(f"Ingresa el número {i+1}",key=f"num_{i}")
            numeros.append(numero)
        st.write(fn.numeros_pares_e_impares(*numeros))

    case "Multiplicación de una lista de números":
        numeros=[]
        cantidad_nums= st.number_input("¿cuántos números deseas multiplicar? ",min_value=0)
       
        for i in range(cantidad_nums):
            numero=st.number_input(f"Ingresa el número {i+1}",key=f"num_{i}")
            numeros.append(numero)
       
        if st.button("Multiplicar"):
            st.write(f"El resultado de la multiplicación es {fn.multiplicar_todos(*numeros)}")

    case "Darme a conocer":
        claves=[]
        valores=[]

        datos_totales=st.number_input("¿Cuántos datos desea dar a conocer? ",min_value=1,step=1)
        for i in range(datos_totales):
            clave=st.text_input(f"Ingrese el nombre del dato {i+1}",key=f"clave_{i}")
            valor=st.text_input(f"Ingrese la información para {clave}:",key=f"valor{i}")

            claves.append(clave)
            valores.append(valor)
        datos=dict(zip(claves,valores))
        st.write(fn.informacion_personal(**datos))    

    case "Calculadora flexible":
        a=st.number_input("Ingresa el primer número: ")
        b=st.number_input("Ingresa el segundo número: ")
        op=st.selectbox("Operación:",
                        ["Suma","Resta","Multiplicación","División"])
        st.write(fn.calculadora_flexible(a,b,op))

#Contacto

with st.container():
    st.write("------")  
    st.header("Contactanos")    
    st.write("Recuerda comentar las dificultades presentadas por nuestra página")
    contact_form= f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
     <input type="text" name="name" placeholder= "Tu nombre" required>
     <input type="email" name="email" placeholder="Tu correo" required>
     <textarea name="message" placeholder="Detalles de su problema"></textarea>
     <button type="submit">Enviar</button>
</form>"""

l_column,r_column= st.columns(2)
with l_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with r_column:
    st.empty() 

                  








