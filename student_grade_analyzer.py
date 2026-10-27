students = {
    "Ali": {"score": 85, "language": "English"},
    "Mona": {"score": 92, "language": "German"},
    "Omar": {"score": 78, "language": "English"},
    "Sara": {"score": 95, "language": "German"}
}

for name, info in students.items():
    print(name, info["score"])

highest_score = 0
highest_student = ""

for name, info in students.items():
    if info["score"] > highest_score:
        highest_score = info["score"]
        highest_student = name

print(f"Highest student: {highest_student}")
print(highest_score)

total = 0

for name, info in students.items():
    total += info["score"]

average = total / len(students)

print(f"The average score is: {average}")
