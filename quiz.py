points=0
switcher=0
ask=str(input("Do you want to attend quiz 1.0 or quiz 2.0??Write i for 1.0 and d for 2.0\t"))
if ask=="i":
    e=str(input("Write s for start and e for leave\t"))
    if e=="s":
         print("What's Your age?")
         print("(a)30")
         print("(b)31")
         print("(c)below 30")
         print("(d)None of these")
         a=str(input("write your answer\t"))
         if a=="b" or a=="c" or a=="a" or a=="d":
             print("I asked it for  fun it was of no use!!")
             switcher=1
    elif e=="e":
          print("THEN PLEASE LEAVE!!")
    if switcher==1:
        print("")
        print("What is electorplating?Say to me and I will decide wheteher to give you points or not")
        a=str(input("Write your answer\t"))
        if a=="points":
            points=points+2
            print("Your answer is right")
            print("Yaa you finished the quiz 1.0")
            print("your score",points)
            switcher=2
        elif a=="noPoints":
              print("You lost it sad")
              print("As the name suggets the plating done by using electricity is called electroplating!")
              print("your score",points)
              switcher=2
if ask=="d" or switcher==2:
    no=str(input("Do you want to enter quiz 2.0??Write y for yes or leave for no\t"))
    if no=="y":
        print("")
        print("Dilute Copper Sulphate solution contains what?")
        print("(a)Copper")
        print("(b)Sulphur")
        print("(c)Water and copper and sulphur")
        print("(d)Water Copper and Sulphate")
        a=str(input("write your answer\t"))
        if a=="d":
            points=points+2
            print("Yaa you got it right!!Your score:",points)
            switcher=3
        elif a=="a" or a=="b" or a=="c":
            print("Youu got it wroong It was option c")
            switcher=3
    if switcher==3:
        print("")
        print("A G.K. question:")
        print("Quit India Movement was started by whom??")
        print("(a)Mahatma Gandhi")
        print("(b)Jwaharlal Nahru")
        print("(c)Netaji Subhas Chandra Bose")
        print("(d)The people of Inida")
        a=str(input("Write your answer\t"))
        if a=="a":
            points=points+2
            print("You got it right!!")
            print("Your score:",points)
        else:
            print("You got it wrong")
            print("Your score:",points)
    if no=="n":
        codecs.open("quiz.html","r","utf-8")
