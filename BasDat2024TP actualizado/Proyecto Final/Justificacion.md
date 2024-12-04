### **Justificación del Diseño del Sistema de Ventas en Línea**

#### **Propósito del Sistema**
El objetivo principal de este sistema es gestionar una tienda en línea que organiza y administra **productos**, **clientes** y **órdenes de compra** de manera eficiente y segura. Este diseño se enfoca en:
1. **Facilidad de uso:** La interfaz y la base de datos evitan duplicados y ofrecen una gestión intuitiva.
2. **Seguridad de datos:** Las restricciones de la base de datos aseguran la consistencia y evitan errores.

-----

### **Entidades y Atributos**
El diseño incluye las siguientes entidades clave, con sus respectivos atributos:

1. **Producto:**
   - **Atributos:** id_producto, nombre, descripcion, precio, stock, categoria_id.
   - **Ejemplo:** Productos organizados en categorías como "Alimentos", "Vestimenta", "Celulares", entre otros.

2. **Cliente:**
   - **Atributos:** id_cliente, nombre, email, telefono, direccion.
   - **Función:** Almacenar información de contacto y ubicación de los clientes.

3. **Orden:**
   - **Atributos:** id_orden, cliente_id, fecha, total.
   - **Función:** Registrar cada transacción generada por los clientes.

4. **DetalleOrden:**
   - **Atributos:** producto_id, cantidad, precio, orden_id.
   - **Función:** Registrar los productos y cantidades específicas compradas en cada transacción.

5. **Categoria:**
   - **Atributos:** id_categoria, nombre.
   - **Función:** Agrupar productos para facilitar la organización y búsqueda durante las compras.

-----

### **Relaciones entre las Entidades**
1. **Cliente y Orden (Uno a Muchos):** 
   - Cada cliente puede realizar múltiples órdenes de compra.
   
2. **Orden y Producto (Muchos a Muchos):**
   - Cada orden puede incluir varios productos, y cada producto puede estar en múltiples órdenes. 
   - La tabla intermedia `DetalleOrden` gestiona esta relación.

3. **Producto y Categoria (Muchos a Uno):**
   - Cada producto pertenece a una categoría específica, pero una categoría puede incluir múltiples productos.

-----

### **Normalización de la Base de Datos**
Para evitar redundancias y garantizar la eficiencia, la base de datos sigue las **tres primeras formas normales (3NF):**

1. **Primera Forma Normal (1NF):**
   - Cada celda contiene un solo valor; no hay listas ni datos agrupados en una misma columna.

2. **Segunda Forma Normal (2NF):**
   - Todos los atributos dependen completamente de la clave principal de su tabla.

3. **Tercera Forma Normal (3NF):**
   - No hay dependencias transitivas; es decir, ningún atributo depende de otro que no sea clave primaria.

-----

### **Integridad de los Datos**
Se utilizan restricciones clave para garantizar consistencia y precisión:

1. **Llaves Primarias:**
   - Cada tabla tiene un identificador único, como id_producto, id_cliente o id_orden, para evitar duplicados.

2. **Llaves Foráneas:**
   - Conectan las tablas entre sí. Por ejemplo:
     - Relación entre un cliente y las órdenes que realiza.
     - Relación entre un producto y su categoría.

Estas restricciones aseguran que los datos sean consistentes y estén organizados, garantizando un sistema confiable y escalable. Este diseño proporciona una solución robusta para la gestión de ventas en línea, con un enfoque en la eficiencia, la organización y la integridad de los datos.