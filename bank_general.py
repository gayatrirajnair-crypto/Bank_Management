import mysql.connector as ms



conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

cl=conn.cursor()
cl.execute('use bank;')
def display():
   # Get the column names from the cursor
   column_names = [desc[0] for desc in cl.description]

# Print the column headers
   print('\t'.join(column_names))

# Print each row with values
   for row in cl.fetchall():
       print('\t'.join(map(str, row)))

   for i in cl.fetchall():
      for j in i:
         print(j,end='\t')
      print()
      
def change_username(sid):
   new_username=input("Enter new username: ")
   cl.execute('set sql_safe_updates=0;')
   cl.execute('UPDATE staffusername SET username=%s where staffid=%s',(new_username,sid,))
   cl.commit()

def change_password(sid):
   new_username=input("Enter new password: ")
   cl.execute('set sql_safe_updates=0;')
   cl.execute('UPDATE staffusername SET password=%s where staffid=%s',(new_username,sid,))
   cl.commit()

def edit_card_status():
   ch=int(input('''Enter a choice:
1. Update card limit
2. Change Status
3. Add a New Card'''))

   if ch==1:
      x=float(input("Enter a new card limit: "))
      acc=input("Enter account number: ")

      cl.execute('UPDATE card_status SET card_limit=%s where account_no=%s',(x,acc,))
      cl.commit()

   if ch==2:
      x=input("Enter a new card status: ")
      acc=input("Enter account number: ")

      cl.execute('UPDATE card_status SET status=%s where account_no=%s',(x,acc,))
      cl.commit()

   if ch==3:
      acc=input("Enter account number: ")
      st=input("Enter status: ")
      ct=input("Enter card type: ")
      DOI=input("Enter Date of issue in YYYY-MM-DD format: ")
      cl=float(input("Enter card limit: "))

      cl.execute('INSERT into card_status values(%s,%s,%s,%s,%s)',(acc,st,ct,DOI,cl))
      conn.commit()
   else:
      print("INVALID CHOICE, TRY AGAIN LATER!")

def change_nominee():
   acc_n=input("Enter new account number for nominee: ")
   scc_p=input("Enter customer's account number: ")
   cl.execute('UPDATE nominee SET account_no_of_nominee=%s where account_no_of_parent=%s',(acc_n,acc_p,))
   conn.commit()

def transactions():
   print('''choose:
1. Enter New transaction
2. Display Transactions associated with particular bank account
3. Display all Transactions''')
   ch=int(input("Enter your choice: "))
   if ch==1:
      acs=input("Enter sender's account number: ")
      acr=input("Enter reciever's account numebr: ")
      er=int(input("Enter the exchange rate: "))
      bos=input("Enter branch of sender: ")
      bor=input("Enter branch of reciever: ")
      sid=input("Enter Staff ID of Personnel incharge: ")
      sor=input("Enter whether transaction was sent or recieved by the customer: ")
      amt=float(input("Enter amount transferred: "))
      cl.execute('INSERT into transactions values(%s,%s,%s,%s,%s,%s,%s,%s)',(acs,acr,er,bos,bor,sid,sor,amt))
      conn.commit()

   if ch==2:
      acs=input("Enter sender's account number: ")
      cl.execute('Select * from transactions where accountno_sender=%s;',(acs,))
      display()

   if ch==3:
      cl.execute('SELECT * FROM transactions;')
      display()
   










      
