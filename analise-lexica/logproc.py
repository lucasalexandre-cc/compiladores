# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 

def t_TIMESTAMP(t):
    r'\d{2}:\d{2}:\d{2}.\d{6}\s-\d{4}'
    t.type = 'TIMESTAMP'
    return t

def t_PROC(t):
    r'\t.*\t'
    t.type = 'PROC'
    t.value = t.value[1:len(t.value) - 1]
    return t

def t_MESSAGE(t):
    r'.+'
    t.type = 'MESSAGE'
    return t

# Error handling rule
def t_error(t):
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            if tok.type == "PROC" and tok.value == "kernel":
                tok_kernel_message = self.lexer.token()
                tokens.append(tok_kernel_message)
                
        return tokens
        
if __name__ == '__main__':
    print(LogProcLexer().collect_messages())
    
