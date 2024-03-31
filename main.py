from greeter import Greeter
from planet import Planet


def start_program():
    # Create a Greeter object
    greeter = Greeter(input("What is your name?: "))

    # Use the inner function through a public method
    print(greeter.greet())  # Friendly greeting
    print(greeter.greet("formal"))  # Formal greeting

    planet = Planet()
    planet.handle()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_program()
