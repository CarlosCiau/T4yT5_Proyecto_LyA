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
import ply.yacc as yacc
from java_lexer import tokens
import java_lexer

VERBOSE = 1

def p_program(p):
	'''
	program : p_package p_importar PUBLIC STATIC VOID MAIN LPAREN ID LBRACKET RBRACKET ARGS RPAREN LBLOCK declaration_list RBLOCK
	'''
	pass

def p_package(p):
	'''
	p_package : PACKAGE ID SEMI
	'''
def p_importar(p):
	'''
	p_importar : IMPORT JAVA DOT UTIL DOT SCANNER SEMI
	'''

	pass
def p_declaration_list(p):
	'''
	declaration_list : declaration_list declaraciones
					| declaraciones
					
	'''
	pass

def p_declaraciones(p):
	'''declaraciones : INT ID SEMI
					 | INT ID EQUAL NUM SEMI
					 | ID ID SEMI
					 | SCANNER ID EQUAL NEW SCANNER LPAREN ID DOT ID RPAREN SEMI
					 | BOOLEAN ID EQUAL FALSE SEMI
					 | opera
					 | sentencia
	'''
	pass
def p_opera(p):
	'''opera : ID EQUAL ID PLUS NUM SEMI
			 | ID EQUAL ID MINUS NUM SEMI
			 | ID EQUAL ID DIVIDE NUM SEMI
			 | ID EQUAL ID TIMES NUM SEMI
			 | ID EQUAL NUM PLUS NUM SEMI
			 | ID EQUAL NUM MINUS NUM SEMI
			 | ID EQUAL NUM DIVIDE NUM SEMI
			 | ID EQUAL NUM TIMES NUM SEMI
			 | ID EQUAL ID PLUS ID SEMI
			 | ID EQUAL ID MINUS ID SEMI
			 | ID EQUAL ID DIVIDE ID SEMI
			 | ID EQUAL ID TIMES ID SEMI
			 | ID EQUAL ID MINUS ID PLUS LPAREN ID PLUS NUM RPAREN SEMI
			 | ID EQUAL ID PLUS ID PLUS LPAREN ID TIMES ID RPAREN SEMI
			 | ID EQUAL ID MINUS ID PLUS LPAREN ID MINUS ID RPAREN SEMI
	'''
	pass
def p_sentencia(p):
	'''sentencia : IF LPAREN ID ISEQUAL ID RPAREN LBLOCK response RBLOCK
				 | IF LPAREN ID LESSEQUAL ID RPAREN LBLOCK response RBLOCK
				 | IF LPAREN ID GREATEREQUAL ID RPAREN LBLOCK response RBLOCK
				 | IF LPAREN ID DEQUAL ID RPAREN LBLOCK response RBLOCK
				 | ELSE LBLOCK response RBLOCK
				 | DO LBLOCK response RBLOCK
				 | WHILE LPAREN ID LESS ID RPAREN SEMI
				 | WHILE LPAREN ID GREATER ID RPAREN SEMI
				 | WHILE LPAREN ID ISEQUAL ID RPAREN SEMI
				 | WHILE LPAREN ID LESSEQUAL ID RPAREN SEMI
				 | WHILE LPAREN ID GREATEREQUAL ID RPAREN SEMI
				 | WHILE LPAREN ID DEQUAL ID RPAREN SEMI
	'''
	pass

def p_response(p):
	'''response : ID DOT ID DOT ID LPAREN STRING RPAREN SEMI
	'''
	pass
def p_error(p):
    if VERBOSE:
        if p is not None:
            print (chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print ("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print (chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print ("\t\tLine:  "+str(java_lexer.lexer.lineno))

    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        parser.parse(scriptdata, tracking=False)
        #print("Hola bebe, no tienes errores sintacticos")
        print (chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python java_parser.py"+chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m")
