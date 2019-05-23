#!/usr/bin/env python3

import re
from collections import Counter


def count_letters(searchstring):
    """search a string for letters contained in pattern

    Args:
      searchstring (str): string being searched

    Returns:
      list: containing tuples of a letter and its count

    Notes:
    """
    letter_list = re.findall(r'\S', searchstring)
    return Counter(letter_list)
