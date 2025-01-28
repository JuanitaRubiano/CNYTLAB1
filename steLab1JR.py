import CnytLab1JR as lc
import unittest

class Testcplxop(unittest.TestCase):

    def test_sumcplx(self):
        self.assertAlmostEqual(lc.sumcplx((3.5,2.4),((5.1,2.2))),(8.6, 4.6))
        self.assertAlmostEqual(lc.sumcplx((1, 1.2), (4, 9)), (5, 10.2))

    #def test_restcplx(self):
        #self.assertAlmostEqual(lc.restcplx ((3.1,2.4),(5.6,1.2)),(-2.5,1.2))


    def test_multcplx(self):
        self.assertAlmostEqual(lc.multcplx((4,2),(5.3,6)),(9.2,34.6))
        self.assertAlmostEqual(lc.multcplx((14,9),(2,1)), (19, 32))

    def test_conjcplx(self):
        self.assertAlmostEqual((lc.conjcplx((5,2))),(5,-2))
        self.assertAlmostEqual((lc.conjcplx((9, 5))), (9, -5))

    def test_divcplx(self):
        self.assertAlmostEqual(lc.divcplx((9,27),(3,9)),(3.0,0.0))


    def modcplx(self):
        self.assertAlmostEqual((8,4),(8.944))
        self.assertAlmostEqual((5, 7), (8.602))

    def coorpaspolarcplx(self):
        self.assertAlmostEqual((-2,1),(2.23,-3.6))
        self.assertAlmostEqual((45, 9.1), (45.91, 0.199))


    def coorpascartapolcplx(self):
        self.assertAlmostEqual((5,14),(0.683,4.953))
        self.assertAlmostEqual((1.2, 2), (-0.499,1.091))


if __name__ == '__main__':
   unittest.main()