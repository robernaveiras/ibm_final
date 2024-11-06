class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

        # Validaciones
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0")

    # Getters y setters
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
        self.__productos = []

    def agregar_producto(self, producto):
        if producto in self.__productos:
            raise ValueError("El producto ya existe en el inventario")
        self.__productos.append(producto)

    def actualizar_producto(self, nombre_producto, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                if nueva_cantidad is not None:
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
            print(f"Nombre: {producto.nombre}, Categoria: {producto.categoria}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")

    def buscar_producto(self, nombre_producto):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                return producto
        return None


# Crear productos
producto1 = Producto("Manzana", "Frutas", 1.5, 10)
producto2 = Producto("Leche", "Lácteos", 2.0, 5)

# Crear inventario
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Mostrar inventario
inventario.mostrar_inventario()

# Buscar un producto
producto_encontrado = inventario.buscar_producto("Manzana")

# Actualizar un producto
inventario.actualizar_producto("Leche", nueva_cantidad=8)

# Eliminar un producto
inventario.eliminar_producto("Manzana")