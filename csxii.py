import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as m
plt.rcParams.update({'font.size': 6}) #Changes the fontsize on plot
c = m.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'csxii')
cursor = c.cursor()
#cursor.execute('create table Students(Admission_Number INT Primary Key, Name varchar(64), Age int, Sex char, Date_of_birth date, IsOnlyChild char)')
def addRec():
    while True:
        Adm = int(input("Admission Number of the student: "))
        Name = input("Name of the student: ")
        Age = int(input("Age of the student: "))
        Sex = input("Sex of the student(M/F/T): ")
        Dob = input("Date of birth (DD-MM-YYYY): ")
        Ioc = input("Is only child (Y/N): ")
        cursor.execute('''INSERT INTO students VALUES("%d", "%s", "%d", "%s", "%s", "%s")'''%(Adm, Name, Age, Sex, Dob, Ioc))
        c.commit()
        
        s = input("Continue?(Y/N) ")
        if s != 'y' or s != 'Y':
            break
#create table repMid(Admission_Number int, Maths int, Phy int, Chem int, CS int, Eng int, Avg int);
def addMarksMid():
    while True:
        Adm = int(input("Adm No: "))
        maths = int(input("Maths: "))
        phy = int(input("Physics: "))
        chem = int(input("Chemistry: "))
        CS = int(input("Computer Science: "))
        eng = int(input("English: "))
        avg = (maths+phy+chem+CS+eng)/5
        cursor.execute('''INSERT INTO repMid VALUES("%d", "%d", "%d", "%d", "%d", "%d", "%d")'''%(Adm, maths, phy, chem, CS, eng, avg))
        c.commit()

        s = input("Continue?(Y/N) ")
        if s.lower() != 'y':
            break
        else:
            continue
def addMarksEnd():
    while True:
        Adm = int(input("Adm No: "))
        maths = int(input("Maths: "))
        phy = int(input("Physics: "))
        chem = int(input("Chemistry: "))
        CS = int(input("Computer Science: "))
        eng = int(input("English: "))
        avg = (maths+phy+chem+CS+eng)/5
        cursor.execute('''INSERT INTO repEnd VALUES("%d", "%d", "%d", "%d", "%d", "%d", "%d")'''%(Adm, maths, phy, chem, CS, eng, avg))
        c.commit()

        s = input("Continue?(Y/N) ")
        if s.lower() != 'y':
            break
        else:
            continue
def updateRec():
    s = int(input("Enter an admission number"))
    k = int(input("What do you want to update?\n1. Name\n2. Age\n3. Sex"))
    if k == 1:
        d = input("Enter the new value")
        cursor.execute('''UPDATE students SET name = "%s" WHERE Admission_Number = "%d"'''%(d, s))
        c.commit()
    elif k == 2:
        d = int(input("Enter the new value"))
        cursor.execute('''UPDATE students SET age = "%d" WHERE Admission_Number = "%d"'''%(d, s))
        c.commit()
    elif k == 3:
        d = input("Enter the new value")
        cursor.execute('''UPDATE students SET sex = "%s" WHERE Admission_Number = "%d"'''%(d, s))
        c.commit()
def updateMidsem():
    s = int(input("Enter admission number"))
    maths = int(input("Updated Maths marks: "))
    phy = int(input("Updated Physics marks: "))
    chem = int(input("Updated Chemistry marks: "))
    CS = int(input("Updated Computer Science marks: "))
    Eng = int(input("Updated English marks: "))
    avg = (maths+phy+chem+CS+Eng)/5
    cursor.execute('''UPDATE repMid SET maths = "%d", phy = "%d", chem = "%d", CS = "%d", Eng = "%d", Avg = "%d" where Admission_Number = "%d"'''%(maths, phy, chem, CS, Eng, avg, s))
    c.commit()
def updateEndsem():
    s = int(input("Enter admission number"))
    maths = int(input("Updated Maths marks: "))
    phy = int(input("Updated Physics marks: "))
    chem = int(input("Updated Chemistry marks: "))
    CS = int(input("Updated Computer Science marks: "))
    Eng = int(input("Updated English marks: "))
    avg = (maths+phy+chem+CS+Eng)/5
    cursor.execute('''UPDATE repEnd SET maths = "%d", phy = "%d", chem = "%d", CS = "%d", Eng = "%d", Avg = "%d" where Admission_Number = "%d"'''%(maths, phy, chem, CS, Eng, avg, s))
    c.commit()
def plotAvg():
    cursor.execute('''SELECT students.name, repMid.avg from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    Names, Average = [], []
    for i in cursor.fetchall():
        Names.append(i[0])
        Average.append(i[1])
    plt.bar(Names, Average)
    plt.ylim(0, 100)
    plt.xlabel("Name of students")
    plt.ylabel("Average Marks out of 100")
    plt.title('Average Marks')
    plt.show()
def plotSubMidsem():
    y = int(input("Choose an option: \n1. Mathematics\n2. Physics\n3. Chemistry\n4. Computer Science\n5. English"))
    if y == 1:
        cursor.execute('''SELECT students.name, repMid.Maths from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    if y == 2:
        cursor.execute('''SELECT students.name, repMid.Phy from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    if y == 3:
        cursor.execute('''SELECT students.name, repMid.Chem from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    if y == 4:
        cursor.execute('''SELECT students.name, repMid.cs from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    if y == 5:
        cursor.execute('''SELECT students.name, repMid.eng from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    Names, Score = [], []
    for i in cursor.fetchall():
        Names.append(i[0])
        Score.append(i[1])
    plt.plot(Names, Score, '--o')
    plt.ylim(0, 100)
    plt.xlabel("Name of students")
    plt.ylabel("Marks out of 100")
    plt.show()
def plotSubEndsem():
    y = int(input("Choose an option: \n1. Mathematics\n2. Physics\n3. Chemistry\n4. Computer Science\n5. English"))
    if y == 1:
        cursor.execute('''SELECT students.name, repEnd.Maths from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    if y == 2:
        cursor.execute('''SELECT students.name, repEnd.Phy from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    if y == 3:
        cursor.execute('''SELECT students.name, repEnd.Chem from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    if y == 4:
        cursor.execute('''SELECT students.name, repEnd.cs from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    if y == 5:
        cursor.execute('''SELECT students.name, repEnd.eng from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    Names, Score = [], []
    for i in cursor.fetchall():
        Names.append(i[0])
        Score.append(i[1])
    plt.plot(Names, Score, '-o')
    plt.ylim(0, 100)
    plt.xlabel("Name of students")
    plt.ylabel("Marks out of 100")
    plt.show()
def plotDblAvg():
    cursor.execute('''SELECT students.name, repMid.avg from students, repMid where students.Admission_Number = repMid.Admission_Number''')
    Names, Average = [], []
    for i in cursor.fetchall():
        Names.append(i[0])
        Average.append(i[1])
    cursor.execute('''SELECT students.name, repEnd.avg from students, repEnd where students.Admission_Number = repEnd.Admission_Number''')
    Names1, Average1 = [], []
    for i in cursor.fetchall():
        Names1.append(i[0])
        Average1.append(i[1])
    width = 0.4
    x = Names
    x1 = [i - width/2 for i in range(len(x))]
    x2 = [i + width/2 for i in range(len(x))]
    plt.bar(x1, Average, width, label = "Mid Sem")
    plt.bar(x2, Average1, width, label = "Final Sem")
    plt.ylim(0, 100)
    plt.xlabel("Name of students")
    plt.ylabel("Average Marks out of 100")
    plt.title('Average Marks')
    plt.xticks(x1, x)
    plt.legend()
    plt.show()
while True:
    x = int(input("Select an option out of the following: \n1. Add new student record to database\n2. Add Mid Semester's Mark\n3. Add End Semester's Marks\n4. Graph of average marks of each student(Mid Sem)\n5. Graph of average marks of student (both semester)\n6. Graph marks for a subject (Mid Semester)\n7. Graph marks for a subject (End Semester)\n8. Update Student database records\n9. Update Mid Semester's marks by Admission Number\n10. Update End Semester's marks by Admission Number"))
    if x == 1:
        addRec()
    elif x == 2:
        addMarksMid()
    elif x == 3:
        addMarksEnd()
    elif x == 4:
        plotAvg()
    elif x == 5:
        plotDblAvg()
    elif x == 6:
        plotSubMidsem()
    elif x == 7:
        plotSubEndsem()
    elif x == 8:
        updateRec()
    elif x == 9:
        updateMidsem()
    elif x == 10:
        updateEndsem()
    else:
        break
        
