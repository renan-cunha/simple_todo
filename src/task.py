from datetime import date


class Task:
    """A task"""
    def __init__(self, name, deadline):
        """Initializes a task with name and deadline"""
        self.name = name
        self.__deadline = None
        self.set_deadline(deadline)

    def set_deadline(self, deadline):
        """Assures deadline is on appropriate format"""
        try:
            year, month, day = list(map(int, deadline.split("-")))
            self.__deadline = date(year, month, day)
        except ValueError:
            raise ValueError("Deadline is not in 'year-month-day' format")

    def get_deadline(self):
        return self.__deadline

    def __str__(self):
        return "Name: {0}; Deadline: {1}".format(self.name, self.__deadline)
