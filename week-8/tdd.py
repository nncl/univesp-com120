from functions import sum

def test_sum():
    assert sum([1,2,3]) == 6, 'should return 6 when summing list'

def test_multiply():
    assert sum([1,2,3]) == 6, 'should return 6 when multiplying list'

if __name__ == '__main__':
    test_sum()
    test_multiply()

    print('All good')