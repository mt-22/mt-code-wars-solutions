#It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    return [item for item in a if item not in b]