import datetime

def save_mood(mood):
    with open("mood_log.txt", "a") as file:
        today = datetime.date.today()
        file.write(f"{today} - Mood: {mood}\n")
    print("Your mood has been saved. Thank you!")

def show_history():
    try:
        with open("mood_log.txt", "r") as file:
            print("\nMood History:")
            print(file.read())
    except FileNotFoundError:
        print("No mood history found.")

def main():
    print("Welcome to the Daily Mood Tracker!")
    while True:
        print("\nChoose an option:")
        print("1. Enter today's mood")
        print("2. View mood history")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            mood = input("How are you feeling today? ")
            save_mood(mood)
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
