from src.todo import ToDo
import os


class Cli:
    """Command Line Interface"""

    def __init__(self):
        """Initializes the system"""
        self.__to_do = ToDo()

    @staticmethod
    def __exception(message):
        """Print exception message and asks user to press ENTER"""
        print(message)
        input("Press ENTER to continue")

    def __show_tasks(self):
        """Show tasks"""
        print(self.__to_do)

    def __create_task(self):
        """Ask user for task name and deadline"""
        name = input("Name of task: ")
        deadline = input("Deadline of task: ")
        self.__to_do.create_task(name, deadline)

    def __modify_deadline(self):
        """Ask user task index to modify its deadline"""
        index = int(input("Task index: "))
        new_deadline = input("New deadline: ")
        self.__to_do.modify_deadline(index, new_deadline)

    def __delete_task(self):
        """Ask user index to delete a task"""
        index = int(input("Task index: "))
        self.__to_do.delete_task(index)

    def __menu(self):
        """The Cli menu"""
        self.__show_tasks()
        option = input("(1) Create a task (2) Modify Task \n" \
                       "(3) Delete task (4) Exit\nOption: ")
        os.system("clear")
        self.__show_tasks()
        try:
            if option == "1":
                self.__create_task()
            elif option == "2":
                self.__modify_deadline()
            elif option == "3":
                self.__delete_task()
            elif option == "4":
                exit()
            else:
                self.__exception("This options does not exist")
        except ValueError as e:
            self.__exception(e)
        except IndexError as e:
            self.__exception(e)
        os.system("clear")

    def run(self):
        """Executes the Cli"""
        while True:
            self.__menu()


if __name__ == "__main__":
    cli = Cli()
    cli.run()
