import re

def generator_numbers(text: str):
    pattern = r"\d+\.\d+"

    for i in re.finditer(pattern, text):
        yield float(i.group())

def sum_profit(text, func):
    numbers_generator = func(text)
    
    return sum(numbers_generator)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(total_income)





















