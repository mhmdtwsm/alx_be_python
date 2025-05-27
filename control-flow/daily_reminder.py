task = input("Enter your task: ")
prio = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound:
    print(f"Reminder: '{task}' is a {prio} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {prio} priority task. Consider completing it when you have free time.")
