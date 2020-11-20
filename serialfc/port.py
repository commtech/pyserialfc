"""
Copyright 2019 Commtech, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
"""

import serial
import os
import ctypes
import sys

if os.name == 'nt':
    DLL_NAME = 'cserialfc.dll'
else:
    if ctypes.sizeof(ctypes.c_voidp) == 4:
        DLL_NAME = 'libcserialfc.so'
    else:
        DLL_NAME = 'libcserialfc.so.6'

try:
    lib = ctypes.cdll.LoadLibrary(DLL_NAME)
except:
    if os.name == 'nt':
        lib = ctypes.cdll.LoadLibrary(os.path.join(sys.prefix, 'DLLS',
                                                   DLL_NAME))
    else:
        lib = ctypes.cdll.LoadLibrary(os.path.join(sys.prefix, 'local', 'DLLs',
                                                   DLL_NAME))

SERIALFC_NOT_SUPPORTED, SERIALFC_INVALID_PARAMETER, \
    SERIALFC_INVALID_ACCESS, \
    SERIALFC_PORT_NOT_FOUND = 17000, 17001, 17002, 17003

CARD_TYPE_PCI, CARD_TYPE_PCIe, CARD_TYPE_FSCC, CARD_TYPE_UNKNOWN = range(4)


class PortNotFoundError(OSError):
    def __init__(self, port_num):
        super(PortNotFoundError, self).__init__(
            'Port {} not found'.format(port_num))


class InvalidAccessError(OSError):
    def __init__(self):
        super(InvalidAccessError, self).__init__('Invalid access')


class InvalidParameterError(ValueError):
    def __str__(self):
        return 'Invalid parameter'


class Port(serial.Serial):

    def __init__(self, port_num, ttyS=None, serialfc=None):
        if os.name == 'nt':
            ttyS_name = 'COM{}'.format(port_num)
            super(Port, self).__init__(ttyS_name)
            try:
                self._handle = self.hComPort
            except AttributeError:
                self._handle = self._port_handle
        else:
            self._handle = ctypes.c_void_p()

            e = lib.serialfc_connect(port_num, ctypes.byref(self._handle))

            Port._check_error(e)

            self._handle = self._handle.value
            self._port_num = port_num

            if ttyS:
                ttyS_name = ttyS
            else:
                ttyS_name = '/dev/ttyS{}'.format(port_num + 4)

            super(Port, self).__init__(ttyS_name)

    @staticmethod
    def _check_error(e):
        if e == 0:
            pass
        elif e == SERIALFC_NOT_SUPPORTED:
            raise AttributeError
        elif e == SERIALFC_INVALID_PARAMETER:
            raise InvalidParameterError()
        elif e == SERIALFC_PORT_NOT_FOUND:
            raise PortNotFoundError()
        elif e == SERIALFC_INVALID_ACCESS:
            raise InvalidAccessError()
        else:
            raise OSError(e)

    def _ctypes_set_bool(self, enable_func, disable_func, status):
        func = enable_func if status else disable_func
        e = func(self._handle)
        Port._check_error(e)

    def _ctypes_get_bool(self, func):
        return bool(self._ctypes_get_uint(func))

    def _ctypes_action(self, func):
        e = func(self._handle)
        Port._check_error(e)

    def _ctypes_set(self, func, *args):
        e = func(self._handle, *args)
        Port._check_error(e)

    def _ctypes_get_int(self, func):
        status = ctypes.c_int()
        e = func(self._handle, ctypes.byref(status))
        Port._check_error(e)
        return status.value

    def _ctypes_get_uint(self, func):
        status = ctypes.c_uint()
        e = func(self._handle, ctypes.byref(status))
        Port._check_error(e)
        return status.value

    def _set_rs485(self, status):
        """Sets the value of the rs485 setting."""
        self._ctypes_set_bool(lib.serialfc_enable_rs485,
                              lib.serialfc_disable_rs485,
                              status)

    def _get_rs485(self):
        """Gets the value of the rs485 setting."""
        return self._ctypes_get_bool(lib.serialfc_get_rs485)

    rs485 = property(fset=_set_rs485, fget=_get_rs485)

    def _set_echo_cancel(self, status):
        """Sets the value of the echo_cancel setting."""
        self._ctypes_set_bool(lib.serialfc_enable_echo_cancel,
                              lib.serialfc_disable_echo_cancel,
                              status)

    def _get_echo_cancel(self):
        """Gets the value of the echo_cancel setting."""
        return self._ctypes_get_bool(lib.serialfc_get_echo_cancel)

    echo_cancel = property(fset=_set_echo_cancel, fget=_get_echo_cancel)

    def _set_termination(self, status):
        """Sets the value of the termination setting."""
        self._ctypes_set_bool(lib.serialfc_enable_termination,
                              lib.serialfc_disable_termination,
                              status)

    def _get_termination(self):
        """Gets the value of the termination setting."""
        return self._ctypes_get_bool(lib.serialfc_get_termination)

    termination = property(fset=_set_termination, fget=_get_termination)

    def _set_sample_rate(self, rate):
        """Sets the value of the sample_rate setting."""
        self._ctypes_set(lib.serialfc_set_sample_rate, rate)

    def _get_sample_rate(self):
        """Gets the value of the sample_rate setting."""
        return self._ctypes_get_uint(lib.serialfc_get_sample_rate)

    sample_rate = property(fset=_set_sample_rate, fget=_get_sample_rate)

    def _set_tx_trigger(self, level):
        """Sets the value of the tx_trigger setting."""
        self._ctypes_set(lib.serialfc_set_tx_trigger, level)

    def _get_tx_trigger(self):
        """Gets the value of the tx_trigger setting."""
        return self._ctypes_get_uint(lib.serialfc_get_tx_trigger)

    tx_trigger = property(fset=_set_tx_trigger, fget=_get_tx_trigger)

    def _set_rx_trigger(self, level):
        """Sets the value of the rx_trigger setting."""
        self._ctypes_set(lib.serialfc_set_rx_trigger, level)

    def _get_rx_trigger(self):
        """Gets the value of the rx_trigger setting."""
        return self._ctypes_get_uint(lib.serialfc_get_rx_trigger)

    rx_trigger = property(fset=_set_rx_trigger, fget=_get_rx_trigger)

    def _set_clock_rate(self, rate):
        """Sets the value of the clock_rate setting."""
        self._ctypes_set(lib.serialfc_set_clock_rate, rate)

    clock_rate = property(fset=_set_clock_rate, fget=None)

    def enable_isochronous(self, mode):
        """Enables isochronous mode."""
        self._ctypes_set(lib.serialfc_enable_isochronous, mode)

    def disable_isochronous(self):
        """Disables isochronous mode."""
        self._ctypes_action(lib.serialfc_disable_isochronous)

    def get_isochronous(self):
        """Gets the value of the isochronous setting."""
        return self._ctypes_get_int(lib.serialfc_get_isochronous)

    def enable_external_transmit(self, num_frames):
        """Enables external transmit mode."""
        self._ctypes_set(lib.serialfc_enable_external_transmit, num_frames)

    def disable_external_transmit(self):
        """Disables external transmit mode."""
        self._ctypes_action(lib.serialfc_disable_external_transmit)

    def get_external_transmit(self):
        """Gets the value of the external transmit setting."""
        return self._ctypes_get_uint(lib.serialfc_get_external_transmit)

    def _set_frame_length(self, num_chars):
        """Sets the value of the frame length setting."""
        self._ctypes_set(lib.serialfc_set_frame_length, num_chars)

    def _get_frame_length(self):
        """Gets the value of the frame length setting."""
        return self._ctypes_get_uint(lib.serialfc_get_frame_length)

    frame_length = property(fset=_set_frame_length, fget=_get_frame_length)

    def _set_9bit(self, status):
        """Sets the value of the 9-bit setting."""
        self._ctypes_set_bool(lib.serialfc_enable_9bit,
                              lib.serialfc_disable_9bit,
                              status)

    def _get_9bit(self):
        """Gets the value of the 9-bit setting."""
        return self._ctypes_get_bool(lib.serialfc_get_9bit)

    nine_bit = property(fset=_set_9bit, fget=_get_9bit)

    def enable_fixed_baud_rate(self, rate):
        """Enables fixed baud rate mode."""
        self._ctypes_set(lib.serialfc_enable_fixed_baud_rate, rate)

    def disable_fixed_baud_rate(self):
        """Disables fixed baud rate mode."""
        self._ctypes_action(lib.serialfc_disable_fixed_baud_rate)

    def get_fixed_baud_rate(self):
        """Gets the value of the fixed baud rate setting."""
        return self._ctypes_get_int(lib.serialfc_get_fixed_baud_rate)

    def _get_card_type(self):
        return self._ctypes_get_uint(lib.serialfc_get_card_type)

    _card_type = property(fget=_get_card_type)

    def close(self):
        lib.serialfc_disconnect(self._handle)
        super(Port, self).close()

# This fixes an issue with Windows 10 where the newer implementations 
# of _reconfigure_port fail if the returned GetCommState isn't 
# exactly the same as the sent SetCommState.
# Luckily, the error is thrown at the end, so we can just ignore it
# https://github.com/pyserial/pyserial/issues/362#issue-336855944
    def _reconfigure_port( self, *args, **kwargs ):
        try:
            super()._reconfigure_port( *args, **kwargs )
        except serial.SerialException:
            pass

if __name__ == '__main__':
    if os.name == 'nt':
        p = Port(3)
        #p = Port(28)
    else:
        p = Port(0)

    try:
        print('Termination', p.termination)
    except AttributeError:
        pass

    try:
        print('Isochronous', p.get_isochronous())
    except AttributeError:
        pass

    try:
        print('Frame Length', p.frame_length)
    except AttributeError:
        pass

    try:
        print('External Transmit', p.get_external_transmit())
    except AttributeError:
        pass

    try:
        print('9-Bit', p.nine_bit)
    except AttributeError:
        pass

    print('RS485', p.rs485)
    print('Echo Cancel', p.echo_cancel)
    print('Sample Rate', p.sample_rate)
    print('Tx Trigger', p.tx_trigger)
    print('Rx Trigger', p.rx_trigger)
    print('Card Type', p._card_type)

    try:
        print('Fixed Baud Rate', p.get_fixed_baud_rate())
    except:
        pass

    try:
        p.enable_isochronous(0)
    except AttributeError:
        pass

    try:
        p.disable_isochronous()
    except AttributeError:
        pass

    try:
        p.frame_length = 1
    except AttributeError:
        pass

    try:
        p.enable_external_transmit(1)
    except AttributeError:
        pass

    try:
        p.disable_external_transmit()
    except AttributeError:
        pass

    try:
        p.termination = True
    except AttributeError:
        pass

    try:
        p.nine_bit = False
    except AttributeError:
        pass

    try:
        p.enable_fixed_baud_rate(115200)
    except:
        pass

    try:
        p.disable_fixed_baud_rate()
    except:
        pass

    p.rs485 = False
    p.echo_cancel = False
    p.sample_rate = 16
    p.tx_trigger = 32
    p.rx_trigger = 32
    #p.clock_rate = 18432000

#    p.baudrate = 115200
#    p.write("UUUUU".encode())

    p.close()
