class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class
        self.test_scores = []

    def add_test_scores(self, score1, score2, score3):
        self.test_scores.extend([score1, score2, score3])

    def calculate_average_score(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

student = Student("Alice", 20, "Physics")

student.add_test_scores(85, 90, 88)

average_score = student.calculate_average_score()
print("Average test score for", student.name, ":", average_score)
