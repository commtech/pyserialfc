import serial
import os
import struct

if os.name == 'nt':
    import win32file
else:
    import fcntl
    import errno


if os.name == 'nt':
    METHOD_BUFFERED = 0
    FILE_ANY_ACCESS = 0

    def CTL_CODE(DeviceType, Function, Method=METHOD_BUFFERED,
                 Access=FILE_ANY_ACCESS):
        return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method

    SERIALFC_IOCTL_MAGIC = 0x8019

    IOCTL_FASTCOM_ENABLE_RS485 = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x800)
    IOCTL_FASTCOM_DISABLE_RS485 = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x801)
    IOCTL_FASTCOM_GET_RS485 = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x802)

    IOCTL_FASTCOM_ENABLE_ECHO_CANCEL = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x803)
    IOCTL_FASTCOM_DISABLE_ECHO_CANCEL = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x804)
    IOCTL_FASTCOM_GET_ECHO_CANCEL = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x805)

    IOCTL_FASTCOM_ENABLE_TERMINATION = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x806)
    IOCTL_FASTCOM_DISABLE_TERMINATION = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x807)
    IOCTL_FASTCOM_GET_TERMINATION = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x808)

    IOCTL_FASTCOM_SET_SAMPLE_RATE = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x809)
    IOCTL_FASTCOM_GET_SAMPLE_RATE = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80A)

    IOCTL_FASTCOM_SET_TX_TRIGGER = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80B)
    IOCTL_FASTCOM_GET_TX_TRIGGER = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80C)

    IOCTL_FASTCOM_SET_RX_TRIGGER = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80D)
    IOCTL_FASTCOM_GET_RX_TRIGGER = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80E)

    IOCTL_FASTCOM_SET_CLOCK_RATE = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x80F)

    IOCTL_FASTCOM_ENABLE_ISOCHRONOUS = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x810)
    IOCTL_FASTCOM_DISABLE_ISOCHRONOUS = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x811)
    IOCTL_FASTCOM_GET_ISOCHRONOUS = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x812)

    IOCTL_FASTCOM_ENABLE_EXTERNAL_TRANSMIT = CTL_CODE(SERIALFC_IOCTL_MAGIC,
                                                      0x813)
    IOCTL_FASTCOM_DISABLE_EXTERNAL_TRANSMIT = CTL_CODE(SERIALFC_IOCTL_MAGIC,
                                                       0x814)
    IOCTL_FASTCOM_GET_EXTERNAL_TRANSMIT = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x815)

    IOCTL_FASTCOM_SET_FRAME_LENGTH = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x816)
    IOCTL_FASTCOM_GET_FRAME_LENGTH = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x817)

    IOCTL_FASTCOM_GET_CARD_TYPE = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x818)

    IOCTL_FASTCOM_ENABLE_9BIT = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x819)
    IOCTL_FASTCOM_DISABLE_9BIT = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x81A)
    IOCTL_FASTCOM_GET_9BIT = CTL_CODE(SERIALFC_IOCTL_MAGIC, 0x81B)
else:
    IOCPARM_MASK = 0x7f
    IO_NONE = 0x00000000
    IO_WRITE = 0x40000000
    IO_READ = 0x80000000

    def FIX(x):
        return struct.unpack("i", struct.pack("I", x))[0]

    def _IO(x, y):
        return FIX(IO_NONE | (x << 8) | y)

    def _IOR(x, y, t):
        return FIX(IO_READ | ((t & IOCPARM_MASK) << 16) | (x << 8) | y)

    def _IOW(x, y, t):
        return FIX(IO_WRITE | ((t & IOCPARM_MASK) << 16) | (x << 8) | y)

    def _IOWR(x, y, t):
        return FIX(IO_READ | IO_WRITE | ((t & IOCPARM_MASK) << 16) |
                   (x << 8) | y)

    SERIALFC_IOCTL_MAGIC = 0x19

    IOCTL_FASTCOM_ENABLE_RS485 = _IO(SERIALFC_IOCTL_MAGIC, 0)
    IOCTL_FASTCOM_DISABLE_RS485 = _IO(SERIALFC_IOCTL_MAGIC, 1)
    IOCTL_FASTCOM_GET_RS485 = _IOR(SERIALFC_IOCTL_MAGIC, 2,
                                   struct.calcsize("P"))

    IOCTL_FASTCOM_ENABLE_ECHO_CANCEL = _IO(SERIALFC_IOCTL_MAGIC, 3)
    IOCTL_FASTCOM_DISABLE_ECHO_CANCEL = _IO(SERIALFC_IOCTL_MAGIC, 4)
    IOCTL_FASTCOM_GET_ECHO_CANCEL = _IOR(SERIALFC_IOCTL_MAGIC, 5,
                                         struct.calcsize("P"))

    IOCTL_FASTCOM_ENABLE_TERMINATION = _IO(SERIALFC_IOCTL_MAGIC, 6)
    IOCTL_FASTCOM_DISABLE_TERMINATION = _IO(SERIALFC_IOCTL_MAGIC, 7)
    IOCTL_FASTCOM_GET_TERMINATION = _IOR(SERIALFC_IOCTL_MAGIC, 8,
                                         struct.calcsize("P"))

    IOCTL_FASTCOM_SET_SAMPLE_RATE = _IOW(SERIALFC_IOCTL_MAGIC, 9,
                                         struct.calcsize("i"))
    IOCTL_FASTCOM_GET_SAMPLE_RATE = _IOR(SERIALFC_IOCTL_MAGIC, 10,
                                         struct.calcsize("P"))

    IOCTL_FASTCOM_SET_TX_TRIGGER = _IOW(SERIALFC_IOCTL_MAGIC, 11,
                                        struct.calcsize("i"))
    IOCTL_FASTCOM_GET_TX_TRIGGER = _IOR(SERIALFC_IOCTL_MAGIC, 12,
                                        struct.calcsize("P"))

    IOCTL_FASTCOM_SET_RX_TRIGGER = _IOW(SERIALFC_IOCTL_MAGIC, 13,
                                        struct.calcsize("i"))
    IOCTL_FASTCOM_GET_RX_TRIGGER = _IOR(SERIALFC_IOCTL_MAGIC, 14,
                                        struct.calcsize("P"))

    IOCTL_FASTCOM_SET_CLOCK_RATE = _IOW(SERIALFC_IOCTL_MAGIC, 15,
                                        struct.calcsize("i"))

    IOCTL_FASTCOM_ENABLE_ISOCHRONOUS = _IOW(SERIALFC_IOCTL_MAGIC, 16,
                                            struct.calcsize("i"))
    IOCTL_FASTCOM_DISABLE_ISOCHRONOUS = _IO(SERIALFC_IOCTL_MAGIC, 17)
    IOCTL_FASTCOM_GET_ISOCHRONOUS = _IOR(SERIALFC_IOCTL_MAGIC, 18,
                                         struct.calcsize("P"))

    IOCTL_FASTCOM_ENABLE_EXTERNAL_TRANSMIT = _IOW(SERIALFC_IOCTL_MAGIC, 19,
                                                  struct.calcsize("i"))
    IOCTL_FASTCOM_DISABLE_EXTERNAL_TRANSMIT = _IO(SERIALFC_IOCTL_MAGIC, 20)
    IOCTL_FASTCOM_GET_EXTERNAL_TRANSMIT = _IOR(SERIALFC_IOCTL_MAGIC, 21,
                                               struct.calcsize("P"))

    IOCTL_FASTCOM_SET_FRAME_LENGTH = _IOW(SERIALFC_IOCTL_MAGIC, 22,
                                          struct.calcsize("i"))
    IOCTL_FASTCOM_GET_FRAME_LENGTH = _IOR(SERIALFC_IOCTL_MAGIC, 23,
                                          struct.calcsize("P"))

    IOCTL_FASTCOM_GET_CARD_TYPE = _IOR(SERIALFC_IOCTL_MAGIC, 24,
                                       struct.calcsize("P"))

CARD_TYPE_PCI, CARD_TYPE_PCIe, CARD_TYPE_FSCC, CARD_TYPE_UNKNOWN = range(4)


NOT_SUPPORTED_TEXT = 'This feature isn\'t supported on this port.'


class Port(serial.Serial):

    def __init__(self, ttyS, serialfc=None):
        super(Port, self).__init__(ttyS)

        if serialfc:
            self.fd = open(serialfc)

    def _ioctl_set_boolean(self, ioctl_enable, ioctl_disable, value):
        ioctl_name = ioctl_enable if value else ioctl_disable

        if os.name == 'nt':
            try:
                win32file.DeviceIoControl(self.hComPort, ioctl_name, None, 0, None)
            except win32file.error as e:
                if e.winerror == 50:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise
        else:
            try:
                fcntl.ioctl(self.fd, ioctl_name)
            except IOError as e:
                if e.errno == errno.EPROTONOSUPPORT:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise

    def _ioctl_get_boolean(self, ioctl_name):
        if os.name == 'nt':
            buf_size = struct.calcsize("?")
            try:
                buf = win32file.DeviceIoControl(self.hComPort, ioctl_name,
                                                None, buf_size, None)
            except win32file.error as e:
                if e.winerror == 50:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise
        else:
            try:
                buf = fcntl.ioctl(self.fd, ioctl_name, struct.pack("?", 0))
            except IOError as e:
                if e.errno == errno.EPROTONOSUPPORT:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise

        value = struct.unpack("?", buf)

        return True if value[0] else False

    def _ioctl_set_integer(self, ioctl_name, value):
        if os.name == 'nt':
            try:
                value = struct.pack("I", value)
                win32file.DeviceIoControl(self.hComPort, ioctl_name, value, 0,
                                          None)
            except win32file.error as e:
                if e.winerror == 50:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                elif e.winerror == 87:
                    raise ValueError("The argument is out of range.")
                else:
                    raise
        else:
            try:
                fcntl.ioctl(self.fd, ioctl_name, value)
            except IOError as e:
                if e.errno == errno.EPROTONOSUPPORT:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                elif e.errno == errno.EINVAL:
                    raise ValueError("The argument is out of range.")
                else:
                    raise

    def _ioctl_get_integer(self, ioctl_name, fmt='i'):
        if os.name == 'nt':
            buf_size = struct.calcsize(fmt)
            try:
                buf = win32file.DeviceIoControl(self.hComPort, ioctl_name, None,
                                                buf_size, None)
            except win32file.error as e:
                if e.winerror == 50:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise
        else:
            try:
                buf = fcntl.ioctl(self.fd, ioctl_name, struct.pack(fmt, 0))
            except IOError as e:
                if e.errno == errno.EPROTONOSUPPORT:
                    raise AttributeError(NOT_SUPPORTED_TEXT)
                else:
                    raise

        value = struct.unpack(fmt, buf)
        return value[0]

    def _ioctl_get_unsigned_integer(self, ioctl_name):
        return self._ioctl_get_integer(self, ioctl_name, 'I')

    def _set_rs485(self, status):
        """Sets the value of the rs485 setting."""
        self._ioctl_set_boolean(IOCTL_FASTCOM_ENABLE_RS485,
                                IOCTL_FASTCOM_DISABLE_RS485,
                                status)

    def _get_rs485(self):
        """Gets the value of the rs485 setting."""
        return self._ioctl_get_boolean(IOCTL_FASTCOM_GET_RS485)

    rs485 = property(fset=_set_rs485, fget=_get_rs485)

    def _set_echo_cancel(self, status):
        """Sets the value of the echo_cancel setting."""
        self._ioctl_set_boolean(IOCTL_FASTCOM_ENABLE_ECHO_CANCEL,
                                IOCTL_FASTCOM_DISABLE_ECHO_CANCEL,
                                status)

    def _get_echo_cancel(self):
        """Gets the value of the echo_cancel setting."""
        return self._ioctl_get_boolean(IOCTL_FASTCOM_GET_ECHO_CANCEL)

    echo_cancel = property(fset=_set_echo_cancel, fget=_get_echo_cancel)

    def _set_termination(self, status):
        """Sets the value of the termination setting."""
        self._ioctl_set_boolean(IOCTL_FASTCOM_ENABLE_TERMINATION,
                                IOCTL_FASTCOM_DISABLE_TERMINATION,
                                status)

    def _get_termination(self):
        """Gets the value of the termination setting."""
        return self._ioctl_get_boolean(IOCTL_FASTCOM_GET_TERMINATION)

    termination = property(fset=_set_termination, fget=_get_termination)

    def _set_sample_rate(self, rate):
        """Sets the value of the sample_rate setting."""
        self._ioctl_set_integer(IOCTL_FASTCOM_SET_SAMPLE_RATE, rate)

    def _get_sample_rate(self):
        """Gets the value of the sample_rate setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_SAMPLE_RATE)

    sample_rate = property(fset=_set_sample_rate, fget=_get_sample_rate)

    def _set_tx_trigger(self, level):
        """Sets the value of the tx_trigger setting."""
        self._ioctl_set_integer(IOCTL_FASTCOM_SET_TX_TRIGGER, level)

    def _get_tx_trigger(self):
        """Gets the value of the tx_trigger setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_TX_TRIGGER)

    tx_trigger = property(fset=_set_tx_trigger, fget=_get_tx_trigger)

    def _set_rx_trigger(self, level):
        """Sets the value of the rx_trigger setting."""
        self._ioctl_set_integer(IOCTL_FASTCOM_SET_RX_TRIGGER, level)

    def _get_rx_trigger(self):
        """Gets the value of the rx_trigger setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_RX_TRIGGER)

    rx_trigger = property(fset=_set_rx_trigger, fget=_get_rx_trigger)

    def _set_clock_rate(self, rate):
        """Sets the value of the clock_rate setting."""
        self._ioctl_set_integer(IOCTL_FASTCOM_SET_CLOCK_RATE, rate)

    clock_rate = property(fset=_set_clock_rate, fget=None)

    def enable_isochronous(self, mode):
        """Enables isochronous mode."""
        self._ioctl_set_integer(IOCTL_FASTCOM_ENABLE_ISOCHRONOUS, mode)

    def disable_isochronous(self):
        """Disables isochronous mode."""
        self._ioctl_set_boolean(IOCTL_FASTCOM_ENABLE_ISOCHRONOUS,
                                IOCTL_FASTCOM_DISABLE_ISOCHRONOUS,
                                False)

    def get_isochronous(self):
        """Gets the value of the isochronous setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_ISOCHRONOUS)

    def enable_external_transmit(self, num_frames):
        """Enables external transmit mode."""
        self._ioctl_set_integer(IOCTL_FASTCOM_ENABLE_EXTERNAL_TRANSMIT,
                                num_frames)

    def disable_external_transmit(self):
        """Disables external transmit mode."""
        self._ioctl_set_boolean(IOCTL_FASTCOM_ENABLE_EXTERNAL_TRANSMIT,
                                IOCTL_FASTCOM_DISABLE_EXTERNAL_TRANSMIT,
                                False)

    def get_external_transmit(self):
        """Gets the value of the external transmit setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_EXTERNAL_TRANSMIT)

    def _set_frame_length(self, num_chars):
        """Sets the value of the frame length setting."""
        self._ioctl_set_integer(IOCTL_FASTCOM_SET_FRAME_LENGTH, num_chars)

    def _get_frame_length(self):
        """Gets the value of the frame length setting."""
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_FRAME_LENGTH)

    frame_length = property(fset=_set_frame_length, fget=_get_frame_length)

    def _set_9bit(self, status):
        """Sets the value of the 9-bit setting."""
        if status:
            win32file.DeviceIoControl(self.hComPort, IOCTL_FASTCOM_ENABLE_9BIT, None, 0, None)
        else:
            win32file.DeviceIoControl(self.hComPort, IOCTL_FASTCOM_DISABLE_9BIT, None, 0, None)

    def _get_9bit(self):
        """Gets the value of the 9-bit setting."""
        buf_size = struct.calcsize("?")
        buf = win32file.DeviceIoControl(self.hComPort, IOCTL_FASTCOM_GET_9BIT, None, buf_size, None)
        value = struct.unpack("?", buf)

        if (value[0]):
            return True
        else:
            return False

    nine_bit = property(fset=_set_9bit, fget=_get_9bit)

    def _get_card_type(self):
        return self._ioctl_get_integer(IOCTL_FASTCOM_GET_CARD_TYPE)

    _card_type = property(fget=_get_card_type)

if __name__ == '__main__':
    if os.name == 'nt':
        p = Port('COM3')
    else:
        p = Port('/dev/ttyS4', '/dev/serialfc0')

    try:
        print("Termination", p.termination)
    except AttributeError as e:
        pass

    try:
        print("Isochronous", p.get_isochronous())
    except AttributeError as e:
        pass

    try:
        print("Frame Length", p.frame_length)
    except AttributeError as e:
        pass

    try:
        print("External Transmit", p.get_external_transmit())
    except AttributeError as e:
        pass

    print("RS485", p.rs485)
    print("Echo Cancel", p.echo_cancel)
    print("Sample Rate", p.sample_rate)
    print("Tx Trigger", p.tx_trigger)
    print("Rx Trigger", p.rx_trigger)
    print("Card Type", p._card_type)

    try:
        p.disable_isochronous()
    except AttributeError as e:
        pass

    try:
        p.frame_length = 1
    except AttributeError as e:
        pass

    try:
        p.disable_external_transmit()
    except AttributeError as e:
        pass

    try:
        p.termination = True
    except AttributeError as e:
        pass

    p.rs485 = False
    p.echo_cancel = False
    p.sample_rate = 16
    p.tx_trigger = 32
    p.rx_trigger = 32

#    p.baudrate = 115200
#    p.write("UUUUU".encode())
