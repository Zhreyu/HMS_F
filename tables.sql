-- Doctors Table
CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    salary FLOAT NOT NULL,
    leave_balance INT NOT NULL DEFAULT 5
);

-- Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    assigned_doctor_id INT,
    FOREIGN KEY (assigned_doctor_id) REFERENCES doctors(id)
);

-- Employees Table (covers pharmacists, other staff, and potentially more roles)
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role CHAR(2) NOT NULL,
    salary FLOAT NOT NULL
);

-- Leave Requests Table
CREATE TABLE leave_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    start_date DATE,
    end_date DATE,
    status ENUM('approved', 'rejected', 'pending') NOT NULL
);

-- Prescriptions Table
CREATE TABLE prescriptions (
    patient_id INT,
    doctor_id INT,
    medicine VARCHAR(255) NOT NULL,
    dosage VARCHAR(255) NOT NULL,
    PRIMARY KEY(patient_id, doctor_id, medicine),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

-- Doctor Schedule Table
CREATE TABLE doctor_schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT NOT NULL,
    day VARCHAR(50) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    appointment_approved BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

-- Pharmacy Inventory Table
CREATE TABLE pharmacy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price FLOAT NOT NULL
);

-- Medical Bills Table
CREATE TABLE medical_bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    amount FLOAT NOT NULL,
    date DATE,
    paid_status ENUM('paid', 'unpaid') NOT NULL,
    payment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('approved', 'pending', 'completed') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);
CREATE TABLE login_info (
    serial_number INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role CHAR(2) NOT NULL  -- D for doctor, PH for pharmacist, O for other staff, etc.
);


