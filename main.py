

# f = open("file.txt", "a")

# print(f.read())
#
# print(f.encoding)
#
# print(f.readlines())

# for l in f:
#     print(l)

# f.write("test write")
# f.close()
#
# f = open("file.txt", "r")
# print(f.read())

# lines = ["\ntest 1", "\ntest 2"]
# f.writelines(lines)

with open("file.txt","r") as f:
    print(f.read())