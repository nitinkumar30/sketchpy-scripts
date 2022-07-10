from sketchpy import library as lib

user_input = int(input('What do you want sketch of? Chose the relevant number:\n1. Robert Downey Junior aka Ironman\n2. Indian Map with Abdul Kalam sir\n3. BTS Actor V(Kim Taehyung)\n4. Indian Flag hoisting\n5. Anime Character Gojo Saturo\n6. Ironman in ascii characters\n7. Hollywood Actor - Tom Holland\n8. Tollywood Actor - Vijay\n\n>>'))


if user_input == 1:
    obj = lib.rdj()  # Robert Downey Junior
    obj.draw()
elif user_input == 2:
    obj = lib.apj()  # Robert Downey Junior
    obj.draw()
elif user_input == 3:
    obj = lib.bts()  # Robert Downey Junior
    obj.draw()
elif user_input == 4:
    obj = lib.flag()  # Robert Downey Junior
    obj.draw()
elif user_input == 5:
    obj = lib.gojo()  # Robert Downey Junior
    obj.draw()
elif user_input == 6:
    obj = lib.ironman_ascii()  # Robert Downey Junior
    obj.draw()
elif user_input == 7:
    obj = lib.tom_holland()  # Robert Downey Junior
    obj.draw()
elif user_input == 8:
    obj = lib.vijay()  # Robert Downey Junior
    obj.draw()
else:
    print('Wrong Input selected.!')

