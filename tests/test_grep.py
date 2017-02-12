import unittest

import tracegrep


SAMPLE_TEXT = """
>>> import re
>>> re.match(r'(\t)+', "                ")
<_sre.SRE_Match object at 0x10a41ec60>
>>> re.findall(r'(\t)+', "              ")
['\t']
>>> re.findall(r'\t+', "                ")
['\t\t']
>>> re.findall(r'\t+', "        ")
['\t']
>>> re.findall(r'\t+', "        1")
['\t']
>>> re.findall(r' {2}+', "  ")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 181, in findall
    return _compile(pattern, flags).findall(string)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 251, in _compile
    raise error, v # invalid expression
sre_constants.error: multiple repeat
>>> re.findall(r'( {2})+', "  ")
['  ']
>>> re.findall(r'( {2})+', " ")
[]
>>> re.findall(r'( {2})+', "  ")
['  ']
>>> re.findall(r'( {2})+', "   ")
['  ']
>>> "           ".lstrip("\t")
''
>>> "            ".lstrip("\t")
' '
>>>
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>>
"""


class TraceGrepTestSuite(unittest.TestCase):
    """TraceGrep test cases."""

    def test_grep(self):
        traces = tracegrep.grep(SAMPLE_TEXT)

        self.assertEqual(len(traces), 2)
        ta, tb = traces
        _, tae = ta
        self.assertEqual(tae, "sre_constants.error")
        _, tbe = tb
        self.assertEqual(tbe, "ZeroDivisionError")


if __name__ == '__main__':
    unittest.main()
