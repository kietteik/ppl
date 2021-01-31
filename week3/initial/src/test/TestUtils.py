import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/mC/parser/' in sys.path:
    sys.path.append('./main/mC/parser/')
if os.path.isdir('../target/main/mC/parser') and not '../target/main/mC/parser/' in sys.path:
    sys.path.append('../target/main/mC/parser/')
from mCLexer import mCLexer
from mCParser import mCParser
from lexererr import *


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename, "w")
        """tmp = repr(inputStr)
        file.write(tmp[1:-1])"""
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        dest = open("./test/solutions/" + str(num) + ".txt", "w")
        lexer = mCLexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except LexerError as err:
            dest.write(err.message)
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        dest = open("./test/solutions/" + str(num) + ".txt", "w")
        lexer = mCLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = mCParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect
