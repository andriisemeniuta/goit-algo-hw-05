def caching_fibonacci():
    # Ініціалізую порожній кеш 
    cache = {}

    def fibonacci(n):
        # Базові випадки рекурсії
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Перевірка, чи є результат у кеші
        if n in cache:
            return cache[n]
        
        # Обчислюю та зберігаю результат у кеш 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаю функцію 
    return fibonacci

# Створюю екземпляр функції 
fib = caching_fibonacci()

# Перевіряю
print(fib(9))  # 34
print(fib(9))  # 34













