# Program: Countries Visited Manager with Inheritance
# Author: Kaylan Chase

# Base class
class Country:
    def __init__(self, name, visited=False):
        self.name = name.title()
        self.visited = visited

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def __str__(self):
        status = "Visited" if self.visited else "Not Visited"
        return f"{self.name} ({status})"


# Subclass (inherits from Country)
class FavoriteCountry(Country):
    def __init__(self, name, rating, reason):
        super().__init__(name, visited=True)  # Always marked visited
        self.rating = rating
        self.reason = reason

    # Override __str__ to include favorite info
    def __str__(self):
        return f"{self.name} - Rating: {self.rating}/10 | Reason: {self.reason}"


# Manages all countries
class TravelTracker:
    def __init__(self):
        self.countries = [
            Country("USA"), Country("Canada"), Country("France"),
            Country("Japan"), Country("Brazil"), Country("Mexico", True)
        ]
        self.favorite_countries = []  # New list for favorites

    def show_countries(self):
        print("\nVisited Countries:")
        for c in self.countries:
            if c.visited:
                print(f" - {c.name}")
        print("\nNot Visited Yet:")
        for c in self.countries:
            if not c.visited:
                print(f" - {c.name}")

    def mark_as_visited(self, name):
        for c in self.countries:
            if c.name == name.title():
                c.mark_visited()
                print(f"{c.name} marked as visited.")
                return
        print("Country not found.")

    def reset(self):
        for c in self.countries:
            c.mark_unvisited()
        self.countries[-1].mark_visited()
        print("Lists have been reset!")

    def add_country(self, name):
        if any(c.name == name.title() for c in self.countries):
            print("That country already exists.")
        else:
            self.countries.append(Country(name))
            print(f"{name.title()} added to list.")

    # New: Add a favorite country
    def add_favorite_country(self, name, rating, reason):
        fav = FavoriteCountry(name, rating, reason)
        self.favorite_countries.append(fav)
        print(f"{name.title()} added as a favorite country!")

    # New: Show all favorite countries
    def show_favorite_countries(self):
        if not self.favorite_countries:
            print("\nNo favorite countries yet.")
        else:
            print("\nFavorite Countries:")
            for fav in self.favorite_countries:
                print(f" - {fav}")


# Main program loop
tracker = TravelTracker()

while True:
    print("\n=== Countries Menu ===")
    print("1. Mark a country as visited")
    print("2. Reset country lists")
    print("3. Add a new country")
    print("4. Show all countries")
    print("5. Quit")
    print("6. Add a favorite country")  # new option
    print("7. Show favorite countries") # new option

    choice = input("Enter your choice (1–7): ").strip()

    if choice == "1":
        name = input("Enter country name: ")
        tracker.mark_as_visited(name)
    elif choice == "2":
        tracker.reset()
    elif choice == "3":
        name = input("Enter new country: ")
        tracker.add_country(name)
    elif choice == "4":
        tracker.show_countries()
    elif choice == "5":
        print("Goodbye!")
        break
    elif choice == "6":
        name = input("Enter country name: ")
        rating = input("Enter your rating (1–10): ")
        reason = input("Why is it your favorite? ")
        tracker.add_favorite_country(name, rating, reason)
    elif choice == "7":
        tracker.show_favorite_countries()
    else:
        print("Invalid option.")
