from student_class import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone_number):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone_number

    def __str__(self):
        return (f"Library:\n\tCity: {self.city}\n\tStreet: {self.street}\n\tZIP Code: {self.zip_code}"
                f"\n\tOpen Hours: {self.open_hours}\n\tPhone: {self.phone}")


class Employee:
    def __init__(self, name, surname, hire_date, birthday, city, street, zip_code, phone):
        self.first_name = name
        self.last_name = surname
        self.hire_date = hire_date
        self.birth_day = birthday
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee:\n\tName: {self.first_name}\n\tSurname: {self.last_name}"
                f"\n\tHire Date: {self.hire_date}\n\tBirth Date: {self.birth_day}"
                f"\n\tCity: {self.city}\n\tStreet: {self.street}\n\tZIP Code: {self.zip_code}"
                f"\n\tPhone: {self.phone}")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = pages

    def __str__(self):
        return (f"Book:\n{self.library}\n\tPublication Date: {self.publication_date}"
                f"\n\tAuthor: {self.author_name} {self.author_surname}\n\t"
                f"Number of Pages: {self.number_of_pages}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        result_string = (f"Order created by:\n{self.employee}\nFor:\n\t{self.student}\nBooks:")
        for book in self.books:
            result_string += f"\n{book}"
        result_string += (f"\nDate:\n\t{self.order_date}")
        return result_string


library1 = Library("Katowice", "Bogucicka 15", "40-200", "09:00 - 18:00",
                   "789 987 456")
library2 = Library("Warsaw", "Naukowa 34", "56-234", "07:00 - 21:00",
                   "671 834 952")

# Bolesław Prus - "Lalka"
# Władysław Reymont "Ziemia obiecana"
# Henryk Sienkiewicz "Qvo Vadis"
# Jarosław Iwaszkiewicz "Panny z Wilka"
# Stefan Żeromski "Przedwiośnie"

book1 = Book(library1, "XX-XX-1889", "Bolesław",
             "Prus", 322)
book2 = Book(library2, "XX-XX-1899", "Władysław",
             "Reymont", 672)
book3 = Book(library2, "XX-02-1896", "Henryk",
             "Sienkiewicz", 640)
book4 = Book(library1, "XX-XX-1933", "Jarosław",
             "Iwaszkiewicz", 215)
book5 = Book(library1, "XX-XX-1924", "Stefan",
             "Żeromski", 248)

employee1 = Employee("Artur", "Chmurka", "15.03.2010", "29.11.1985",
                     "Cracow", "Stradomska", "35-500", "147 852 369")
employee2 = Employee("Daniel", "Plich", "30.05.2011", "15.08.1987",
                     "Katowice", "Pod Brzegiem", "40-200", "753 987 642")
employee3 = Employee("Krystyna", "Gil", "11.01.2002", "29.02.1972",
                     "Warsaw", "Ptasia", "56-236", "764 2841 349")

student1 = Student("Jan Kowalski", [100, 100, 100])
student2 = Student("Anna Nowak", [0, 0, 0])
student3 = Student("Alojzy Gwizdek", [50, 51, 52])

order1 = Order(employee1, student1, [book1, book2, book4], "29-02-2024")
order2 = Order(employee3, student3, [book3, book1, book5, book4], "06-03-2024")

# print(library1)
# print()
# print(library2)

# print(employee1)
# print()
# print(employee2)
# print()
# print(employee3)

# print(book1)
# print()
# print(book2)
# print()
# print(book3)
# print()
# print(book4)
# print()
# print(book5)
# print()

# print(student1)
# print()
# print(student2)
# print()
# print(student3)
# print()

print(f"{order1}\n")
print(order2)
