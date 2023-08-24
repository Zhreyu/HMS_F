import mysql.connector
class OtherStaffModule:
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

    def apply_for_leave(self, user_id):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        query = "INSERT INTO leave_requests (user_id, start_date, end_date, status) VALUES (%s, %s, %s, 'pending')"
        values = (user_id, start_date, end_date)
        self.execute_query(query, values, fetch=False)
        print("Leave request submitted.")

    def view_salary_info(self, user_id):
        query = "SELECT salary FROM employees WHERE id = %s"
        result = self.execute_query(query, (user_id,))
        if result:
            print(f"Your salary: {result[0][0]}")
        else:
            print("Error retrieving salary info.")

    def view_personal_info(self, user_id):
        query = "SELECT * FROM employees WHERE id = %s"
        result = self.execute_query(query, (user_id,))
        if result:
            user_info = result[0]
            print(f"ID: {user_info[0]}")
            print(f"Name: {user_info[1]}")
            print(f"Role: {user_info[2]}")
            print(f"Salary: {user_info[3]}")
        else:
            print("Error retrieving personal info.")

    def other_staff_module(self, user_id):
        print("Welcome Staff Member!")

        while True:
            print("\nStaff Options:")
            print("1. Apply for Leave")
            print("2. View Salary")
            print("3. View Personal Info")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.apply_for_leave(user_id)
            elif choice == "2":
                self.view_salary_info(user_id)
            elif choice == "3":
                self.view_personal_info(user_id)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

        self.db.close()
