import mysql.connector

# Database configuration
config = {
    'user': 'root',
    'password': 'shreyas',
    'host': 'localhost',
    'database': 'HMS_F'
}

# Connect to the MySQL server
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Create tables
commands = [
    # Users Table
    """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        role ENUM('doctor', 'patient', 'pharmacist', 'staff', 'admin') NOT NULL,
        account_status ENUM('active', 'inactive') DEFAULT 'active'
    )
    """,
    # Doctors Table
    """
    CREATE TABLE IF NOT EXISTS doctors (
        user_id INT PRIMARY KEY,
        speciality VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """,
    # Patients Table
    """
    CREATE TABLE IF NOT EXISTS patients (
        user_id INT PRIMARY KEY,
        doctor_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (doctor_id) REFERENCES users(id)
    )
    """,
    # Pharmacists Table
    """
    CREATE TABLE IF NOT EXISTS pharmacists (
        user_id INT PRIMARY KEY,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """,
    # Staff Table
    """
    CREATE TABLE IF NOT EXISTS staff (
        user_id INT PRIMARY KEY,
        job_title VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """,
    # Prescriptions Table
    """
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        doctor_id INT,
        medicine_name VARCHAR(255),
        dose VARCHAR(255),
        FOREIGN KEY (patient_id) REFERENCES users(id),
        FOREIGN KEY (doctor_id) REFERENCES users(id)
    )
    """,
    # Appointments Table
    """
    CREATE TABLE IF NOT EXISTS appointments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        doctor_id INT,
        appointment_date DATE,
        FOREIGN KEY (patient_id) REFERENCES users(id),
        FOREIGN KEY (doctor_id) REFERENCES users(id)
    )
    """,
    # Medicines Table
    """
    CREATE TABLE IF NOT EXISTS medicines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        quantity INT,
        pharmacist_id INT,
        FOREIGN KEY (pharmacist_id) REFERENCES users(id)
    )
    """,
    # Bills Table
    """
    CREATE TABLE IF NOT EXISTS bills (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        amount FLOAT,
        payment_status ENUM('paid', 'unpaid'),
        FOREIGN KEY (patient_id) REFERENCES users(id)
    )
    """,
    # Leaves Table
    """
    CREATE TABLE IF NOT EXISTS leaves (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        start_date DATE,
        end_date DATE,
        status ENUM('approved', 'pending', 'rejected'),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """,
    # Salaries Table
    """
    CREATE TABLE IF NOT EXISTS salaries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        amount FLOAT,
        payment_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
]

# Execute each command
for command in commands:
    cursor.execute(command)

# Close the connection
cursor.close()
connection.close()
