Wrapper for termcolor.py
------------------------

Usage
=====
Call termprint() with the first argument as either:
 * INFO - green bold text
 * WARNING - yellow bold text
 * ERROR - red bold text


Todo: Join color groups together for easier print functions


.. code-block:: python
    from termprint import *
    termprint("INFO", "Green cool text, OK!")
    termprint("WARNING", "Warning text, uhoh!")
    termprint("ERROR", "Error Message")

