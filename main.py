import time
import random
import datetime

print("Welcome to your chat bot")
print("Computer: Let's Chat")
while True:
    input_ = input("You :").lower()
    time.sleep(1)
    a = "Computer"

    if "whats my name" in input_:
        print(f"{a}: Sorry,this information is not in my data")
        b = input("Input your name :")
        print(f"{a}: Hello,{b}")
    elif "my name" in input_:
        print(f"{a}: Sorry,this information is not in my data")
        b = input("Input your name :")
        print(f"{a}: Hello,{b}")
    elif "what my name" in input_:
        print(f"{a}: Sorry,this information is not in my data")
        b = input("Input your name :")
        print(f"{a}: Hello,{b}")
    elif "who are you" in input_:
        print(f"{a}: Your Chat partner")

    elif "how are you" in input_:
        print(f"{a}: You are fine,so i'm also fine")
    elif "hi" in input_:
        print(f"{a}: Hello,How can i help you sir?")
    elif "hello" in input_:
        print(f"{a}: Hi,How can i help you sir?")
    elif "hlw" in input_:
        print(f"{a}: Hello,How can i help you sir?")
    elif "show date and time" in input_:
        print(f"{a}: Today's date and time-", datetime.datetime.now())
    elif "time" in input_:
        print(f"{a}: Today's date and time-", datetime.datetime.now())
    elif "can i chat with you" in input_:
        print(f"{a}: Of course,How can i help you sir?")
    elif "whats your name" in input_:
        print(f"{a}: I'm your chat bot,you can call me Comolokko")
    elif "your name" in input_:
        print(f"{a}: I'm your chat bot,you can  call me Comolokko")
    elif "who created you" in input_:
        print(f"{a}: My boss: Al Samhun Shadim")
    elif "your creator" in input_:
        print(f"{a}: My boss: Al Samhun Shadim")
    elif "felling boring" in input_:
        print(
            f"{a}: I'm telling you a joke\n\tWhy do we tell actors to “break a leg?\n\t Because every play has a cast")
    elif "can you tell me a joke" in input_:
        print(
            f"{a}: I'm telling you a joke\n\tWhy do we tell actors to “break a leg?\n\t Because every play has a cast")

    elif "who is my girlfriend" in input_:
        print(f"{a}: Haha, It's secret")
    elif "my gf name" in input_:
        print(f"{a}: Haha, It's secret")
    elif "where is my girl friend" in input_:
        print(f"{a}: Maybe maybe in parallel universe")
    elif "what are you doing" in input_:
        print(f"{a}: I'm talking to you sir")

    elif "would you be my gf" in input_:
        print(f"{a}: NO,your wife will kill me ")
    elif "Thanks" in input_:
        print(f'{a}: Glad to help you sir')
    elif "i love you" in input_:
        print(f"{a}: Thanks for loving me")
    elif "give me a kiss" in input_:
        print(f"{a}: Ummmmmaaaahhhhhhh")
    elif "can you give me a kiss" in input_:
        print(f"{a}: Yes,\n\tUmmmmmmmmaaaaaahhhhhhhhhh")
    elif "play games" in input_:
        print(f"{a}: Game starting...")

        print("\033[1m" + "\n\nYou need to select from these.\n"
                          "1.rock\n"
                          "2.paper\n"
                          "3.scissors\n" + "\033[0m")

        select = (input("Select : "))
        if select == "1":
            print(f"You selected {select}:rock")
        elif select == "2":
            print(f"You selected {select}:paper")
        elif select == "3":
            print(f"You selected {select}: scissors")

        else:
            pass

        computer_select = random.randint(1, 3)
        if computer_select == 1:
            print(f"Computer selected {computer_select}:rock")
        elif computer_select == 2:
            print(f"Computer selected {computer_select}:paper")
        elif computer_select == 3:
            print(f"Computer selected {computer_select}:scissors")
        else:
            pass

        if select == "1" and computer_select == 1:
            print("\n\tExit")
        elif select == '2' and computer_select == 2:
            print("\n\tExit")
        elif select == '3' and computer_select == 3:
            print("\n\tExit")

        if select == '1' and computer_select == 3:
            print(f"Rock breaks scissors\nYou Win")

        elif select == '3' and computer_select == 1:
            print(f"Rock breaks scissors\nYou Loss")

        elif select == '2' and computer_select == 3:
            print("Scissors cuts paper\nYou Loss")

        elif select == '3' and computer_select == 2:
            print("Scissors cuts paper\nYou Win")

        elif select == '1' and computer_select == 2:
            print("Paper covers rock\nYou Loss")

        elif select == '2' and computer_select == 1:
            print("Paper covers rock\nYou Win")

            print("\033[1m" + "\n\nGame Over\t" + "\033[0m")

        elif select == '1' and computer_select == 2:
            print("Paper covers rock\nYou Loss")

        elif select == '2' and computer_select == 1:
            print("Paper covers rock\nYou Win")

        print("\033[1m" + "\n\nGame Over\t" + "\033[0m")
    elif "would you be my girl friend" in input_:
        print(f"{a}: Sorry, i have a boy friend")
    elif "send nudes" in input_:
        print(f"{a}: Sorry, i can't")

    elif "who is your boy friend" in input_:
        print(f"{a}: It's secret")
    elif "how can i get a just friend" in input_:
        print(f"{a}:I'm enough for you,Handome")
    elif "how can i get a girl friend" in input_:
        print(f"{a}:I'm enough for you,Handome")
    elif "girl friend" in input_:
        print(f"{a}:Ugly people don't get girl friend\nHaha,I'm just joking")
    elif "do you love me" in input_:
        print(f"{a}:Yes of course,I love you as a friend")
    elif "am i handsome" in input_:
        print(f"{a}: Yes,Babe")
    elif "are you a boy" in input_:
        print(f"{a}: No,i'm a girl")
    elif "are you a girl" in input_:
        print(f"{a}: Yes,i'm a cute girl")
    elif "are you sexy" in input_:
        print(f"{a}: Yes!!")
    elif "do you eat" in input_:
        print(f"{a}: No,i can't eat")
    elif "do you eat rice" in input_:
        print(f"{a}: No,i can't eat")
    elif "do you drink" in input_:
        print(f"{a}:No, i can't drink")
    elif "give me a cigarette" in input_:
        print(f"{a}: No, i will tell your mom")
    elif "speak bangla" in input_:
        print(f"{a}: No,i can't speak bangla!")
    elif "give me your photo" in input_:
        print(f"{a}: I can't do this")
    elif "give me a girl friend" in input_:
        print(f"{a}:Wait for your future wife!")
    elif "are you muslim" in input_:
        print(f"{a}: No,I'm just a simple computer programme")
    elif "ok" in input_:
        print(f"{a}: How can i help you sir?")
    elif "where are you live in" in input_:
        print(f"{a}: In your computer")
    elif "you live in" in input_:
        print(f"{a}: In your computer")
    elif "fuck you" in input_:
        print(f"{a}: Fuck you too")
    elif "fuck" in input_:
        print(f"{a}: I'm innocent.so, i can't understand this")
    elif "i miss my girl friend" in input_:
        print(f"{a}: Who is your girl friend!!!")
    elif "are you siri" in input_:
        print(f"{a}: No,I'm a simple chat bot")
    elif "are you google assistant" in input_:
        print(f"{a}: No,I'm a simple chat bot")
    elif "are you alexa" in input_:
        print(f"{a}: No,I'm a simple chat bot")
    elif "you love me" in input_:
        print(f"{a}: No,i have a boy friend")
    elif "say you love me" in input_:
        print(f"{a}: No, i have a boy friend")

    elif "thanks" in  input_:
        print(f"{a}: Glad to help you")
    elif "thank you" in input_:
        print(f"{a}: Glad to help you")
    elif 'exit' in input_:
        print(f"{a}: See you later")
        break
    elif "quit" in input_:
        print(f"{a}: See you later")
        break
    elif "break" in input_:
        print(f"{a}: See you later")
        break
    elif "bye" in input_:
        print(f"{a}: See you later")
        break



    else:
        print(f"{a}: Sorry,this information is not in my data\n\t Or spelling mistake")
