from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING, Any
from datetime import datetime


class Project:
    """Project representation.

        Attributes:
            title (str): Project's name.
            start_date (str): Start date.
            developers (List[Developer]): List of assigned developers.
            limit (int): Maximum number of workers.
        """
    def __init__(self, title: str, start_date: datetime, developers: list[str], limit: int):  # list[str] is  developers
        self.title = title
        self.start_date = start_date
        self.developers = developers
        self.limit = limit

    def add_developer(self, new_developer) -> None:  # Attributes: New developer
        if len(self.developers) >= self.limit:
            print(f"The limit is exceeded and is {self.limit}. You can add a developer only after removing another!")
        else:
            self.developers.append(new_developer)
            print(f"Developer successfully added.And now {len(self.developers)} developers are working on the project.")

    def remove_developer(self, which_developer_remove) -> None:  # Attributes:  With developer should be removed
        if which_developer_remove not in self.developers:
            print(f"There is no developer named {which_developer_remove}")
        else:
            self.developers.remove(which_developer_remove)
            print(f"The developer named {which_developer_remove} is removed")


class Assignment:

    """
    Attributes:

        received_tasks (Dict): dictionary in form of
                        {date1: task1, date2: task2,...}.
        is_done (bool): True, if all tasks are completed.
        description (str): General assignment description.
        status (str): Percent of completed tasks.

    """

    def __init__(self, received_tasks: dict, is_done: bool, description: str, status: str):
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.description = description
        self.status = status

    def get_tasks_to_date(self, date: datetime) -> List:  # Returns all tasks before date in arguments.

        """
        Arguments:
            date: datatime
        """
        return [value for key, value in self.received_tasks.items()
                if key <= date]


class Developer:
    """Developer representation.

       Attributes:
           _id (int): Developers ID, is incremented for each instance.
           name (str): First + last names.
           address (str): Registration address.
           email (str): Personal company e-mail.
           phone_number (str) : Person's working phone number.
           position (str): Persons company position (e.g., 'Junior').
           salary (str): Salary amount (can be re-calculated).
           projects (List[Projects]): List of assigned projects
       """
    def __init__(self, _id: int, name: str, address: str, phone_number: str, email: str, position: int, rank: str,
                 salary: float, projects: list[str]):
        self._id = _id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.projects = projects

    def assign_possibility(self) -> bool:
        if self.limit > len(Project.developers):
            print(f'Developer {self.name}  Andriy can be assigned to the project')
            return True
        else:
            print(f'Too many developers are working on the project,and developer {self.name}'
                  f' Andriy can not be assigned to the project')
            return False

    def assigned_projects(self) -> List[str]:  # Assigns current developer to project instance
        return [str(project.title) for project in self.projects]

    def assign(self, project: Project) -> None:  # Assigns current developer to project instance
        project.add_developer(self.name)

    def unassign(self, project: Project) -> None:  # Project instance to be removed from developer
        project.remove_developer(self.name)


class QAEngineer:
    """
       Attributes:

           _id (int): QAEngineer ID, is incremented for each instance.
           name (str): First + last names.
           address (str): Registration address.
           phone_number (str) : Person's working phone number.
           email (str): Personal company e-mail.
           salary (str): Salary amount (can be re-calculated).
           rank (str): Persons company position (e.g., 'Junior').
           position (str): Persons company position (e.g., 'Junior').

       """
    def __init__(self, _id: int, name: str, address: str, phone_number: str, email: str, salary: float,
                 rank: str, position: str):
        self._id = _id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    def test_feature(self, assignment) -> str:   # will be implemented in the future
        return f"Assignment {assignment} has been tested"


class ProjectManager:
    """
       Attributes:
           _id (int): PM's ID, is incremented for each instance.
           name (str): First + last names.
           address (str): Registration address.
           phone_number (str) : Person's working phone number.
           email (str): Personal company e-mail.
           salary (str): Salary amount (can be re-calculated).
           project (Projects): Assume PM -> Project relation.
       """
    def __init__(self, _id: int, name: str, address: str, phone_number: str, email: str,
                 salary: float, project: Project):
        self._id = _id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project

    def discuss_progress(self, assignment) -> str:  # discuss_progress
        return f"Discussion about the progress of the project with such a task: {assignment}"


project_01 = Project("Venera", (2020, 9, 15), ["Tom", "Patricia", "Robert", "John", "Michael"], 6)


print(project_01.developers)        # test add developer
project_01.add_developer("Dimon")
print(project_01.developers)

project_01.remove_developer("Robert")   # test remove developer
print(project_01.developers)
project_01.remove_developer("Mike")
print(project_01.developers)

assignment_01 = Assignment({(2020, 3, 12): "Create a loop", (2022, 7, 17): "Create a drop-down list",
                            (2018, 4, 14): "Create artificial intelligence",
                            (2017, 7, 21): "Delete all your work"}, True, "Good assignment!", "Done!")

print(len(assignment_01.received_tasks))
print(assignment_01.get_tasks_to_date((2020, 3, 12)))  # test get tasks to date

man_01 = QAEngineer(1, "Peter", "Lviv Yabluneva 45", "+380-97-212-21-65", "peterparker@ukr.net",
                    1221.1, "Junior", "Junior")

print(man_01.email)
print(QAEngineer.test_feature(QAEngineer, "Create a loop"))  # test future
print(ProjectManager.discuss_progress(ProjectManager, "Create a loop"))  # test discuss progress
