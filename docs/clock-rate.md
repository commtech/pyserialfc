# Clock Rate

###### Code Support
| Code | Version |
| -----| ------- |
| serialfc-windows | 2.1.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | Yes |
| Async-PCIe (17V35X) | Not required |


###### Operating Range
| Card Family | Range |
| ----------- | ----- |
| FSCC (16C950) | 200 Hz - 270 MHz |
| Async-335 (17D15X) | 6 Mhz - 180 Mhz |
| Async-PCIe (17V35X) | Not required |


## Property
```python
card_type = property(...)
```

## Set

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |
| `InvalidParameterError` | `ValueError` | Invalid parameter |

###### Examples
```python
import serialfc
...

# 18.M32 MHz
p.clock_rate = 18432000
```


### Additional Resources
- Complete example: [`examples/clock-rate.py`](../examples/clock-rate.py)
