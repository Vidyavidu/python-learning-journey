
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def final_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("Student Performance Report")
        print("Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.final_grade())


student1 = Student("Rahul", [80, 90, 70])
student1.display_report()
