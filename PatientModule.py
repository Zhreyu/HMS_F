import mysql.connector

class PatientModule:
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

    def get_assigned_doctor_info(self, patient_id):
        try:
            query = """
            SELECT doctors.id AS assigned_doctor_id, doctors.name AS doctor_name
            FROM patients
            JOIN doctors ON patients.assigned_doctor_id = doctors.id
            WHERE patients.id = %s
            """
            result = self.execute_query(query, (patient_id,))
            return result[0] if result else None
        except Exception as e:
            print("An error occurred:", e)
            return None

    def view_prescriptions_by_patient(self, patient_id):
        query = "SELECT * FROM prescriptions WHERE patient_id = %s"
        return self.execute_query(query, (patient_id,))

    def view_medical_bills(self, patient_id):
        query = "SELECT * FROM medical_bills WHERE patient_id = %s"
        return self.execute_query(query, (patient_id,))

    def pay_medical_bill(self, bill_id):
        query = "UPDATE medical_bills SET paid_status = 'paid', payment_date = CURRENT_DATE WHERE id = %s"
        self.execute_query(query, (bill_id,), fetch=False)

    def make_appointment(self, patient_id, doctor_id, date):
        query = """
        INSERT INTO appointments (doctor_id, patient_id, appointment_date, start_time, end_time, status) 
        VALUES (%s, %s, %s, '09:00:00', '10:00:00', 'pending')
        """
        values = (doctor_id, patient_id, date)

        self.execute_query(query,values, fetch=False)

    def patient_module(self, patient_id):
        print("Welcome Patient!")

        while True:
            print("\nPatient Options:")
            print("1. View Assigned Doctor")
            print("2. View Prescriptions")
            print("3. View Medical Bills")
            print("4. Pay Medical Bill")
            print("5. Make Appointment")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                doctor_info = self.get_assigned_doctor_info(patient_id)
                if doctor_info:
                    print(f"Assigned Doctor ID: {doctor_info['assigned_doctor_id']}")
                    print(f"Doctor Name: {doctor_info['doctor_name']}")
                else:
                    print("No assigned doctor found for the given patient.")
            elif choice == "2":
                prescriptions = self.view_prescriptions_by_patient(patient_id)
                for prescription in prescriptions:
                    print(prescription)
            elif choice == "3":
                medical_bills = self.view_medical_bills(patient_id)
                for bill in medical_bills:
                    print(bill)
            elif choice == "4":
                bill_id = int(input("Enter the ID of the bill you want to pay: "))
                self.pay_medical_bill(bill_id)
                print("Medical bill paid.")
            elif choice == "5":
                doctor_id = int(input("Enter the ID of the doctor you want to make an appointment with: "))
                date = input("Enter the appointment date (YYYY-MM-DD): ")
                self.make_appointment(patient_id, doctor_id, date)
                print("Appointment made.")
            elif choice == "6":
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

    patient_id = int(input("Enter your patient ID: "))
    patient_module = PatientModule(config)
    patient_module.patient_module(patient_id)
