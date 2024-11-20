#Clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

# Gets para nombre categoria precio y cantidad

    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria
    
    def get_precio(self):
        return self.__precio
        
    def get_cantidad(self):
        return self.__cantidad

# Setea precio y cantidad

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0")

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad tiene que ser mayor o igual que cero")

#Clase Inventario
class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):  
        for p in self._productos:
            if p.get_nombre() == producto.get_nombre(): # Comprobamos que el producto no exista ya en el inventario
                raise ValueError("Este producto ya existe en el inventario")
        self._productos.append(producto) # Añadimos el producto a la lista inventario

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        for p in self._productos:
            if p.get_nombre() == nombre:
                if precio is not None: 
                    p.set_precio(precio) # Actualizamos el precio llamando a set de precio
                if cantidad is not None:
                    p.set_cantidad(cantidad) # Actualizamos cantidad llamando al set de cantidad
                return
        raise ValueError("Este producto no exite en el inventario")
    
    def eliminar_producto(self, nombre):
        for i in range(len(self._productos)):
            if self._productos[i].get_nombre() == nombre: # Comprobamos primero que el producto exista en el inventario
                del self._productos[i] # Eliminamos el producto de la lista inventario
                return
        raise ValueError("Este producto no existe en el inventario por lo que no se puede elminar")
    
    def mostrar_inventario(self):
        for p in self._productos:
            print(f"Nombre: {p.get_nombre()}, Categoria: {p.get_categoria()}, Precio: {p.get_precio()}, Cantidad: {p.get_cantidad()}")

    def buscar_producto(self, nombre):
        for p in self._productos:
            if p.get_nombre() == nombre:
                return p
        raise ValueError("El producto no existe en el inventario")

#Ejemplos de uso

producto1 = Producto("Manzana", "Frutas", 2.0, 10)
producto2 = Producto("Blusa", "Ropa", 43.0, 30)
producto3 = Producto("Pera", "Frutas", 0.8, 14)
inventario = Inventario()

print("Añadimos los productos")
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)
inventario.mostrar_inventario()

print("Eliminamos 'Manzana'")
inventario.eliminar_producto("Manzana")
inventario.mostrar_inventario()

print("Actualizamos BLusa")
inventario.actualizar_producto("Blusa", 49.9, 25)
inventario.mostrar_inventario()

print("Buscamos 'Pera'")
inventario.buscar_producto("Pera")
