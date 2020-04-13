def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter

if __name__ == '__main__':
    print(transmit_to_space("Test"))