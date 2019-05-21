
mem = {
	0x0804c160:    {'l': 0x0804c19c, 'd': 0x47bbfa96, 'r': 0x0804c178},
	0x0804c16c:    {'l': 0x0804c214, 'd': 0x50171a6e, 'r': 0x0804c1b4},
	0x0804c178:    {'l': 0x0804c1d8, 'd': 0x23daf3f1, 'r': 0x0804c1a8},
	0x0804c184:    {'l': 0x0804c19c, 'd': 0x634284d3, 'r': 0x0804c1c0},
	0x0804c190:    {'l': 0x0804c1f0, 'd': 0x344c4eb1, 'r': 0x0804c1fc},
	0x0804c19c:    {'l': 0x0804c1cc, 'd': 0x0c4079ef, 'r': 0x0804c214},
	0x0804c1a8:    {'l': 0x0804c178, 'd': 0x425ebd95, 'r': 0x0804c184},
	0x0804c1b4:    {'l': 0x0804c1cc, 'd': 0x07ace749, 'r': 0x0804c1a8},
	0x0804c1c0:    {'l': 0x0804c1e4, 'd': 0x237a3a88, 'r': 0x0804c184},
	0x0804c1cc:    {'l': 0x0804c1f0, 'd': 0x4b846cb6, 'r': 0x0804c184},
	0x0804c1d8:    {'l': 0x0804c214, 'd': 0x1fba9a98, 'r': 0x0804c1c0},
	0x0804c1e4:    {'l': 0x0804c19c, 'd': 0x3a4ad3ff, 'r': 0x0804c1c0},
	0x0804c1f0:    {'l': 0x0804c184, 'd': 0x16848c16, 'r': 0x0804c178},
	0x0804c1fc:    {'l': 0x0804c190, 'd': 0x499ee4ce, 'r': 0x0804c1b4},
	0x0804c208:    {'l': 0x0804c1c0, 'd': 0x261af8fb, 'r': 0x0804c184},
	0x0804c214:    {'l': 0x0804c1cc, 'd': 0x770ea82a, 'r': 0x0804c1fc}
}


xor_val = 0x47bbfa96
depth = 0
found = False
solution = []

def step(addr, xor_val, direction):
    global depth
    global found
    global solution
    depth += 1
    if depth > 10:
        depth -= 1
        return
    new_addr = mem[addr][direction]
    new_xor_val = xor_val ^ mem[new_addr]['d']
    if new_xor_val == 0x40475194:
        print "address: 0x%0.8x" % new_addr
        print "xor_val: 0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[new_addr]['d'], new_xor_val)
        print 'found'
        print len(solution)
        print solution
        found = True
        return
    step(new_addr, new_xor_val, 'l')
    if found:
        solution.append('l')
        print 'l'
        print "address: 0x%0.8x" % new_addr
        print "xor_val: 0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[new_addr]['d'], new_xor_val)
        return
    step(new_addr, new_xor_val, 'r')
    if found:
        solution.append('r')
        print 'r'
        print "address: 0x%0.8x" % new_addr
        print "xor_val: 0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[new_addr]['d'], new_xor_val)
        return
    depth -= 1
    return

solution = []


step(0x0804c160, 0x47bbfa96, 'l')
if found:
    solution.append('l')
    print 'l'
else:
    step(0x0804c160, 0x47bbfa96, 'r')
    if found:
        solution.append('r')
        print 'r'
print
print
print 'solution'
print '---------'
print solution

xor_val = 0x47bbfa96
addr = 0x0804c160
for direction in reversed(solution):
    addr = mem[addr][direction]
    data = mem[addr]['d']
    xor_val = xor_val ^ data
    print "0x%0.8x" % xor_val
