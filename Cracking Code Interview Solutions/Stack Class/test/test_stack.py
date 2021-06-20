import unittest
from stack.stack import stack

class stackTest(unittest.TestCase):
    def setUp(self):
        self.test_stack = stack()

    def test_isEmptyTest(self):
        self.assertTrue(self.test_stack.isempty())

    def test_peek(self):
        self.test_stack.push(1)
        self.assertEqual(self.test_stack.peek(), 1)

    def test_push(self):
        self.test_stack.push("Hello ")
        self.test_stack.push("World!")
        self.assertEqual(self.test_stack.peek(), "World!")

    def test_pop(self):
        self.test_stack.push("Hello ")
        self.test_stack.push("World!")
        self.test_stack.pop()
        self.assertEqual(self.test_stack.peek(), "Hello ")

    def test_size(self):
        self.test_stack.push(True)        
        self.test_stack.push(False)        
        self.test_stack.push(True)
        self.assertEqual(self.test_stack.size(),3)   

if __name__ == '__main__':
    unittest.main()


