class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

        #Validaciones

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0")
    #Getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter

    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        self.__precio = nuevo_precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0")
        self.__cantidad = nueva_cantidad


class Inventario:
    def __init__(self):
        self.productos= []

    def agregar_producto(self, producto):
        if producto in self.__productos:
            raise ValueError("El producto ya existe en el inventario")
        self.producto.append(producto)

    def actualizar_producto(self, nombre_producto, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.nonmbre == nombre_producto:
                if nuevo_precio:
                    producto.precio = nuevo_precio
                if nueva_cantidad:
                    producto.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado")

    def eliminar_producto(self, nombre_producto):
        for i, producto in enumerate(self.__productos):
            if producto.nombre == nombre_producto:
                del self.__productos[i]
                return
        raise ValueError("Producto no encontrado")

    def mostrar_inventario(self):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                return producto
        return None