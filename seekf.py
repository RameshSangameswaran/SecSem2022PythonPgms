fi = open("/home/pguser/Documents/new.txt", "r+")
print("Name of the file: ", fi.name)

line_1 = fi.readline()
print("Read Line: %s" % (line_1))

# Again, set the pointer to the beginning
fi.seek(0, 1)
line_2 = fi.readline()
print("Read Line: %s" % (line_2))

# Close opend file
fi.close()