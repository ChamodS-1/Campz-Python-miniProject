
bookArray = [{'ISBN Number': 'ISBN56545446', 'Title': 'Harry Potter', 'Format': 'Paperback', 'Available Subject': 'Science', 'Rental Price per Day': 23.6, 'Number of Copies': 45}, {'ISBN Number': 'ISBN56545447', 'Title': 'Spider man', 'Format': 'Paperback',
                                                                                                                                                                                     'Available Subject': 'Science', 'Rental Price per Day': 40.5, 'Number of Copies': 10}, {'ISBN Number': 'ISBN56545448', 'Title': 'Bat man', 'Format': 'Paperback', 'Available Subject': 'Science', 'Rental Price per Day': 12.36, 'Number of Copies': 0}]
magazineArray = []
dvdArray = []
cdArray = [{'CD Number': '54644', 'Title': 'Hulk', 'Available Subject': 'Foreign Language',
            'Rental Price per Day': 12.36, 'Number of Copies': 45}]
allArray = bookArray + magazineArray + dvdArray + cdArray

newBookarray = []
newMagazine = []
newDvd = []
newCD = []

bookCopy = 0
magazineCopy = 0
dvdCopy = 0
cdCopy = 0

# view -resouces(subject vise)


def allres(catagory):
    print('===============================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL ALL RESOURCES(Subject vise) | {catagory}')

    allArray = bookArray + magazineArray + dvdArray + cdArray
    newSub = []
    for key in allArray:
        if (key.get('Available Subject') == catagory):
            newSub.append(key)

    print('-------------------------------------------------------------------------------')
    print(f'{len(newSub)} of total {catagory} catagory Resources are founds!')

    for key in newSub:
        print(key)

    print('-------------------------------------------------------------------')
    print('''
                    0 - Go Back
                   ''')

    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                allResources()
        except ValueError:
            print('Enter valid choice')

# main-fuction remove -resouces


def remove(Array, catagory):
    print('=====================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL RECEIVE RESOURCES | {catagory}')
    input1 = input(f'Enter {catagory} ID number to remove:')

    i = 0
    for key in Array:
        if ((key.get('ISBN Number') == input1) or (key.get('Magazine Number') == input1) or (key.get('DVD Number') == input1) or (key.get('CD Number') == input1)):
            Array.pop(i)
            print(
                f'Susscessfully removed Tuple raw include {input1} ID number')
            break
        i = i + 1
    else:
        print('Make sure you entered ID number is valid')

    print('-------------------------------------------------------------------')
    print('''
                0 - Go Back
                ''')

    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                receiveResources()
        except ValueError:
            print('Enter valid choice')

# main fuction -noavailable


def noavai(Array, catagory):
    print('===========================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL NOT AVAILABLE RESOURCES | {catagory}')

    newBookarray.clear()
    for key in Array:
        if ((key.get('Number of Copies') > 0)):
            continue
        newBookarray.append(key)

    print(f'{len(newBookarray)} of total NonAvailable {catagory} Resources are founds!')

    for key in newBookarray:
        print(key)

    print('-------------------------------------------------------------------')
    print('''
                0 - Go Back
                ''')
    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                nonavaResources()
        except ValueError:
            print('Enter valid choice')

# main fuction -available


def avai(Array, catagory):
    print('=======================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL AVAILABLE RESOURCES | {catagory}')

    newBookarray.clear()
    for key in Array:
        if ((key.get('Number of Copies') == 0)):
            continue
        newBookarray.append(key)

    print(f'{len(newBookarray)} of total Available {catagory} Resources are founds!')

    for key in newBookarray:
        print(key)

    print('-------------------------------------------------------------------')
    print('''
                0 - Go Back
                ''')

    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                avaResources()
        except ValueError:
            print('Enter valid choice')

# main fuction -lend


def lend(Array, catagory):
    print('===================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL LEND RESOURCES | {catagory}')
    input1 = input(f'Enter {catagory} ID number :')
    input2 = int(input('Enter how many copies lend: '))

    for key in Array:
        if ((key.get('ISBN Number') == input1) or (key.get('Magazine Number') == input1) or (key.get('DVD Number') == input1) or (key.get('CD Number') == input1)):
            copy = key['Number of Copies']
            key['Number of Copies'] = copy - input2
            if (key['Number of Copies'] < 0):
                key['Number of Copies'] = 0
                print(
                    '-------------------------------------------------------------------')
                print(
                    f'Susscessfully removed {copy} Copies from {input1} ID number')
                print(
                    '-------------------------------------------------------------------')
                print('''
                               0 - Go Back
                               ''')
                goBack = int(input('Enter choice :'))
                if (goBack == 0):
                    lendResources()
            else:
                print(
                    '-------------------------------------------------------------------')
                print(
                    f'Susscessfully removed {input2} Copies from {input1} ID number')
                print(
                    '-------------------------------------------------------------------')
                print('''
                                              0 - Go Back
                                              ''')

                goBack = 1
                while (goBack != 0):
                    try:
                        goBack = int(input('Enter choice :'))
                        if (goBack == 0):
                            lendResources()
                    except ValueError:
                        print('Enter valid choice')

        else:
            print('Make sure you entered ID number is valid')

    print('-------------------------------------------------------------------')
    print('''
                0 - Go Back
                ''')
    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                lendResources()
        except ValueError:
            print('Enter valid choice')

# main fuction -Receive


def recive(Array, catagory):
    print('=====================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL RECEIVE RESOURCES | {catagory}')
    input1 = input(f'Enter {catagory} ID number :')
    input2 = int(input('Enter how many copies received: '))

    for key in Array:
        if ((key.get('ISBN Number') == input1) or (key.get('Magazine Number') == input1) or (key.get('DVD Number') == input1) or (key.get('CD Number') == input1)):
            copy = key['Number of Copies']
            key['Number of Copies'] = copy + input2
            print('-------------------------------------------------------------------')
            print(f'Susscessfully added {input2} Copies to {input1} ID number')
            break
        # print(key)
        else:
            print('Make sure you entered ID number is valid')

    print('-------------------------------------------------------------------')
    print('''
                0 - Go Back
                ''')

    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                receiveResources()
        except ValueError:
            print('Enter valid choice')

# main fuction -show


def show(Array, catagory):
    print('=================================================================')
    print(
        f'WELCOME TO UNIVERSITY LIBRARY TERMINAL VIEW RESOURCES | {catagory}')
    print('-----------------------------------------------------------------')

    print(f'{len(Array)} of total Tuple records are founds!')
    print('-------------------------------------------------------------')
    for key in Array:
        print(key)
    print('---------------------------------------')
    print('''
                0 - Go Back
                ''')

    goBack = 1
    while (goBack != 0):
        try:
            goBack = int(input('Enter choice :'))
            if (goBack == 0):
                viewResources()
        except ValueError:
            print('Enter valid choice')

# remove resouses


def removeResources():
    print('========================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL REMOVE RESOURCES')
    print('--------------------------------------------------------')
    print('Choose what type of resource')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                remove(bookArray, 'BOOKS')
            elif (userInput == 2):
                remove(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                remove(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                remove(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# all resourses


def allResources():
    print('===================================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL VIEW RESOURCES(Subject vise)')
    print('-------------------------------------------------------------------')
    print('Choose what type of Subject')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Science
    2 - History
    3 - Literature
    4 - Astronomy
    5 - Math
    6 - Technology
    7 - Music
    8 - Forigen languages
    9 - Sports
    0 - Main Menu
      
    ''')

    userInput = 10
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5 and userInput != 6 and userInput != 7 and userInput != 8 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                allres('Science')
            elif (userInput == 2):
                allres('History')
            elif (userInput == 3):
                allres('Literatures')
            elif (userInput == 4):
                allres('Astronomy')
            elif (userInput == 5):
                allres('Math')
            elif (userInput == 6):
                allres('Technology')
            elif (userInput == 7):
                allres('Music')
            elif (userInput == 8):
                allres('Forigen languages')
            elif (userInput == 9):
                allres('Sports')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# view resourses


def viewResources():
    print('======================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL VIEW RESOURCES')
    print('------------------------------------------------------')
    print('Choose what type of resouse')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                show(bookArray, 'BOOKS')
            elif (userInput == 2):
                show(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                show(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                show(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# nonava Resources


def nonavaResources():
    print('===============================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL NOT AVAILABLE RESOURCES')
    print('---------------------------------------------------------------')
    print('Choose what type of resouse')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                noavai(bookArray, 'BOOKS')
            elif (userInput == 2):
                noavai(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                noavai(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                noavai(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# ava Resources


def avaResources():
    print('===========================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL AVAILABLE RESOURCES')
    print('-----------------------------------------------------------')
    print('Choose what type of resouse')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                avai(bookArray, 'BOOKS')
            elif (userInput == 2):
                avai(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                avai(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                avai(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# Lend Resources


def lendResources():
    print('=======================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL LEND RESOURCES')
    print('-------------------------------------------------------')
    print('Choose what type of resouse')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                lend(bookArray, 'BOOKS')
            elif (userInput == 2):
                lend(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                lend(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                lend(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# Recive Resources


def receiveResources():
    print('=========================================================')
    print(f'WELCOME TO UNIVERSITY LIBRARY TERMINAL RECEIVE RESOURCES')
    print('---------------------------------------------------------')
    print('Choose what type of resouse')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                recive(bookArray, 'BOOKS')
            elif (userInput == 2):
                recive(magazineArray, 'MAGAZINES')
            elif (userInput == 3):
                recive(dvdArray, 'EDUCATIONAL DVDs')
            elif (userInput == 4):
                recive(cdArray, 'LECTURE CDs')
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# lectureCDs


def addLectureCDs():
    print('======================================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL ADD LECTURE CDs')
    print('------------------------------------------------------')
    print('''

    Available Subjects
    --------------------
    1 - Music
    2 - Math
    3 - Foreign Language
     ''')

    mainLogic = True
    i = 1

    while (mainLogic):
        cdNumber = ''
        subject = 0
        rentalPrice = 0
        cdCopy = 0
        logic = True

        print('---------------------------------------')
        print(f'Enter CD {i} details')

        while (logic):
            try:
                cdNumber = input('Enter CD Number: ')
                logic = False
            except ValueError:
                print('Enter valid CD Number')

        titile = input('CD title: ').strip(" ")

        logic = True
        while (logic):
            try:
                subject = int(input('Enter Available Subject: '))
                if (subject == 1 or subject == 2 or subject == 3):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('Enter valid Choice')

        logic = True
        while (logic):
            try:
                rentalPrice = float(input('Rental Price a day :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        logic = True
        while (logic):
            try:
                cdCopy = int(input('Number of Copies :'))
                logic = False
            except ValueError:
                print('Enter valid Number')

        Subjects = {
            1: 'Music',
            2: 'Maths',
            3: 'Foreign Language'
        }

        newSubject = Subjects.get(subject)

        cdMap = {
            'CD Number': cdNumber,
            'Title': titile,
            'Available Subject': newSubject,
            'Rental Price per Day': rentalPrice,
            'Number of Copies': cdCopy
        }
        cdArray.append(cdMap)

        print('---------------------------------------')
        print(f'Susscessfully Added! CD {i} tuple')
        print(cdMap)

        i = i + 1

        print('---------------------------------------')
        print('''
            1 - Add CD Again
            0 - Finished Add
            ''')

        mainLogic1 = {
            1: True,
            0: False
        }

        enter = int(input('Enter choice: '))
        mainLogic = mainLogic1.get(enter)

    addResources()


# add educational Dvds
def addEducational():
    print('===========================================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL ADD EDUCATIONAL DVDs')
    print('-----------------------------------------------------------')
    print('''

    Available Subjects
    --------------------
    1 - Astronomy
    2 - Technology
    3 - Maths
     ''')

    mainLogic = True
    i = 1

    while (mainLogic):
        dvdNumber = ''
        subject = 0
        rentalPrice = 0
        dvdCopy = 0
        logic = True

        print('---------------------------------------')
        print(f'Enter DVD {i} details')

        while (logic):
            try:
                dvdNumber = input('Enter DVD Number: ')
                logic = False
            except ValueError:
                print('Enter valid DVD Number')

        titile = input('DVD title: ').strip(' ')

        logic = True
        while (logic):
            try:
                subject = int(input('Enter Available Subject: '))
                if (subject == 1 or subject == 2 or subject == 3):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('Enter valid Choice')

        logic = True
        while (logic):
            try:
                rentalPrice = float(input('Rental Price a day :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        logic = True
        while (logic):
            try:
                dvdCopy = int(input('Number of Copies :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        Subjects = {
            1: 'Astronomy',
            2: 'Technology',
            3: 'Maths'
        }

        newSubject = Subjects.get(subject)

        dvdMap = {
            'DVD Number': dvdNumber,
            'Title': titile,
            'Available Subject': newSubject,
            'Rental Price per Day': rentalPrice,
            'Number of Copies': dvdCopy
        }
        dvdArray.append(dvdMap)

        print('-----------------------------------------------')
        print(f'Susscessfully Added! Educational DVD {i} tuple')
        print(dvdMap)
        i = i + 1

        print('-----------------------------------------------')
        print('''
            1 - Add DVD Again
            0 - Finished Add
            ''')

        mainLogic1 = {
            1: True,
            0: False
        }

        enter = int(input('Enter choice: '))
        mainLogic = mainLogic1.get(enter)

    addResources()


# add magazine
def addMgzine():
    print('===================================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL ADD MAGAZINE')
    print('---------------------------------------------------')
    print('''
    Color Format
    --------------------
    1 - Color
    2 - Black&White

    Available Subjects
    --------------------
    1 - Science
    2 - Technology
    3 - Sports
     ''')

    mainLogic = True
    i = 1

    while (mainLogic):
        magazineNumber = ''
        mgColor = 0
        subject = 0
        rentalPrice = 0
        magazineCopy = 0
        logic = True

        print('---------------------------------------')
        print(f'Enter Magazine {i} details')

        while (logic):
            try:
                magazineNumber = input('Enter Magazine Number: ')
                logic = False
            except ValueError:
                print('Enter valid Magazine Number')

        titile = input('Magazine title: ').strip(' ')

        logic = True
        while (logic):
            try:
                mgColor = int(input('Enter Color: '))
                if (mgColor == 1 or mgColor == 2):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('Enter valid Choice')

        logic = True
        while (logic):
            try:
                subject = int(input('Enter Available Subject: '))
                if (subject == 1 or subject == 2 or subject == 3):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('Enter valich Choice')

        logic = True
        while (logic):
            try:
                rentalPrice = float(input('Rental Price a day :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        logic = True
        while (logic):
            try:
                magazineCopy = int(input('Number of Copies :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        color = {
            1: 'Color',
            2: 'Black&White'
        }

        Subjects = {
            1: 'Science',
            2: 'Technology',
            3: 'Sports'
        }

        newColor = color.get(mgColor)
        newSubject = Subjects.get(subject)

        magazineMap = {
            'Magazine Number': magazineNumber,
            'Title': titile,
            'Color': newColor,
            'Available Subject': newSubject,
            'Rental Price per Day': rentalPrice,
            'Number of Copies': magazineCopy
        }
        magazineArray.append(magazineMap)

        print('---------------------------------------')
        print(f'Susscessfully Added! Magazine {i} tuple')
        print(magazineMap)

        i = i + 1

        print('---------------------------------------')
        print('''
            1 - Add Magazine Again
            0 - Finished Add
            ''')

        mainLogic1 = {
            1: True,
            0: False
        }

        enter = int(input('Enter choice: '))
        mainLogic = mainLogic1.get(enter)

    addResources()


# add books
def addBooks():
    print('=================================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL ADD BOOKS')
    print('-------------------------------------------------')
    print('''
    Available Format
    --------------------
    1 - Handover
    2 - Paperback

    Available Subjects
    --------------------
    1 - Science
    2 - History
    3 - Literature
     ''')
    mainLogic = True
    i = 1

    while (mainLogic):
        isbnNumber = 0
        format = 0
        subject = 0
        rentalPrice = 0
        bookCopy = 0
        logic = True

        print('---------------------------------------')
        print(f'Enter book {i} details')
        print('')

        while (logic):
            try:
                isbnNumber = int(input('Enter ISBN Number: '))
                logic = False
            except ValueError:
                print('error')

        titile = input('Book title: ').strip(' ')

        logic = True
        while (logic):
            try:
                format = int(input('Enter Available Format: '))
                if (format == 1 or format == 2):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('error')

        logic = True
        while (logic):
            try:
                subject = int(input('Enter Available Subject: '))
                if (subject == 1 or subject == 2 or subject == 3):
                    logic = False
                else:
                    logic = True
            except ValueError:
                print('error')

        logic = True
        while (logic):
            try:
                rentalPrice = float(input('Rental Price a day :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        logic = True
        while (logic):
            try:
                bookCopy = int(input('Number of Copies :'))
                logic = False
            except ValueError:
                print('Enter Valid Number')

        formats = {
            1: 'Handover',
            2: 'Paperback'
        }

        Subjects = {
            1: 'Science',
            2: 'History',
            3: 'Literature'
        }

        newFormat = formats.get(format)
        newSubject = Subjects.get(subject)

        booksMap = {
            'ISBN Number': f'ISBN{isbnNumber}',
            'Title': titile,
            'Format': newFormat,
            'Available Subject': newSubject,
            'Rental Price per Day': rentalPrice,
            'Number of Copies': bookCopy
        }
        bookArray.append(booksMap)
        print('---------------------------------------')
        print(f'Susscessfully Added! Book {i} tuple')
        print(booksMap)

        i = i + 1
        print('---------------------------------------')
        print('''
            1 - Add Book Again
            0 - Finished Add
            ''')

        mainLogic1 = {
            1: True,
            0: False
        }

        enter = int(input('Enter choice: '))
        mainLogic = mainLogic1.get(enter)

    addResources()

# add resources


def addResources():
    print('===================================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL ADD RESOURCE')
    print('---------------------------------------------------')
    print('Choose what you want to Add Resource')
    print('---------------------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - Books
    2 - Magazines
    3 - Educatinal DVDs
    4 - Lecuter CDs
    0 - Main Menu
    ''')

    userInput = 5
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                addBooks()
            elif (userInput == 2):
                addMgzine()
            elif (userInput == 3):
                addEducational()
            elif (userInput == 4):
                addLectureCDs()
            elif (userInput == 0):
                mainCode()
        except ValueError:
            print('Error')

# main menu


def mainCode():
    print('=======================================')
    print('WELCOME TO UNIVERSITY LIBRARY TERMINAL')
    print('---------------------------------------')
    print('Choose Your Navigation')
    print('---------------------------------------')
    print('#Navigation pane:')

    print('''
    1 - View Resources
    2 - Add Resources
    3 - Receive Resources
    4 - Lend Resources
    5 - Show Available Resources
    6 - Show not Available Resources
    7 - Remove Resources
    8 - View all Resources(Subject vise)
    0 - Exit Programme
    ''')

    userInput = 9
    while (userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5 and userInput != 6 and userInput != 7 and userInput != 8 and userInput != 0):
        try:
            userInput = int(input('Enter your choice: '))
            if (userInput == 1):
                viewResources()
            elif (userInput == 2):
                addResources()
            elif (userInput == 3):
                receiveResources()
            elif (userInput == 4):
                lendResources()
            elif (userInput == 5):
                avaResources()
            elif (userInput == 6):
                nonavaResources()
            elif (userInput == 7):
                removeResources()
            elif (userInput == 8):
                allResources()
            elif (userInput == 0):
                print('---------------------------------------')
                print('Thanks for using this service')
                exit(0)
        except ValueError:
            print('Error')


mainCode()
