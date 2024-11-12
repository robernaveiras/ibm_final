#Clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = self.__validar_precio(precio)
        self._cantidad = self.__validar_cantidad(cantidad)

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre=valor

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        self.__validar_precio(valor)
        self._precio = valor

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, valor):
        self.__validar_cantidad(valor)
        self._cantidad = valor

    @staticmethod
    def __validar_precio(precio):
        if precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        return precio
    
    @staticmethod
    def __validar_cantidad(cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad debe ser mayor o igual que 0")
        return cantidad


#Clase Inventario
class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        for p in self._productos:
            if p.nombre == producto.nombre:
                raise ValueError("Producto ya existe en el inventario")
        self._productos.append(producto)

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        for p in self._productos:
            if p.nombre == nombre:
                if precio is not None:
                    p.precio = precio
                if cantidad is not None:
                    p.cantidad = cantidad
                return
        raise ValueError("Producto no exite en el inventario")
    
    def eliminar_producto(self, nombre):
        for i in range(len(self._productos)):
            if self._productos[i].nombre == nombre:
                del self._productos[i]
                return
        raise ValueError("Producto no existe en el inventario")
    
    def mostrar_inventario(self):
        for p in self._productos:
            print(f"Nombre: {p.nombre}, Categoria: {p.categoria}, Precio: {p.precio}, Cantidad: {p.cantidad}")

    def buscar_producto(self, nombre):
        for p in self._productos:
            if p.nombre == nombre:
                return p
        raise ValueError("Producto no existe en el inventario")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    producto1 = Producto("Camisa", "Ropa", 20, 10)
    producto2 = Producto("Zapato", "Calzado", 50, 5)
    producto3 = Producto("Mesa", "Muebles", 1000, 3)
    producto4 = Producto("Pantalon", "Ropa", 22, 65)
    producto5 = Producto("Botas", "Calzado", 350, 3)
    
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)
    inventario.agregar_producto(producto4)
    inventario.agregar_producto(producto5)

    print("Inventario actual:")
    inventario.mostrar_inventario()

    inventario.actualizar_producto("Camisa", precio=25)

    print("\nInventario actualizado:")
    inventario.mostrar_inventario()

    inventario.eliminar_producto("Zapato")

    print("\nInventario actualizado después de eliminar zapato:")
    inventario.mostrar_inventario()

    try:
        inventario.agregar_producto(producto1)
    except ValueError as e:
        print(e)

    try:
        inventario.actualizar_producto("Camisa", cantidad=-5)
    except ValueError as e:
        print(e)

    try:
        inventario.buscar_producto("Zapato")
    except ValueError as e:
        print(e)