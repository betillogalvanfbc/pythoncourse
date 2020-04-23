friends = ["Beto", "Bernanrdo", "Benito"]
starts_s = [friend for friend in friends if friend.startswith("B")]
print(starts_s)
print(friends)
print(friends is starts_s)
print("friends:", id(friends), "starts_s:", id(starts_s))
