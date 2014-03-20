# TX Trigger Level

The TX FIFO trigger level generates an interrupt whenever the data level in the transmit FIFO falls below this preset trigger level.

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.0.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | Yes |
| Async-PCIe (17V35X) | Yes |

###### Operating Range
| Card Family | Range |
| ----------- | ----- |
| FSCC (16C950) | 0 - 127 |
| Async-335 (17D15X) | 0 - 64 |
| Async-PCIe (17V35X) | 0 - 255 |


## Property
```python
rx_trigger = property(...)
```

## Get

###### Examples
```python
import serialfc
...

level = p.rx_trigger
```


## Set

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `InvalidParameterError` | `ValueError` | Invalid parameter |

###### Examples
```python
import serialfc
...

p.rx_trigger = 32
```


### Additional Resources
- Complete example: [`examples/tx-trigger.py`](../examples/tx-trigger.py)
