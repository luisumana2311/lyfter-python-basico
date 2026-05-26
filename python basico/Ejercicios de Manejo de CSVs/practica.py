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



def save_csv(video_games):
    with open("video_games.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(["name", "genre", "developer", "rating"])
        
        writer.writerows(video_games)
    
    print("\nCSV file created successfully ✔")



def main():
    data = get_video_games()
    save_csv(data)



main()