#Clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria
    
    def get_precio(self):
        return self.__precio
        
    def get_cantidad():
        return self.__cantidad

    
    def precio(self, precio):
        if precio > 0:
            self.__precio = precio
        raise ValueError("El precio debe ser mayor que 0")

    def cantidad(self, valor):
        if cantidad >= 0:
            self.__cantidad = cantidad
        raise ValueError("La cantidad tiene que ser mayor o igual que cero")

#Clase Inventario
class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        for p in self._productos:
            if p.nombre == producto.nombre:
                raise ValueError("Este producto ya existe en el inventario")
        self._productos.append(producto)

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        for p in self._productos:
            if p.nombre == nombre:
                if precio is not None:
                    p.precio = precio
                if cantidad is not None:
                    p.cantidad = cantidad
                return
        raise ValueError("Este producto no exite en el inventario")
    
    def eliminar_producto(self, nombre):
        for i in range(len(self._productos)):
            if self._productos[i].nombre == nombre:
                del self._productos[i]
                return
        raise ValueError("Este producto no existe en el inventario por lo que no se puede elminar")
    
    def mostrar_inventario(self):
        for p in self._productos:
            print(f"Nombre: {p.nombre}, Categoria: {p.categoria}, Precio: {p.precio}, Cantidad: {p.cantidad}")

    def buscar_producto(self, nombre):
        for p in self._productos:
            if p.nombre == nombre:
                return p
        raise ValueError("El producto no existe en el inventario")

   