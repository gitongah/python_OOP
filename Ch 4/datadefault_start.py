# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,48))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)

# b1 = Book()
# print(b1)

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rey", "Leo Tolstoy", 1225)

print(b1)
print(b2)