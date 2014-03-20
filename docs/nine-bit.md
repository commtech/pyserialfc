# 9-Bit Protocol

Enabling 9-Bit protocol has a couple of effects.

- Transmitting with 9-bit protocol enabled automatically sets the 1st byte's 9th bit to MARK, and all remaining bytes's 9th bits to SPACE.
- Receiving with 9-bit protocol enabled will return two bytes per each 9-bits of data. The second of each byte-duo contains the 9th bit.

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.2.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.1.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | No |
| Async-PCIe (17V35X) | No |


## Property
```python
nine_bit = property(...)
```

## Get

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

status = p.nine_bit
```


## Enable

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

p.nine_bit = True
```


## Disable

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

p.nine_bit = False
```


### Additional Resources
- Complete example: [`examples/nine-bit.py`](../examples/nine-bit.py)
