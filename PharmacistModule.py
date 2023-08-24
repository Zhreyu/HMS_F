import mysql.connector
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

    def view_inventory():
        try:
            cursor.execute("SELECT * FROM pharmacy")
            inventory = cursor.fetchall()
            if not inventory:
                print("Inventory is empty.")
                return

            print("\nInventory:")
            for item in inventory:
                print(f"Medicine ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}")
        except Exception as e:
            print("An error occurred:", e)

    def update_inventory():
        medicine_id = input("Enter medicine ID (or 'new' if it's a new medicine): ")
        
        if medicine_id == 'new':
            medicine_name = input("Enter new medicine name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            try:
                query = "INSERT INTO pharmacy (name, quantity, price) VALUES (%s, %s, %s)"
                cursor.execute(query, (medicine_name, quantity, price))
                db.commit()
                print("New medicine added to inventory.")
            except Exception as e:
                print("An error occurred:", e)
        else:
            medicine_name = input("Enter updated medicine name (or press enter to skip): ")
            quantity = input("Enter quantity to add/update (or press enter to skip): ")
            price = input("Enter updated price (or press enter to skip): ")
            
            query_parts = []
            values = []

            if medicine_name:
                query_parts.append("name = %s")
                values.append(medicine_name)
            if quantity:
                query_parts.append("quantity = quantity + %s")
                values.append(int(quantity))
            if price:
                query_parts.append("price = %s")
                values.append(float(price))

            if query_parts:
                try:
                    query = f"UPDATE pharmacy SET {', '.join(query_parts)} WHERE id = %s"
                    values.append(medicine_id)
                    cursor.execute(query, values)
                    db.commit()
                    print("Medicine inventory updated successfully.")
                except Exception as e:
                    print("An error occurred:", e)
            else:
                print("No updates provided.")

    
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

