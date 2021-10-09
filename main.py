import random
from os import system

def main():
    while 1:
        clear()
        print(" Main Menu\n")
        print(" 1 | Generate")
        print(" 2 | Settings")
        print(" X | Exit")
        option = input(" > | ")
        if option == "1":
            generate()
        elif option == "2":
            settings()
        elif option in ("x","X"):
            return
def settings():
    while 1:
        clear()
        print(" Settings\n")
        print(" 1 | Length    | {} Characters".format(Password.length))
        print(" 2 | Uppercase | {}".format(Password.use_uppercase))
        print(" 3 | Lowercase | {}".format(Password.use_lowercase))
        print(" 4 | Numbers   | {}".format(Password.use_numbers))
        print(" 5 | Symbols   | {}".format(Password.use_symbols))
        print(" X | Back")
        option = input(" > | ")
        if option == "1":
            clear()
            print("Pick New Password Length\n")
            try:
                am = int(input("> | "))
            except:
                pass
            else:
                Password.length = am
        if option == "2":
            if Password.use_uppercase == True:
                Password.use_uppercase = False
            else:
                Password.use_uppercase = True
        if option == "3":
            if Password.use_lowercase == True:
                Password.use_lowercase = False
            else:
                Password.use_lowercase = True
        if option == "4":
            if Password.use_numbers == True:
                Password.use_numbers = False
            else:
                Password.use_numbers = True
        if option  == "5":
            if Password.use_symbols == True:
                Password.use_symbols = False
            else:
                Password.use_symbols = True
        if option in ("x","X"):
            return
def generate():
    while 1:
        clear()
        p = "".join( random.choices( get_characters() , k = Password.length ) )
        print(" Generated Password\n")
        print(" Password: {}\n".format(p))
        print(" 1 | Generate")
        print(" X | Back")
        option = input(" > | ")
        if option in ("x","X"):
            return
def get_characters():
    characters = []
    if Password.use_lowercase:
        characters += Password.lowercase
    if Password.use_uppercase:
        characters += Password.uppercase
    if Password.use_numbers:
        characters += Password.numbers
    if Password.use_symbols:
        characters += Password.symbols
    return characters

class Password:
    uppercase = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z".split(".")
    lowercase = "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z".split(".")
    numbers = "1.2.3.4.5.6.7.8.9.0".split(".")
    symbols = "!,@,#,+,_,-,*,&,%,$,.".split(",")
    length = 10
    use_uppercase = True
    use_lowercase = True
    use_numbers = True
    use_symbols = True

if __name__ == "__main__":
    clear = lambda: system("cls")
    system("title Password Generator")
    main()