"""
Utility functions and classes for testing TyC compiler
"""

import os
import sys

# Add project root and build directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
build_dir = os.path.join(project_root, 'build')
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

from build.TyCLexer import TyCLexer
from build.TyCParser import TyCParser
from antlr4 import InputStream, CommonTokenStream
from src.utils.error_listener import NewErrorListener


class Tokenizer:
    """Lexer wrapper for testing"""

    def __init__(self, source_code: str):
        self.source_code = source_code

    def get_tokens_as_string(self) -> str:
        """Get tokens as comma-separated string"""
        input_stream = InputStream(self.source_code)
        lexer = TyCLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        tokens = []
        for token in token_stream.tokens:
            if token.type != -1:  # EOF
                token_name = lexer.symbolicNames[token.type]
                token_text = token.text if token.text else ""
                tokens.append(f"{token_name},{token_text}")

        tokens.append("EOF")
        return ",".join(tokens)


class Parser:
    """Parser wrapper for testing"""

    def __init__(self, source_code: str):
        self.source_code = source_code

    def parse(self) -> str:
        """Parse source code and return result"""
        input_stream = InputStream(self.source_code)
        lexer = TyCLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TyCParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(NewErrorListener.INSTANCE)

        try:
            tree = parser.program()
            return "success"
        except Exception as e:
            return str(e)
