from typing import List

class Delimiters:
    def __init__(self, open: str, close: str):
        self.openDel = open
        self.closeDel = close

    def getDelimitersList(self, tokens: List[str]) -> List[str]:
        delimiters = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == self.openDel or token == self.closeDel:
                delimiters.append(token)
        return delimiters

    def isBalanced(self, delimiters: List[str]) -> bool:
        balanced = 0
        for i in range(len(delimiters)):
            token = delimiters[i]
            if token == self.openDel:
                balanced += 1
            elif token == self.closeDel:
                balanced -= 1

        return balanced == 0
            

def test_1():
    delimiters = Delimiters("(", ")")
    delimitersList = delimiters.getDelimitersList(["(", "x + y", ")", "* 5"])
    assert delimiters.isBalanced(delimitersList) == True, "balanced"

def test_2():
    delimiters = Delimiters("<q>", "</q>")
    delimitersList = delimiters.getDelimitersList(["<q>", "yy", "</q>", "zz", "</q>"])
    assert delimiters.isBalanced(delimitersList) == False, "not balanced"

test_1()
test_2()