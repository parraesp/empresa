from unittest import TestCase
from Departamento import *
from mockito import *
from Empleado import *
__author__ = 'Alberto L'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        em1 = mock(Empleado)
        em2 = mock(Empleado)
        em3 = mock(Empleado)

        when(em1).get_salario().thenReturn(1200)
        when(em2).get_salario().thenReturn(2200)
        when(em3).get_salario().thenReturn(1600)

        dep = Departamento("dep1","d01")

        dep.aniadir_empleado(em1)
        dep.aniadir_empleado(em2)
        dep.aniadir_empleado(em3)

        res = dep.get_salario_total()

        print(res)

        self.assertEqual(res, 5000)