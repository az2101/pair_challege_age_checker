from datetime import datetime


def age_checker(date_of_birth):
    today = datetime.today().date()
    print(today)
    dob = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
    print(dob)
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age > 16:
        return "Access Granted"
    elif age < 0:
        raise Exception("Date is in the future")
    elif age < 16:
        return f"Access denied. You are {age}, you must be over 16 to enter!"
    elif age == ValueError:
        raise ValueError("Invalid date format")
    
    


