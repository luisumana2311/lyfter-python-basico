def open_and_print_files(file_path):
    songs = []
    with open(file_path) as file:
        for line in file:
            songs.append(line.strip())
    return songs


def sort_songs(songs):
    songs.sort()
    return songs


def write_file(file_path, songs):
    with open(file_path, "w") as file:
        for song in songs:
            file.write(song + "\n")


def main():
    songs = open_and_print_files("songs.txt")
    sorted_songs = sort_songs(songs)
    write_file("sorted_songs.txt", sorted_songs)


if __name__ == "__main__":
    main()