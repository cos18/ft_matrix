from Vector import Vector


class TestVector:
    def test_vector_mutable(self):
        test_list = [10, 20]
        v = Vector(test_list)
        test_list.append(30)
        assert len(v) == 2

    def test_vector_str(self):
        v = Vector([10, 20])
        assert str(v) == "[10, 20]"
