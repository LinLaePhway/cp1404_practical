import project_management as pm


def main():
    current_projects = []

    while True:
        MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
        print(MENU)

        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter a file name you want to load your projects from: ")
            try:
                current_projects = pm.load_projects(file_name)
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == 's':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                file_name = input("Enter a file name you want your projects to save to: ")
                pm.save_projects(current_projects, file_name)
        elif choice == 'd':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                pm.display_projects(current_projects)
        elif choice == 'f':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                pm.filter_projects_by_date(current_projects)
        elif choice == 'a':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
                current_projects = [pm.add_new_project()]  # Initialize the list if empty
            else:
                current_projects.append(pm.add_new_project())
        elif choice == 'u':
            if len(current_projects) < 1:
                print("Currently No Projects Loaded!")
            else:
                current_projects = pm.update_project(current_projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid menu option. Enter your choice again: ")


if __name__ == "__main__":
    main()