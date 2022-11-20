import wikipedia
import string
import sqlite3
import os

def SuggestPeople(username: str) -> str:
    suggest_name = wikipedia.suggest(username)
    return None if suggest_name is None else suggest_name

def CreateMenu(title: str, options: list[str]) -> int:
    os.system("cls")
    content = '\n'.join([f"{nb}. {option}" for nb, option in enumerate(options, start=1)])
    print("=" * len(title))
    print(title)
    print(content)
    print("=" * len(title))
    element = input("Choice a number : ")
    if element.isdigit():
        value = int(element)
        if not 0 < value <= len(options):
            return CreateMenu(title, options)
        return options[value - 1]
    else:
        return CreateMenu(title, options)

def CheckDatabase() -> None:
    try:
        connection = sqlite3.connect("wikipedia.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM famous_people")
    except sqlite3.OperationalError:
        connection.execute(
            '''CREATE TABLE famous_people
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME           NVARCHAR(300) NOT NULL,
                SUMMARY        TEXT NOT NULL);
            ''')
    finally:
        if connection:
            connection.close()

def DataExists(username: str, cursor) -> bool:
    if cursor.execute("SELECT NAME FROM famous_people WHERE NAME = ?", [username]).fetchone():
        return True
    return False

def DataToDatabase(username: str):
    try:
        connection = sqlite3.connect("wikipedia.db")
        cursor = connection.cursor()
        if not DataExists(username, cursor):
            query = "INSERT INTO famous_people (NAME, SUMMARY) VALUES (? , ?)"
            cursor.execute(query, (username, wikipedia.summary(username, auto_suggest=False)))
            connection.commit()
            input(f"{username} has been added in the famous_people table. Press ENTER to continue.")
        else:
            input("Data already exists in the table. Press ENTER to continue.")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert date into table famous_people.", error)
        input("Press ENTER to continue.")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    CheckDatabase()
    while True:
        choice = CreateMenu("What do you want to do ?", ["Add famous people", "Exit"])
        if choice != "Exit":
            os.system("cls")
            username = string.capwords(input("Which famous person do you research on Wikipedia ?\n"))
            infos = wikipedia.search(username)
            if len(infos) == 0 or not username.__eq__(infos[0]):
                suggest_name = SuggestPeople(username)
                if suggest_name is not None:
                    suggest_name = string.capwords(suggest_name)
                    choice = CreateMenu(f"Did you mean {suggest_name} ?", ["Yes", "No"])
                    if choice == "Yes":
                        DataToDatabase(suggest_name)
                else:
                    input(f"{username} doesn't exist on Wikipedia. Press ENTER to continue.")
            else:
                DataToDatabase(username)
        else:
            exit()
