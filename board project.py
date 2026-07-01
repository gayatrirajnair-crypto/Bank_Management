import mysql.connector as ms
from prettytable import PrettyTable

print("**********BANK MANAGEMENT***********")


def gus(username):
  conn = ms.connect(host='localhost', user='root', passwd='root1234', database='bank')
  cl = conn.cursor()

        # Query to find staff ID based on username
  cl.execute("SELECT sid FROM up WHERE username = %s AND role = 'staff'", (username,))
  result = cl.fetchone()

        # If the result is found, return the staff ID
  if result:
    for i in result:
      return i
  else:
    print(f"No staff found with username '{username}'.")



def guc(username):
  conn = ms.connect(host='localhost', user='root', passwd='root1234', database='bank')
  cl = conn.cursor()
  cl.execute("SELECT cid FROM up WHERE username = %s", (username,))
  result = cl.fetchone()
  if result:
    for i in result:
      return i
  else:
    print(f"No customer found with username '{username}'.")
 

t=0
def authenticate(u,p):
   t=0
   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')
   cl=conn.cursor()
   cl.execute('SELECT password, role FROM up WHERE username = %s', (u,))

   r=cl.fetchone()

   
   if r:

      if r[0]==p:
         print("Login successful")
         t+=1
         if t==0:
            pass
         else:
            if r[1]=='admin':
               admin_page(u)
            elif r[1]=='staff':
               staff_page(u)
            elif r[1]=='customer':
               customer_page(u)

      

      else:
         print("incorrect username or password entered!")
   else:
      print("INCORRECT!")

      
      

def admin_page(u):
   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')
   cl=conn.cursor()
   while True:
      print('''
   Select:
   1. to view all users
   2. to search for customer or staff
   3. to view/edit staff salary
   4. to view transactions
   5. to change role of staff to admin
   6. to add new staff member
   7. to delete a record
   8. logout''')

      ch=int(input("Enter your choice: "))

      if ch==1:
         print("***************VIEW ALL USERS****************")
         cl.execute("SELECT * FROM cdata")  
         customers = cl.fetchall()
         print("Customers:")
         if customers:
           table = PrettyTable(["Customer ID", "First Name", "Last Name", "Email", "Phone", "Address", "Account Balance"])
           for i in customers:
             table.add_row(i)
           print(table)
           
            
         cl.execute("SELECT * FROM sdata") 
         staff = cl.fetchall()
         if staff:
           table = PrettyTable(["Staff ID", "First Name", "Last Name", "Email", "Phone", "Role", "Hire Date", "Salary"])
           print("Staff:")
           for member in staff:
              table.add_row(member)
           print(table)

      if ch==2:
         print("***************SEARCH*********************")
         x=int(input("Enter 1 for staff and 2 for customer: "))
         if x == 1:
            sid = int(input("Enter staff ID to search: "))
            cl.execute("SELECT * FROM sdata WHERE sid = %s", (sid,))
            staff = cl.fetchone()
            if staff:
                table = PrettyTable(["Staff ID", "First Name", "Last Name", "Email", "Phone", "Role", "Hire Date", "Salary"])
                table.add_row(staff)
                print(table)
            else:
                print("Staff not found.")
         elif x == 2:
            cid = int(input("Enter customer ID to search: "))
            cl.execute("SELECT * FROM cdata WHERE cid = %s", (cid,))
            customer = cl.fetchone()
            if customer:
                table = PrettyTable(["Customer ID", "First Name", "Last Name", "Email", "Phone", "Address", "Account Balance"])
                table.add_row(customer)
                print(table)
            else:
                print("Customer not found.")

      if ch==3:
         print('**************STAFF SALARY****************')

         sid = int(input("Enter staff ID to view/edit salary: "))
         cl.execute("SELECT salary FROM sdata WHERE sid = %s", (sid,))
         staff_salary = cl.fetchone()
         if staff_salary:
            print(f"Current salary: {staff_salary[0]}")
            edit = input("Do you want to edit salary? (y/n): ")
            if edit.lower() == 'y':
                new_salary = float(input("Enter new salary: "))
                cl.execute("UPDATE sdata SET salary = %s WHERE sid = %s", (new_salary, sid))
                conn.commit()
                print("Salary updated successfully.")
         else:
            print("Staff not found.")

      if ch==4:
         print('************TRANSACTIONS******************')
         cl.execute("SELECT * FROM transactions")
         transactions = cl.fetchall()
         table = PrettyTable(["Transaction ID", "Customer ID", "Type", "Date", "Amount", "Balance After"])
         for transaction in transactions:
           table.add_row(transaction)
         
      if ch==5:

         print('************* CHANGE ROLE ******************')

         sid = int(input("Enter staff ID to change role to admin: "))
         cl.execute("select * from up where role='staff' and sid=%s;",(sid,))
         result=cl.fetchall()
         if result:
           cl.execute("UPDATE up SET role = 'admin' WHERE sid = %s AND role='staff'", (sid,))
           conn.commit()
           print("Role updated to admin.")

         else:
           print("not found")


         
      if ch==6:
         print('*************ADD NEW STAFF****************')

         fname = input("Enter first name: ")
         lname = input("Enter last name: ")
         email = input("Enter email: ")
         phone = input("Enter phone number: ")
         role = input("Enter role: ")
         hire_date = input("Enter hire date (YYYY-MM-DD): ")
         salary = float(input("Enter salary: "))

         username = input("Enter username for the staff member: ")
         password = input("Enter password for the staff member: ")

         
         cl.execute("INSERT INTO sdata (fname, lname, email, phone, role, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                    (fname, lname, email, phone, role, hire_date, salary))
         cursor.execute("SELECT LAST_INSERT_ID()")
         sid = cursor.fetchone()[0]

         cursor.execute("""
                INSERT INTO up (username, password, role, sid)
                VALUES (%s, %s, %s, %s)
            """, (username, password, role, sid))
          
         conn.commit()
         print("New staff member added successfully.")
      if ch==7:
         print("***********DELETE A RECORD**************")
         delete_choice = int(input("Enter 1 to delete customer or 2 to delete staff: "))
         if delete_choice == 1:
           cid = int(input("Enter customer ID to delete: "))
           cl.execute('select * from cdata where cid=%s',(cid,))
           cust=cl.fetchone()
           if cust:
             cl.execute("DELETE FROM cdata WHERE cid = %s", (cid,))
             conn.commit()
             print("Customer deleted successfully.")
           else:
             print("Not Found")
         elif delete_choice == 2:
           sid = int(input("Enter Staff ID to delete: "))
           cl.execute('select * from sdata where sid=%s',(sid,))
           st=cl.fetchone()
           if st:
             cl.execute("DELETE FROM sdata WHERE sid = %s", (sid,))
             conn.commit()
             print("Staff deleted successfully.")
           else:
             print("Not Found")
      if ch==8:
         print("loging out....")
         break
   

def customer_page(u):
  conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')
  cl=conn.cursor()
  while True:
    cid=guc(u)
    print('''
   Select:
   1. To update details
   2. Contact info of employee assigned to you
   3. Apply for loan
   4. Make a transaction
   5. Logout''')

    ch=int(input("Enter your choice: "))

    if ch==1:
      print("***************UPDATE DETAILS****************")

         


      cl.execute("SELECT * FROM cdata WHERE cid = %s", (cid,))
      customer = cl.fetchone()
      if customer:
        table = PrettyTable(["ID", "Name", "  Surame     ","        DOB        ", "       Email                                    ", "               Phone             ", "       Location/Address                         ", "      Account Balance       "])
        table.add_row(customer)

        print(table)
        update = input("Do you want to update your details? (y/n): ")
        if update.lower() == 'y':
          while True:
            print('''what would you like to change:

1. Last Name
2. email
3. Phone
4. Address
5.Exit
''')
            c=int(input("Enter your choice: "))
            if c==1:
              lname = input("Enter new last name: ")
              cl.execute("UPDATE cdata SET lname = %s WHERE cid = %s", (lname, cid))
            if c==2:
              email = input("Enter new email : ")
              cl.execute("UPDATE cdata SET email = %s WHERE cid = %s", (email, cid))
                
            if c==3:
              phone = input("Enter new phone number : ")
              cl.execute("UPDATE cdata SET phone = %s WHERE cid = %s", (phone, cid))
            if c==4:
              address = input("Enter new address : ")
              cl.execute("UPDATE cdata SET address = %s WHERE cid = %s", (address, cid))
            if c==5:
                print("exiting...")
                break



            conn.commit()
            print("Your details have been updated.")
      else:
        print("Customer not found.")


    if ch==2:
      print("***************CONTACT INFO*********************")
         
      cl.execute("SELECT sdata.fname, sdata.lname, sdata.phone, sdata.email FROM sdata "
                 "JOIN up ON sdata.sid = up.sid WHERE up.cid = %s", (cid,))
      employee = cl.fetchone()
      if employee:
        print(f"Employee Assigned: {employee[0]} {employee[1]}")
        print(f"Phone: {employee[2]}")
        print(f"Email: {employee[3]}")
      else:
        print("No employee assigned or customer not found.")



    if ch==3:
      print("************LOAN APPLICATION*************")
         
      cl.execute("SELECT * FROM loan WHERE cid = %s", (cid,))
      existing_loan = cl.fetchone()
      if existing_loan:
        print("You already have an active loan application.")
      else:
        lamount = float(input("Enter loan amount: "))
        ltype = input("Enter loan type (e.g., personal, home): ")
        interest = float(input("Enter interest rate: "))
        start_date = input("Enter loan start date (YYYY-MM-DD): ")
        end_date = input("Enter loan end date (YYYY-MM-DD): ")
        status = "Pending"
        cl.execute("INSERT INTO loan (cid, lamount, ltype, interest, start_date, end_date, status) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (cid, lamount, ltype, interest, start_date, end_date, status))
        conn.commit()
        print("Your loan application has been submitted successfully.")

    if ch==4:
         print("************TRANSACTION********************")
         
         transaction_type = input("Enter transaction type (Deposit/Withdrawal): ")
         
         amount = float(input("Enter transaction amount: "))
         cl.execute("SELECT abalance FROM cdata WHERE cid = %s", (cid,))


         current_balance = cl.fetchone()
         print("your bank balance is: ",current_balance)
         if current_balance:
            new_balance = current_balance[0]
            if transaction_type.lower() == "deposit":
                new_balance += amount
            elif transaction_type.lower() == "withdrawal":
                if amount <= current_balance[0]:
                    new_balance -= amount
                else:
                    print("Insufficient balance for withdrawal.")
                    continue
            cl.execute("UPDATE cdata SET abalance = %s WHERE cid = %s", (new_balance, cid))
            cl.execute("INSERT INTO transactions (cid, type, date, amount, balance_after) VALUES (%s, %s, CURDATE(), %s, %s)",
                        (cid, transaction_type, amount, new_balance))
            conn.commit()
            print(f"Transaction successful. New balance: {new_balance}")
         else:
            print("Customer not found.")
    if ch==5:
         print("logging out...")
         break

def staff_page(u):
   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')
   cl=conn.cursor()
   while True:
      print('''
   Select:
   1. Search for a customer
   2. Edit loan details
   3. Edit transaction details
   4. Add a customer
   5. Delete a customer
   6. View Your Salary Details
   7. Log Out''')
      ch=int(input("Enter your choice: "))

      if ch==1:
         print("***************VIEW CUSTOMERS****************")
         cid = int(input("Enter customer ID to search: "))
         cl.execute("SELECT * FROM cdata WHERE cid = %s", (cid,))
         customer = cl.fetchone()
         if customer:
           table = PrettyTable(["Customer ID", "First Name", "Last Name", "Email", "Phone", "Address", "Account Balance"])
           table.add_row(customer)
           print(table)
         else:
            print("Customer not found.")

      if ch==2:
         print("***************EDIT LOAN DETAILS*********************")

         cid = int(input("Enter customer ID to edit loan: "))


         cl.execute("SELECT * FROM loan WHERE cid = %s", (cid,))
         loan = cl.fetchone()

         if loan:
           print("Loan details:", loan)
           print("What would you like to edit?")
           print("1. Change Loan Amount")
           print("2. Change Interest Rate")
           print("3. Change Loan Status")
           print("4. Exit")

           choice = int(input("Enter your choice: "))

           if choice == 1:
              # Change loan amount
              new_amount = float(input("Enter new loan amount: "))
              cl.execute("UPDATE loan SET lamount = %s WHERE cid = %s", (new_amount, cid))
              conn.commit()
              print("Loan amount updated successfully.")

           elif choice == 2:
              # Change interest rate
              new_interest = float(input("Enter new interest rate: "))
              cl.execute("UPDATE loan SET interest = %s WHERE cid = %s", (new_interest, cid))
              conn.commit()
              print("Interest rate updated successfully.")

           elif choice == 3:
              # Change loan status
              new_status = input("Enter new loan status (e.g., 'Approved', 'Pending', 'Rejected'): ")
              cl.execute("UPDATE loan SET status = %s WHERE cid = %s", (new_status, cid))
              conn.commit()
              print("Loan status updated successfully.")

           elif choice == 4:
              print("Exiting the loan editing process.")

           else:
              print("Invalid choice, please try again.")

         else:
           print("No loan found for this customer.")

      if ch==3:

         print('************ TRANSACTIONS ******************')
         tid = int(input("Enter transaction ID to edit: "))
         cl.execute("SELECT * FROM transactions WHERE tid = %s", (tid,))
         transaction = cl.fetchone()
         if transaction:
            table = PrettyTable(["Transaction ID", "Customer ID", "Type", "Date", "Amount", "Balance After"])
            for transaction in transactions:
              table.add_row(transaction)
              print(table)
            edit = input("Do you want to edit transaction details? (y/n): ")
            if edit.lower() == 'y':
                new_amount = float(input("Enter new transaction amount: "))
                cl.execute("UPDATE transactions SET amount = %s WHERE tid = %s", (new_amount, tid))
                conn.commit()
                print("Transaction updated successfully.")
         else:
            print("Transaction not found.")

      if ch==4:
         print("**********ADD A CUSTOMER***************")

         fname = input("Enter first name: ")
         lname = input("Enter last name: ")
         dob = input("Enter date of birth (YYYY-MM-DD): ")
         email = input("Enter email: ")
         phone = input("Enter phone number: ")
         address = input("Enter address: ")
         abalance = float(input("Enter account balance: "))

         username = input("Enter username for the customer: ")
         password = input("Enter password for the customer: ")

         cl.execute("INSERT INTO cdata (fname, lname, dob, email, phone, address, abalance) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                    (fname, lname, dob, email, phone, address, abalance))

         cursor.execute("SELECT LAST_INSERT_ID()")
         cid = cursor.fetchone()[0]

         cursor.execute("""
                INSERT INTO up (username, password, role, cid)
                VALUES (%s, %s, 'customer', %s)
            """, (username, password, cid))

          



         conn.commit()
         print("Customer added successfully.")
      if ch==5:
         print("**********DELETE A CUSTOMER***********")

         cid = int(input("Enter customer ID to delete: "))
         cl.execute('select * from cdata where cid=%s',(cid))
         cust=cl.fetchone()
         if cust:
           cl.execute("DELETE FROM cdata WHERE cid = %s", (cid,))
           conn.commit()
           print("Customer deleted successfully.")

         else:
            print("Customer not found")
      if ch==6:
         print("************VIEW SALARY**************")
         sid = gus(u)
         cl.execute("SELECT salary FROM sdata WHERE sid = %s", (sid,))
         staff_salary = cl.fetchone()
         if staff_salary:
            print(f"Your current salary is: {staff_salary[0]}")
         else:
            print("Staff not found.")
      if ch==7:
         print("logging out..")
         break


def login():
   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')
   cl=conn.cursor()


   u=input("Enter your username: ")
   p=input("Enter your password: ")

   authenticate(u,p)


while True:
   c=int(input("Enter 1 to Login and any other number to sign out: "))

   if c==1:
      login()
   else:
      break

