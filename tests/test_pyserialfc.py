import unittest

import serialfc


p = serialfc.Port(0)._card_type
card_type = serialfc.Port(0)._card_type


class SerialFCTestCase(unittest.TestCase):
    def setUp(self):
        self.port = serialfc.Port(0)


class GenericTestCase(SerialFCTestCase):
    def test_rs485(self):
        self.port.rs485 = True
        self.assertEqual(self.port.rs485, True)
        self.port.rs485 = False
        self.assertEqual(self.port.rs485, False)

    def test_echo_cancel(self):
        self.port.echo_cancel = True
        self.assertEqual(self.port.echo_cancel, True)
        self.port.echo_cancel = False
        self.assertEqual(self.port.echo_cancel, False)


@unittest.skipUnless(card_type == serialfc.CARD_TYPE_PCI,
                     "not supported with this card")
class PCITestCase(SerialFCTestCase):
    def test_sample_rate(self):
        self.port.sample_rate = 16
        self.assertEqual(self.port.sample_rate, 16)
        self.port.sample_rate = 8
        self.assertEqual(self.port.sample_rate, 8)
        self.port.sample_rate = 4
        self.assertEqual(self.port.sample_rate, 8)

    def test_termination(self):
        self.port.termination = True
        self.assertEqual(self.port.termination, True)
        self.port.termination = False
        self.assertEqual(self.port.termination, False)


@unittest.skipUnless(card_type == serialfc.CARD_TYPE_PCIe,
                     "not supported with this card")
class PCIeTestCase(SerialFCTestCase):
    def test_sample_rate(self):
        self.port.sample_rate = 16
        self.assertEqual(self.port.sample_rate, 16)
        self.port.sample_rate = 8
        self.assertEqual(self.port.sample_rate, 8)
        self.port.sample_rate = 4
        self.assertEqual(self.port.sample_rate, 4)
        self.port.sample_rate = 2
        self.assertEqual(self.port.sample_rate, 4)

    def test_termination(self):
        self.port.termination = True
        self.assertEqual(self.port.termination, True)
        self.port.termination = False
        self.assertEqual(self.port.termination, False)


@unittest.skipUnless(card_type == serialfc.CARD_TYPE_FSCC,
                     "not supported with this card")
class FSCCTestCase(SerialFCTestCase):
    def test_sample_rate(self):
        self.port.sample_rate = 16

        with self.assertRaises(serialfc.InvalidParameterError):
            self.port.sample_rate = 3
            self.assertEqual(self.port.sample_rate, 16)

        with self.assertRaises(serialfc.InvalidParameterError):
            self.port.sample_rate = 17
            self.assertEqual(self.port.sample_rate, 16)

        for i in range(4, 16 + 1):
            self.port.sample_rate = i
            self.assertEqual(self.port.sample_rate, i)


if __name__ == '__main__':
    unittest.main()
