import unittest
from parcial2.calculadorabasica import suma,resta,multi,div

class TestOperaciones(unittest.TestCase):

    def test_suma_posotivos(self):
        self.assertEqua(suma(300,3),303)

        def test_suma_negativos(self):
            self.assertEqua(suma)