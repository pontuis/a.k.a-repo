import math

tasks = []
# weekday = int(input("Enter weekday day number (1-7) : "))
#
#
# if weekday == 1:
#      print("\nMonday")
# elif weekday == 2:
#      print("\nTuesday")
# elif weekday == 3:
#      print("\nWednesday")
# elif weekday == 4:
#      print("\nThursday")
# elif weekday == 5:
#     print("\nFriday")
# elif weekday == 6:
#     print("\nSaturday")
# elif weekday == 7:
#     print("\nSunday")
# else:
#     print("\nPlease enter weekday number between 1-7.")
#
#
#
# num1 = int(input("enter largest number :"))
# num2 = int(input("enter largest number :"))
# num3 = int(input("enter largest number :"))
# if num1 > num2 and num1> num3:
#     print(" Largest number is:" , num1)
# elif num2 > num1 and num2 > num3:
#     print ("Is largest number" , num2)
# elif num3 > num1 and num2 > num1:
#     print ("is largest number" , num3)
#
# else:
#     print ('Error')
#
#
#
# num = int(input("enter a number:"))
#
# if num % 2 == 0 and num % 3 == 0:
#     print("the number is divisble by both 2 and 3.")
# else:
#     print("the number is not divisble by both 2 and 3.")
#

# list1 = [3, 2, 8, 5, 500, 6]
#
# max_number = max(list1)
#
# print("The largest number is:", max_number)
#
#
#
# even_numbers = [i for i in range(1, 21) if i % 2 == 0]
# print("Even numbers between 1 and 20:", even_numbers)
#
#
# num = int(input("Enter a number: "))
#
#
# table = []
#
# for i in range(1, 11):
#     table.append(num * i)
#
# print("The multiplication table of", num, "is:")
# for i in range(len(table)):
#     print(num, "x", i+1, "=", table[i])


# values = ([1, 2, 3], ["dog", "cow", "cat"], ["name", True, 30.2])
#
# for sublist in values:
#     for element in sublist:
#         print(element)

# A while loop in Python is used to repeatedly execute a block of code as long as a certain condition is true. The syntax is:
#
# python
# Verify
# Edit
# Run
# Full Screen
# Copy code
# while condition:
#     code to be executed
# Here is an example of a while loop that prints numbers from 1 to 5:
#
# python
# Verify
# Edit
# Run
# Full Screen
# Copy code
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# In this example, the loop continues to execute as long as the value of count is less than or equal to 5. Inside the loop, the current value of count is printed and then count is incremented by 1. Once count becomes 6, the condition is no longer true and the loop exits.
#
# People Also Ask
# What is the purpose of the condition in a while loop in Python?
# How is the count variable updated in the given while loop example?
# What would happen if the count += 1 line is removed from the example?
#
#
#
# Answer 2
# 3
# Scroll to bottom
#
# Continue


# name = input("enter name")
# while name != "kevin":
#     print("enter correct name")
#     enter = input("enter name: ")
# print("hello kevin")
#
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "dog", "man", "cat")
# i = 10
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1
#
#
# name = input("enter name: ")
# counter = 0
# while name != "kevin":
#     print("enter correct name")
#     enter = input("enter name: ")
# print("locked")
#

# name = input("enter name: ")
# counter = 1
# while True:
#     if name == "kevin":
#         print("hello kevin")
#         break
#     else:
#         print("invalid name")
#         name = input("enter name: ")
#         counter += 1
#         if counter == 3:
#            if name == "kevin":
#                print("hello kevin")
#            else:
#                print("locked")
#                break


# while True:
#         print("Select operation:")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
#
#         choice = input("Enter your choice (1/2/3/4/5): ")
#
#         if choice in ('1', '2', '3', '4'):
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#
#             if choice == '1':
#                 print(num1, "+", num2, "=", num1 + num2)
#             elif choice == '2':
#                 print(num1, "-", num2, "=", num1 - num2)
#             elif choice == '3':
#                 print(num1, "*", num2, "=", num1 * num2)
#             elif choice == '4':
#                 if num2 != 0:
#                     print(num1, "/", num2, "=", num1 / num2)
#                 else:
#                     print("Cannot divide by zero")
#         elif choice == '5':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid...)


# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
#
# for i in range(start, end + 1):
#     print(i)


# num = float(input("Enter a number: "))
# if num >= 0:
#         result = math.sqrt(num)
#         print(f"The square root of {num} is {result}")
# else:
#         print("Invalid input. Please enter a non-negative number.")
#
#
#
#
#
#
#
#
# while True:
#     print("\nTo-Do List")
#     print("----------")
#     print("1. Add a new task")
#     print("2. Remove an existing task")
#     print("3. View all tasks")
#     print("4. Exit the application")
#     print("----------")
#
#     option = input("Enter an option (1-4): ")
#
#     if option == "1":
#         tasks.append(input("Enter a new task: "))
#     elif option == "2":
#         if not tasks:
#             print("Error: The to-do list is empty.")
#         else:
#             task_to_remove = input("Enter the task to remove: ")
#             if task_to_remove in tasks:
#                 print("Error: The task does not exist in the to-do list.")
#             else:
#                 tasks.remove(task_to_remove)
#     elif option == "3":
#         if not tasks:
#             print("Error: The to-do list is empty.")
#         else:
#             print("\nTasks:")
#             for task in tasks:
#                 print("- " + task)
#     elif option == "4":
#         print("Goodbye!")
#
#     else:
#         print("Error: Invalid option. Please try again.")


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1 | set2)


# cars = {
#     "color": "black",
#     "model": 2022,
#     "price": 2103.22,
#     "name": ["toyota", "nissan", "bmw"]
# }
#
# for i in cars["name"]:
#     print(i)


# person = {}
#
# person["name"] = input("Enter your name")
# person["age"] = input("enter your age")
# person["gender"] = input("enter your gender")
# person["city"] = input("enter your city")
#
# print(person)
#
#
#
#
#
#
#
# while True:
#     print("\nContacts List Menu:")
#     print("1. Add Contact")
#     print("2. Lookup Contact")
#     print("3. Delete Contact")
#     print("4. Display Contacts")
#     print("5. Exit")
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         "add_contact"
#     elif choice == "2":
#         "lookup_contact"
#     elif choice == "3":
#         "delete_contact"
#     elif choice == "4":
#         "display_contact"
#     elif choice == "5":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again!")


# while True:
#   try:
#     num1 = int(input("enter number"))
#     num2 = int(input("enter number"))
#     result = num1 / num2
#     print(result)
#   except ValueError:
#     print("enter just numbers")
#   except ZeroDivisionError:
#     print("can`t  divide numbers by 0")
#   choice = input("do you want to continue")
#   if choice != "yes":
#         print("exiting..")
#         break
#
#
#
# numbers = [10, 20, 30, 40, 50]
#
#
# while True:
#     num = input("Enter a new element to add to the list: ")
#     try:
#         num = int(num)
#         numbers.append(num)
#         print("Updated list:", numbers)
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#
# print("Final list:", numbers)
# try:
#     with open('mbox.txt', 'r') as file:
#         count = 0
#         for line in file:
#             print(line.strip())
#             count += 1
#             print(count)
#             print("total lines in file:", count)
#         print(file.read())


# with open('mbox.txt', 'r') as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             print(word)
#             count += 1
#             print("total words are:", count)

# except FileNotFoundError:
#     print("File is not currently in this project")


# def is_palindrome(lst):
#     """
#     Check if the list is a palindrome.
#
#     :param lst: List of elements
#     :return: True if the list is a palindrome, False otherwise
#     """
#
#     if len(lst) < 2:
#         return False
#
#     return lst == lst[::-1]
#
#
# test_list = [ [1, 2, 3, 5, 7, 7, 0],
#                ['Red', 'Green', 'Blue'],
#                [1, 0, 0, 1, 0, 0, 1],
#                ['Red', 'Yellow', 'Green', 'Yellow', 'Red']
# ]
#
# for list in test_list:
#     print(f"{list} {is_palindrome(list)}")


# import requests
# from bs4 import BeautifulSoup, NavigableString
#
# url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
# file = requests.get(url).text
# soup = BeautifulSoup(file, 'html.parser')
# tag = soup.find('li', class_="clearfix job-bx wht-shd-bx")
# print(tag.find('span', class_="srp-skills").text.strip().replace(" ", ""))
# print(tag.find('span', class_="sim-posted").text)
# print(tag.h2.a["href"].strip())
# print(tag.h3.text.strip())
#
# import requests
# from bs4 import BeautifulSoup, NavigableString

# url = "https://ng.indeed.com/viewjob?jk=1574c2f79212e65c&tk=1hvn3sjva34qs025&from=serp&vjs=3"
# file = requests.get(url).text
# soup = BeautifulSoup(file, 'html.parser')
# tag = soup.find('li', class_="clearfix jobwht-shd-bx")
# print(tag.find('span', class_="srp-skills").text.strip().replace(" ", ""))
# print(tag.find('span', class_="tabindex="))


import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Form")
        self.master.geometry('340x440')
        self.master.configure(bg='#333333')

        self.frame = tk.Frame(self.master, bg='#333333')
        self.frame.pack()

        self.create_widgets()

    def create_widgets(self):

        self.login_label = tk.Label(
            self.frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30)
        )
        self.username_label = tk.Label(
            self.frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16)
        )
        self.username_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 16))
        self.password_label = tk.Label(
            self.frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)
        )
        self.login_button = tk.Button(
            self.frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login
        )

        self.login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

    def login(self):
        username = "johnsmith"
        password = "12345"
        if self.username_entry.get() == username and self.password_entry.get() == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()
