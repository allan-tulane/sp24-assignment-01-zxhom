"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  if x <= 1:
    return x

  else:
    ra = foo(x - 1)
    rb = foo(x - 2)
    return ra + rb


def test_foo():
  assert foo(0) == 0
  assert foo(1) == 1
  assert foo(2) == 1
  assert foo(3) == 2
  assert foo(4) == 3
  assert foo(5) == 5
  assert foo(6) == 8
  assert foo(7) == 13


test_foo()


def longest_run(mylist, key):
  count = 0
  max_count = 0
  for i in range(len(mylist)):
    if mylist[i] == key:
      count += 1
      #print("key: ", count)
    else:
      if count > max_count:
        max_count = count
        #print("if: ", count)
        count = 0
      else:
        #print("else: ", count)
        count = 0
  if count > max_count:
    max_count = count

  #return print("max run: ", max_count)
  return max_count


def test_longest_run():
  assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
  assert longest_run([3, 2, 2, 3, 2, 2, 2, 2], 2) == 4
  assert longest_run([3, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1], 1) == 8
  assert longest_run([1, 4, 5, 2, 9, 9, 9, 2, 6, 3, 9, 9, 1, 3, 9, 9], 9) == 3


test_longest_run()


class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def to_value(v):
  """
    if it is a Result object, return longest_size.
    else return v
    """
  if type(v) == Result:
    return v.longest_size
  else:
    return int(v)


def longest_run_recursive(mylist, key):
  # Base Case when mylist = 1
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)

    else:
      return Result(0, 0, 0, False)
  else:
    # Recursive Case
    mid = len(mylist) // 2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)
    # Case 1: both sides are entirely the key
    if (left.is_entire_range and right.is_entire_range) == True:
      return Result(left.longest_size + right.longest_size,
                    left.longest_size + right.longest_size,
                    left.longest_size + right.longest_size, True)
    # Case 2: left side is entirely the key but right is not
    elif left.is_entire_range == True and right.is_entire_range == False:
      return Result(
          left.longest_size + right.left_size, right.right_size,
          max(left.longest_size + right.left_size, right.longest_size), False)
    # Case 3: right side is entirely the key but left is not
    elif left.is_entire_range == False and right.is_entire_range == True:
      # Run on left side to find longest run for middle case
      return Result(
          left.left_size, left.right_size + right.longest_size,
          max(left.right_size + right.longest_size, left.longest_size), False)
    else:
      # checks for middle case when key runs in both left/right
      return Result(
          left.left_size, right.right_size,
          max(left.longest_size, right.longest_size,
              left.right_size + right.left_size), False)


#print(to_value(longest_run_recursive([3, 2, 2, 3, 2, 2, 2, 2], 2)))
#print(to_value(
#           longest_run_recursive([3, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1], 1)))


def test_longest_run_recursive():
  assert (to_value(
      longest_run_recursive([2, 12, 12, 8, 12, 12, 12, 0, 12, 1],
                            12)) == 3) == True
  assert (to_value(longest_run_recursive([3, 2, 2, 3, 2, 2, 2, 2],
                                         2)) == 4) == True
  assert (to_value(
      longest_run_recursive([3, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1],
                            1)) == 8) == True
  assert (to_value(
      longest_run_recursive([1, 4, 5, 2, 9, 9, 9, 2, 6, 3, 9, 9, 1, 3, 9, 9],
                            9)) == 3) == True
  assert (to_value(
      longest_run_recursive([1, 4, 5, 2, 9, 9, 9, 2, 6, 3, 9, 9, 1, 3, 9, 9],
                            10)) == 0) == True
  assert (to_value(longest_run_recursive([2, 2, 2, 2, 2, 2, 2, 2, 2],
                                         2)) == 9) == True


test_longest_run_recursive()
