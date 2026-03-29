
def count_occurrences(main_str, sub_str):
    index = 0
    count = 0
    main_str = main_str.lower()
    sub_str = sub_str.lower()
    while (index := main_str.find(sub_str, index)) != -1: 
        index += 1
        count +=1
    return count

print(count_occurrences("hello world Hello", "hello"))