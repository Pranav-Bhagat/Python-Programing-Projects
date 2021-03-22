# tests

test_img = [
    [225, 000, 000], [000, 225, 000], [000, 000, 225], 
    [225, 225, 000], [225, 000, 000], [225, 000, 000], 
    [225, 225, 225], [000, 225, 000], [000, 225, 000]
]

fade_1 = [[45, 0, 0], [0, 45, 0], [0, 0, 45],
        [45, 45, 0], [225, 0, 0], [45, 0, 0],
        [45, 45, 45], [0, 45, 0], [0, 45, 0]]

fade_2 = [[13, 0, 0], [0, 22, 0], [0, 0, 13],
        [22, 22, 0], [225, 0, 0], [22, 0, 0],
        [13, 13, 13], [0, 22, 0], [0, 13, 0]]

fade_3 = [[6, 0, 0], [0, 14, 0], [0, 0, 6],
        [14, 14, 0], [225, 0, 0], [14, 0, 0],
        [6, 6, 6], [0, 14, 0], [0, 6, 0]]

blur_1 = [[61, 7, 0], [43, 4, 1], [59, 3, 1],
        [41, 8, 1], [29, 6, 1], [39, 5, 1],
        [61, 8, 1], [43, 6, 1], [59, 5, 0]]

blur_2 = [[29, 6, 1], [29, 6, 1], [29, 6, 1],
        [29, 6, 1], [29, 6, 1], [29, 6, 1],
        [29, 6, 1], [29, 6, 1], [29, 6, 1]]

blur_3 = [[29, 6, 1], [29, 6, 1], [29, 6, 1],
        [29, 6, 1], [29, 6, 1], [29, 6, 1],
        [29, 6, 1], [29, 6, 1], [29, 6, 1]]


assert fade_image(test_img, 3, 1, 1, 1) == fade_1
assert fade_image(test_img, 3, 1, 1, 2) == fade_2
assert fade_image(test_img, 3, 1, 1, 3) == fade_3

assert blur_image(test_img, 3, 1) == blur_1
assert blur_image(test_img, 3, 2) == blur_2
assert blur_image(test_img, 3, 3) == blur_3

usage1 = "Usage: python3 pixelmagic.py <mode> <image>"
usage2 = "Usage: python3 pixelmagic.py fade <image> <row> <col> <radius>"
usage3 = "Error: Invalid mode"
usage4 = "Could not open file INVALID_FILE"
assert check_args(['pixelmagic.py']) ==  usage1
assert check_args(['pixelmagic.py','fade','INVALID_FILE']) ==  usage2
assert check_args(['pixelmagic.py','NO_MODE','INVALID_FILE']) ==  usage3
assert check_args(['pixelmagic.py','blur','INVALID_FILE']) ==  usage4
assert check_args(['pixelmagic.py','blur','pixelmagic.py']) ==  None
