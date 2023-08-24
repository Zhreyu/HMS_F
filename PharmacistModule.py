class PharmacistModule:
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

    def view_inventory(self):
        try:
            # Your view_inventory code
        except Exception as e:
            print("An error occurred:", e)

    def update_inventory():
        medicine_name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity to add/update: "))
        price = float(input("Enter price: "))
        try:
            query = """
            INSERT INTO pharmacy_inventory (medicine_name, quantity, price) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE quantity=quantity+%s, price=%s
            """
            cursor.execute(query, (medicine_name, quantity, price, quantity, price))
            db.commit()
            print("Inventory updated successfully.")
        except Exception as e:
            print("An error occurred:", e)

    
    def view_salary_info(user_id):
        try:
            query = "SELECT salary FROM employees WHERE id = %s"
            cursor.execute(query, (user_id,))
            salary = cursor.fetchone()
            if salary:
                print(f"Your salary: {salary[0]}")
            else:
                print("Error retrieving salary info.")
        except Exception as e:
            print(
                "An error occurred:", e)
    
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

    def pharmacist_module(user_id):
        print("Welcome Pharmacist!")
        
        while True:
            print("\nPharmacist Options:")
            print("1. View Inventory")
            print("2. Update Inventory")
            print("3. View Salary")
            print("4. Apply for Leave")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                view_inventory()
            elif choice == "2":
                update_inventory()
            elif choice == "3":
                view_salary_info(user_id)
            elif choice == "4":
                apply_for_leave(user_id)
            elif choice == "5":
                print("Logging out...\n")
                break
            else:
                print("Invalid option, please try again.")

