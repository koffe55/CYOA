#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from dialog import *
import time
import re
class StoryReader:

    debug = False
    
    def __init__(self,parent):
        self.q=1
        self.loadstory()

    def loadstory(self):
        try:
            with open ("story.txt", "r") as myfile:
                self.story=myfile.read().replace('\xe2\x80\x99', '\'').replace('\r', '\n')#.replace('\t', '').replace('\x92', "\'").replace('x96', "-")
                self.story = self.story.replace('\t', '').replace('\x92', "\'").replace('x96', "-").replace('\x94', '"')
            if self.debug: print repr(self.story)
        except:
            print("Couldn't find the story.txt file." +
                  "Make sure that this text file is in the same"
                  + "directory where you launched the application.")
            return
        reg2 = r"If selected "
        self.splitup = re.split(reg2, self.story)

    def CheckQuestion(self, question):
        regex = r"\[" + str(question) + "\]"
        x = re.search(regex, self.story)
        if x:
            return True
        else:
            print "ERROR: Question " + str(question) + " doesn't seem to exist"
            return False

    def FindBlock(self,num, splitup):
        splitup = re.split(r"\[", self.story)       #split up by [ characters
        reg3 = r"" + str(num) + "\].*"       #build regex to find 'num]' block
        for questions in splitup:               #get question block
            block = re.match(reg3, questions, re.DOTALL)
            if block:
                return block.group()
        print 'ERROR: Cant find question block.'
    
    def GetOptions(self, block):        #takes question block, returns choice text, number
        optlist =[]
        optblock = re.findall(r"\(.*", block)      #find all options
        if optblock:
            if self.debug: print optblock
            for options in optblock:
                g = re.search(r"\(.*\)", options)
                if g:
                    try:
                        h = str(g.group())     #strip parens off and make into string
                        h= h[1:-1]
                        if self.debug: print 'This is string about to be h', h
                        num = int(h)                    #make it an int.
                    except:
                        print 'Error converting textual question number to an int.'
                        return None
                    firstletter=r"[a-zA-Z].*"           #remove number at beginning
                    text = re.search(firstletter, options)
                    
                    try:
                        if self.debug: print text.group()
                    except:
                        print 'ERROR: Tried to remove number text from choice, failed.'
                        
                    text = str(text.group())
                    temp = [text, num]
                    optlist += temp
                else:
                    print 'ERROR: Found that question, but no choices.'
        else:
            print 'ERROR Couldnt find options.'
        return optlist

    def GetText(self, question):       #Find text prompt
        x = self.CheckQuestion(question)
        if not x:
            return 'Question ' + str(question) + ' doesn\'t seem to exist.'
        block = self.FindBlock(question, self.splitup)
        
        if not block:
            print 'ERROR: Can\'t find that question!'
            return "Oppsies. We're experiencing some technical difficulties."
        
        prompt = re.search(r"[a-zA-Z].*?\(", block, re.DOTALL)
        prompt = str(prompt.group())       #make into string
        prompt = prompt[0:-1]               #remove last character (left parens)
        prompt = prompt.replace('\n', ' ') #remove newlines so its prettier
        return prompt

    def choices(self, question):
        x = self.CheckQuestion(question)
        if not x:
            return ['Error, that quesiton doesnt exit.']
        
        block = self.FindBlock(question, self.splitup) #get textblock    
        optlist = self.GetOptions(block)        #pass it here to serpeate out options
        if self.debug: print optlist
        return optlist
   



    #def storyloop(self):                #dont use this.
    #    while True:
    #        self.ask()
    #        question = self.get()
    #        time.sleep(2)
    #        print("Restarting storyloop")



    
