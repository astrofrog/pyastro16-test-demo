import pytest

def test_pass():
    print("hello")


def test_equality():
    a = 1
    assert a == 1


# def test_fails():
#     a = 1
#     assert a != 1


def test_sum():
    a = [1,2,3]
    assert sum(a) == 6


def test_catch_exception():
    a = 1
    with pytest.raises(AttributeError):
        a.sort()

def test_catch_exception_msg():
    a = 1
    with pytest.raises(AttributeError) as exc:
        a.sort()
    assert exc.value.args[0] == "'int' object has no attribute 'sort'"


@pytest.mark.parametrize(('values', 'result'),
                         [([1], 1),
                          ([1,2], 3),
                          ([1,2,3], 6)])
def test_sum(values, result):
    assert sum(values) == result
    
    
import os

DATA = os.path.join(os.path.dirname(__file__), 'MSX_E.fits')
    
def test_fits():
    from astropy.io import fits
    hdulist = fits.open(DATA)
    hdulist.close()
    

def test_write(tmpdir):
    filename = tmpdir.join('data.txt').strpath
    print(filename)
    with open(filename, 'w') as f:
        f.write("BANANA!!")


















    
    
    

