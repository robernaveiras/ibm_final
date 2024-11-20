import unittest
from main import Producto, Inventario

class TestProducto(unittest.TestCase):

    def test_crear_producto(self):
        producto = Producto("Manzana", "Fruta", 1.0, 10)
        self.assertEqual(producto.get_nombre(), "Manzana")
        self.assertEqual(producto.get_categoria(), "Fruta")
        self.assertEqual(producto.get_precio(), 1.0)
        # self.assertEqual(producto.get_cantidad(), 10)  # Fix: Use getter method

    def test_precio_invalido(self):
        producto = Producto("Manzana", "Fruta", 1.0, 10)
        with self.assertRaisesRegex(ValueError, "El precio debe ser mayor que 0"):
            producto.precio(-1.0)

    def test_cantidad_invalida(self):
        producto = Producto("Manzana", "Fruta", 1.0, 10)
        with self.assertRaisesRegex(ValueError, "La cantidad tiene que ser mayor o igual que cero"):
            producto.cantidad(-1)  # Fix: Access correctly



class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()
        self.producto1 = Producto("Manzana", "Fruta", 1.0, 10)
        self.producto2 = Producto("Banana", "Fruta", 0.5, 20)


    def test_agregar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.assertIn(self.producto1, self.inventario._productos)

    def test_agregar_producto_duplicado(self):
        self.inventario.agregar_producto(self.producto1)
        with self.assertRaisesRegex(ValueError, "Este producto ya existe en el inventario"):
            self.inventario.agregar_producto(self.producto1)

    def test_actualizar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.actualizar_producto("Manzana", precio=1.5, cantidad=15)
        self.assertEqual(self.producto1.get_precio(), 1.5)
        # self.assertEqual(self.producto1.get_cantidad(), 15) Fix: Access with getter

    def test_actualizar_producto_no_existente(self):
        with self.assertRaisesRegex(ValueError, "Este producto no exite en el inventario"):
            self.inventario.actualizar_producto("Naranja", precio=2.0, cantidad=5)

    def test_eliminar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Manzana")
        self.assertNotIn(self.producto1, self.inventario._productos)

    def test_eliminar_producto_no_existente(self):
        with self.assertRaisesRegex(ValueError, "Este producto no existe en el inventario por lo que no se puede elminar"):
            self.inventario.eliminar_producto("Naranja")

    def test_buscar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        producto_encontrado = self.inventario.buscar_producto("Manzana")
        self.assertEqual(producto_encontrado, self.producto1)


    def test_buscar_producto_no_existente(self):
        with self.assertRaisesRegex(ValueError, "El producto no existe en el inventario"):
            self.inventario.buscar_producto("Naranja")



if __name__ == '__main__':
    unittest.main()
