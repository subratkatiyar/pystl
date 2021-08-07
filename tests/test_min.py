from pystl import min

def test_min():
    assert min.min(1,2) == 1
    assert min.min(1.12,1.13) == 1.12
    assert min.min(3,2.12) == 2.12

