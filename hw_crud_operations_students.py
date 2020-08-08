student_names = ["Ion Drop", "Tatiana Hush", "Maria Nush", "John Doe", "Steven Banderas", "Fred Oleson", "Christina Martin", "Joe Statham", "Willie Zuckerberg"]
student_specs = ["IT", "Filology", "Filology", "Management", "Law", "IT", "IT", "Education", "Nothing"]
student_grades = [9.567, 9.667, 8.001, 9.099, 9.121, 9.101, 9.888, 9.111, 10.000]


def not_found():
        print("##### ERROR ##### STUDENT NOT FOUND! ##### TRY AGAIN ##### ERROR #####")
        return False


def read():
    for i in range(len(student_names)):
        print(f" > {student_names[i]:30s} ( {student_specs[i]:10s} )")


def details():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print("STUDENT FOUND!")
            print(f" >>> {student_names[i]:30s} ( {student_specs[i]:2s} ) {student_grades[i]:4.1f}")
            return True
    else:
        not_found()


def delete():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print("STUDENT DELETED!")
            student_names.pop(i)
            student_specs.pop(i)
            student_grades.pop(i)
            return True
    else:
        not_found()


def edit():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print("STUDENT FOUND!")

            new_name = input(" ENTER THE STUDENT'S NAME > ").lower().title()
            if len(new_name.strip()) == 0:
                new_name = student_names[i]
            else:
                student_names[i] = new_name

            new_spec = input(" ENTER THE STUDENT'S SPECIALITY > ").lower().title()
            if len(new_spec.strip()) == 0:
                new_spec = student_specs[i]
            else:
                student_specs[i] = new_spec

            try:
                new_grade = float(input(" ENTER THE STUDENT'S GRADE > "))
                if new_grade > 10 or new_grade < 0:
                    print("##### ERROR ##### The lowest grade in educational system is (1), the highest is (10) ##### ERROR #####")
                    break
                if len(new_grade.strip()) == 0:
                    new_grade = student_grades[i]
                else:
                    student_grades[i] = new_grade
            except ValueError:
                break
            return True
    else:
        not_found()


def menu():
    option = - 1
    try:
        while option != 0:
            print("\n\n")
            print("########## MENU ##########")
            print("1. Show Students List")
            print("2. Show Student Details")
            print("3. Edit Student Details")
            print("4. Delete Student")
            print("0. Exit")
            print("##########################")
            print("CHOOSE OPTION > ")

            option = int(input())

            if option == 1:
                read()
            if option == 2:
                details()
            if option == 3:
                edit()
            if option == 4:
                delete()
            if option > 4 or option <= -1:
                print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
                menu()
            if option == 0:
                print("##### EXIT #####")
    except ValueError:
        menu()
menu()
