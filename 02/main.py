def closest_to_zero(arr):
    distances = {}
    for elem in arr:
        distance = distances.get(abs(elem), [])
        distance.append(elem)
        distances[abs(elem)] = distance
    if not distances:
        return []
    return distances[min(distances)]


def merge(sequence1, sequence2):
    sequence_merged = []
    for elem in sequence1:
        if elem in sequence2 and elem not in sequence_merged:
            sequence_merged.append(elem)
    return sequence_merged


def test_closest_to_zero():
    assert closest_to_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]
    assert closest_to_zero([-5, 9, 6, -8]) == [-5]
    assert closest_to_zero([]) == []
    assert closest_to_zero([0]) == [0]


def test_merge():
    seq1 = [1, 1, 2, 5, 7]
    seq2 = (1, 1, 2, 3, 4, 7)
    assert merge(seq1, seq2) == [1, 2, 7]

    seq1 = [1, 2, 3]
    seq2 = [4, 5, 6]
    assert merge(seq1, seq2) == []

    seq1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    seq2 = (1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4)
    assert merge(seq1, seq2) == [1, 2, 3, 4]


test_closest_to_zero()
test_merge()
