#-- IMPORTS ------------------------------------------------------------------------------------------------------------------------------------------------------------------
import mysql.connector
from mysql.connector import Error

#-- DATABASE CONNECTION ------------------------------------------------------------------------------------------------------------------------------------------------------
def DatabaseConnection():
    try:
        Connection = mysql.connector.connect(
            host = 'localhost',
            database = 'OnlineSalesSystem',
            user = 'root', 
            password = 'ig1234567'  
        )
        if Connection.is_connected():
            print("Conexión establecida exitosamente. Prosiguiendo...")
            return Connection
        else:
            print("La conexión no pudo ser establecida, aunque no arrojó errores.")
            return None
    except Error as ConnectionError:
        print("Se ha presentado un error al conectar con la base de datos. Intentalo nuevamente.")
        print("Información del error:\n",ConnectionError)
        return None

#-- CUSTOMER MAIN MENU -------------------------------------------------------------------------------------------------------------------------------------------------------
def Menu():
    print("\n--- ★ ~ SISTEMA DE VENTAS ~ ★ ---")
    print("(1) Gestión de productos")
    print("(2) Gestión de clientes")
    print("(3) Procesamiento de órdenes")
    print("(4) Búsquedas avanzadas")
    print("(5) Reporte de productos más vendidos")
    print("(6) Modificación del valor de un producto")
    print("(7) Salir")

#-- MENU FUNCTIONS -----------------------------------------------------------------------------------------------------------------------------------------------------------
def ProductManagement(connection):
    cursor = connection.cursor()
    print("Gestión de productos:")
    print("(1) Agregar producto")
    print("(2) Actualizar producto")
    print("(3) Ver productos")
    print("(4) Eliminar producto")
    Input = input("Elija una opción: ")

    if Input == "1":
        ProductName = input("Nombre del producto: ")
        ProductDescription = input("Descripción del producto: ")
        ProductPrice = float(input("Precio del producto: "))
        ProductStock = int(input("Stock del producto disponible: "))
        CategoryID = int(input("ID de la categoría del producto: "))
        cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, stock, categoria_id) VALUES (%s, %s, %s, %s, %s)",
                    (ProductName, ProductDescription, ProductPrice, ProductStock, CategoryID))
        connection.commit()
        print("Producto agregado correctamente.")

    elif Input == "2":
        cursor.callproc("obtener_productos")
        for Product in cursor.stored_results():
            Products = Product.fetchall()
            for Product in Products:
                print(f"ID: {Product[0]}, Nombre: {Product[1]}, Precio: {Product[3]}, Stock: {Product[4]}")
        ProductID = int(input("ID del producto a actualizar: "))
        NewProductPrice = float(input("Nuevo precio: "))
        NewProductQuantity = int(input("Nuevo stock: "))
        cursor.callproc("actualizar_producto", (ProductID, NewProductPrice, NewProductQuantity))
        connection.commit()
        print("Producto actualizado correctamente.")

    elif Input == '3':
        cursor.callproc("obtener_productos")
        for Product in cursor.stored_results():
            Products = Product.fetchall()
            for Product in Products:
                print(f"ID: {Product[0]}, Nombre: {Product[1]}, Precio: {Product[3]}, Stock: {Product[4]}")
    
    elif Input == '4':
        cursor.callproc("obtener_productos")
        for Product in cursor.stored_results():
            Products = Product.fetchall()
            for Product in Products:
                print(f"ID: {Product[0]}, Nombre: {Product[1]}")
        ProductID = int(input("ID del producto a eliminar: "))
        cursor.callproc("eliminar_producto", (ProductID,))  # Llamamos al procedimiento
        connection.commit()
        print("Producto eliminado correctamente.")
   
def CustomerManagement(connection):
    cursor = connection.cursor()
    print("\nGestión de Clientes")
    print("(1) Registrar Cliente")
    print("(2) Actualizar Cliente")
    print("(3) Ver todos los clientes")
    Input = input("Elija una opción: ")

    if Input == '1':
        CustomerName = input("Nombre del cliente: ")
        CustomerEmail = input("Email del cliente: ")
        CustomerPhone = input("Teléfono del cliente: ")
        CustomerAddress = input("Dirección del cliente: ")
        
        cursor.execute("INSERT INTO Cliente (nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s)",
                    (CustomerName, CustomerEmail, CustomerPhone, CustomerAddress))
        connection.commit()
        print("Cliente registrado correctamente.")

    elif Input == '2':
        cursor.execute("SELECT * FROM Cliente")
        Customers = cursor.fetchall()
        for Customer in Customers:
            print(f"ID: {Customer[0]}, Nombre: {Customer[1]}, Email: {Customer[2]}, Teléfono: {Customer[3]}, Dirección: {Customer[4]}")
        CustomerID = int(input("ID del cliente a actualizar: "))
        NewCustomerPhone = input("Nuevo teléfono: ")
        NewCustomerAddress = input("Nueva dirección: ")
        
        cursor.execute("UPDATE Cliente SET telefono = %s, direccion = %s WHERE id_cliente = %s", 
                    (NewCustomerPhone, NewCustomerAddress, CustomerID))
        connection.commit()
        print("Cliente actualizado correctamente.")

    elif Input == '3':
        cursor.execute("SELECT * FROM Cliente")
        Customers = cursor.fetchall()
        for Customer in Customers:
            print(f"ID: {Customer[0]}, Nombre: {Customer[1]}, Email: {Customer[2]}, Teléfono: {Customer[3]}, Dirección: {Customer[4]}")

def OrderProcessing(connection):
    cursor = connection.cursor()
    print("\nProcesamiento de Órdenes")
    CustomerID = int(input("ID del cliente: "))
    Date = input("Fecha de la orden (Formato: Año-Mes-Día): ")
    Total = float(input("Total de la orden: "))
    cursor.execute("INSERT INTO Orden (cliente_id, fecha, total) VALUES (%s, %s, %s)", (CustomerID, Date, Total))
    connection.commit()
    print("Orden procesada correctamente.")

def AdvancedSearches(connection):
    cursor = connection.cursor()
    ProductName = input("Ingrese el nombre del producto a buscar: ")
    cursor.execute("SELECT * FROM Producto WHERE nombre LIKE %s", ('%' + ProductName + '%',))
    Products = cursor.fetchall()
    if Products:
        for Product in Products:
            print(f"ID: {Product[0]}, Nombre: {Product[1]}, Precio: {Product[3]}, Stock: {Product[4]}")
    else:
        print("No se han encontrado productos que coincidan con la busqueda.")

def BestSellingProductsPeport(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT p.nombre, SUM(d.cantidad) AS cantidad_vendida
        FROM Producto p
        JOIN DetalleOrden d ON p.id_producto = d.producto_id
        GROUP BY p.id_producto
        ORDER BY cantidad_vendida DESC
        LIMIT 1
    """)
    Product = cursor.fetchone()
    print(f"\nProducto más vendido: {Product[0]}, Cantidad vendida: {Product[1]}")

def ModificationOfTheValueOfAProduct(connection):
    cursor = connection.cursor()
    MaximumQuantity = int(input("Cantidad máxima que se puede vender para todos los productos: "))
    
    cursor.execute("UPDATE Producto SET stock = %s", (MaximumQuantity,))
    connection.commit()
    print(f"El stock de todos los productos fue actualizado a {MaximumQuantity} correctamente.")

#-- MAIN FUNCTION ------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    connection = DatabaseConnection()
    if connection is None:
        return
    while True:
        Menu()
        option = input("Elija una opción: ")
        if option == '1':
            ProductManagement(connection)
        elif option == '2':
            CustomerManagement(connection)
        elif option == '3':
            OrderProcessing(connection)
        elif option == '4':
            AdvancedSearches(connection)
        elif option == '5':
            BestSellingProductsPeport(connection)
        elif option == '6':
            ModificationOfTheValueOfAProduct(connection)
        elif option == '7':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
    connection.close()

#-- CODE EXECUTION -----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()