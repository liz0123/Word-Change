import string
from collections import deque
class WordPath():
    def __init__(self, dictionary):
        self.dic = []
        self.w1 = ""
        self.w2 = ""
        self.setDict(dictionary)
        self.ALPHABET ='abcdefghijklmnopqrstuvwxyz'

    def setDict(self,words):
        dic =[]
        wordList = words+","
        word =""
        for char in wordList:
            if char == " " or char ==",":
                if word != "":
                    dic.append(word)
                    word = ""
            else:
                word = word+char
        self.dic = dic

    def getDic(self):
        return self.dic

    def clearDic(self):
        self.dic = []

    def BFS(self):

        graph = {}
        visited =[]
        de = deque([self.w1])
        nodeList =[self.w1]

        while de:
            current = de.pop()
            if current == self.w2:
                break
            if current not in visited:
                visited.append(current)
                child = self.childern(current,nodeList)
                if child:
                    for ch in child:
                        if ch not in visited:
                            de.appendleft(ch)
                            nodeList.append(ch)
                    graph.update({current:child})         
        return graph
        
    def childern(self,word,nodes):
        branch =[]
        for i in range(len(word)):
            child = word
            for char in self.ALPHABET:
                child = child[:i]+char+child[i+1:]
                if child !=word and child not in nodes:
                    if child in self.dic or child== self.w2:
                        branch.append(child)
        return branch
    
    def findPath(self,graph,start,end, path):
        path = path+[start]
        if start == end:
            return path
        if not graph.get(start):
            return  None
        for node in graph[start]:
            if node not in path:
                newpath = self.findPath(graph, node, end, path)
                if newpath: return newpath
        return None

    def getStringPath(self,word1, word2):
        self.w1 = word1
        self.w2 = word2
        stringPath =""
        graph = self.BFS()
        path = self.findPath(graph,self.w1,self.w2,[])

        if path:
            length = len(path) 
            for i in range(length-1):
                stringPath =stringPath + path[i]+" -> "
            stringPath = stringPath+path[length-1]+""
            return stringPath
        return "NONE"
        
        

#DICT ="boy,buy,pox,pip,pin,tom,mug,toy,pot,pop"


        
                
                
        
        
