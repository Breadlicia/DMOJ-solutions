sentence=input()

if sentence.count(":-)") > sentence.count(":-("):
    print("happy")
elif sentence.count(":-(") > sentence.count(":-)"):
    print("sad")
elif sentence.count(":-)") == sentence.count(":-(") and sentence.count(":-)") > 0:
    print("unsure")
else:
    print("none")
