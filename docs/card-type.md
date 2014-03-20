# Card Type

###### Code Support
| Code | Version |
| ---- | ------- |
| serialfc-windows | 2.1.6 |
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
_card_type = property(...)
```

## Get
###### Examples
```python
import serialfc
...

type = p._card_type
```


### Additional Resources
- Complete example: [`examples/card-type.py`](../examples/card-type.py)
