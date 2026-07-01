def insert_staff_data():

   import mysql.connector as ms



   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

   cl=conn.cursor()
   cl.execute('use bank;')
   
   staffid=input("Enter staff ID: ")
   name=input("Enter Name: ")
   age= input("Enter Age: ")
   DOB=input("Enter Date of Birth in YYYY-MM-DD Format: ")
   Designation=input("Enter Designation: ")
   Branch=input("Enter Branch Name: ")
   phone=input("Enter phone number: ")

   cl.execute('insert into staffdata values(%s,%s,%s,%s,%s,%s,%s)',(staffid,name,age,DOB,Designation,Branch,phone))
   conn.commit()


def update_data_staff(sid):
   import mysql.connector as ms



   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

   cl=conn.cursor()
   cl.execute('use bank;')
   print("""Choose field you wish to update from the below menu:
1. Name
2. Age
3. Date Of Birth
4. Designation
5. Branch
6. phone
7.Salary""")
   ch=int(input("Enter your choice: "))

   cl.execute('set sql_safe_updates=0;')

   if ch==1:
      new_name=input("Enter updated name: ")
      cl.execute('UPDATE staffdata SET name=%s where staffid=%s',(new_name,sid,))
      conn.commit()

   if ch==2:
      new_age=int(input("Enter updated age: "))
      cl.execute('UPDATE staffdata SET age=%s where staffid=%s',(new_age,sid,))
      conn.commit()

   if ch==3:
      new_DOB=input("Enter updated Date of Birth: ")
      cl.execute('UPDATE staffdata SET DOB=%s where staffid=%s',(new_DOB,sid,))
      conn.commit()

   if ch==4:
      new_Designation=input("Enter updated Designation: ")
      cl.execute('UPDATE staffdata SET designation=%s where staffid=%s',(new_Designation,sid,))
      conn.commit()
   
   if ch==5:
      new_Branch=input("Enter updated name: ")
      cl.execute('UPDATE staffdata SET branch=%s where staffid=%s',(new_Branch,sid,))
      conn.commit()

   if ch==6:
      new_phone=input("Enter updated name: ")
      cl.execute('UPDATE staffdata SET phone=%s where staffid=%s',(new_phone,sid,))
      conn.commit()

   if ch==7:
      new_salary=float(input("Enter updated salary: "))
      cl.execute('UPDATE staffsalary SET salary=%s where staffid=%s',(new_salary,sid,))
      conn.commit()

   print("Record Updated Successfully!")

def search_staff():
   import mysql.connector as ms



   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

   cl=conn.cursor()
   cl.execute('use bank;')
   
   sid=input("Enter Staff ID: ")
   cl.execute('SELECT * from staffdata where staffid=%s',(sid,))
   column_names = [desc[0] for desc in cl.description]
   print('\t'.join(column_names))
   for row in cl.fetchall():
       print('\t'.join(map(str, row)))
   for i in cl.fetchall():
      for j in i:
         print(j,end='\t')
      print()



def delete_staff():
   import mysql.connector as ms



   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

   cl=conn.cursor()
   cl.execute('use bank;')
   
   sid=input("Enter Staff ID: ")
   cl.execute('DELETE from staffdata where staffid=%s',(sid,))
   print("DELETED SUCCESSFULLY!")
   conn.commit()
   
def role_change():
   import mysql.connector as ms



   conn=ms.connect(host='localhost',user='root',passwd='root1234',database='bank')

   cl=conn.cursor()
   cl.execute('use bank;')
   
   sid=input("Enter Staff ID: ")
   cl.execute('UPDATE staffusername SET role=%s where staffid=%s',('Admin',sid,))
   conn.commit()


   



            
