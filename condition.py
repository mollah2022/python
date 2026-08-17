is_valid_roll = True
is_gender = "Male"
exam_marks = 95

if is_valid_roll:
    if is_gender == "Male":
        if exam_marks >= 90:
            print("Eligible for scholarship.")
        else:
            print("Not eligible for scholarship.")

    else:
        print("Only male students are eligible for this scholarship.")


else:
    print("Invalid roll number.")




day = "Monday"

match day:

    case "Saturday":
        print("It's the weekend!")
    case "Sunday":
        print("It's the weekend!")
    case "Monday":
        print("It's a weekday.")        
    case "Tuesday":
        print("It's a weekday.")
    case "Wednesday":
        print("It's a weekday.")
    case "Thursday":
        print("It's a weekday.")
    case "Friday":
        print("It's a weekday.")

    case _:
        print("Invalid day.")