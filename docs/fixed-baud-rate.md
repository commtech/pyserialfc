# Fixed Baud Rate

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.3.0 |
| serialfc-linux | 2.0.0 |
| pyserialfc | 1.3.0 |

###### Card Support
| Card Family | Supported |
| ----------- |:-----:|
| FSCC (16C950) | Yes |
| Async-335 (17D15X) | Yes |
| Async-PCIe (17V35X) | Yes |


## Get
```python
def get_fixed_baud_rate(self)
```

###### Examples
```python
import serialfc
...

baud_rate = p.get_fixed_baud_rate()
```


## Enable
```python
def enable_fixed_baud_rate(self, rate)
```

###### Examples
```python
import serialfc
...

p.enable_fixed_baud_rate(9600)
```


## Disable
```c
def disable_fixed_baud_rate(self)
```

###### Examples
```python
import serialfc
...

p.disable_fixed_baud_rate()
```


### Additional Resources
- Complete example: [`examples/fixed-baud-rate.py`](../examples/fixed-baud-rate.py)
