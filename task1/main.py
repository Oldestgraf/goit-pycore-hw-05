def caching_fibonacci():
    """Calculate fibonacci using closure"""

    cache = {} # Create empty dictionary

    def fibonacci(n):

        # Check if value is saved to cache
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Calculate fibonacci value
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
