# Homework 3 - hw3.py
# Alex Pine
# 2015/02/15

## Taken from http://web.stanford.edu/class/cs221/ Assignment #2 Support Code

def dotProduct(d1, d2):
    """
    @param dict d1: a feature vector represented by a mapping from a feature (string) to a weight (float).
    @param dict d2: same as d1
    @return float: the dot product between d1 and d2
    """
    if len(d1) < len(d2):
        return dotProduct(d2, d1)
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.iteritems())

def increment(d1, scale, d2):
    """
    Implements d1 += scale * d2 for sparse vectors.
    @param dict d1: the feature vector which is mutated.
    @param float scale
    @param dict d2: a feature vector.
    """
    for f, v in d2.iteritems():
        d1[f] = d1.get(f, 0) + v * scale


def scale(d1, scale):
    '''Question 3.2 and 4.2: A function to scale a feature weight vector by a scalar.'''
    for f, v in d1.iteritems():
        d1[f] = d1[f] * scale
