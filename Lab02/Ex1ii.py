def calculate_efficiency():
    time_taken = float(input("Enter the time taken to complete the job (in hours): "))

    if time_taken >= 2 and time_taken < 3:
        return "Highly efficient"
    elif time_taken >= 3 and time_taken < 4:
        return "Improve speed"
    elif time_taken >= 4 and time_taken < 5:
        return "Training needed"
    elif time_taken >= 5:
        return "Worker must leave the company"
    else:
        return "Invalid input"

efficiency = calculate_efficiency()
print("Efficiency:", efficiency)