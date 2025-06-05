import mysql.connector

class ConexionBD:
    
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(host='localhost',  # Dirección del servidor MySQL
                                                database='paises_del_mundo',  # Nombre de la base de datos
                                                user='root',  # Usuario de MySQL
                                                password='Cali2025')  # Contraseña de MySQL
            print("Conexión Correcta")
            print(conexion)
            return conexion 
        
        except mysql.connector.Error as error: 
            print("Error al conectarte la Base de Datos {}".format(error))              
            
            return conexion
    
    ConexionBaseDeDatos()  
 
