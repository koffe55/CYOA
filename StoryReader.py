from dialog import *
import time
import re
class StoryReader:

    def __init__(self,parent):
        self.q=1
        self.loadstory()

    def loadstory(self):
        try:
            with open ("story.txt", "r") as myfile:
                self.story=myfile.read().replace('\xe2\x80\x99', '\'')
                #self.story=self.story.replace('\xe2\x80\x9c', '\"').replace('\xe2\x80\x9d', '\"')
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
            print "Question " + str(question) + " doesn't seem to exist"
            return False

    def FindBlock(self,num, splitup):
        splitup = re.split(r"\[", self.story)       #split up by [ characters
        reg3 = r"" + str(num) + "\].*"       #build regex to find 'num]' block
        for questions in splitup:               #get question block
            block = re.match(reg3, questions, re.DOTALL)
            if block:
                return block.group()
            
    
    def GetOptions(self, block):        #takes question block, returns choice text, number
        optlist =[]
        optblock = re.findall(r"\(.*", block)      #find all options
        if optblock:
            #print optblock
            for options in optblock:
                g = re.search(r"\(.*\)", options)
                if g:
                    try:
                        h = str(g.group())     #strip parens off and make into string
                        h= h[1:-1]
                        print 'This is string about to be h', h
                        num = int(h)                    #make it an int.
                    except:
                        print 'Error converting textual question number to an int.'
                        return None
                    firstletter=r"[a-zA-Z].*"           #remove number at beginning
                    text = re.search(firstletter, options)
                    text = str(text.group())
                    
                    #optlist += [text, num]
                    temp = [text, num]
                    optlist += temp
                else:
                    print 'error: Couldnt seem to find options associated with that question.'
        else:
            print 'Couldnt find options.'
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
            return ['There has been an error']
        
        block = self.FindBlock(question, self.splitup) #get textblock    
        optlist = self.GetOptions(block)        #pass it here to serpeate out options
        print optlist
        return optlist
   




##    def choices(self, question):
##        val = self.parse(question)
##        return val
##
##
##
##        #packs a list of the text and numbers
##
##        #find the question
##        reg = r"\[" + str(question) +"\]" #capture [5] or [99]
##        print reg
##        for words in self.story:
##            #if re.match("(.*)\((.*)\)", line):          #change line to paragraph
##            if re.match(reg, line):
##                print ("Parsing"+line)
##                val = line
##                #while  re.match("(.*)\((.*)\)") is False:
##                while  re.match(r"\[") is False:
##                    pass
####                if re.search( "("+qnumber+")", self.story):
####                    #print everything until next number
####                    pass
##
##                pass
##        #split the questions up
##        #splitup = re.split(r'(.*)\((.*)\)', self.story); #make a list with number then text?
##
##        #example
##        self.parse(question)
##        val = [
##        ("Jump off a bridge.", 1),
##        ("Go home.", 2)
##        ]
##        return val


    #def storyloop(self):                #dont use this.
    #    while True:
    #        self.ask()
    #        question = self.get()
    #        time.sleep(2)
    #        print("Restarting storyloop")



    