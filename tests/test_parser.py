import sys
import os
import pytest

# --- PATH SETUP ---
project_root = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

from tests.utils import Parser

# ==============================================================================
# 1. SPECIFICATION EXAMPLES (6 Tests)
# ==============================================================================

def test_spec_hello_world():
    src = 'void main() { printString("Hello, World!"); }'
    assert Parser(src).parse() == "success"

def test_spec_calculator():
    src = """
    int add(int x, int y) { return x + y; }
    int multiply(int x, int y) { return x * y; }
    void main() {
        auto a = readInt(); auto b = readInt();
        printInt(add(a, b)); printInt(multiply(a, b));
    }
    """
    assert Parser(src).parse() == "success"

def test_spec_loop_conditions():
    src = """
    void main() {
        auto n = readInt(); auto i = 0;
        while (i < n) { printInt(i); ++i; }
        for (auto j = 0; j < n; ++j) { if (j % 2 == 0) printInt(j); }
    }
    """
    assert Parser(src).parse() == "success"

def test_spec_factorial():
    src = """
    int factorial(int n) {
        if (n <= 1) return 1; else return n * factorial(n - 1);
    }
    void main() { printInt(factorial(readInt())); }
    """
    assert Parser(src).parse() == "success"

def test_spec_struct_usage():
    src = """
    struct Point { int x; int y; };
    struct Person { string name; int age; };
    void main() {
        Point p1; p1.x = 10;
        Point p2 = {30, 40};
        Person person1 = {"John", 25};
        auto p3 = p2;
    }
    """
    assert Parser(src).parse() == "success"

def test_spec_variable_decl():
    src = """
    void main() {
        auto x = 10; auto y = 3.14; auto msg = "hello";
        int a; float b; string c;
        a = 10;
    }
    """
    assert Parser(src).parse() == "success"

# ==============================================================================
# 2. STRUCT DECLARATIONS (12 Tests)
# ==============================================================================
@pytest.mark.parametrize("src", [
    "struct Empty {};",
    "struct Point { int x; int y; };",
    "struct Vector { float x; float y; float z; };",
    "struct User { string name; };",
    "struct NestedType { Point p; };",
    "struct Mixed { int a; float b; string c; Point d; };",
    "struct A { int x; }; struct B { A a; };",
])
def test_struct_valid(src):
    assert Parser(src).parse() == "success"

@pytest.mark.parametrize("src", [
    "struct {};",              # Missing name
    "struct S { int x }",      # Missing semi inside
    "struct S { int x; ",      # Unclosed
    "struct S { auto x; };",   # Auto not allowed in struct
    "struct S { struct N { int x; }; };" # Nested decl not allowed
])
def test_struct_invalid(src):
    assert Parser(src).parse() != "success"

# ==============================================================================
# 3. FUNCTION DECLARATIONS (12 Tests)
# ==============================================================================
@pytest.mark.parametrize("src", [
    "void f() {}",
    "int f() { return 1; }",
    "float f(int a) { return 0.0; }",
    "string f(string s, int i) { return s; }",
    "Point f(Point p) { return p; }",
    "f() { return; }",              # Inferred return
    "f(int a, float b, string c) {}"
])
def test_func_valid(src):
    assert Parser(src).parse() == "success"

@pytest.mark.parametrize("src", [
    "void f(auto x) {}",            # Auto param not allowed
    "void f(int a,) {}",            # Trailing comma
    "void f(int a int b) {}",       # Missing comma
    "int f;",                       # Missing body/params
    "void f() return 1;"            # Missing block
])
def test_func_invalid(src):
    assert Parser(src).parse() != "success"

# ==============================================================================
# 4. VARIABLE DECLARATIONS (18 Tests)
# ==============================================================================
@pytest.mark.parametrize("stmt", [
    "int x;",
    "int x = 5;",
    "float y = 3.14;",
    "string s = \"str\";",
    "Point p;",
    "Point p = {1, 2};",
    "auto a = 10;",
    "auto b;",
    "auto c = a + b;",
    "List list;",       # Valid: 'List' is a struct type name (ID)
    "MyType v = call();"
])
def test_var_decl_valid(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

@pytest.mark.parametrize("stmt", [
    "int x",            # Missing semi
    "auto x = ;",       # Missing expr
    "int x = var int;", # Invalid expr syntax
    "void x;",          # VOID is NOT in varType
    "auto;",            # Missing ID
    "int = 5;",         # Missing ID
])
def test_var_decl_invalid(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() != "success"

# ==============================================================================
# 5. CONTROL FLOW (30 Tests)
# ==============================================================================

# IF Statements
@pytest.mark.parametrize("stmt", [
    "if (x) return;",
    "if (x) { return; }",
    "if (x) a=1; else a=2;",
    "if (x) { a=1; } else { a=2; }",
    "if (x) if (y) a=1; else a=2;", # Dangling else
    "if (1) {} else if (2) {} else {}",
])
def test_if_stmts(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

# WHILE Statements
@pytest.mark.parametrize("stmt", [
    "while(1) break;",
    "while(i < 10) { i++; }",
    "while(x) continue;",
    "while(a && b) if(x) break;"
])
def test_while_stmts(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

# FOR Statements
@pytest.mark.parametrize("stmt", [
    "for(int i=0; i<10; i++) {}",           # VarDecl Init
    "for(auto i=0; i<10; i++) {}",          # Auto Init
    "for(i=0; i<10; i++) {}",               # Expr Init
    "for(; i<10; i++) {}",                  # Empty Init
    "for(int i=0; ; i++) {}",               # Empty Cond
    "for(int i=0; i<10; ) {}",              # Empty Update
    "for(;;) {}",                           # All Empty
    "for(int i=0; i<10; i=i+1) {}",         # Assignment Update
])
def test_for_stmts(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

# SWITCH Statements
@pytest.mark.parametrize("stmt", [
    "switch(x) { case 1: break; }",
    "switch(x) { default: break; }",
    "switch(x) { case 1: case 2: break; }",
    "switch(x) { case 1: a=1; break; case 2: a=2; }",
    "switch(x) { default: break; case 1: break; }",
    "switch(x) {}", 
    "switch(x+1) { case (1+1): break; }"
])
def test_switch_stmts(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

# Break/Continue/Return
@pytest.mark.parametrize("stmt", [
    "break;", "continue;", "return;", "return 1 + 2;", "return x;"
])
def test_jump_stmts(stmt):
    src = f"void main() {{ {stmt} }}"
    assert Parser(src).parse() == "success"

# ==============================================================================
# 6. EXPRESSIONS & PRECEDENCE (30 Tests)
# ==============================================================================
@pytest.mark.parametrize("expr", [
    "a", "1", "1.0", "\"s\"", "a.b", "a.b.c",
    "a++", "a--", "-a", "+a", "!a", "++a", "--a",
    "a * b", "a / b", "a % b",
    "a + b", "a - b",
    "a < b", "a <= b", "a > b", "a >= b",
    "a == b", "a != b",
    "a && b", "a || b",
    "a = b"
])
def test_simple_expressions(expr):
    src = f"void main() {{ auto x = {expr}; }}"
    assert Parser(src).parse() == "success"

@pytest.mark.parametrize("expr", [
    "a.b++",                # . > post
    "-a++",                 # post > pre
    "!a.b",                 # . > pre
    "a * b + c",            # * > +
    "a + b * c",            # * > +
    "a + b < c",            # + > rel
    "a < b == c",           # rel > eq
    "a == b && c",          # eq > and
    "a && b || c",          # and > or
    "a = b || c",           # or > assign
    "a = b = c",            # Right assoc
    "(a + b) * c",          # Parens
    "f(1, 2) + 3",          # Func call
    "{1, 2}.x"              # Struct lit
])
def test_complex_precedence(expr):
    src = f"void main() {{ auto x = {expr}; }}"
    assert Parser(src).parse() == "success"

# ==============================================================================
# 7. STRUCT LITERALS (5 Tests)
# ==============================================================================
@pytest.mark.parametrize("expr", [
    "{1, 2}",
    "{{1, 2}, 3}",
    "{a, b+c}",
    "{f()}",
    "{}"
])
def test_struct_literals(expr):
    src = f"void main() {{ auto x = {expr}; }}"
    assert Parser(src).parse() == "success"

# ==============================================================================
# 8. INTEGRATION / COMPLEX (5 Tests)
# ==============================================================================
def test_complex_nesting():
    src = """
    void main() {
        if (x) {
            while (y) {
                switch(z) {
                    case 1: for(;;) break;
                }
            }
        }
    }
    """
    assert Parser(src).parse() == "success"

def test_complex_calc():
    src = """
    int calc(int a, int b) {
        return (a * a) + (b * b) - 2 * a * b;
    }
    """
    assert Parser(src).parse() == "success"