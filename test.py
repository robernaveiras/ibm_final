import unittest
from main import Producto, Inventario
# Assuming Producto and Inventario classes are defined as above


class TestProducto(unittest.TestCase):
    def test_creation(self):
        producto = Producto("Laptop", "Electronics", 1000, 5)
        self.assertEqual(producto.get_nombre(), "Laptop")
        self.assertEqual(producto.get_categoria(), "Electronics")
        self.assertEqual(producto.get_precio(), 1000)
        self.assertEqual(producto.get_cantidad(), 5)

    def test_set_precio(self):
        producto = Producto("Mouse", "Peripherals", 20, 10)
        producto.set_precio(30)
        self.assertEqual(producto.get_precio(), 30)

        with self.assertRaises(ValueError):
            producto.set_precio(-10)

    def test_set_cantidad(self):
        producto = Producto("Keyboard", "Peripherals", 50, 20)
        producto.set_cantidad(15)
        self.assertEqual(producto.get_cantidad(), 15)

        with self.assertRaises(ValueError):
            producto.set_cantidad(-5)


class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()
        self.producto1 = Producto("Laptop", "Electronics", 1000, 5)
        self.producto2 = Producto("Mouse", "Peripherals", 20, 10)

    def test_agregar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.assertEqual(len(self.inventario._productos), 1)

        with self.assertRaises(ValueError):
            self.inventario.agregar_producto(self.producto1)

    def test_actualizar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.actualizar_producto("Laptop", precio=1200, cantidad=7)
        producto = self.inventario.buscar_producto("Laptop")
        self.assertEqual(producto.get_precio(), 1200)
        self.assertEqual(producto.get_cantidad(), 7)

        with self.assertRaises(ValueError):
            self.inventario.actualizar_producto("Keyboard", precio=50, cantidad=3)

    def test_eliminar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Laptop")
        self.assertEqual(len(self.inventario._productos), 0)

        with self.assertRaises(ValueError):
            self.inventario.eliminar_producto("Mouse")

    def test_mostrar_inventario(self):
        import sys
        from io import StringIO

        # Redirect stdout to capture the print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        self.inventario.mostrar_inventario()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = (
            "Nombre: Laptop, Categoria: Electronics, Precio: 1000, Cantidad: 5\n"
            "Nombre: Mouse, Categoria: Peripherals, Precio: 20, Cantidad: 10\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_buscar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        producto = self.inventario.buscar_producto("Laptop")
        self.assertIsNotNone(producto)
        self.assertEqual(producto.get_nombre(), "Laptop")

        with self.assertRaises(ValueError):
            self.inventario.buscar_producto("Keyboard")


if __name__ == "__main__":
    unittest.main()
