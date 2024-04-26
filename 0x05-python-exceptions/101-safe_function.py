#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
<<<<<<< HEAD
        retValue = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
    else:
        return (retValue)
=======
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
