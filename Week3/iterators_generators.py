# iterators_generators.py

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

import random

def random_number_generator(low, high, count):
    for _ in range(count):
        yield random.randint(low, high)

def main():
    # Demonstrate Countdown iterator
    print("Counting down from 5:")
    countdown_iterator = Countdown(5)
    for num in countdown_iterator:
        print(num, end=' ')
    print()

    # Demonstrate Fibonacci generator
    print("\nFibonacci numbers up to 100:")
    for fib in fibonacci_generator(100):
        print(fib, end=' ')
    print()

    # Demonstrate random number generator
    print("\nRandom numbers between 1 and 10:")
    for num in random_number_generator(1, 10, 5):
        print(num, end=' ')
    print()

if __name__ == "__main__":
    main()
