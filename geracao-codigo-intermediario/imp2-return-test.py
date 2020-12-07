import unittest
import tatsu
from impiler import Impiler
from pi import run

class TestImpGrammar(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_output(self, file_name, expect_output):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        pi_ast = self.parser.parse(source, semantics=Impiler())
        (trace, step, out, dt) = run(pi_ast, color=False)

        self.assertEqual(out, expect_output)

    def test_return_basic(self):
        # Call method that just return the parameter sended
        # and print it
        file_name = "examples_return/return_basic.imp2"
        expect_output = [1]
        self.__test_output(file_name, expect_output)

    def test_return_inside_if(self):
        # Call method that calculate your investiment return.
        # If you invest less than 3000, you have 2x of return.
        # If you invest more than 3000, you have 3x of return.
        # I print the result send 4000 and 2000 of values
        file_name = "examples_return/return_inside_if.imp2"
        expect_output = [12000, 4000]
        self.__test_output(file_name, expect_output)

    def test_return_inside_while(self):
        # Call method created just to test go_to_ret inside while
        # It's a method that increase your parameter value until 100
        # and than return it. But the while is with a conditional True
        # forever, so the go_to_ret will need to break the while block and
        # go to return outside while
        file_name = "examples_return/return_inside_while.imp2"
        expect_output = [100]
        self.__test_output(file_name, expect_output)

    def test_return_factorial_not_recursive(self):
        # Call method that calculate factorial, with a way not
        # recursive. I pass 5 with parameter
        file_name = "examples_return/return_factorial.imp2"
        expect_output = [120]
        self.__test_output(file_name, expect_output)

    def test_return_fibonacci_not_recursive(self):
        # Call method that calculate N first fib numbers. I pass N = 6
        file_name = "examples_return/return_fibonacci.imp2"
        expect_output = [[0, 1, 1, 2, 3, 5]]
        self.__test_output(file_name, expect_output)

    def test_return_factorial_recursive(self):
        # raise error on my implementation
        file_name = "examples_return/return_factorial_recursive.imp2"
        expect_output = [120]
        self.__test_output(file_name, expect_output)

        
if __name__ == '__main__':
    unittest.main()
