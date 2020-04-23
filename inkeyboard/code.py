#family = ["Ana", "Beto", "Zeus", "Athena"]
#print("Ana" in family)

# codes_know = {"c#", "python", "ruby"}
#lan_code = input(   "Enter something whats is you prefered language code?").lower()
#print(lan_code in codes_know)

codes_know = {"c#", "python", "ruby"}
lan_code = input(
    "Enter something whats is you prefered language code?").lower()

if lan_code in codes_know:
    print(f"The best code is {lan_code}!")
else:
    print(f"example")
