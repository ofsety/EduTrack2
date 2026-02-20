class Student:
    def init(self, name, p1, p2, p3):
        self.name = name
        self.medium_point = (p1 + p2 + p3) / 3

    def str(self):
        return f"{self.name}: avg={self.medium_point:.1f}"


student1 = Student("Ivan", 14, 8, 8)
student2 = Student("Maxim", 16, 10, 6)


class StudentActions:
    def main(self):
        print(student1, student2)

        renew1 = input(f"Input new points for student 1 ({student1.name}) or press enter to skip: ")
        renew2 = input(f"Input new points for student 2 ({student2.name}) or press enter to skip: ")

        if renew1:
            student1.medium_point = float(renew1)
        if renew2:
            student2.medium_point = float(renew2)

        print(student1, student2)


actions = StudentActions()
actions.main()