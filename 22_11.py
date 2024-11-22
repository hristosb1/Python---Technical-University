class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrowed = 0

    def print_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def borrow(self):
        if self.is_available:
            self.is_available = False
            self.borrowed += 1
            print(f"You have borrowed the book {self.title}")
        else:
            print(f"The book {self.title} is already taken.")

    def return_book(self):
        self.is_available = True
        print(f"You have returned the book {self.title}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if book.is_available:
                print(book.title)

    def is_limit_reached(self):
        count = 0
        for book in self.books:
            if not book.is_available:
                count += 1
            if count == 3:
                return True
        return False

    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                if self.is_limit_reached():
                    print('You have reached the limit of 3 books')
                    return
                
                book.borrow()
                return
        print(f"The book {title} is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"The book {title} has been successfully returned.")

    def list_borrowed_books(self):
        for book in self.books:
            if not book.is_available:
                print(f"{book.title} - {book.author}")

    def search_by_author(self, author):
        found = False
        for book in self.books:
            if author in book.author:
                print(book.title)
                found = True
        if not found:
            print("No books found matching the given criteria.")

class Animal:
    def __init__(self, name, species, age, health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health

    def print_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Health: {self.health}")

class Mammal(Animal):
    def __init__(self, name, species, age, health, fur_color, diet):
        super().__init__(name, species, age, health)
        self.fur_color = fur_color
        self.diet = diet

    def print_info(self):
        super().print_info()
        print(f"Fur Color: {self.fur_color}, Diet: {self.diet}")

class Bird(Animal):
    def __init__(self, name, species, age, health, wing_span, can_fly):
        super().__init__(name, species, age, health)
        self.wing_span = wing_span
        self.can_fly = can_fly

    def print_info(self):
        super().print_info()
        print(f"Wing Span: {self.wing_span}, Can Fly: {self.can_fly}")

class Reptile(Animal):
    def __init__(self, name, species, age, health, is_venomous, preferred_temperature):
        super().__init__(name, species, age, health)
        self.is_venomous = is_venomous
        self.preferred_temperature = preferred_temperature

    def print_info(self):
        super().print_info()
        print(f"Venomous: {self.is_venomous}, Preferred Temperature: {self.preferred_temperature}")

class Zoo:
    def __init__(self):
        self.enclosures = {}

    def add_animal(self, animal, enclosure_number):
        if enclosure_number not in self.enclosures:
            self.enclosures[enclosure_number] = []
        self.enclosures[enclosure_number].append(animal)

    def remove_animal(self, name):
        for animals in self.enclosures.values():
            for animal in animals:
                if animal.name == name:
                    animals.remove(animal)
                    return
        print(f"The animal {name} was not found.")

    def list_animals_in_enclosure(self, enclosure_number):
        if enclosure_number in self.enclosures:
            for animal in self.enclosures[enclosure_number]:
                animal.print_info()
        else:
            print(f"Enclosure {enclosure_number} does not exist.")

    def transfer_animal(self, name, old_enclosure, new_enclosure):
        for animals in self.enclosures.values():
            for animal in animals:
                if animal.name == name:
                    animals.remove(animal)
                    self.add_animal(animal, new_enclosure)
                    return
        print(f"The animal {name} was not found.")

    def find_animals_by_species(self, species):
        found = False
        for animals in self.enclosures.values():
            for animal in animals:
                if animal.species == species:
                    animal.print_info()
                    found = True
        if not found:
            print(f"No animals of species {species} found.")




book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book4 = Book("Moby Dick", "Herman Melville", 1851)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print("Available books:")
library.list_books()

library.search_book("1984")
library.search_book("The Great Gatsby")
library.search_book("Moby Dick")
library.search_book("To Kill a Mockingbird")  # should reach limit

print("Borrowed books:")
library.list_borrowed_books()

library.return_book("1984")
library.return_book("Moby Dick")

# books after return
print("Available books after returns:")
library.list_books()

library.search_by_author("Harper Lee")




# creating animals
lion = Mammal("Leo", "Lion", 5, 9, "Golden", "Carnivore")
elephant = Mammal("Dumbo", "Elephant", 10, 7, "Grey", "Herbivore")
parrot = Bird("Polly", "Parrot", 2, 8, 25, True)
snake = Reptile("Slither", "Snake", 4, 6, True, 30)

zoo = Zoo()

# adding animals to enclosures
zoo.add_animal(lion, 1)
zoo.add_animal(elephant, 1)
zoo.add_animal(parrot, 2)
zoo.add_animal(snake, 3)

# listing animals in enclosure 1
print("\nAnimals in enclosure 1:")
zoo.list_animals_in_enclosure(1)

# transferring an animal to a new enclosure
zoo.transfer_animal("Polly", 2, 1)

# listing animals in enclosure 1 after transfer
print("\nAnimals in enclosure 1 after transfer:")
zoo.list_animals_in_enclosure(1)

# removing an animal
zoo.remove_animal("Slither")

# listing animals in enclosure 3 after removal
print("\nAnimals in enclosure 3 after removal:")
zoo.list_animals_in_enclosure(3)

# finding animals by species
print("\nFinding all Lions in the zoo:")
zoo.find_animals_by_species("Lion")
