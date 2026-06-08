

def zip_sentence(first, second):
    zipped = ""

    for index in range(len(first)):
        print(f"Pair {index}: {first[index]} {second[index]}")
        
        if index != len(second) - 1:
            zipped += first[index] + " " + second[index] + " "
        else:
            zipped += first[index] + second[index]

    return zipped


def main():
    first = ['The', 'brown', 'jumps', 'the', 'dog']
    second = ['quick', 'fox', 'over', 'lazy', '!']

    zipped = zip_sentence(first, second)

    print(f"\nSentence: {zipped}\n")


main()