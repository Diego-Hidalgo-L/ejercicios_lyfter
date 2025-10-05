
def input_student_to_delete():
    student_to_delete = input("Enter the name of the student's info you want to delete: ")

    return student_to_delete

def ask_for_confirmation(student_to_delete):
    while True:
        confirm = input(f"Are you sure you want to delete {student_to_delete}'s information? Yes or No: ").upper()

        if confirm in ("YES", "NO"):
            if confirm == "YES":
                print(f"\n{student_to_delete}'s information was deleted from the database.")
                break
            elif confirm == "NO":
                print("\nThen what the fuck?\n")
        else:
            print("\nInvalid answer. Please answer either Yes or No.\n")


def main():
    student_to_delete = input_student_to_delete()
    ask_for_confirmation(student_to_delete)


main()