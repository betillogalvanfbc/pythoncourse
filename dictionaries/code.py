#friend_ages = {"Carlos": 24, "Adam": 30, "Anne": 25}
# print(friend_ages["Adam"])
#friend_ages["Carlos"] = 20
# print(friend_ages)

# friends = [
#     {"name": "Carlos", "age": 24},
#     {"name": "Pedro", "age": 26},
#     {"name": "Ignacio", "age": 25},
# ]
# print(friends[0]["name"])


student_attedance = {"Rolf": 22, "Juan": 23, "Carlos": 23}

# for student in student_attedance:
#    print(f"{student}: {student_attedance[student]}")
# betterway

for student, attendace in student_attedance.items():
    print(f"{student}:{attendace}")

