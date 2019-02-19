from src.task import Task
import pickle
import os


class ToDo:
    """To-do system"""
    def __init__(self):
        """Initializes the to-do system. Load tasks if there is an object
        file, if not, tasks are empty"""
        self.tasks = []
        path = os.path.dirname(os.path.abspath(__file__))
        self.__obj_file_name = "{0}/../checkpoint/checkpoint.obj".format(path)
        if os.path.isfile(self.__obj_file_name):
            self.__load()

    def create_task(self, name, deadline):
        """Append new tasks"""
        self.tasks.append(Task(name, deadline))
        self.__save()

    def __test_index(self, index):
        """Test if index is greater than 0 and smaller than list size"""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("List index out of range")

    def modify_deadline(self, index, new_deadline):
        """Modify deadline of a certain task based on its index"""
        self.__test_index(index)
        self.tasks[index].set_deadline(new_deadline)
        self.__save()

    def delete_task(self, index):
        """Delete a task based on index"""
        self.__test_index(index)
        self.tasks.pop(index)
        self.__save()

    def __sort_tasks(self):
        """Sort tasks based on deadline, closer appears first"""
        self.tasks.sort(key=lambda x: x.get_deadline())

    def __save(self):
        """Save the tasks"""
        object_file = open(self.__obj_file_name, "wb")
        pickle.dump(self.tasks, object_file)
        object_file.close()

    def __load(self):
        """Load the tasks"""
        object_file = open(self.__obj_file_name, "rb")
        self.tasks = pickle.load(object_file)
        object_file.close()

    def __str__(self):
        self.__sort_tasks()
        result = ""
        for i in range(len(self.tasks)):
            result += "{1}: {0}\n".format(self.tasks[i], i)
        return result


