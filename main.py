from AdminModule import AdminModule,admin_module
from DoctorModule import DoctorModule,doctor_module
from PatientModule import PatientModule,patient_module
from PharmacistModule import PharmacistModule,pharmacist_module
from OtherStaffModule import OtherStaffModule,other_staff_module



def login(username, password):
    query = "SELECT * FROM login_info WHERE username = %s AND password = %s"
    result = execute_query(query, (username, password))
    return result[0] if result else None

def main():
    print("################################")
    print("Welcome to Hospital Management System (HMS)")
    print("################################\n")

    while True:
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            user = login(username, password)
            
            if user:
                role = user[3]
                user_id = user[4]

                if role == "doctor":
                    doctor_module(user_id)
                elif role == "patient":
                    patient_module(user_id)
                elif role == "pharmacist":
                    pharmacist_module()
                elif role == "admin":
                    admin_module()
                elif role == "other":
                    other_staff_module(user_id)
                else:
                    print("Invalid role. Please contact the system administrator.")
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            print("Thank you for using HMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
