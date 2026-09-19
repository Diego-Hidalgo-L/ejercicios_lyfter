
def describe_order(customer_name, *items, **details):
    print(f"Customer: {customer_name}\n")

    print("Items:")
    for item in items:
        print(f"- {item}")
    
    print(f"\nDetails:")
    for key, value in details.items():
        print(f"{key}: {value}")


def main():
    describe_order(
    "Diego",
    "Pizza",
    "Soda",
    "Ice Cream",
    table=5,
    waiter="Carlos"
)


main()