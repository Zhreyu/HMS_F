import mysql.connector
from tables import setup_database  # Assuming tables.py contains a function named setup_database
from AdminModule import AdminModule
from DoctorModule import DoctorModule
from PatientModule import PatientModule
from PharmacistModule import PharmacistModule
from OtherStaffModule import OtherStaffModule

config = {
    'host': 'your_host',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_database'
}

def login():
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    query = "SELECT role FROM login_info WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return result[0] if result else None

def main():
    # Setup the database tables
    setup_database(config)
    
    while True:
        user_role = login()
        
        if not user_role:
            print("Invalid login. Please try again.")
            continue
        
        if user_role == 'admin':
            admin_module = AdminModule(config)
            admin_module.admin_module()
        elif user_role == 'doctor':
            doctor_id = input("Enter your doctor ID: ")
            doctor_module = DoctorModule(config, doctor_id)
            doctor_module.doctor_module()
        elif user_role == 'patient':
            patient_id = input("Enter your patient ID: ")
            patient_module = PatientModule(config)
            patient_module.patient_module(patient_id)
        elif user_role == 'pharmacist':
            pharmacist_module = PharmacistModule(config)
            pharmacist_module.pharmacist_module()
        elif user_role == 'other':
            other_staff_module = OtherStaffModule(config)
            other_staff_module.other_staff_module()
        else:
            print("Invalid role. Please try again.")

if __name__ == "__main__":
    main()
