# **Justificación del Diseño del Sistema de Ventas en Línea**

El sistema de ventas en línea tiene por objetivo gestionar eficientemente las operaciones básicas de una tienda, como por ejemplo la administración de productos, clientes, órdenes de compra, entre otros.  
	Este diseño busca ser más amigable con el usuario usando una estructura de datos que permite ser ejecutado de forma confiable, sin complicar al usuario.

# **Entidades y Atributos**

El modelo de datos cuenta con cinco entidades que están diseñadas para cumplir con las necesidades del proyecto. Entre ellas podemos encontrar Productos, Clientes, Orden, Detalle de orden y Categorías.

* *Producto*: id\_producto, nombre, descripción, precio, stock, categoria\_id.  
  Busca representar los productos disponibles en la tienda, dando datos relevantes como su nombre, una breve descripción, su valor, stock en tienda y a qué categoría pertenece.  
* *Cliente*: id\_cliente, nombre, email, telefono, direccion.  
  Almacena la información de los clientes para facilitar el procesamiento de órdenes y servicio al cliente.  
* *Orden*: id\_orden, cliente\_id, fecha, total.  
  Registra las compras realizadas relacionándolas a un cliente y sumando el total de compras.  
* *DetalleOrden*: producto\_id, orden\_id, cantidad, precio.  
  Registra los productos incluidos en cada orden y la cantidad adquirida y el total de la orden.  
* *Categoria*: id\_categoria, nombre.  
  Agrupa los productos por categorías para facilitar las búsquedas.

# **Relaciones entre las Entidades**

Las entidades están conectadas por las siguientes relaciones:

* *Cliente y Orden (Uno a Muchos)*: Un cliente puede realizar varias órdenes, pero cada orden pertenece a un solo cliente.  
* *Orden y Producto (Muchos a Muchos*): Una orden puede incluir múltiples productos, y un producto puede aparecer en varias órdenes (la tabla DetalleOrden actúa como intermediaria).  
* *Producto y Categoría (Muchos a Uno)*: Cada producto pertenece a una categoría, pero una categoría puede incluir varios productos.

# **Normalización**

Primera Forma Normal (1NF): Cada celda de las tablas contiene un único valor, sin listas o datos repetidos en una columna.  
	Segunda Forma Normal (2NF): Los atributos dependen de la clave primaria de su tabla.  
	Tercera Forma Normal (3NF): Cada atributo no clave depende únicamente de la clave primaria.

# **Integridad**

* *Llaves Primarias*: Identifican de manera única cada registro en las tablas (por ejemplo, id\_producto o id\_orden).  
* *Llaves Foráneas*: Vinculan las tablas relacionadas, como cliente\_id en la tabla Orden y categoria\_id en la tabla Producto.  
* *Validación de Transacciones:* Cada cambio en la base de datos (como agregar o actualizar datos) está protegido por transacciones que aseguran su éxito antes de confirmar los cambios.

## **Procesos**

* *Gestión de Productos:* Permite agregar, actualizar, eliminar y consultar productos.  
* *Gestión de Clientes:* Permite registrar y actualizar la información de clientes y visualizar los clientes ya registrados.  
* *Procesamiento de Órdenes:* Crea órdenes asociadas a clientes específicos y lleva un registro de los productos comprados en cada orden.

