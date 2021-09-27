try:
    num_a = int(input("Enter a number between 1 and 5: "))
    num_b = int(input("Enter a number between 5 and 10: "))
    assert num_a >= 1, "number must be between greater or eq to 1"
    assert num_a <= 5, "number must be less than or eq to 5"
    assert num_b >= 5, "number must be between less than or eq to 5"
    assert num_b <= 10
    num_c = num_b ** num_a
    print("%d is the result" % num_c)

except OSError as e:
    print(e)
