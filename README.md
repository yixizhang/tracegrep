# TraceGrep
-

This is a simple utils to grep Python tracebacks from plain text.


# Install
-

```
pip install tracegrep
```

# Use
-

```python
from tracegrep import tracegrep

sample_text = """
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>>
"""

traces = tracegrep(sample_text)
trace, errortype = traces[0]
trace == """
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
"""
errortype == "ZeroDivisionError"
```