task_description = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match task_priority:
    case "high":
        if time == "yes":
            print(f'\"{task_description}\" is a {task_priority} priority task that requires immediate attention today!')
        else:
            print(f'\"{task_description}\" is a {task_priority} priority task. Consider completing it when you have free time.')

     case "medium":
        if time == "yes":
            print(f'\"{task_description}\" is a {task_priority} priority task that requires immediate attention today!')
        else:
            print(f'\"{task_description}\" is a {task_priority} priority task. Consider completing it when you have free time.')

     case "low":
        if time == "yes":
            print(f'\"{task_description}\" is a {task_priority} priority task that requires immediate attention today!')
        else:
            print(f'\"{task_description}\" is a {task_priority} priority task. Consider completing it when you have free time.')
    default:
        print("Invalid input)
    
