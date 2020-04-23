friends = ["Beto","Bernanrdo","Carlos","Benito"]
starts_s =[]

for friend in friends:
    if friend.startswith("B"):
        starts_s.append(friend)
print(starts_s)