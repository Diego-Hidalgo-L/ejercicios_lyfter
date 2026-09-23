
def write_songs_file(file_path, songs_input):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(songs_input.strip())


def read_songs_file(file_path):
    raw_list = []

    with open(file_path, encoding='utf-8') as file:
        for line in file:
            raw_list.append(line.strip())
    
    return raw_list


def sort_raw_list(raw_list):
    for outer_index in range(len(raw_list) - 1):
        has_made_changes = False

        for index in range(len(raw_list) - outer_index - 1):
            current_element = raw_list[index]
            next_element = raw_list[index + 1]

            if current_element > next_element:
                raw_list[index] = next_element
                raw_list[index + 1] = current_element
                has_made_changes = True
        
        if not has_made_changes:
            break
    
    return raw_list


def write_songs_sorted_file(file_path, sorted_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for song in sorted_list:
            file.write(song + "\n")


def read_songs_sorted_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            print(line.strip())


def write_songs_reversed(file_path, sorted_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index in range(len(sorted_list) -1, -1, -1):
            file.write(sorted_list[index] + '\n')


def main():
    songs_input = """
For Whom the Bell Tolls
Chameleon Paint
You Let My Tyres Down
Virou Lágrimas
Te Gosto
Para Machucar Meu Coração
Leãozinho
¿Por qué será?
"""

    write_songs_file("semana_18/ejercicios/file_handling/exercise_1/songs_input.txt", songs_input)
    raw_list = read_songs_file("semana_18/ejercicios/file_handling/exercise_1/songs_input.txt")
    sorted_list = sort_raw_list(raw_list)
    write_songs_sorted_file("semana_18/ejercicios/file_handling/exercise_1/songs_sorted.txt", sorted_list)
    write_songs_reversed("semana_18/ejercicios/file_handling/exercise_1/songs_reversed.txt", sorted_list)

    print("\nSorted list:")
    read_songs_sorted_file("semana_18/ejercicios/file_handling/exercise_1/songs_sorted.txt")

main()
