nums = [1, 2, 3, 4]

i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        print("No more data")
        break
