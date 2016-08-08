#!../env/bin/python
execfile("1_money_example.py")
import unittest

print('\n Chapter 1 - 2 - 3 - 4 - 5 - 6 \n');


row_1 = infos('IBM',1000.0,25.0,'USD')
row_2 = infos('Novartis',400.0,150.0,'CHF')

inf = list_infos(row_1,row_2);

class MyTest(unittest.TestCase):

    def testMultiplication(self):

        five = Money.dolar(5)

        self.assertEqual(Dolar(10),five.times(2))
        self.assertEqual(Dolar(15),five.times(3))

        five = Money.franc(5)
        self.assertEqual(Franc(10),five.times(2))
        self.assertEqual(Franc(15),five.times(3))

    def testEquality(self):
        self.assertTrue(Dolar(5)==Dolar(5))
        self.assertFalse(Dolar(5)== None)
        self.assertFalse(Dolar(5)==Franc(5))
        self.assertFalse(Franc(5)== Franc(6))
        self.assertTrue(Franc(5)==Franc(5))
        self.assertFalse(Franc(5)== None)







    def test_1(self):
        self.assertEqual(inf.get_total('USD'), 65000)


    def test_CHF_USD(self):
        self.assertEqual(inf.get_total('CHF'), 97500)

    def test_rate_conversion(self):
        usd = inf.get_total('USD')
        chf = inf.get_total('CHF')

        rate = filter(lambda x: x['from']=='USD' and x['to']=='CHF',exchange)[0]['rate']
        self.assertEqual(chf/usd,rate)




if __name__ == '__main__':
    unittest.main()
