# --- Project name : Library management system using Mysql---

# --- Submited by : Sasikumar ---

# --- Dtoudh Demo 💻 -----

import mysql.connector

from datetime import date

from tabulate import tabulate

from termcolor import colored

from pyfiglet import Figlet

from colored import fg, bg, attr

def clear():

for _ in range(1):

print

def add_book():

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='root')

cursor = conn.cursor()

title = input('Enter Book Title :')

author = input('Enter Book Author : ')

publisher =input('Enter Book Publisher : ')

pages = input('Enter Book Pages : ')

price = input('Enter Book Price : ')

edition = input('Enter Book Edition : ')

copies = int(input('Enter copies : '))

#databaseCall

sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \

title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'

for _ in range(0,copies):

cursor.execute(sql)

conn.close()

print('\n')

print ('%s Booyah !!🎉 New Book added successfully %s' % (fg(10), attr(1)))

wait = input('\n >>>> Press any key to continue....')

main_menu()

def add_member():

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

name = input('Enter Member Name :')

empid = input('Enter Member EMP-ID : ')

branch = input('Enter Member EMP-Branch : ')

phone = input('Enter Member Phone : ')

email = input('Enter Member EMP-Email : ')

sql = 'insert into member(name,empid,branch,phone,email) values ( "' + \

name + '","' + empid+'","'+branch+'","'+phone + \

'","'+email+'");'

cursor.execute(sql)

conn.close()

print ('%s Great! New Member added successfully %s' % (fg(191), attr(1)))

wait = input('\n >>>>Press any key to continue....')

main_menu()

def mem_issue_status(empid):

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

sql ='select * from transaction where empid ='+empid+' and dor is NULL;'

#print(sql)

cursor.execute(sql)

results = cursor.fetchall()

return results

def book_status(book_id):

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

sql = 'select * from book where id ='+book_id + ';'

cursor.execute(sql)

result = cursor.fetchone()

return result[5]
def book_issue_status(book_id,empid):

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

sql = 'select * from transaction where b_id ='+book_id + ' and empid ='+ empid +' and dor is NULL;'

cursor.execute(sql)

result = cursor.fetchone()

return result

def issue_book():

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print('\n ')

print ('%s:::::::🕵️‍♂️ BOOK ISSUE SCREEN 🕵️‍♂️::::::: %s' % (fg(14), attr(0)))

print('-'*50)

book_id = input('Enter Book ID : ')

empid = input('Enter Member/EMP ID :')

result = book_status(book_id)

result1 = mem_issue_status(empid)

#print(result1)

today = date.today()

if len(result1) == 0:

if result == 'available':

sql = 'insert into transaction(b_id, empid, doi) values('+book_id+','+empid+',"'+str(today)+'");'

sql_book = 'update book set status="issue" where id ='+book_id + ';'

cursor.execute(sql)

cursor.execute(sql_book)

print('\n '+book_id +', Book issued successfully !!!')

else:

print('\n\n Book is not available for ISSUE... Current status :',result1)

else:

if len(result1)<2:

sql = 'insert into transaction(b_id, empid, doi) values(' + \

book_id+','+empid+',"'+str(today)+'");'

sql_book = 'update book set status="issue" where id ='+book_id + ';'

cursor.execute(sql)

cursor.execute(sql_book)

print('\n Book issued successfully to Member Id -',empid)

else:

print('\n\n Member already have book from the Library')

conn.close()

wait = input('\n >>>> Press any key to continue....')

main_menu()

def return_book():

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print('\n ++++++ BOOK RETURN SCREEN ++++++')

print('-'*50)

book_id = input('Enter Book ID : ')

empid = input('Enter Member ID :')

today =date.today()

result = book_issue_status(book_id,empid)

if result==None:

print('Book was not issued...Check Book Id and Member ID again..')

else:

sql='update book set status ="available" where id ='+book_id +';'

din = (today - result[3]).days

cursor.execute(sql)

#cursor.execute(sql1)

print('\nBook returned successfully')

conn.close()

wait = input('\n>>>> Press any key to continue....')

main_menu()

def search_book(field): #search book funtion

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print ('%s%s <<----🕵️‍♂️ BOOK SEARCH SCREEN 🕵️‍♂️---->> %s' % (fg(14), bg(0), attr(0)))

print('-'*50)

msg ='Enter '+ field +' Value :'

title = input(msg)

sql ='select * from book where '+ field + ' like "%'+ title+'%"'

cursor.execute(sql)

records = cursor.fetchall()

clear()

print('Search Result for :',field,' :' ,title)

print('-'*50)

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue....')

main_menu()

def report_book_list():

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print ('%s << --- ▤▤▤ --REPORT : ALL BOOK LIST --▤▤▤ --- >> %s' % (fg(162), attr(0)))

print('-'*50)

sql ='select * from book ORDER BY id'

cursor.execute(sql)

records = cursor.fetchall()

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue.....')

def report_issued_books(): #3.Issued Books

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print ('%s << 📊 REPORT >> BOOK TITLES - Issued %s' % (fg(14), attr(0)))

print('-'*50)

sql = 'select * from book where status = "issue";'

cursor.execute(sql)

records = cursor.fetchall()

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue.....')

def report_available_books(): #4.Available Books

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print ('%s << 📊 REPORT >> - BOOK TITLES - Available %s' % (fg(10), attr(0)))

print('-'*50)

sql = 'select * from book where status = "available";'

cursor.execute(sql)

records = cursor.fetchall()

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue.....')

def report_lost_books(): #5.Lost Book

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print ('%s << 📊 REPORT >> - BOOK TITLES - lost %s' % (fg(1), attr(0)))

print('-'*50)

sql = 'select * from book where status = "lost";'

cursor.execute(sql)

records = cursor.fetchall()

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue.....')

def report_member_list(): #2.Member List

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

clear()

print('-'*50)

print ('%s << 📊 REPORT >> - Members List %s' % (fg(9), attr(0)))

print('-'*50)

sql = 'select * from member ORDER BY empid'

cursor.execute(sql)

records = cursor.fetchall()

for record in records:

print(record)

conn.close()

wait = input('\n>>>>Press any key to continue.....')

def report_menu():

while True:

clear()

print('-----------------------------')

print ('%s%s ********BOOK REPORT MENUS ******** %s' % (fg(1), bg(4), attr(0)))

print("\n1. 📚 Book List")

print('\n2. 🎎 Membera List')

print('\n3. ✔️ Issued Books')

print('\n4. 📰 Available Books')

print('\n5. ❗ Lost Book')

print('\n6. 🔙 Back to main Menu')

choice = int(input('Enter your choice ...: '))

if choice == 1:

report_book_list()

if choice == 2:

report_member_list()

if choice == 3:

report_issued_books()

if choice == 4:

report_available_books()

if choice == 5:

report_lost_books()

if choice == 6:

main_menu()\

def change_book_status(status,book_id):

conn = mysql.connector.connect(

host='localhost', database='library', user='root', password='')

cursor = conn.cursor()

sql = 'update book set status = "'+status +'" where id ='+book_id + ' and status ="available"'

cursor.execute(sql)

print('Book status changed to ',status)

print('\n')

conn.close()

wait = input('\nPress any key to continue.....')

ef main_menu():

while True:

clear()

print('\n')

print('*****************************************')

print ('%s%s 🌠 ⫷ WELLCOME TO DTOUCH LIBRARY ⫸ 🌠s %s' % (fg(11), bg(15), attr(0)))

print(tabulate([

['1- 🆕 Add Books' ],

['2- 📚 Add Member'],

['3- ⏩ Issue Book'],

['4- ↪️ Return Book'],

['5- 📊 Report Menu(submenu)'],

['6- 🚫 Update Lost Book'],

['7- 📇 Search by Book Title'],

['8- ✏️ Search by Book Author'],

['9- 📢 Search by Publisher'],

['0- ❌ Close application']], headers=['Menu Actions'],tablefmt='orgtbl'))

print('*****************************************')

choice = int(input('>>>>Enter your choice ...❓:(only enter above numbers) '))

if choice == 1:

add_book()

if choice == 2:

add_member()

if choice == 3:

issue_book()

if choice == 4:

return_book()

if choice == 5:

report_menu()

status=''

if choice == 6:

status = 'lost'

book_id = input('>>>>Enter book id :')

change_book_status(status,book_id)

field =''

if choice == 7:

field='title'

search_book(field)

if choice == 8:

field = 'author'

search_book(field)

if choice == 9:

field = 'publisher'

search_book(field)

if choice == 0:

break

if __name__ == "__main__":

main_menu()

-------------------------------------------------------------END--------------------------------------------------
