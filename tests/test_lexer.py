import pytest
from tests.utils import Tokenizer

# --- Helper for valid token strings ---
def check_lexer(source, expected_text_only):
    t = Tokenizer(source)
    # Adding <EOF> at the end
    expected = f"{expected_text_only},<EOF>"
    assert t.get_tokens_as_string() == expected

# --- 1. Keywords ---
@pytest.mark.parametrize("kw", [
    "auto", "break", "case", "continue", "default", "else", 
    "float", "for", "if", "int", "return", "string", 
    "struct", "switch", "void", "while"
])
def test_keywords(kw):
    check_lexer(kw, kw)

# --- 2. Operators & Separators ---
@pytest.mark.parametrize("op", [
    "==", "!=", "<=", ">=", "&&", "||", "++", "--",
    "+", "-", "*", "/", "%", "<", ">", "!", "=", ".",
    "{", "}", "(", ")", ";", ",", ":"
])
def test_operators_separators(op):
    check_lexer(op, op)

# --- 3. Identifiers ---
@pytest.mark.parametrize("id_name", [
    "x", "_var", "var123", "my_long_name", "A1_B2", "____", "i", "count", "Point", "MyStruct",
    "camelCase", "snake_case", "PascalCase", "UPPER_CASE", "v1", "z0", "flag", "temp", "data", "result"
])
def test_identifiers(id_name):
    check_lexer(id_name, id_name)

# --- 4. Literals ---
@pytest.mark.parametrize("val", [
    "0", "42", "007", "999999", "1", "100", "255", "123456789", "5", "10"
])
def test_int_literals(val):
    check_lexer(val, val)

@pytest.mark.parametrize("val", [
    "3.14", "0.5", "1.", ".5", "1.2e3", "5.6E-2", "0.0", "12.e+5",
    "10.0", "0.001", "1e-5", "3.14159", ".2E4", ".123"
])
def test_float_literals(val):
    check_lexer(val, val)

# --- 5. String Literals ---
@pytest.mark.parametrize("src,content", [
    ('"hello"', "hello"), 
    ('""', ""), 
    ('"tab\\t"', "tab\\t"), 
    ('"quote\\"inside"', 'quote\\"inside'), 
    ('"back\\\\slash"', 'back\\\\slash'),
    ('" "', " "), 
    ('"123"', "123"), 
    ('"!@#"', "!@#"), 
    ('"mixed \\t and \\n"', "mixed \\t and \\n"), 
    ('"auto"', "auto"), 
    ('"float"', "float"), 
    ('"while"', "while")
])
def test_string_literals(src, content):
    check_lexer(src, content)

# --- 6. Lexer Errors ---

@pytest.mark.parametrize("src,error_text", [
    ('"bad \\a"', "bad \\a"), 
    ('"err \\x"', "err \\x"), 
    ('"\\1"', "\\1"), 
    ('" \\ "', " \\ ")
])
def test_illegal_escape_exception(src, error_text):
    t = Tokenizer(src)
    assert t.get_tokens_as_string() == "Illegal Escape In String: " + error_text

@pytest.mark.parametrize("src,error_text", [
    ('"unclosed', "unclosed"), 
    ('"missing quote\n', "missing quote"), 
    ('"slash end\\', "slash end\\") 
])
def test_unclose_string_exception(src, error_text):
    t = Tokenizer(src)
    assert t.get_tokens_as_string() == "Unclosed String: " + error_text

@pytest.mark.parametrize("src,error_text", [
    ("?", "?"), 
    ("@", "@"), 
    ("#", "#"), 
    ("$", "$")
])
def test_error_char_exception(src, error_text):
    t = Tokenizer(src)
    assert t.get_tokens_as_string() == "Error Token " + error_text

# --- 7. Complex Whitespace/Munch/Mixed ---

def test_whitespace_and_comments():
    src = "auto /* comment */ x = // line\n 5;"
    check_lexer(src, "auto,x,=,5,;")

def test_comments_in_strings():
    """Ensure comment syntax inside strings is treated as literal text"""
    check_lexer('"/* not a comment */"', "/* not a comment */")
    check_lexer('"// also not a comment"', "// also not a comment")

def test_comments_delimiting_tokens():
    """Ensure comments act as delimiters"""
    # 'int' and 'x' should be separate tokens, not 'intx'
    check_lexer("int/**/x", "int,x") 
    check_lexer("int//comment\nx", "int,x")

def test_maximal_munch_logic():
    check_lexer("+++", "++,+")
    check_lexer("---", "--,-")
    check_lexer("===", "==,=")
    check_lexer("+++", "++,+")
    check_lexer("< =", "<,=")
    check_lexer("<=", "<=")
    check_lexer(">>>", ">,>,>")

def test_mixed_tokens_1():
    check_lexer("if(x==10){return;}", "if,(,x,==,10,),{,return,;,}")

def test_mixed_tokens_2():
    check_lexer("float f = 1.5;", "float,f,=,1.5,;")

def test_mixed_tokens_3():
    check_lexer("struct P { int x; };", "struct,P,{,int,x,;,},;")
