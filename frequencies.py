"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items = (str(x) for x in items)
    frequencies = {}
    
    for item in items:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    
    return frequencies




  