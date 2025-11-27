#!/usr/bin/python3
"""My list"""


class MyList(list):
    """custom list class"""

    def print_sorted(self):
        return self.sort()
