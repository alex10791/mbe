
mem = {
	0x0804c160 +  0 * 12:    {'l': 0x0804c19c, 'd': 0x47bbfa96, 'r': 0x0804c178},
	0x0804c160 +  1 * 12:    {'l': 0x0804c214, 'd': 0x50171a6e, 'r': 0x0804c1b4},
	0x0804c160 +  2 * 12:    {'l': 0x0804c1d8, 'd': 0x23daf3f1, 'r': 0x0804c1a8},
	0x0804c160 +  3 * 12:    {'l': 0x0804c19c, 'd': 0x634284d3, 'r': 0x0804c1c0},
	0x0804c160 +  4 * 12:    {'l': 0x0804c1f0, 'd': 0x344c4eb1, 'r': 0x0804c1fc},
	0x0804c160 +  5 * 12:    {'l': 0x0804c1cc, 'd': 0x0c4079ef, 'r': 0x0804c214},
	0x0804c160 +  6 * 12:    {'l': 0x0804c178, 'd': 0x425ebd95, 'r': 0x0804c184},
	0x0804c160 +  7 * 12:    {'l': 0x0804c1cc, 'd': 0x07ace749, 'r': 0x0804c1a8},
	0x0804c160 +  8 * 12:    {'l': 0x0804c1e4, 'd': 0x237a3a88, 'r': 0x0804c184},
	0x0804c160 +  9 * 12:    {'l': 0x0804c1f0, 'd': 0x4b846cb6, 'r': 0x0804c184},
	0x0804c160 + 10 * 12:    {'l': 0x0804c214, 'd': 0x1fba9a98, 'r': 0x0804c1c0},
	0x0804c160 + 11 * 12:    {'l': 0x0804c19c, 'd': 0x3a4ad3ff, 'r': 0x0804c1c0},
	0x0804c160 + 12 * 12:    {'l': 0x0804c184, 'd': 0x16848c16, 'r': 0x0804c178},
	0x0804c160 + 13 * 12:    {'l': 0x0804c190, 'd': 0x499ee4ce, 'r': 0x0804c1b4},
	0x0804c160 + 14 * 12:    {'l': 0x0804c1c0, 'd': 0x261af8fb, 'r': 0x0804c184},
	0x0804c160 + 15 * 12:    {'l': 0x0804c1cc, 'd': 0x770ea82a, 'r': 0x0804c1fc}
}

xor_val = 0x47bbfa96

depth = 0

found = False
solution2 = []

def step(addr, xor_val, direction, solution):
    global depth
    global found
    global solution2
    depth += 1
    if depth > 10:
        depth -= 1
        return
    new_xor_val = xor_val ^ mem[mem[addr][direction]]['d']
    if new_xor_val == 0x40475194:
        print "0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[mem[addr][direction]]['d'], new_xor_val)
        print 'found'
        print len(solution)
        print solution
        found = True
        #exit()
        return
    solution.append('l')
    step(mem[addr][direction], new_xor_val, 'l', solution)
    if found:
        solution2.append('l')
        print 'l'
        print "0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[mem[addr][direction]]['d'], new_xor_val)
        return
    solution = solution[0:-1]
    solution.append('r')
    step(mem[addr][direction], new_xor_val, 'r', solution)
    if found:
        solution2.append('r')
        print 'r'
        print "0x%0.8x ^ 0x%0.8x = 0x%0.8x" % (xor_val, mem[mem[addr][direction]]['d'], new_xor_val)
        return
    solution = solution[0:-1]
    depth -= 1
    return

solution = []

solution2.append('l')
print 'l'
step(0x0804c160, 0x47bbfa96, 'l', solution)
if not found:
    solution2.append('r')
    print 'r'
    step(0x0804c160, 0x47bbfa96, 'r', solution)

print
print
print 'solution2'
print '---------'
print solution2

xor_val = 0x47bbfa96
addr = 0x0804c160
for direction in reversed(solution2):
    addr = mem[addr][direction]
    data = mem[addr]['d']
    xor_val = xor_val ^ data
    print "0x%0.8x" % xor_val

print
print
print 'solution1'
print '---------'

xor_val = 0x47bbfa96
addr = 0x0804c160
for direction in reversed(solution):
    addr = mem[addr][direction]
    data = mem[addr]['d']
    xor_val = xor_val ^ data
    print "0x%0.8x" % xor_val


