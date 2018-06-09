import sys  # provides getsizeof function

data = []
n = 26

for k in range(n):  # NOTE : must fix choice of n
    a = len(data)   # number of elements
    b = sys.getsizeof(data)  # actual sixe in bytes
    print('Length : {0:3d}; size in bytes : {1:4d}'.format(a, b))
    data.append(None)  # increase length by one

"""

OUTPUT :

Length :   0; size in bytes :   72
Length :   1; size in bytes :  104
Length :   2; size in bytes :  104
Length :   3; size in bytes :  104
Length :   4; size in bytes :  104
Length :   5; size in bytes :  136
Length :   6; size in bytes :  136
Length :   7; size in bytes :  136
Length :   8; size in bytes :  136
Length :   9; size in bytes :  200
Length :  10; size in bytes :  200
Length :  11; size in bytes :  200
Length :  12; size in bytes :  200
Length :  13; size in bytes :  200
Length :  14; size in bytes :  200
Length :  15; size in bytes :  200
Length :  16; size in bytes :  200
Length :  17; size in bytes :  272
Length :  18; size in bytes :  272
Length :  19; size in bytes :  272
Length :  20; size in bytes :  272
Length :  21; size in bytes :  272
Length :  22; size in bytes :  272
Length :  23; size in bytes :  272
Length :  24; size in bytes :  272
Length :  25; size in bytes :  272
"""
