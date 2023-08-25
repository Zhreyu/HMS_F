import mysql.connector
from getpass import getpass

class DoctorModule:
    def __init__(self, config, doctor_id):
        self.config = config
        self.doctor_id = doctor_id

    def connect_to_db(self):
        return mysql.connector.connect(**self.config)

    def execute_query(self, query, values=None, fetch=True):
        conn = self.connect_to_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, values)
        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None
        cursor.close()
        conn.close()
        return result

    def view_assigned_patients(self):
        query = "SELECT user_id FROM doctors WHERE user_id = %s"
        return self.execute_query(query, (self.doctor_id,))

    def manage_prescriptions(self, patient_id, medicine, dosage):
        query = "INSERT INTO prescriptions (patient_id, doctor_id, medicine, dosage) VALUES (%s, %s, %s, %s)"
        self.execute_query(query, (patient_id, self.doctor_id, medicine, dosage), fetch=False)

    def view_doctor_schedule(self):
        query = "SELECT * FROM appointments WHERE doctor_id = %s"
        #query = "SELECT * FROM doctor_schedule WHERE doctor_id = %s"
        return self.execute_query(query, (self.doctor_id,))

    def apply_for_leave(self, start_date, end_date):
        query = "INSERT INTO leave_requests (user_id, start_date, end_date, status) VALUES (%s, %s, %s, 'pending')"
        self.execute_query(query, (self.doctor_id, start_date, end_date), fetch=False)

    def view_salary(self):
        query = "SELECT salary FROM doctors WHERE user_id = %s"
        result = self.execute_query(query, (self.doctor_id,))
        return result[0]['salary'] if result else None

    def update_schedule(self, day, start_time, end_time):
        query = """
        INSERT INTO doctor_schedule (doctor_id, day, start_time, end_time, appointment_approved) 
        VALUES (%s, %s, %s, %s, 0)
        ON DUPLICATE KEY UPDATE start_time=%s, end_time=%s
        """
        self.execute_query(query, (self.doctor_id, day, start_time, end_time, start_time, end_time), fetch=False)

    def approve_appointment(self):
        query = "SELECT * FROM appointments WHERE doctor_id = %s AND status = 'pending'"

        appointments = self.execute_query(query, (self.doctor_id,))

        if not appointments:
            print("No pending appointments.")
            return

        print("Pending Appointments:")
        for idx, app in enumerate(appointments, start=1):
            print(f"{idx}. {app['day']} - {app['start_time']} to {app['end_time']}")

        choice = int(input("Select an appointment to approve (by number): "))

        if 1 <= choice <= len(appointments):
            app_id = appointments[choice - 1]['id']
            query = "UPDATE appointments SET status = 'approved' WHERE appointment_id = %s"
            self.execute_query(query, (app_id,), fetch=False)
            print("Appointment approved.")
        else:
            print("Invalid choice.")

    def doctor_module(self):
        print("Welcome Doctor!")
        while True:
            print("1. View Assigned Patients")
            print("2. Manage Prescriptions")
            print("3. View Schedule")
            print("4. Apply for Leave")
            print("5. View Salary")
            print("6. Update Schedule")
            print("7. Approve Appointments")
            print("8. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                patients = self.view_assigned_patients()
                for patient in patients:
                    print(patient)
            elif choice == "2":
                patient_id = int(input("Enter patient ID: "))
                medicine = input("Enter medicine name: ")
                dosage = input("Enter dosage: ")
                self.manage_prescriptions(patient_id, medicine, dosage)
                print("Prescription added.")
            elif choice == "3":
                schedule = self.view_doctor_schedule()
                for entry in schedule:
                    print(entry)
            elif choice == "4":
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                self.apply_for_leave(start_date, end_date)
                print("Leave request submitted.")
            elif choice == "5":
                salary = self.view_salary()
                print(f"Your salary: {salary}")
            elif choice == "6":
                day = input("Enter day (e.g., Monday, Tuesday): ")
                start_time = input("Enter start time (HH:MM:SS): ")
                end_time = input("Enter end time (HH:MM:SS): ")
                self.update_schedule(day, start_time, end_time)
                print("Schedule updated.")
            elif choice == "7":
                self.approve_appointment()
            elif choice == "8":
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'hospital_management'
    }
    
    doctor_id = int(input("Enter your doctor ID: "))
    doctor_module = DoctorModule(config, doctor_id)
    doctor_module.doctor_module()
