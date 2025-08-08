import numpy as np


def hello():
  """
  This is a sample function that we will try to import and run to ensure that
  our environment is correctly set up on Google Colab.
  """
  print('Hello from numpy_basic.py!')


def create_sample_array():
  """
  Return a numpy array of shape (3, 2) which is filled with zeros, except for
  element (0, 1) which is set to 10 and element (1, 0) which is set to 100.

  Inputs: None

  Returns:
  - Array of shape (3, 2) as described above.
  """
  x = np.array([[0, 10], [100, 0], [0, 0]])
  return x


def mutate_array(x, indices, values):
  """
  Mutate the  array x according to indices and values.
  Specifically, indices is a list [(i0, j0), (i1, j1), ... ] of integer indices,
  and values is a list [v0, v1, ...] of values. This function should mutate x
  by setting:

  x[i0, j0] = v0
  x[i1, j1] = v1

  and so on.

  If the same index pair appears multiple times in indices, you should set x to
  the last one.

  Inputs:
  - x: An array of shape (H, W)
  - indicies: A list of N tuples [(i0, j0), (i1, j1), ..., ]
  - values: A list of N values [v0, v1, ...]

  Returns:
  - The input array x
  """
  for indice, value in zip(indices, values):
    x[indice[0], indice[1]] = value

  return x


def count_array_elements(x):
  """
  Count the number of scalar elements in an array x.

  For example, an array of shape (10,) has 10 elements.an array of shape (3, 4)
  has 12 elements; an array of shape (2, 3, 4) has 24 elements, etc.

  You may not use the functions np.size or x.size. The input array should
  not be modified.

  Inputs:
  - x: An array of any shape

  Returns:
  - num_elements: An integer giving the number of scalar elements in x
  """
  num_elements = 1
  for dimension in x.shape:
    num_elements *= dimension
  return num_elements


def create_array_of_pi(M, N):
  """
  Returns an array of shape (M, N) filled entirely with the value 3.14

  Inputs:
  - M, N: Positive integers giving the shape of array to create

  Returns:
  - x: An array of shape (M, N) filled with the value 3.14
  """
  x = np.full((M, N), np.pi)
  return x


def multiples_of_ten(start, stop):
  """
  Returns an array of dtype numpy.float64 that contains all of the multiples of
  ten (in order) between start and stop, inclusive. If there are no multiples
  of ten in this range you should return an empty array of shape (0,).

  Inputs:
  - start, stop: Integers with start <= stop specifying the range to create.

  Returns:
  - x: array of dtype float64 giving multiples of ten between start and stop.
  """
  x = None
  multiples = []
  for i in range(start, stop + 1):
    if i % 10 == 0:
      multiples.append(i)
  x = np.array(multiples, dtype = np.float64)
  return x


def slice_indexing_practice(x):
  """
  Given a two-dimensional array x, extract and return several subarrays to
  practice with slice indexing. Each array should be created using a single
  slice indexing operation.

  The input array should not be modified.

  Input:
  - x: array of shape (M, N) -- M rows, N columns with M >= 3 and N >= 5.

  Returns a tuple of:
  - last_row: array of shape (N,) giving the last row of x. It should be a
    one-dimensional array.
  - third_col: array of shape (M, 1) giving the third column of x.
    It should be a two-dimensional array.
  - first_two_rows_three_cols: array of shape (2, 3) giving the data in the
    first two rows and first three columns of x.
  - even_rows_odd_cols: Two-dimensional array containing the elements in the
    even-valued rows and odd-valued columns of x.
  """
  out = None
  last_row = x[-1]
  third_col = x[:, 2:3]
  first_two_rows_three_cols = x[0:2, 0:3]
  even_rows_odd_cols = x[0::2, 1::2]
  out = (last_row, third_col, first_two_rows_three_cols, even_rows_odd_cols)
  return out


def slice_assignment_practice(x):
  """
  Given a two-dimensional array of shape (M, N) with M >= 4, N >= 6, mutate its
  first 4 rows and 6 columns so they are equal to:

  [0 1 2 2 2 2]
  [0 1 2 2 2 2]
  [3 4 3 4 5 5]
  [3 4 3 4 5 5]

  Your implementation must obey the following:
  - You should mutate the array x in-place and return it
  - You should only modify the first 4 rows and first 6 columns; all other
    elements should remain unchanged
  - You may only mutate the array using slice assignment operations, where you
    assign an integer to a slice of the array
  - You must use <= 6 slicing operations to achieve the desired result

  Inputs:
  - x: An array of shape (M, N) with M >= 4 and N >= 6

  Returns: x
  """
  x[0:2, 0] = 0
  x[0:2, 1] = 1
  x[0:2, 2:6] = 2
  x[2:4, 0:3:2] = 3
  x[2:4, 1:4:2] = 4
  x[2:4, 4:6] = 5
  
  return x


def shuffle_cols(x):
  """
  Re-order the columns of an input array as described below.

  Your implementation should construct the output array using a single integer
  array indexing operation. The input array should not be modified.

  Input:
  - x: An array of shape (M, N) with N >= 3

  Returns: An array y of shape (M, 4) where:
  - The first two columns of y are copies of the first column of x
  - The third column of y is the same as the third column of x
  - The fourth column of y is the same as the second column of x
  """
  idx = np.array([0, 0, 2, 1])
  y = x[:, idx]
  return y


def reverse_rows(x):
  """
  Reverse the rows of the input array.

  Your implementation should construct the output array using a single integer
  array indexing operation. The input array should not be modified.

  Input:
  - x: An array of shape (M, N)

  Returns: An array y of shape (M, N) which is the same as x but with the rows
           reversed; that is the first row of y is equal to the last row of x,
           the second row of y is equal to the second to last row of x, etc.
  """
  idx = list(reversed(np.arange(x.shape[0])))
  y = x[idx]
  return y


def take_one_elem_per_col(x):
  """
  Construct a new array by picking out one element from each column of the
  input array as described below.

  The input array should not be modified.

  Input:
  - x: An array of shape (M, N) with M >= 4 and N >= 3.

  Returns: An array y of shape (3,) such that:
  - The first element of y is the second element of the first column of x
  - The second element of y is the first element of the second column of x
  - The third element of y is the fourth element of the third column of x
  """
  idx0 = np.array([0, 1, 2])  
  idx1 = np.array([1, 0, 3])
  y = x[idx1, idx0]
  return y


def count_negative_entries(x):
  """
  Return the number of negative values in the input array x.

  Your implementation should perform only a single indexing operation on the
  input array. You should not use any explicit loops. The input array should
  not be modified.

  Input:
  - x: An array of any shape

  Returns:
  - num_neg: Integer giving the number of negative values in x
  """
  num_neg = x[x < 0].size
  return num_neg


def make_one_hot(x):
  """
  Construct an array of one-hot-vectors from a list of Python integers.

  Input:
  - x: A list of N integers

  Returns:
  - y: An array of shape (N, C) and where C = 1 + max(x) is one more than the max
       value in x. The nth row of y is a one-hot-vector representation of x[n];
       In other words, if x[n] = c then y[n, c] = 1; all other elements of y are
       zeros. The dtype of y should be numpy.float32.
  """
  y = np.zeros((len(x), max(x) + 1), dtype=np.float32)
  for i, n in enumerate(x):
    y[i, n] = 1
  return y


def reshape_practice(x):
  """
  Given an input array of shape (24,), return a reshaped array y of shape
  (3, 8) such that

  y = [
    [x[0], x[1], x[2],  x[3],  x[12], x[13], x[14], x[15]],
    [x[4], x[5], x[6],  x[7],  x[16], x[17], x[18], x[19]],
    [x[8], x[9], x[10], x[11], x[20], x[21], x[22], x[23]],
  ]

  You must construct y by performing a sequence of reshaping operations on x
  (view, t, transpose, permute, contiguous, reshape, etc). The input array
  should not be modified.

  Input:
  - x: An array of shape (24,)

  Returns:
  - y: A reshaped version of x of shape (3, 8) as described above.
  """
  y = x.reshape(2, 3, 4).copy()
  y = y.transpose(1, 0, 2)
  y = y.reshape(3, 8)
  return y


def zero_row_min(x):
  """
  Return a copy of x, where the minimum value along each row has been set to 0.

  For example, if x is:
  x = numpy.array([[
        [10, 20, 30],
        [ 2,  5,  1]
      ]])

  Then y = zero_row_min(x) should be:
  numpy.array([
    [0, 20, 30],
    [2,  5,  0]
  ])

  Your implementation should use reduction and indexing operations; you should
  not use any explicit loops. The input array should not be modified.

  Inputs:
  - x: array of shape (M, N)

  Returns:
  - y: array of shape (M, N) that is a copy of x, except the minimum value
       along each row is replaced with 0.
  """
  y = x.copy()
  idx0 = np.arange(y.shape[0])
  min_index_axis1 = np.argmin(y, axis=1)
  y[idx0, min_index_axis1] = 0
  
  return y


def batched_matrix_multiply(x, y, use_loop=True):
  """
  Perform batched matrix multiplication between the array x of shape (B, N, M)
  and the array y of shape (B, M, P).

  If use_loop=True, then you should use an explicit loop over the batch
  dimension B. If loop=False, then you should instead compute the batched
  matrix multiply without an explicit loop using a single  operator.

  Inputs:
  - x: array of shape (B, N, M)
  - y: array of shape (B, M, P)
  - use_loop: Whether to use an explicit Python loop.

  Hint: numpy.stack, bmm

  Returns:
  - z: array of shape (B, N, P) where z[i] of shape (N, P) is the result of
       matrix multiplication between x[i] of shape (N, M) and y[i] of shape
       (M, P). It should have the same dtype as x.
  """
  z = None

  B, N, M = x.shape  
  _, _, P = y.shape  
    
  if use_loop:  
    z = np.empty((B, N, P), dtype=x.dtype)  
    for i in range(B):  
      z[i] = np.matmul(x[i], y[i])  
  else:  
    z = np.matmul(x, y)
  return z


def normalize_columns(x):
  """
  Normalize the columns of the matrix x by subtracting the mean and dividing
  by standard deviation of each column. You should return a new array; the
  input should not be modified.

  More concretely, given an input array x of shape (M, N), produce an output
  array y of shape (M, N) where y[i, j] = (x[i, j] - mu_j) / sigma_j, where
  mu_j is the mean of the column x[:, j].

  Your implementation should not use any explicit Python loops (including
  list/set/etc comprehensions); you may only use basic arithmetic operations on
  arrays (+, -, *, /, **, sqrt), the sum reduction function, and reshape
  operations to facilitate broadcasting. You should not use numpy.mean,
  numpy.std, or their instance method variants x.mean, x.std.

  Input:
  - x: array of shape (M, N).

  Returns:
  - y: array of shape (M, N) as described above. It should have the same dtype
    as the input x.
  """
  M, N = x.shape
  y = np.empty((M, N), dtype=x.dtype)

  mean = np.sum(x, axis=0) / M
  squared_diff = (x - mean) ** 2  
  variance = np.sum(squared_diff, axis=0) / (M-1)
  std = np.sqrt(variance)

  y = (x - mean) / std
  return y