import csv
import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"


def load_projects(file_name):
    if not file_name.endswith(".txt"):
        file_name += '.txt'

    all_projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                name, start_date, priority, cost_estimate, completion_percentage = row
                all_projects.append(
                    Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    except FileNotFoundError:
        pass

    return all_projects


def save_projects(projects, file_name):
    if not file_name.endswith(".txt"):
        file_name += '.txt'

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.cost_estimate,
                             project.completion_percentage])


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    incomplete_projects.sort(key=lambda x: x.priority)
    completed_projects.sort(key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("Completed projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [p for p in projects if
                         datetime.datetime.strptime(p.start_date, "%d/%m/%Y").date() > filter_date]
    filtered_projects.sort(key=lambda x: x.start_date)

    for project in filtered_projects:
        print(project)


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
    return new_project


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_index = int(input("Project choice: "))
        print(projects[project_index])
        new_percentage = int(input("New Percentage: "))
        new_priority = int(input("New Priority: "))

        projects[project_index].priority = new_priority
        projects[project_index].completion_percentage = new_percentage
    except (ValueError, IndexError):
        pass

    return projects
