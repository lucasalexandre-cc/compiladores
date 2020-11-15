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

    def test_array_inicialization(self):
        # Initialize array [1, 2, 3, 4, 5] and print it
        file_name = "examples_array/array_init.imp2"
        expect_output = [[1, 2, 3, 4, 5]]
        self.__test_output(file_name, expect_output)

    def test_array_projection(self):
        # Initialize array [1, 2, 3, 4, 5] and print last element
        file_name = "examples_array/array_projection.imp2"
        expect_output = [5]
        self.__test_output(file_name, expect_output)

    def test_array_append(self):
        # Initialize array [1, 2, 3, 4, 5], append a new value 6 and print the array
        file_name = "examples_array/array_append.imp2"
        expect_output = [[1, 2, 3, 4, 5, 6]]
        self.__test_output(file_name, expect_output)

    def test_array_concat(self):
        # Initialize array [1, 2, 3, 4, 5], concat with a new array [6, 7, 8] and print the final array
        file_name = "examples_array/array_concat.imp2"
        expect_output = [[1, 2, 3, 4, 5, 6, 7, 8]]
        self.__test_output(file_name, expect_output)
    
    def test_array_size(self):
        # Initialize array [1, 2, 3, 4, 5, 6] and print it size
        file_name = "examples_array/array_size.imp2"
        expect_output = [6]
        self.__test_output(file_name, expect_output)

    def test_array_bubble_sort(self):
        # Sort array [54,26,93,17,77,31,44,55,20] and print sorted array
        file_name = "examples_array/array_bubble_sort.imp2"
        expect_output = [[17, 20, 26, 31, 44, 54, 55, 77, 93]]
        self.__test_output(file_name, expect_output)
        
if __name__ == '__main__':
    unittest.main()
