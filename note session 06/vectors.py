List01 = [1, 2, 3]
List02 = [4, 5, 6]


def multipliesTwoVectors(List01, List02):
    List = []
    assert len(List01) == len(List02)
    for i in range(0, len(List01)):
        v = List01[i] * List02[i]
        List.append(v)
    print(sum(List))


multipliesTwoVectors(List01=List01, List02=List02)
