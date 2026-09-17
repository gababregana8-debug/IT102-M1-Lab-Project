class ProjectApp:
    def __init__(self):
        self.running = True

    def start(self):
        print("================================")
        print("       MY PROJECT APP")
        print("================================")

        while self.running:
            self.main_menu()

    def main_menu(self):
        print("\nMAIN MENU")
        print("1. View Services")
        print("2. My Profile")
        print("3. Help")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.view_services()
        elif choice == "2":
            self.profile()
        elif choice == "3":
            self.help()
        elif choice == "4":
            print("\nThank you for using the app!")
            self.running = False
        else:
            print("\nInvalid choice. Please try again.")

    def view_services(self):
        print("\n================================")
        print("         SERVICES")
        print("================================")
        print("1. Service A")
        print("2. Service B")
        print("3. Service C")
        print("4. Back to Main Menu")

        choice = input("Choose a service: ")

        if choice in ["1", "2", "3"]:
            self.service_details(choice)
        elif choice == "4":
            return
        else:
            print("Invalid choice.")

    def service_details(self, service):
        services = {
            "1": "Service A",
            "2": "Service B",
            "3": "Service C"
        }

        print("\n================================")
        print("       SERVICE DETAILS")
        print("================================")
        print("Selected:", services[service])
        print("Description: This is a prototype feature.")
        print("Status: Available")

        input("\nPress Enter to return...")
        
    def profile(self):
        print("\n================================")
        print("          MY PROFILE")
        print("================================")
        print("Name: Demo User")
        print("Email: user@example.com")

        input("\nPress Enter to return...")

    def help(self):
        print("\n================================")
        print("             HELP")
        print("================================")
        print("This prototype demonstrates the")
        print("navigation and user journey of")
        print("the proposed application.")

        input("\nPress Enter to return...")


# Create an object and run the application
app = ProjectApp()
app.start()
