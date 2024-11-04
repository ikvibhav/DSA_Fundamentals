import unittest

from ..canConstruct import can_construct


class TestCan(unittest.TestCase):

    def test_can_construct(self):
        self.assertEqual(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']), True)
        self.assertEqual(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), False)
        self.assertEqual(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']), True)
        self.assertEqual(can_construct('eeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']), False)


if __name__ == "__main__":
    unittest.main()