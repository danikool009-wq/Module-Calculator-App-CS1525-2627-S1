def get_operation():

    while True:
        opp= input("what operation do you want to do?(/,*,-,+)")
        if opp == "/" or opp == "*" or opp == "-" or opp == "+":
            return opp

        else:
            print("invalid operation")