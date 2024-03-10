import unittest
import codeDocumentation

class TestAdd(unittest.TestCase): ## unit tests can be written by inheriting unittest.TestCase
    
  def test_add_positive(self):
    myClass = codeDocumentation.Calculator()
    result = myClass.add(2, 3)
    self.assertEqual(result, 5)

  def test_add_should_raise_exception_if_given_non_integers(self):
    myClass = codeDocumentation.Calculator()   
    with self.assertRaises(TypeError):
      myClass.add('hejsan', 3)

if __name__ == '__main__':
  unittest.main()