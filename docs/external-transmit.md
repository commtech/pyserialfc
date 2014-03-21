# External Transmit

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.1.5 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | No |
| Async-PCIe (17V35X) | No |

###### Operating Range
| Card Family | Range |
| ----------- | ----- |
| FSCC (16C950) | 0 - 8191 |



## Get
```python
def get_external_transmit(self)
```

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

num_frames = p.get_external_transmit()
```


## Enable
```python
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

p.enable_external_transmit(4)
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

p.disable_external_transmit()
```


### Additional Resources
- Complete example: [`examples/external-transmit.py`](../examples/external-transmit.py)
