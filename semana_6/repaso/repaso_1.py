
def print_message():
    print("Esta es la primera función.")


def call_first():
    print_message()


def call_second():
    call_first()


call_second()