# Connect

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.0.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.0.0 |


## Connect
```python
def __init__(self, port_num, ttyS=None, serialfc=None)
```


| Exception | Base Exception | Cause |
| ----------- | -----:| ----- |
| `InvalidAccessError` | `OSError` | Insufficient permissions |
| `PortNotFoundError` | `OSError` | Port not found |

###### Examples
Connect to port 3.
```python
import serialfc
...

p = serialfc.Port(0)
```


### Additional Resources
- Complete example: [`examples/tutorial.py`](../examples/tutorial.py)
