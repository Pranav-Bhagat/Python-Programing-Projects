# Some Test objects
R1 = Robbery(5,  '01:00')
R2 = Robbery(6,  '13:00')
R3 = Robbery(7,  '00:01')
R4 = Robbery(8,  '12:00')
R5 = Robbery(9,  '06:03')
R6 = Robbery(11, '06:09')
R7 = Robbery(11, '18:09')
R8 = Robbery(12)
R9 = Robbery(12)

# Constructor tests
assert R8.crime_id == 12
assert R8.time == None
assert R3.crime_id == 7
assert R3.time == '00:01'
assert R2.crime_id == 6
assert R2.time == '13:00'
assert R1.crime_id == 5
assert R1.time == '01:00'

# equals test
assert not(R1 == R2)
assert (R6 == R6)
assert (R9 == R9)

# representation tests
assert repr(R1) == '5\t1:00AM\n'
assert repr(R2) == '6\t1:00PM\n'
assert repr(R3) == '7\t12:01AM\n'
assert repr(R4) == '8\t12:00PM\n'
assert repr(R5) == '9\t6:03AM\n'
assert repr(R6) == '11\t6:09AM\n'
assert repr(R7) == '11\t6:09PM\n'
assert repr(R8) == '12\tNone\n'
assert repr(R9) == '12\tNone\n'

# Less than tests
assert R1 < R2
assert not(R2 < R1)
assert R3 < R1
assert R3 < R4
assert R5 < R6
assert not(R6 < R5)
assert R6 < R7
assert not(R8 < R9)
assert R1 < R6

# copy tests
assert R1.copy() == R1
assert R9.copy() == R9
assert R8.copy() == R9

# Sort tests
assert sort_crimes([R5, R4], 'id') == [R4, R5]
assert sort_crimes([R4, R5], 'id') == [R4, R5]
assert sort_crimes([R9, R8, R7,
    R6, R5, R4, R3, R2, R1], 'id') == [R1, R2, 
            R3, R4, R5, R6, R7, R8, R9]
assert sort_crimes([], 'id') == []

assert sort_crimes([R5, R4], 'time') == [R5, R4]
assert sort_crimes([R4, R5], 'time') == [R5, R4]
assert (sort_crimes([R9, R8, R7, R6, R5, R4, R3, R2, R1], 
    'time')) ==  (sort_crimes_time([R9, R8, R7, R6, R5, R4, R3, R2, R1] ))

assert (sort_crimes([R9, R8, R7, R6, R5, R4, R3, R2, R1], 
    'id')) ==  (sort_crimes_id([R9, R8, R7, R6, R5, R4, R3, R2, R1] ))

assert sort_crimes([R5, R4], '') == None

# Search tests
most_crimes = [R1, R2, R3, R5, R6, R8]
assert find_crime(most_crimes, R1.crime_id) == 0
assert find_crime(most_crimes, R2.crime_id) == 1
assert find_crime(most_crimes, R3.crime_id) == 2
assert find_crime(most_crimes, R4.crime_id) == -1
assert find_crime(most_crimes, R5.crime_id) == 3
assert find_crime(most_crimes, R6.crime_id) == 4
assert find_crime(most_crimes, R8.crime_id) == 5
