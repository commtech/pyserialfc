# Frame Length

The frame length specifies the number of bytes that get transmitted between the start and stop bits. The standard asynchronous serial communication protocol uses a frame length of one.

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


## Property
```python
frame_length = property(...)
```

## Get

| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `AttributeError` | | Not supported on this family of cards |

###### Examples
```python
import serialfc
...

frame_length = p.frame_length
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

p.frame_length = 4
```


### Additional Resources
- Complete example: [`examples/frame-length.py`](../examples/frame-length.py)
