from .solution import coin_change_canonical, coin_change_user


def test_coin_change():
    coins = [1, 2, 5]
    amount = 11
    expected = 3
    for solution in [coin_change_user, coin_change_canonical]:
        assert solution(coins, amount) == expected

    coins2 = [2]
    amount2 = 3
    expected2 = -1
    for solution in [coin_change_user, coin_change_canonical]:
        assert solution(coins2, amount2) == expected2

    coins3 = [1]
    amount3 = 0
    expected3 = 0
    for solution in [coin_change_user, coin_change_canonical]:
        assert solution(coins3, amount3) == expected3
