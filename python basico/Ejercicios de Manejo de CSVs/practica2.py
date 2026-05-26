import csv


def get_video_games():
    video_games = []
    
    n = int(input("Enter the number of video games: "))
    
    for i in range(n):
        print(f"\nVideo Game #{i+1}")
        
        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        rating = input("ESRB Rating: ")
        
        video_games.append([name, genre, developer, rating])
    
    return video_games


def save_tsv(video_games):
    with open("video_games.tsv", "w", newline="", encoding="utf-8") as file:
        
        # Key change: tab delimiter
        writer = csv.writer(file, delimiter="\t")
        
        # header
        writer.writerow(["name", "genre", "developer", "rating"])
        
        # data
        writer.writerows(video_games)
    
    print("\nTSV file created successfully ✔")



def main():
    data = get_video_games()
    save_tsv(data)



main()