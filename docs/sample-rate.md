# Sample Rate

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
| FSCC (16C950) | 4 - 16 |
| Async-335 (17D15X) | 8, 16 |
| Async-PCIe (17V35X) | 4, 8, 16 |


## Property
```python
sample_rate = property(...)
```

## Get

###### Examples
```python
import serialfc
...

rate = p.sample_rate
```


## Set

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `InvalidParameterError` | `ValueError` | Invalid parameter |

###### Examples
```python
import serialfc
...

p.sample_rate = 16
```


### Additional Resources
- Complete example: [`examples/sample-rate.py`](../examples/sample-rate.py)
