
def write_songs_to_file(path, text):
    with open(path, 'w') as file:
        file.write(text)


def open_file_and_create_raw_list(path):
	raw_list = []
	with open(path, encoding="utf-8") as file:
		for line in file.readlines():
			raw_list.append(line)
	return raw_list


def sort_list(raw_list):
	raw_list.sort()
	return raw_list


def convert_list_to_string(sorted_list):
	new_string = ""
	for song in sorted_list:
		new_string += song
	return new_string


# Solución de ChatGPT para tener todo en líneas separadas:

# def convert_list_to_string(sorted_list):
	# return "".join(f"{song.rstrip('\r\n')}\n" for song in sorted_list)


def create_and_write_new_file(new_path, new_string):
	with open(new_path, 'w') as file:
		file.write(new_string)


text_to_write = """
Paranoid
N.I.B.
Iron Man
Sabbath, Bloody Sabbath
Planet Caravan
Hand of Doom
Electric Funeral
"""


def main():
	write_songs_to_file("songs.txt", text_to_write)
	raw_list = open_file_and_create_raw_list('songs.txt')
	sorted_list = sort_list(raw_list)
	new_string = convert_list_to_string(sorted_list)
	create_and_write_new_file("songs_new.txt", new_string)


main()