import datetime
import platform

def system_info():
    print("----- SYSTEM INFORMATION -----")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print("------------------------------\n")


def greet_user(name):
    print(f"Hello {name}, welcome to Jenkins + Docker CI/CD!\n")


def calculate_sum():
    print("----- SIMPLE CALCULATION -----")
    a = 10
    b = 20
    print(f"Sum of {a} + {b} = {a + b}")
    print("------------------------------\n")


def show_time():
    print("----- CURRENT TIME -----")
    now = datetime.datetime.now()
    print("Current Date & Time:", now)
    print("------------------------\n")


def main():
    print("===== APPLICATION STARTED =====\n")

    greet_user("Santhosh")
    system_info()
    calculate_sum()
    show_time()

    print("===== APPLICATION FINISHED =====")


if __name__ == "__main__":
    main()
