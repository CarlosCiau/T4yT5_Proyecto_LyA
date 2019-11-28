# Copyright 2016 Carlos Gutierrez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import ply.lex as lex

# TOKENS http://php.net/manual/es/tokens.php
tokens = (

    # OPEN AND CLOSE TAG
    'OPENTAG','CLOSETAG',

    # RESERVERD WORDS LIST
    # http://php.net/manual/es/reserved.keywords.php
    
    'ABSTRACT', 'ASSERT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH', 'CHAR', 
    'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE', 'ENUM',
    'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'GOTO', 'IF', 'IMPLEMENTS', 
    'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LONG', 'NATIVE', 'NEW', 'PACKAGE',
    'PRIVATE', 'PROTECTED', 'PUBLIC', 'RETURN', 'SHORT', 'STATIC', 'STRICTFP',
    'SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 'THROW', 'THROWS', 'TRANSIENT',
    'TRY', 'VOLATILE', 'WHILE','AND','ARRAY', 


    #boolean
    'TRUE','FALSE',

    # SYMBOLS
    'PLUS','PLUSPLUS','PLUSEQUAL','MINUS','MINUSMINUS','MINUSEQUAL','TIMES',
    'TIMESTIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','EQUAL',
    'DEQUAL','DISTINT','ISEQUAL','SEMI','COMMA','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG','DOT','QUOTES',
    'APOSTROPHE','DOT_DOT', 'MODULO', 'OR',

    # OTHERS
    'COMMENTS','COMMENTS_C99','ID','IDVAR','NUM','STRING','VOID',
)


# RE Tokens

# Take from: http://www.dabeaz.com/ply/example.html
# Ignored characters
t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


# RE OPEN AND CLOSE TAG
def t_OPENTAG(t):
    r'(<\?(php)?)'
    return t
    
def t_CLOSETAG(t):
    r'\?>'
    return t


# RE RESERVERD WORDS LIST
def t_ABSTRACT(t):
    r'abstract'
    return t

def t_ASSERT(t):
    r'assert'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t


def t_ARRAY(t):
    r'array'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_BREAK(t):
    r'break;'
    return t

def t_BYTE(t):
    r'byte'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ENUM(t):
    r'enum'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_FOR(t):
    r'for'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_INSTANCEOF(t):
    r'instandceof'
    return t

def t_INT(t):
    r'int'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_LONG(t):
    r'long'
    return t

def t_NATIVE(t):
    r'native'
    return t

def t_NEW(t):
    r'new'
    return t

def t_PACKAGE(t):
    r'package'
    return t

def t_SUPER(t):
    r'super'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_SYNCHRONIZED(t):
    r'synchronized'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_THROWS(t):
    r'throws'
    return t

def t_TRANSIENT(t):
    r'transient'
    return t

def t_TRY(t):
    r'try'
    return t



def t_VOLATILE(t):
    r'volatile'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

# RE SYMBOLS
t_MODULO    =r'%'
t_OR        =r'\|\|'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'='
t_DISTINT   = r'!'
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBLOCK    = r'{'
t_RBLOCK    = r'}'
t_COLON     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


# RE OTHERS


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print ("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            i += 1

        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script java como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python java_lexer.py"+chr(27)+"[1;31m"+" <filename>.java"+chr(27)+"[0m")
