# open both files
with open('/home/pguser/Documents/new.txt', 'r') as firstfile, open('/home/pguser/Documents/newwrite.txt', 'w') as secondfile:
    # read content from first file
    for line in firstfile:
        # write content to second file
        secondfile.write(line)