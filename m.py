import mysql.connector as ms
from prettytable import PrettyTable
import random
conn = ms.connect(host='localhost', user='root', passwd='root1234', database='bank')
cl = conn.cursor()


def customer_panel(username):
    while True:
        print("\nCustomer Panel:")
        print("1. View My Details")
        print("2. Change My Username/Password")
        print("3. Update My Details")
        print("4. Make a Transaction")
        print("5. Apply for a Loan/Card")
        print("6. Cancel Loan")
        print("7. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_my_details()  # View customer details
        elif choice == 2:
            change_my_username_password(username)  # Change username/password
        elif choice == 3:
            update_my_details(username)  # Update personal details
        elif choice == 4:
            make_transaction(username)  # Make transaction
        elif choice == 5:
            apply_for_loan_or_card(username)  # Apply for loan/card
        elif choice == 6:
            cancel_loan(username)  # Cancel loan
        elif choice == 7:
            print("Logging out...")
            break  # Exit the customer panel and log out
        else:
            print("Invalid choice, please try again.")
def view_my_details(username):
    # Query the customer's details from the database
    cl.execute('SELECT * FROM customer_data WHERE username = %s', (username,))
    customer = cl.fetchone()

    if customer:
        print(f"\nAccount No: {customer[0]}")
        print(f"Name: {customer[1]}")
        print(f"Balance: {customer[2]}")
        print(f"Location: {customer[3]}")
        print(f"Phone: {customer[4]}")
        print(f"Designation: {customer[5]}")
        print(f"Date Joined: {customer[6]}")
        print(f"Age: {customer[7]}")
    else:
        print("Customer not found.")
def change_my_username_password(username):
    new_username = input("Enter your new username: ")
    new_password = input("Enter your new password: ")

    # Update the customer's username and password
    cl.execute('UPDATE customerusername SET username = %s, password = %s WHERE username = %s', 
               (new_username, new_password, username))
    conn.commit()

    print("Your username and password have been updated.")
def update_my_details(username):
    print("\nWhich detail would you like to update?")
    print("1. Name")
    print("2. Location")
    print("3. Phone")
    print("4. Designation")
    print("5. Age")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_name = input("Enter your updated name: ")
        cl.execute('UPDATE customer_data SET name = %s WHERE username = %s', (new_name, username))
        conn.commit()
        print("Your name has been updated.")

    elif choice == 2:
        new_location = input("Enter your updated location: ")
        cl.execute('UPDATE customer_data SET location = %s WHERE username = %s', (new_location, username))
        conn.commit()
        print("Your location has been updated.")

    elif choice == 3:
        new_phone = input("Enter your updated phone number: ")
        cl.execute('UPDATE customer_data SET phone = %s WHERE username = %s', (new_phone, username))
        conn.commit()
        print("Your phone number has been updated.")

    elif choice == 4:
        new_designation = input("Enter your updated designation: ")
        cl.execute('UPDATE customer_data SET designation = %s WHERE username = %s', (new_designation, username))
        conn.commit()
        print("Your designation has been updated.")

    elif choice == 5:
        new_age = int(input("Enter your updated age: "))
        cl.execute('UPDATE customer_data SET age = %s WHERE username = %s', (new_age, username))
        conn.commit()
        print("Your age has been updated.")

    else:
        print("Invalid choice.")
def make_transaction(username):
    amount = float(input("Enter the amount you want to transfer: "))
    recipient_account = input("Enter the recipient's account number: ")

    # Check if the customer has sufficient balance
    cl.execute('SELECT balance FROM customer_data WHERE username = %s', (username,))
    customer = cl.fetchone()

    if customer and customer[0] >= amount:
        # Update the sender's balance
        cl.execute('UPDATE customer_data SET balance = balance - %s WHERE username = %s', 
                   (amount, username))

        # Update the recipient's balance
        cl.execute('UPDATE customer_data SET balance = balance + %s WHERE account_no = %s', 
                   (amount, recipient_account))
        conn.commit()
        print(f"Transaction of {amount} to account {recipient_account} has been completed.")
    else:
        print("Insufficient balance or invalid account number.")
def apply_for_loan_or_card(username):
    print("\n1. Apply for a Loan")
    print("2. Apply for a Credit Card")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        loan_amount = float(input("Enter the loan amount you want to apply for: "))
        loan_type = input("Enter the type of loan (e.g., Personal, Car, Home): ")
        cl.execute('INSERT INTO loan_applications (username, loan_amount, loan_type) VALUES (%s, %s, %s)',
                   (username, loan_amount, loan_type))
        conn.commit()
        print(f"Your loan application of {loan_amount} for {loan_type} has been submitted. You will receive an email response in 2-5 business days.")

    elif choice == 2:
        card_type = input("Enter the type of card (e.g., Debit, Credit): ")
        cl.execute('INSERT INTO card_applications (username, card_type) VALUES (%s, %s)', 
                   (username, card_type))
        conn.commit()
        print(f"Your {card_type} card application has been submitted. You will receive an email response in 2-5 business days.")

    else:
        print("Invalid choice.")
def cancel_loan(username):
    cl.execute('SELECT * FROM loan_applications WHERE username = %s AND status = %s', (username, 'Pending'))
    loan = cl.fetchone()

    if loan:
        print(f"Loan Application ID: {loan[0]}")
        cancel_choice = input("Do you want to cancel this loan application? (yes/no): ").lower()

        if cancel_choice == 'yes':
            cl.execute('DELETE FROM loan_applications WHERE username = %s AND status = %s', (username, 'Pending'))
            conn.commit()
            print("Your loan application has been canceled.")
        else:
            print("Loan cancellation aborted.")
    else:
        print("You have no pending loan applications to cancel.")
def logout():
    print("Logging out...")
    exit()  # Exit the program or break out of the current loop in the customer panel.


def admin_panel(username):
    while True:
        print("\nAdmin Panel:")
        print("1. Add New Staff Member")
        print("2. Update Staff Salary")
        print("3. Change Staff Username/Password")
        print("4. Search for Staff Member")
        print("5. Delete Staff Member Record")
        print("6. Make Staff Member an Admin")
        print("7. View All Staff")
        print("8. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_new_staff()  # Add new staff member
        elif choice == 2:
            update_staff_salary()  # Update staff salary
        elif choice == 3:
            change_staff_username_password()  # Change staff username/password
        elif choice == 4:
            search_staff()  # Search for a staff member
        elif choice == 5:
            delete_staff_member()  # Delete a staff record
        elif choice == 6:
            make_staff_admin()  # Promote normal staff to admin
        elif choice == 7:
            view_all_staff()  # View all staff members
        elif choice == 8:
            print("Logging out...")
            break  # Exit the admin panel and log out
        else:
            print("Invalid choice, please try again.")
def add_new_staff():
    staff_id = input("Enter new staff ID: ")
    role = input("Enter staff role (Admin/Staff): ")
    salary = float(input("Enter staff salary: "))
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    cl.execute('INSERT INTO staff_credentials (staff_id, role, salary, username, password) VALUES ( %s, %s, %s, %s, %s)', 
               (staff_id,role, salary, username, password))
    conn.commit()
    print("New staff member added successfully.")
def update_staff_salary():
    staff_id = input("Enter the staff ID of the staff whose salary you want to update: ")
    new_salary = float(input("Enter the new salary: "))

    cl.execute('UPDATE staff_credentials SET salary = %s WHERE staff_id = %s', (new_salary, staff_id))
    conn.commit()
    print(f"Salary of staff ID {staff_id} has been updated to {new_salary}.")
def change_staff_username_password():
    staff_id = input("Enter the staff ID whose username/password you want to change: ")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    cl.execute('UPDATE staff_credentials SET username = %s, password = %s WHERE staff_id = %s', 
               (new_username, new_password, staff_id))
    conn.commit()
    print(f"Username and password for staff ID {staff_id} have been updated.")
def search_staff():
    search_criteria = input("Search by staff ID or username (enter 'id' or 'username'): ").lower()

    if search_criteria == 'id':
        staff_id = input("Enter the staff ID to search: ")
        cl.execute('SELECT * FROM staff_credentials WHERE staff_id = %s', (staff_id,))
        staff = cl.fetchone()
        if staff:
            print(f"\nStaff ID: {staff[0]}")
            print(f"Role: {staff[1]}")
            print(f"Salary: {staff[4]}")
            print(f"Username: {staff[3]}")
        else:
            print("Staff member not found.")

    elif search_criteria == 'username':
        username = input("Enter the username to search: ")
        cl.execute('SELECT * FROM staff_credentials WHERE username = %s', (username,))
        staff = cl.fetchone()
        if staff:
            print(f"\nStaff ID: {staff[0]}")
            print(f"Role: {staff[1]}")
            print(f"Salary: {staff[2]}")
            print(f"Username: {staff[3]}")
        else:
            print("Staff member not found.")
    else:
        print("Invalid search criteria.")
def delete_staff_member():
    staff_id = input("Enter the staff ID to delete: ")
    cl.execute('DELETE FROM staff_credentials WHERE staff_id = %s', (staff_id,))
    conn.commit()
    print(f"Staff member with ID {staff_id} has been deleted.")
def make_staff_admin():
    staff_id = input("Enter the staff ID to promote to Admin: ")
    cl.execute('UPDATE staff_credentials SET role = %s WHERE staff_id = %s', ('Admin', staff_id))
    conn.commit()
    print(f"Staff member with ID {staff_id} has been promoted to Admin.")
def view_all_staff():
    cl.execute('SELECT * FROM staff_credentials')
    staff_list = cl.fetchall()
    if staff_list:
        print("\nList of all staff members:")
        print(f"{'Staff ID':<15}{'Role':<15}{'Salary':<10}{'Username':<20}")
        print("-" * 70)
        for staff in staff_list:
            print(f"{staff[0]:<15}{staff[1]:<15}{staff[2]:<10}{staff[3]:<20}")
    else:
        print("No staff members found.")
def staff_panel(username):
    while True:
        print("\nStaff Panel:")
        print("1. View My Details")
        print("2. Change My Username/Password")
        print("3. View/Update Customer Data")
        print("4. View/Manage Loan Status")
        print("5. Search for a Customer")
        print("6. View My Transactions")
        print("7. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_my_details()  # View own details
        elif choice == 2:
            change_my_username_password(username)  # Change own username/password
        elif choice == 3:
            view_update_customer_data()  # View and update customer data
        elif choice == 4:
            view_manage_loans()  # View and manage loan status
        elif choice == 5:
            search_customer()  # Search for a customer
        elif choice == 6:
            account_no=input("Enter the Account number: ")
            view_transactions(account_no)  # View own transactions
        elif choice == 7:
            print("Logging out...")
            break  # Exit the staff panel and log out
        else:
            print("Invalid choice, please try again.")
def view_my_details():
    account_no=input("Enter your account number: ")

    cl.execute('SELECT staffid FROM staff_credentials WHERE username = %s', (username,))
    staff = cl.fetchone()
    if staff:
        cl.execute('SELECT * from staff_credentials where staff_id=%s',(staff))
        staff2 = cl.fetchone()
    if staff2:
        print(f"\nStaff ID: {staff[0]}")
        print(f"Username: {staff[1]}")
        print(f"Password: {staff[2]}")
        print(f"role: {staff[3]}")

    else:
        print("Staff member not found.")
def change_my_username_password(username):
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    cl.execute('UPDATE staff_credentials SET username = %s, password = %s WHERE username = %s', 
               (new_username, new_password, username))
    conn.commit()
    print("Your username and password have been updated.")
def view_update_customer_data():
    account_no = input("Enter the account number of the customer: ")

    # View Customer Data
    cl.execute('SELECT * FROM customer_data WHERE account_no = %s', (account_no,))
    customer = cl.fetchone()
    if customer:
        print(f"\nAccount No: {customer[0]}")
        print(f"Name: {customer[1]}")
        print(f"Bank Balance: {customer[2]}")
        print(f"Location: {customer[3]}")
        print(f"Phone: {customer[4]}")
        print(f"Designation: {customer[5]}")
        print(f"Date of Joining: {customer[6]}")
        print(f"Age: {customer[7]}")
        print(f"Assigned Staff ID: {customer[8]}")
        
        update = input("\nDo you want to update this data? (yes/no): ").lower()
        if update == 'yes':
            update_customer_data(account_no)
    else:
        print("Customer not found.")
        
def update_customer_data(account_no):
    print("Select the field you want to update:")
    print("1. Name")
    print("2. Bank Balance")
    print("3. Location")
    print("4. Phone")
    print("5. Designation")
    print("6. Age")

    field = int(input("Enter your choice: "))
    
    if field == 1:
        name = input("Enter the updated name: ")
        cl.execute('UPDATE customer_data SET name = %s WHERE account_no = %s', (name, account_no))
    elif field == 2:
        balance = float(input("Enter the updated bank balance: "))
        cl.execute('UPDATE customer_data SET bank_balance = %s WHERE account_no = %s', (balance, account_no))
    elif field == 3:
        location = input("Enter the updated location: ")
        cl.execute('UPDATE customer_data SET location = %s WHERE account_no = %s', (location, account_no))
    elif field == 4:
        phone = input("Enter the updated phone number: ")
        cl.execute('UPDATE customer_data SET phone = %s WHERE account_no = %s', (phone, account_no))
    elif field == 5:
        designation = input("Enter the updated designation: ")
def view_manage_loans():
    account_no = input("Enter the account number of the customer: ")

    # View Loan Status
    cl.execute('SELECT * FROM loan_applications WHERE account_no = %s', (account_no,))
    loan = cl.fetchone()
    if loan:
        print(f"\nLoan ID: {loan[0]}")
        print(f"Account No: {loan[1]}")
        print(f"Loan Amount: {loan[2]}")
        print(f"Loan Status: {loan[3]}")
        
        action = input("\nDo you want to update loan status? (yes/no): ").lower()
        if action == 'yes':
            new_status = input("Enter the new loan status: ")
            cl.execute('UPDATE loan_applications SET loan_status = %s WHERE account_no = %s', (new_status, account_no))
            conn.commit()
            print("Loan status has been updated.")
    else:
        print("No loan found for this customer.")
def search_customer():
    search_criteria = input("Search by account number or username (enter 'account' or 'username'): ").lower()

    if search_criteria == 'account':
        account_no = input("Enter the account number to search: ")
        cl.execute('SELECT * FROM customer_data WHERE account_no = %s', (account_no,))
        customer = cl.fetchone()
        if customer:
            print(f"\nAccount No: {customer[0]}")
            print(f"Name: {customer[1]}")
            print(f"Bank Balance: {customer[2]}")
            print(f"Location: {customer[3]}")
            print(f"Phone: {customer[4]}")
            print(f"Designation: {customer[5]}")
            print(f"Date of Joining: {customer[6]}")
            print(f"Age: {customer[7]}")
        else:
            print("Customer not found.")

    elif search_criteria == 'username':
        username = input("Enter the username to search: ")
        cl.execute('SELECT * FROM customer_data WHERE username = %s', (username,))
        customer = cl.fetchone()
        if customer:
            print(f"\nAccount No: {customer[0]}")
            print(f"Name: {customer[1]}")
            print(f"Bank Balance: {customer[2]}")
            print(f"Location: {customer[3]}")
            print(f"Phone: {customer[4]}")
            print(f"Designation: {customer[5]}")
            print(f"Date of Joining: {customer[6]}")
            print(f"Age: {customer[7]}")
        else:
            print("Customer not found.")
    else:
        print("Invalid search criteria.")
def view_transactions(account_no):
    cl.execute('SELECT * FROM transactions WHERE account_no = %s', (account_no,))
    transactions = cl.fetchall()
    if transactions:
        print("\nList of transactions:")
        for transaction in transactions:
            print(f"\nTransaction ID: {transaction[0]}")
            print(f"Account No: {transaction[1]}")
            print(f"Transaction type: {transaction[2]}")
            print(f"Transaction Amount: {transaction[3]}")
            print(f"Transaction Date: {transaction[4]}")
    else:
        print("No transactions found for you.")
