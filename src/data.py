class Data:
    def __init__(self, range: str = "0", number_of_primes: int = 0, duration: float = 0.0):
        self.range = range
        self.number_of_primes = number_of_primes
        self.duration = duration

    def update(self, range: str, number_of_primes: int, duration: float):
        self.range = range
        self.number_of_primes = number_of_primes
        self.duration = duration

    def __str__(self):
        return f'{self.range};{self.number_of_primes};{self.duration}'
