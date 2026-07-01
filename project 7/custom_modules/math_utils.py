def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def power(base, exponent):
    return base ** exponent


def square_root(number):
    return number ** 0.5


if __name__ == "__main__":
    print(km_to_miles(10))
    print(celsius_to_fahrenheit(100))
    print(power(2, 10))
    print(square_root(81))
