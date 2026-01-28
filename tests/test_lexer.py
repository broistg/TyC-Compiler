import sys
import os
import pytest

# --- PATH SETUP START ---
project_root = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)
# --- PATH SETUP END ---

from tests.utils import Tokenizer
from lexererr import UncloseString, IllegalEscape, ErrorToken

# --- Helper for valid token strings ---
def check_lexer(source, expected):
    t = Tokenizer(source)
    assert t.get_tokens_as_string() == expected

# --- 1. Keywords (16 cases) ---
@pytest.mark.parametrize("kw", [
    "auto", "break", "case", "continue", "default", "else", 
    "float", "for", "if", "int", "return", "string", 
    "struct", "switch", "void", "while"
])
def test_keywords(kw):
    check_lexer(kw, f"{kw.upper()},{kw},EOF")

# --- 2. Operators & Separators (25 cases) ---
@pytest.mark.parametrize("op,name", [
    ("==", "EQ"), ("!=", "NEQ"), ("<=", "LEQ"), (">=", "GEQ"),
    ("&&", "AND"), ("||", "OR"), ("++", "INCR"), ("--", "DECR"),
    ("+", "ADD"), ("-", "SUB"), ("*", "MUL"), ("/", "DIV"), ("%", "MOD"),
    ("<", "LT"), (">", "GT"), ("!", "NOT"), ("=", "ASSIGN"), (".", "DOT"),
    ("{", "LB"), ("}", "RB"), ("(", "LP"), (")", "RP"), (";", "SEMI"), 
    (",", "COMMA"), (":", "COLON")
])
def test_operators_separators(op, name):
    check_lexer(op, f"{name},{op},EOF")

# --- 3. Identifiers (20 cases - Expanded) ---
@pytest.mark.parametrize("id_name", [
    "x", "_var", "var123", "my_long_name", "A1_B2", "____", "i", "count", "Point", "MyStruct",
    "camelCase", "snake_case", "PascalCase", "UPPER_CASE", "v1", "z0", "flag", "temp", "data", "result"
])
def test_identifiers(id_name):
    check_lexer(id_name, f"ID,{id_name},EOF")

# --- 4. Literals (Int: 10 cases, Float: 14 cases - Expanded) ---
@pytest.mark.parametrize("val", [
    "0", "42", "007", "999999", "1", "100", "255", "123456789", "5", "10"
])
def test_int_literals(val):
    check_lexer(val, f"INTLIT,{val},EOF")

@pytest.mark.parametrize("val", [
    "3.14", "0.5", "1.", ".5", "1.2e3", "5.6E-2", "0.0", "12.e+5",
    "10.0", "0.001", "1e-5", "3.14159", ".2E4", ".123"
])
def test_float_literals(val):
    check_lexer(val, f"FLOATLIT,{val},EOF")

# --- 5. String Literals (12 cases - Expanded) ---
@pytest.mark.parametrize("src,content", [
    ('"hello"', "hello"), ('""', ""), ('"tab\\t"', "tab\\t"), 
    ('"quote\\"inside"', 'quote\\"inside'), ('"back\\\\slash"', 'back\\\\slash'),
    ('" "', " "), ('"123"', "123"), ('"!@#"', "!@#"), 
    ('"mixed \\t and \\n"', "mixed \\t and \\n"), ('"auto"', "auto"), 
    ('"float"', "float"), ('"while"', "while")
])
def test_string_literals(src, content):
    check_lexer(src, f"STRLIT,{content},EOF")

# --- 6. Lexer Errors (Catching custom exceptions - 15 cases) ---

@pytest.mark.parametrize("src,error_text", [
    ('"bad \\a"', "bad \\a"), 
    ('"err \\x"', "err \\x"), 
    ('"\\1"', "\\1"), 
    ('" \\ "', " \\ ")
])
def test_illegal_escape_exception(src, error_text):
    t = Tokenizer(src)
    with pytest.raises(IllegalEscape) as exc:
        t.get_tokens_as_string()
    assert str(exc.value) == "Illegal Escape In String: " + error_text

@pytest.mark.parametrize("src,error_text", [
    ('"unclosed', "unclosed"), 
    ('"missing quote\n', "missing quote"), 
    ('"slash end\\', "slash end\\") 
])
def test_unclose_string_exception(src, error_text):
    t = Tokenizer(src)
    with pytest.raises(UncloseString) as exc:
        t.get_tokens_as_string()
    assert str(exc.value) == "Unclosed String: " + error_text

@pytest.mark.parametrize("src,error_text", [
    ("?", "?"), 
    ("@", "@"), 
    ("#", "#"), 
    ("$", "$")
])
def test_error_char_exception(src, error_text):
    t = Tokenizer(src)
    with pytest.raises(ErrorToken) as exc:
        t.get_tokens_as_string()
    assert str(exc.value) == "Error Token " + error_text

# --- 7. Complex Whitespace/Munch/Mixed (12 cases - Expanded) ---
def test_whitespace_and_comments():
    src = "auto /* comment */ x = // line\n 5;"
    check_lexer(src, "AUTO,auto,ID,x,ASSIGN,=,INTLIT,5,SEMI,;,EOF")

def test_maximal_munch_logic():
    check_lexer("+++", "INCR,++,ADD,+,EOF")
    check_lexer("---", "DECR,--,SUB,-,EOF")
    check_lexer("===", "EQ,==,ASSIGN,=,EOF")

def test_mixed_tokens_1():
    check_lexer("if(x==10){return;}", "IF,if,LP,(,ID,x,EQ,==,INTLIT,10,RP,),LB,{,RETURN,return,SEMI,;,RB,},EOF")

def test_mixed_tokens_2():
    check_lexer("float f = 1.5;", "FLOAT,float,ID,f,ASSIGN,=,FLOATLIT,1.5,SEMI,;,EOF")

def test_mixed_tokens_3():
    check_lexer("struct P { int x; };", "STRUCT,struct,ID,P,LB,{,INT,int,ID,x,SEMI,;,RB,},SEMI,;,EOF")