def test(list):
    if list.count(19) == 2 and list.count(5) >= 3:
        print("There are exactly 2 occurences of 19 and", list.count(5), "occurences of 5")
    else:
        print("There is", list.count(19), "of 19. \nThere is", list.count(5), "of 5.")

nums = [19, 19, 1, 5, 5, 5, 5, 5]

test(nums)