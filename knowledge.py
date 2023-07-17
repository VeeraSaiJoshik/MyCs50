from typing import Any


class Symbol:
    def __init__(self, name, truthValue = True):
        self.name = name
        self.value = truthValue
    def setValue(self, val):
        self.value = val
    def evaluate(self, model):
        instance = self.findInList(model)
        return model[instance].value
    def findInList(self, model):
        for instance in range(len(model)) : 
            
            if model[instance].name == self.name : 
                return instance
        

#looking at all the operators
class And:
    def __init__(self, val1 = 0, val2 = 0):
        self.val1  = val1
        self.val2 = val2
        self.symbol = "∧"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        if type(self.val2) == Symbol : 
            val2 = model[self.val2.findInList(model)].value
        else : 
            val2 = self.val2.evaluate(model)
        return val2 and val1
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        if type(self.val2) == Symbol:
            tempSymbol.append(self.val2.name)
        else : 
            tempSymbol.extend(self.val2.getSymbolsNeeded())
        return tempSymbol   
        
class Or:
    def __init__(self, val1 = 0, val2 = 0):
        self.val1  = val1
        self.val2 = val2
        self.symbol = "∨"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        if type(self.val2) == Symbol : 
            val2 = model[self.val2.findInList(model)].value
        else : 
            val2 = self.val2.evaluate(model)
        
        return val1 or val2
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        if type(self.val2) == Symbol:
            tempSymbol.append(self.val2.name)
        else : 
            tempSymbol.extend(self.val2.getSymbolsNeeded())
        
        return tempSymbol
class Xor:
    def __init__(self, val1 = 0, val2 = 0):
        self.val1  = val1
        self.val2 = val2
        self.symbol = "⊻"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        if type(self.val2) == Symbol : 
            val2 = model[self.val2.findInList(model)].value
        else : 
            val2 = self.val2.evaluate(model)
        
        return (val1 or val2) and (val1 == val2) == False
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        if type(self.val2) == Symbol:
            tempSymbol.append(self.val2.name)
        else : 
            tempSymbol.extend(self.val2.getSymbolsNeeded())
        
        return tempSymbol
class Not:
    def __init__(self, val1 = 0):
        self.val1  = val1
        self.symbol = "¬"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        return val1 == False
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        
        return tempSymbol
class Implication:
    def __init__(self, val1 = 0, val2 = 0):
        self.val1  = val1
        self.val2 = val2
        self.symbol = "→"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        if type(self.val2) == Symbol : 
            val2 = model[self.val2.findInList(model)].value
        else : 
            val2 = self.val2.evaluate(model)
        if val1 == False : 
            return True
        return val1 == val2
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        if type(self.val2) == Symbol:
            tempSymbol.append(self.val2.name)
        else : 
            tempSymbol.extend(self.val2.getSymbolsNeeded())
        
        return tempSymbol
class BiConditional:
    def __init__(self, val1 = 0, val2 = 0):
        self.val1  = val1
        self.val2 = val2
        self.symbol = "↔"
    def evaluate(self, model):
        if type(self.val1) == Symbol : 
            val1 = model[self.val1.findInList(model)].value
        else : 
            val1 = self.val1.evaluate(model)
        
        if type(self.val2) == Symbol : 
            val2 = model[self.val2.findInList(model)].value
        else : 
            val2 = self.val2.evaluate(model)
        return val1 == val2
    def getSymbolsNeeded(self):
        tempSymbol = []
        if type(self.val1) == Symbol:
            tempSymbol.append(self.val1.name)
        else : 
            tempSymbol.extend(self.val1.getSymbolsNeeded())
        if type(self.val2) == Symbol:
            tempSymbol.append(self.val2.name)
        else : 
            tempSymbol.extend(self.val2.getSymbolsNeeded())
        
        return tempSymbol
#creating the statement class

class ModelSpace:
    def __init__(self, symbols):
        self.symbols = symbols
    def generateAllPossibleModes(self, i = 0):
        tempSelfTrue = Symbol(self.symbols[i].name, True)
        tempSelfFalse = Symbol(self.symbols[i].name, False)
        if i == len(self.symbols) - 1 : 
            return [[tempSelfTrue], [tempSelfFalse]]
        possibleLists = self.generateAllPossibleModes(i + 1)
        finalList = []
        for i in possibleLists : 
            tempList = [Symbol(x.name, x.value) for x in i]
            tempList.append(tempSelfTrue)
            finalList.append(tempList)
            tempList = [Symbol(x.name, x.value) for x in i]
            tempList.append(tempSelfFalse)
            finalList.append(tempList)
        self.finalList = finalList
        return finalList
    def printAllPossibleMoves(self):
        print([s.name for s in self.finalList[0]])
        for case in self.finalList : 
            print([s.value for s in case])
    def modelCheckingInfer(self, sentence, knowledge):
        allWorlds =  self.generateAllPossibleModes()
        for world in allWorlds : 
            print("===")
            print(knowledge.modelIsTrue(world))
            if knowledge.modelIsTrue(world) and sentence.evaluate(world) == False:
                for symbol in world : 
                    print(symbol.name + " " + str(symbol.value))
                return False
        return True
class KnowledgeBase:
    def __init__(self, knowledge):
        self.knowledge = []
        self.knowledge.extend(knowledge)
    def modelIsTrue(self, testingModel):
        for condition in self.knowledge : 
            print([(x.name, x.value) for x in testingModel])
            print(getStringRepresentation(condition))
            print("so what it is " + str(condition.evaluate(testingModel)))
            if condition.evaluate(testingModel) == False :
                return False
        return True    
def getStringRepresentation(symbol):
        val1String = ""
        val2String = ""
        if type(symbol) == Symbol:
            return symbol.name
        if type(symbol.val1) == Symbol : 
            val1String = symbol.val1.name
        else : 
            val1String = getStringRepresentation(symbol.val1)
        if type(symbol) != Not and type(symbol.val2) == Symbol : 
            val2String = symbol.val2.name
        elif type(symbol) != Not: 
            val2String = getStringRepresentation(symbol.val2)
        if val2String == "" : return symbol.symbol + val1String
        return "(" + val1String + " " + symbol.symbol + " " + val2String + ")"
def biconditionalElimation(symbol):
    return And(Implication(symbol.val2, symbol.val1), Implication(symbol.val1, symbol.val2))
def implicationElimination(symbol):
    return Or(Not(symbol.val1), symbol.val2)

def notElimination(symbol, depth = 0):
    if type(symbol.val1) == Not : 
        return symbol.val1.val1
    elif type(symbol.val1) != Symbol : 
        
        if type(symbol.val1) == And : 
            return Or( Not(symbol.val1.val1),  Not(symbol.val1.val2))
        else : 
            return And( Not(symbol.val1.val1),  Not(symbol.val1.val2))
    
def recursionAlgorithm(detection, elimination, node, depth = 0): 
    if type(node) == Symbol or (type(node) == Not and type(node.val1) == Symbol): 
        return True
    if node.symbol == detection : 
        node = elimination(node)
        if depth != 0  : 
            return node
    if type(node) == Not: 
        while recursionAlgorithm(detection, elimination, node.val1, depth + 1) != True : 
            node.val1 = recursionAlgorithm(detection, elimination, node.val1, depth + 1) 
            
    else : 
        while recursionAlgorithm(detection, elimination, node.val1, depth + 1) != True :
            node.val1 = recursionAlgorithm(detection, elimination, node.val1, depth + 1)
        while recursionAlgorithm(detection, elimination, node.val2, depth + 1) != True :
            node.val2 = recursionAlgorithm(detection, elimination, node.val2, depth + 1)
    if depth == 0 : return node
    return True

def turnIntoCNF(symbol):
    for algorithm in [[biconditionalElimation, "↔"], [implicationElimination, "→"], [notElimination, "¬"]] : 
        detectionSymbol = algorithm[1]
        eliminationFunction = algorithm[0]
        val = recursionAlgorithm(detectionSymbol, eliminationFunction, symbol)
        if val != True : 
            symbol = val
        
        print(getStringRepresentation(symbol))
        print("==" * 100)
    return symbol
hagrid = Symbol("Hagrid")
rain = Symbol("Rain")
dumbeldore = Symbol("Dumledore")
world = ModelSpace([hagrid, rain, dumbeldore])

symbol = BiConditional(Implication(hagrid, rain), BiConditional(rain, dumbeldore))
print(getStringRepresentation(symbol))
symbol2 = turnIntoCNF(BiConditional(Implication(hagrid, rain), BiConditional(BiConditional(hagrid, rain), BiConditional(BiConditional(hagrid, rain), dumbeldore))))
kb = KnowledgeBase([BiConditional(Implication(hagrid, rain), BiConditional(BiConditional(hagrid, rain), BiConditional(BiConditional(hagrid, rain), dumbeldore)))])
print("cnf implementation : ")
print(getStringRepresentation(symbol2))
print(world.modelCheckingInfer(symbol2, kb))