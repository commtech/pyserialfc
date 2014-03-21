# Termination

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.0.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | No |
| Async-335 (17D15X) | No |
| Async-PCIe (17V35X) | Yes |


## Property
```python
termination = property(...)
```

## Get

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

status = p.termination
```


## Enable

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

p.termination = True
```


## Disable

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

p.termination = False
```


### Additional Resources
- Complete example: [`examples/termination.py`](../examples/termination.py)
