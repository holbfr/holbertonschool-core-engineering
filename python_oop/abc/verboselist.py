#!/usr/bin/env python3
"""
Simple module for task validation
"""


class VerboseList(list):
    """VerboseList class definition"""

    def append(self, item):
        """Redifinition of the append method"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Redefinition of the extend method"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Redefinition of the remove method"""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=None):
        """Redefinition of the pop method"""
        if item is None:
            deleted_item = super().pop()
        else:
            deleted_item = super().pop(item)
        print("Popped [{}] from the list.".format(deleted_item))
        return deleted_item
