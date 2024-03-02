import matplotlib.pyplot as plt
import random

class CaringHands:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None
        self.health_data = {'vital_signs': {'heart_rate': [], 'blood_pressure': []},
                           'symptoms': [],
                           'medications': []}

    def show_login_signup(self):
        while True:
            print("\nWelcome to Caring Hands")
            print("1. Login")
            print("2. Signup")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.signup()
            elif choice == '3':
                print("Exiting Caring Hands. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username] == password:
            print("Login successful! Welcome back, {}".format(username))
            self.logged_in_user = username
            self.show_dashboard()
        else:
            print("Invalid credentials. Please try again or sign up.")

    def signup(self):
        username = input("Choose a username: ")
        password = input("Choose a password: ")

        if username not in self.users:
            self.users[username] = password
            print("Signup successful! Welcome, {}".format(username))
            self.logged_in_user = username
            self.show_dashboard()
        else:
            print("Username already exists. Please choose a different username.")

    def show_dashboard(self):
        while True:
            print("\nPatient Dashboard - Welcome, {}".format(self.logged_in_user))
            print("1. Overview of current health status")
            print("2. Quick access to vital signs, recent activities, and medication schedule")
            print("3. Health Data Input")
            print("4. Notifications for upcoming appointments or tasks")
            print("5. Logout")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                self.show_health_status()
            elif choice == '2':
                self.show_quick_access()
            elif choice == '3':
                self.health_data_input()
            elif choice == '4':
                self.show_notifications()
            elif choice == '5':
                print("Logging out. Goodbye, {}!".format(self.logged_in_user))
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    def show_health_status(self):
        # Simulating health data for visualization
        days = list(range(1, 8))
        heart_rate = [random.randint(60, 100) for _ in range(7)]
        blood_pressure = [random.randint(90, 120) for _ in range(7)]

        plt.plot(days, heart_rate, label='Heart Rate', marker='o')
        plt.plot(days, blood_pressure, label='Blood Pressure', marker='o')

        plt.xlabel('Days')
        plt.ylabel('Values')
        plt.title('Weekly Health Status')
        plt.legend()
        plt.show()

    def show_quick_access(self):
        # Simulating quick access data
        print("Vital Signs: Heart Rate - 75 bpm, Blood Pressure - 110/70 mmHg")
        print("Recent Activities: Walked 5000 steps today")
        print("Medication Schedule: Aspirin - 1 tablet daily, 9:00 AM")

    def health_data_input(self):
        print("\nHealth Data Input")
        print("1. Enter Vital Signs")
        print("2. Enter Symptoms")
        print("3. Enter Medications")
        print("4. Upload Data from Wearables/IoT devices")
        print("5. Back to Dashboard")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            self.enter_vital_signs()
        elif choice == '2':
            self.enter_symptoms()
        elif choice == '3':
            self.enter_medications()
        elif choice == '4':
            self.upload_wearable_data()
        elif choice == '5':
            pass
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    def enter_vital_signs(self):
        heart_rate = input("Enter your heart rate (bpm): ")
        blood_pressure = input("Enter your blood pressure (mmHg): ")

        self.health_data['vital_signs']['heart_rate'].append(int(heart_rate))
        self.health_data['vital_signs']['blood_pressure'].append(int(blood_pressure))

        print("Vital signs recorded successfully!")

    def enter_symptoms(self):
        symptom = input("Enter your symptoms: ")
        self.health_data['symptoms'].append(symptom)
        print("Symptoms recorded successfully!")

    def enter_medications(self):
        medication = input("Enter your medication: ")
        self.health_data['medications'].append(medication)
        print("Medication recorded successfully!")

    def upload_wearable_data(self):
        # Placeholder for data upload from wearables/IoT devices
        print("Uploading data from wearables/IoT devices...")

    def show_notifications(self):
        # Simulating notifications
        print("Upcoming Appointment: Dr. Smith, 10:30 AM tomorrow")
        print("Task Reminder: Take medication at 9:00 AM")

if __name__ == "__main__":
    caring_hands = CaringHands()
    caring_hands.show_login_signup()
