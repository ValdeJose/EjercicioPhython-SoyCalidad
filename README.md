## Detalles de Implementación

El programa utiliza tres diccionarios para almacenar la información de los productos:

- `Productos`: Almacena el nombre de los productos con su ID como clave.
- `Precios`: Almacena el precio de los productos con su ID como clave.
- `Stock`: Almacena la cantidad disponible de los productos con su ID como clave.

### Funciones Principales

- **`mostrar_datos()`**: Muestra una tabla con todos los productos, incluyendo ID, nombre, precio y stock.
- **`agregar_producto()`**: Solicita al usuario los datos del nuevo producto, realiza validaciones y lo agrega a los diccionarios.
- **`eliminar_producto()`**: Elimina un producto existente basado en el ID proporcionado por el usuario.
- **`actualizar_producto()`**: Actualiza la información de un producto existente basado en el ID proporcionado por el usuario.
- **`main()`**: Muestra el menú principal y gestiona las opciones del usuario.

## Validaciones

- **Nombre del producto**: Solo se permiten letras y espacios.
- **Precio**: Debe ser un número mayor a 0.
- **Cantidad**: Debe ser un número entero no menor a 0.
- **Opción del menú**: Debe ser un número entero entre 1 y 4.
