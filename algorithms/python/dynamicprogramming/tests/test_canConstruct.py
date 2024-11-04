import unittest

from ..canConstruct import can_construct, can_construct_memo


class TestCan(unittest.TestCase):

    def test_can_construct(self):
        self.assertTrue(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertFalse(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
        self.assertTrue(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
        self.assertFalse(can_construct('eeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
    
    def test_can_construct_memo(self):
        self.assertTrue(can_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
        self.assertFalse(can_construct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
        self.assertTrue(can_construct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
        self.assertFalse(can_construct_memo('eeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {}))      


if __name__ == "__main__":
    unittest.main()