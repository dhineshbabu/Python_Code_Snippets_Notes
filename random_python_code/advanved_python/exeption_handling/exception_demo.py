# Exceptions

from typing import cast


def test_one(x, y):
    try:
        z = x / y
        print(f'Result: {z}')
    except:
        print(f'Something bad happened x: {x} , y: {y}')
    finally:
        # moving along
        print('Complete')

test_one(5, 0)
test_one(5, 'Cat')
test_one(5, 2)

def test_two(x, y):
    try:
        assert(x>0)
        assert(y>0)
    except AssertionError:
        print(f'Failed to assert x:{x}, y:{y}')
    except Exception as e:
       print(f'Something bad happened x: {x} , y: {y}, issue: {e}')
    else:
        z = x/y 
        print(f'Result: {z}')
    finally:
        print('Complete')

test_two(5, 0)
test_two(5, 'Cat')
test_two(5, 2)

# User Defined Exception and Raising
class CatError(RuntimeError):
    def __init__(self, *args: object) -> None:
        # super().__init__(*args)
        self.args = args

def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty < 9:
            raise CatError('Must Own more than 9 cats')
    except Exception as e:
        print(f'Oops: {e.args}')
    finally:
        print('complete')

test_cats(3)
test_cats('ABC')
test_cats(12.3)
test_cats(11)