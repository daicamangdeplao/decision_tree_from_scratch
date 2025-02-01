import numpy as np

one_list_warning = "One argument is a list"
two_lists_warning = "Both arguments are lists, not arrays"

def custom_sum(arg1, arg2):
    if isinstance(arg1, type([])) and isinstance(arg2, type([])):
        return two_lists_warning
    if isinstance(arg1, type([])) or isinstance(arg2, type([])):
        return one_list_warning
    return arg1 + arg2
