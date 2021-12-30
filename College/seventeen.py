# 17th program - unique words

fn = input("Enter filename: ")
f = open(fn, "r")

l = f.read().split(" ")
uniquelist = sorted(list(dict.fromkeys(l)))
print(uniquelist)
