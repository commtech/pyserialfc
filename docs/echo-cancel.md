# Echo Cancel

The echo cancel feature disables the receiver while transmitting. This is mainly used in RS485 mode when the transmit and receive lines are tied together. 

_This is a board-wide (as opposed to port-by-port) setting on the Async-335 family of cards._

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


## Property
```python
echo_cancel = property(...)
```

## Get
###### Examples
```python
import serialfc
...

status = p.echo_cancel
```


## Enable
###### Examples
```python
import serialfc
...

p.echo_cancel = True
```


## Disable
###### Examples
```python
import serialfc
...

p.echo_cancel = False
```


### Additional Resources
- Complete example: [`examples/echo-cancel.py`](../examples/echo-cancel.py)
