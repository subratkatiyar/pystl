import pytest
from pystl import lower_bound

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2.0, 3, 4.0, 5, 6.0, 7.0, 8.0, 9, 10]
list3 = [1123, 21, 123, 4, 5123, 1236, 71, 1238, 9, 10]
list4 = [11.123, 9.123, 8.12, 7, 6, 5, 4]
list5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_lower_bound():
    assert lower_bound.lower_bound(list1, 5) == 4
    assert lower_bound.lower_bound(list1, 11) == 10
    assert lower_bound.lower_bound(list1, 0) == -1
    with pytest.raises(ValueError):
        lower_bound.lower_bound(list3, 20)
        lower_bound.lower_bound(list4, 6)
        lower_bound.lower_bound(list5, 14)
