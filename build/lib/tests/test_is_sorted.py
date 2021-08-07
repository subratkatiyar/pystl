from pystl.is_sorted import is_sorted
from pystl import is_sorted

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2.0, 3, 4.0, 5, 6.0, 7.0, 8.0, 9, 10]
list3 = [1123, 21, 123, 4, 5123, 1236, 71, 1238, 9, 10]
list4 = [11.123, 9.123, 8.12, 7, 6, 5, 4]
list5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_is_sorted():
    assert is_sorted.is_sorted(list1) == True
    assert is_sorted.is_sorted(list2) == True
    assert is_sorted.is_sorted(list3) == False
    assert is_sorted.is_sorted(list4) == False
    assert is_sorted.is_sorted(list5) == False