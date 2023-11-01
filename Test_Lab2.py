import Lab2

def test_find_min_max():
    input = [5,4,2]
    result = Lab2.find_min_max(input)
    test_result = [2,5]

    assert (result == test_result)

def test_calc_average():
    input = [1,2,3]
    result = Lab2.calc_average(input)
    test_result = 2

    assert (result == test_result)

def test_median_temperature():
    input = [1,3,5,7,9]
    result = Lab2.calc_median_temperature(input)
    test_result = 5

    assert (result == test_result)

