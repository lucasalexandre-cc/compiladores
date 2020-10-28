import unittest
import tatsu                            

class TestImpGrammar(unittest.TestCase):
    def setUp(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        self.parser = tatsu.compile(imp_grammar)

    def __test_parse(self, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        self.assertEqual(str(self.parser.parse(source)), ast)

    def test_cmd_parse0(self):
        '''
        Escreva um programa Imp examples/cmd-test0.imp2 que tenha a árvore sintática dada
        pela string passada como segundo parâmetro de __test_parse.
        '''
        self.__test_parse('examples/cmd-test0.imp2', "AST({'ds': AST({'d': AST({'op': 'var', 'idn': ['x', 'y'], 'e': ['10', '1']})}), 'cs': AST({'ac': [AST({'op': 'while', 't': AST({'e': AST({'e1': 'x', 'op': '>', 'e2': '0'})}), 'b': AST({'ds': [], 'cs': AST({'ac': [AST({'idn': 'y', 'op': ':=', 'e': AST({'e1': 'y', 'op': '*', 'e2': 'x'})}), AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': 'x', 'op': '-', 'e2': '1'})})]})})}), AST({'op': 'print', 'e': AST({'e': 'y'})})]})})")

    def test_cmd_parse1(self):
        '''
        Escreva um programa Imp examples/cmd-test1.imp2 que tenha a árvore sintática dada
        pela string passada como segundo parâmetro de __test_parse.
        '''
        self.__test_parse('examples/cmd-test1.imp2',"AST({'ds': AST({'d': AST({'op': 'var', 'idn': ['x', 'y', 'z'], 'e': ['1', '0', '0']})}), 'cs': AST({'ac': [AST({'idn': 'x', 'op': ':=', 'e': '0'}), AST({'idn': 'y', 'op': ':=', 'e': '1'}), AST({'idn': 'z', 'op': ':=', 'e': '3'}), AST({'op': 'if', 't': AST({'e': AST({'e1': 'x', 'op': '<', 'e2': '2'})}), 'b1': AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'z', 'op': ':=', 'e': '3'})})})}), AST({'op': 'print', 'e': AST({'e': 'z'})})]})})")
        
if __name__ == '__main__':
    unittest.main()
