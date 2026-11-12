from database import create_database,get_connection

def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        conn=get_connection()
        cursor=conn.cursor()

        query="""
        INSERT INTO tb (id, name, age, course, marks)
        VALUES (%s, %s, %s, %s, %s)
        """

        values=(student_id,name,age,course,marks)

        cursor.execute(query,values)
        conn.commit()

        print("Student added successfully")

    except ValueError:
        print("Please enter valid numbers for ID ,age and marks")

    except Exception as e:
        print("Error:",e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def view_students():
    try:
        conn=get_connection()
        cursor=conn.cursor()

        cursor.execute("select * from tb")
        students=cursor.fetchall()

        if not students:
            print("No students found")
        else:
            print("\n===== STUDENT DETAILS =====")
            for student in students:
                print("--------------------------------")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Course:", student[3])
                print("Marks:", student[4])
    except Exception as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def search_student():
    try:
        student_id = int(input("Enter Student ID to search: "))

        conn=get_connection()
        cursor=conn.cursor()

        query = "SELECT * FROM tb WHERE id = %s"
        cursor.execute(query,(student_id,))

        student=cursor.fetchone()

        if student:
            print("\n===== STUDENT FOUND =====")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Marks:", student[4])
        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid Student ID.")

    except Exception as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def update_student():
    try:
        student_id = int(input("Enter Student ID to update: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tb WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            print("\nCurrent Details:")
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Marks:", student[4])

            print("\nEnter New Details:")
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")
            marks = float(input("New Marks: "))

            query = """
            UPDATE tb
            SET name = %s, age = %s, course = %s, marks = %s
            WHERE id = %s
            """

            values = (name, age, course, marks, student_id)

            cursor.execute(query, values)
            conn.commit()

            print("Student updated successfully!")

        else:
            print("Student not found!")

    except ValueError:
        print("Please enter valid numbers for ID, age and marks.")

    except Exception as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))

        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM tb WHERE id = %s"
        cursor.execute(query, (student_id,))

        if cursor.rowcount > 0:
            conn.commit()
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid Student ID.")

    except Exception as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice=input("\n Enter your choice: ")

        if choice=="1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__=="__main__":
    create_database()
    menu()