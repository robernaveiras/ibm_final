import unittest

class TestInventario(unittest.TestCase):

    def setUp(self):
        self.producto1 = Producto("Manzana", "Frutas", 1.5, 10)
        self.producto2 = Producto("Leche", "Lácteos", 2.0, 5)
        self.inventario = Inventario()
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)

    def test_agregar_producto(self):
        producto3 = Producto("Pan", "Granos", 1.0, 20)
        self.inventario.agregar_producto(producto3)
        self.assertEqual(len(self.inventario._Inventario__productos), 3)

    def test_agregar_producto_existente(self):
        with self.assertRaises(ValueError):
            self.inventario.agregar_producto(self.producto1)

    def test_actualizar_producto(self):
        self.inventario.actualizar_producto("Leche", nueva_cantidad=8)
        self.assertEqual(self.producto2.cantidad, 8)

    def test_actualizar_producto_no_encontrado(self):
        with self.assertRaises(ValueError):
            self.inventario.actualizar_producto("No Existe", nueva_cantidad=5)

    def test_eliminar_producto(self):
        self.inventario.eliminar_producto("Manzana")
        self.assertEqual(len(self.inventario._Inventario__productos), 1)

    def test_eliminar_producto_no_encontrado(self):
        with self.assertRaises(ValueError):
            self.inventario.eliminar_producto("No Existe")

    def test_buscar_producto(self):
        encontrado = self.inventario.buscar_producto("Leche")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Leche")

        with self.assertRaises(ValueError):
            self.inventario.buscar_producto("No Existe")
