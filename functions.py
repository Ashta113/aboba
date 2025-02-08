def prod_non_zero_diag(x):
    n = 1
    for i in range(min(len(x), len(x[0]))):
        if (x[i][i] != 0):
            n *= x[i][i]
    return n


def are_multisets_equal(x, y):
    s1 = set(x)
    s2 = set(y)
    return s1 == s2


def max_after_zero(x):
    n = x[0]
    for i in range(1, len(x)):
        if x[i - 1] == 0 and (n == x[0] or n < x[i]):
            n = x[i]
    return n


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
