import pandas as pd

tablaEmpleados=pd.read_csv('./empleados.csv')

#imprime la tabla los primeros registros
#print(tablaEmpleados)
#imprime la tabla todos los registros
#print(tablaEmpleados.to_string())

#quiero tener todos los datos de los analistas 1  
#tablaAnalista1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"]
#print(tablaAnalista1)

#si quiero solo los 50 primeros le agrego.head(50)

#tablaAnalista1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
#Exportar la tabla ya creada a un archivo de html
#archivoHTML=tablaAnalista1.to_html()
#crear el archivo y que abra con permisos de escritura se le coloca la "w"
#archivoTEXTO=open("Datosanalistas1.html","w") #abrir el archivo de texto 
#archivoTEXTO.write(archivoHTML) #agregar el archivo de texto el archivo que creamos
#archivoTEXTO.close() #cerrar el archivo de texto 
#tabla analista 2 

#tablaAnalista2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
#Exportar la tabla ya creada a un archivo de html
#archivoHTML=tablaAnalista2.to_html()
#crear el archivo y que abra con permisos de escritura se le coloca la "w"
#archivoTEXTO=open("Datosanalistas2.html","w") #abrir el archivo de texto 
#archivoTEXTO.write(archivoHTML) #agregar el archivo de texto el archivo que creamos
#archivoTEXTO.close() #cerrar el archivo de texto 

tablaFiltro=tablaEmpleados[(tablaEmpleados['salario']>=5500000) & (tablaEmpleados['edad']<=30)] 
print(tablaFiltro)
#Exportar la tabla ya creada a un archivo de html
archivoHTML=tablaFiltro.to_html()
#crear el archivo y que abra con permisos de escritura se le coloca la "w"
archivoTEXTO=open("Datosfiltro.html","w") #abrir el archivo de texto 
archivoTEXTO.write(archivoHTML) #agregar el archivo de texto el archivo que creamos
archivoTEXTO.close() #cerrar el archivo de texto 






