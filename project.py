# ============================================
#        STUDENT GRADE ANALYZER
#        Built using core Python concepts
# ============================================

students = {}

def add_students():
    print("\n📋 ENTER STUDENT DETAILS")
    print("-" * 35)
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("⚠️  Name cannot be empty. Try again.\n")
            continue
        try:
            marks = float(input(f"Enter marks for {name} (0-100): "))
            if marks < 0 or marks > 100:
                print("⚠️  Marks must be between 0 and 100. Try again.\n")
                continue
            students[name] = marks
            print(f"✅ {name} added!\n")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.\n")

def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def pass_or_fail(marks):
    return "✅ Pass" if marks >= 50 else "❌ Fail"

def show_report():
    if not students:
        print("\n⚠️  No students found. Please add students first.")
        return

    print("\n")
    print("=" * 50)
    print("        📊 STUDENT GRADE REPORT")
    print("=" * 50)
    print(f"{'NAME':<20} {'MARKS':<10} {'GRADE':<8} {'STATUS'}")
    print("-" * 50)

    for name, marks in students.items():
        grade = assign_grade(marks)
        status = pass_or_fail(marks)
        print(f"{name:<20} {marks:<10.1f} {grade:<8} {status}")

    print("-" * 50)

    passed = [name for name, marks in students.items() if marks >= 50]
    failed = [name for name, marks in students.items() if marks < 50]

    print(f"\n📌 SUMMARY")
    print(f"   Total Students : {len(students)}")
    print(f"   Total Passed   : {len(passed)}")
    print(f"   Total Failed   : {len(failed)}")

    if failed:
        print(f"\n   ❌ Failed : {', '.join(failed)}")

    print("=" * 50)

def main():
    print("=" * 50)
    print("     🎓 STUDENT GRADE ANALYZER")
    print("=" * 50)

    while True:
        print("\n📌 MENU")
        print("  1. Add Students")
        print("  2. View Report")
        print("  3. Exit")
        print("-" * 30)

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            add_students()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("⚠️  Invalid choice. Enter 1, 2, or 3.")

main()