# Isochronous

If you apply an external clock to the card before turning on isochronous mode your system will freeze due to too many serial interrupts. Make sure and apply the clock after you are the  isochronous mode (so the interrupts are disabled).

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.1.1 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | No |
| Async-PCIe (17V35X) | No |

| Mode | Description |
| ----:| ----------- |
| 0 | Transmit using external RI# |
| 1 | Transmit using internal BRG |
| 2 | Receive using external DSR# |
| 3 | Transmit using external RI#, receive using external DSR# |
| 4 | Transmit using internal BRG, receive using external DSR# |
| 5 | Receive using internal BRG |
| 6 | Transmit using external RI#, receive using internal BRG |
| 7 | Transmit using internal BRG, receive using internal BRG |
| 8 | Transmit and receive using external RI# |
| 9 | Transmit clock is output on DTR# |
| 10 | Transmit clock is output on DTR#, receive using external DSR# |


## Get
```c
def get_isochronous(self)
```

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

mode = p.get_isochronous()
```


## Enable
```c
def enable_external_transmit(self, num_frames)
```

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |
| `InvalidParameterError` | `ValueError` | Invalid parameter |

###### Examples
```python
import serialfc
...

p.enable_isochronous_mode(7)
```


## Disable
```c
def disable_external_transmit(self)
```

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

p.disable_isochronous_mode()
```


### Additional Resources
- Complete example: [`examples/isochronous.py`](../examples/isochronous.py)
