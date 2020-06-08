import unittest
from Stack import MyStack, StackEmptyException

class Test_myStack(unittest.TestCase):
    def setUp(self):
        self.testStack = MyStack()

    def test_pop_emptyStackCase(self):
        with self.assertRaises(StackEmptyException):
            self.testStack.pop()

    def test_pop_done(self):
        self.testStack.push('abc')
        self.testStack.push('xyz')
        self.testStack.push('123')
        self.testStack.pop()
        self.assertEqual(self.testStack.data, ['abc','xyz'])


    def test_peek(self):
        with self.assertRaises(StackEmptyException):
            self.testStack.peek()

    def test_push_typeErrorCase(self):
        with self.assertRaises(TypeError):
            self.testStack.push(10)

    def test_push_done(self):
        self.testStack.push('abc')
        self.testStack.push('xyz')
        self.testStack.push('123')
        self.testStack.push('456')
        self.assertEqual(self.testStack.data, ['abc','xyz','123','456'])

    def test_contain(self):
        self.testStack.push('abc')
        self.assertTrue(self.testStack.contains('abc'), 'Must be True')
    
if __name__ == '__main__':
    unittest.main()