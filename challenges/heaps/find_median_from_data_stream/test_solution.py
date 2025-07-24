from .solution import MedianFinder


def test_median_finder():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0

    mf2 = MedianFinder()
    mf2.add_num(-1)
    mf2.add_num(-2)
    mf2.add_num(-3)
    assert mf2.find_median() == -2.0
    mf2.add_num(-4)
    assert mf2.find_median() == (-2 + -3) / 2
