import mysql.connector
from AdminModule import AdminModule
from DoctorModule import DoctorModule
from PatientModule import PatientModule
from PharmacistModule import PharmacistModule
from OtherStaffModule import OtherStaffModule

config = {
    'user': 'root',
    'password': 'shreyas',
    'host': 'localhost',
    'database': 'hms'
}

def login(username,password):
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
   # username = input("Enter username: ")
  #  password = input("Enter password: ")
    
    query = "SELECT role FROM login_info WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return result[0] if result else None
def fetch_id(username):
    db = mysql.connector.connect(**config)
    cursor=db.cursor()
    query=f"SELECT user_id FROM login_info where username='{username}'"
    cursor.execute(query)
def main():
    
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_role = login(username,password)
        print(user_role)
        
        if not user_role:
            print("Invalid login. Please try again.")
            continue
        
        if user_role == "AD":
            admin_module = AdminModule(config)
            admin_module.admin_module()
        elif user_role == 'D':
            doctor_id = fetch_id(username)
            doctor_module = DoctorModule(config, doctor_id)
            doctor_module.doctor_module()
        elif user_role == 'PT':
            patient_id = fetch_id(username)
            patient_module = PatientModule(config)
            patient_module.patient_module(patient_id)
        elif user_role == 'PH':
            pharmacist_module = PharmacistModule(config)
            pharmacist_module.pharmacist_module()
        elif user_role == 'O':
            other_staff_module = OtherStaffModule(config)
            other_staff_module.other_staff_module()
        else:
            print("Invalid role. Please try again.")

if __name__ == "__main__":
    main()
