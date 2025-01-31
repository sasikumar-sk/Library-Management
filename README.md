# Library-Management
Basic Library Management System using Mysql and Python

Library Management System is a system that maintains the information about the books
present in the library, their authors, the members of the library to whom books are issued,
library staff, and all. This is very difficult to organize manually. Maintenance of all this
information manually is a very complex task.

Owing to the advancement of technology improvement, the organization of a Library
becomes much easier. I trying to make Library Management designed using python to
computerize and automate the few operations performed over the information about the
members, book issues and returns, and some other operations

---------------------------------------------------------------------------------------------
Functions used
        tabulate for table view
        colored for style        
        mysql.connector.connect for sql call        
        SQL query [ insert , select, update, orderby ]

Software Tools :
        Visual Studio code editor
        XAMPP (mysql)
---------------------------------------------------------------------------------
Database and Data Tables
        library (DB)
        Book (Table)
        Member (Table)
        Transaction(Table)
----------------------------------------------------------------------------------
Navigation Structure
        Add Books (To add new book )
        Add Member ( To addning new member/ office staff )
        Issue Book ( To Provide the book to the user)
        Return Book (To returning the book)
        Report Menu{submenu} (To view additional options to show more data)
              Book List (Listing all books)
              Membera List (Listing all members)
              Issued Books (Listing all Issued book lists only)
              Available Books (Listing all books that are not issued book lists only)
              Lost Book (Listing all Lost book lists only)
        Update Lost Book (To update the lost book data)
        Search by Book Title
        Search by Book Author
        Search by Publisher
        Close application
