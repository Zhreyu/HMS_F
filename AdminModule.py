import mysql.connector

class AdminModule:
    def __init__(self, config):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()

    def execute_query(self, query, values=None, fetch=True):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

            if fetch:
                return self.cursor.fetchall()
            self.db.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def add_employee(self,role):
        if role == "D":
            doctor_id = input("Enter Doctor ID: ")
            name = input("Enter Doctor name: ")
            specialty = input("Enter specialty: ")
            salary = float(input("Enter Doctor salary: "))
            leave_balance = 5
            query = "INSERT INTO doctors(id, name, specialty, salary, leave_balance) VALUES (%s, %s, %s, %s, %s)"
            values = (doctor_id, name, specialty, salary, leave_balance)
            self.execute_query(query, values, fetch=False)
        
        elif role == "PT":
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            query = "INSERT INTO patients(patient_id, name, age) VALUES (%s, %s, %s)"
            values = (patient_id, name, age)
            self.execute_query(query, values, fetch=False)
        
        elif role in ["PH", "O"]:
            employee_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            query = "INSERT INTO employees(id, name, role, salary) VALUES (%s, %s, %s, %s)"
            values = (employee_id, name, role, salary)
            self.execute_query(query, values, fetch=False)

        print(f"{role.capitalize()} added successfully!")


    def assign_doctor_to_patient(self, patient_id, doctor_id):
        query = "UPDATE patients SET assigned_doctor_id = %s WHERE id = %s"
        self.execute_query(query, (doctor_id, patient_id), fetch=False)

    def increment_salary(self,role, employee_id):
        new_salary = float(input("Enter new salary: "))
    
        if role == "doctor":
            query = "UPDATE doctors SET salary = %s WHERE id = %s"
        else:  # assuming roles other than doctor are stored in the employees table
            query = "UPDATE employees SET salary = %s WHERE id = %s"
    
        values = (new_salary, employee_id)
        self.execute_query(query, values, fetch=False)

        print(f"Salary for {role} with ID {employee_id} updated to {new_salary}")


    def approve_leave(self, leave_id, status):
        query = "UPDATE leave_requests SET status = %s WHERE id = %s"
        self.execute_query(query, (status, leave_id), fetch=False)

    def view_all_doctors(self):
        query = "SELECT * FROM doctors"
        return self.execute_query(query)

    def view_all_patients(self):
        query = "SELECT * FROM patients"
        return self.execute_query(query)

    def view_all_other_employees(self):
        query = "SELECT * FROM employees WHERE role = 'other'"
        return self.execute_query(query)

    def admin_module(self):
        print("Welcome Admin!")

        while True:
            print("\nAdmin Options:")
            print("1. Add Employee/Patient")
            print("2. Assign Doctor to Patient")
            print("3. Increment Salary")
            print("4. Approve Leave")
            print("5. View All Patients")
            print("6. View All Doctors")
            print("7. View All Other Employees")
            print("8. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                role = input("Enter role (D/PH/PT/O): ")
                self.add_employee(role)
            elif choice == "2":
                patient_id = int(input("Enter patient ID: "))
                doctor_id = int(input("Enter doctor ID: "))
                self.assign_doctor_to_patient(patient_id, doctor_id)
                print("Doctor assigned to patient.")
            elif choice == "3":
                employee_id = input("Enter employee ID: ")
                self.increment_salary(employee_id)
                print("Salary incremented.")
            elif choice == "4":
                leave_id = int(input("Enter leave request ID: "))
                status = input("Enter status (approved/rejected): ")
                self.approve_leave(leave_id, status)
                print("Leave request updated.")
            elif choice == "5":
                patients = self.view_all_patients()
                for patient in patients:
                    print(patient)
            elif choice == "6":
                doctors = self.view_all_doctors()
                for doctor in doctors:
                    print(doctor)
            elif choice == "7":
                other_employees = self.view_all_other_employees()
                for employee in other_employees:
                    print(employee)
            elif choice == "8":
                break
            else:
                print("Invalid option, please try again.")

        self.db.close()

if __name__ == "__main__":
    config = {
        'host': 'your_host',
        'user': 'your_user',
        'password': 'your_password',
        'database': 'your_database'
    }

    admin_module = AdminModule(config)
    admin_module.admin_module()
