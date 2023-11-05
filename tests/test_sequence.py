from ficus.sequence import ProportionalSequence

def test_proportional_sequence():
    seq = ProportionalSequence(2, 5, 10)
    for i in seq.items:
        print(i)