import re

# Diccionarios
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

def mostrar_datos():
    print("\n" + ("=" * 50))
    print("\t\tLista de Productos:")
    print("=" * 50)
    print(f"{'ID':<5} {'Nombre Producto':<20} {'Precio':<10} {'Stock':<5}")
    print("-" * 50)
    
    for id_producto in Productos:
        print(f"{id_producto:<5} {Productos[id_producto]:<20} {Precios[id_producto]:<10.2f} {Stock[id_producto]:<5}")
    
    print("=" * 50)


def agregar_producto():
    id_nuevo = max(Productos.keys()) + 1
    
    while True:
        nombre = input("Ingrese el nombre del nuevo producto: ")
        if re.match("^[A-Za-z]+$", nombre):
            break
        else:
            print("El nombre solo puede contener letras. Intente de nuevo.")
    
    while True:
        try:
            precio = float(input("Ingrese el precio del nuevo producto: "))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0. Intente de nuevo.")
        except ValueError:
            print("El precio debe ser un número válido. Intente de nuevo.")
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
            if cantidad >= 0:
                break
            else:
                print("La cantidad no puede ser menor a 0. Intente de nuevo.")
        except ValueError:
            print("La cantidad debe ser un número entero válido. Intente de nuevo.")
    
    Productos[id_nuevo] = nombre
    Precios[id_nuevo] = precio
    Stock[id_nuevo] = cantidad
    print(f"Producto {nombre} agregado exitosamente.")

def eliminar_producto():
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    if id_eliminar in Productos:
        del Productos[id_eliminar]
        del Precios[id_eliminar]
        del Stock[id_eliminar]
        print("Producto eliminado exitosamente.")
    else:
        print("El ID del producto no existe.")

def actualizar_producto():
    id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
    if id_actualizar in Productos:
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        
        Productos[id_actualizar] = nombre
        Precios[id_actualizar] = precio
        Stock[id_actualizar] = cantidad
        print("Producto actualizado exitosamente.")
    else:
        print("El ID del producto no existe.")

def main():
    while True:
        mostrar_datos()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        
        while True:
            opcion = input("Elija opción: ")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion in [1, 2, 3, 4]:
                    break
                else:
                    print("Opción no válida. Debe ser 1, 2, 3 o 4.")
            else:
                print("Entrada inválida. Debe ingresar un número.")

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()