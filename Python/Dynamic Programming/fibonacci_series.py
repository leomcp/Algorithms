def fibonacci(n):
    """Return the nth Fibonacci number."""
    # r[i] will contain the ith Fibonacci number
    r = [-1]*(n + 1)
    return fibonacci_helper(n, r)
 
 
def fibonacci_helper(n, r):
    """Return the nth Fibonacci number and store the ith Fibonacci number in
    r[i] for 0 <= i <= n."""
    if r[n] >= 0:
        return r[n]
 
    if (n == 0 or n == 1):
        q = n
    else:
        q = fibonacci_helper(n - 1, r) + fibonacci_helper(n - 2, r)
    r[n] = q
 
    return q
 
 
n = int(input('Enter n: '))
 
ans = fibonacci(n)
print('The nth Fibonacci number:', ans)