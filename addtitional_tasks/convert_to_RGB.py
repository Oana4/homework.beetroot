# Type conversion. Several formats are used to represent color.
# For example, the primary format for LCDs, digital cameras, and web pages—known as the RGB format—specifies
# the level of red (R), green (G), and blue (B) on an integer scale from 0 to 255.
# The primary format for publishing books and magazines—known as the CMYK format—specifies the level of cyan (C),
# magenta (M), yellow (Y), and black (K) on a real scale from 0.0 to 1.0.
# Create a program that after the start, indefinitely waits for user input in CMYK format
# and on each input converts to RGB

users_choice = input('Choose the level of cyan, magenta, '
                     'yellow, black from 0.0-1.0 or type "exit": ')

white, red, green, blue = 0, 0, 0, 0
cyan, magenta, yellow, black = 0, 0, 0, 0

while users_choice != 'exit':
    users_choice = users_choice.split()
    if len(users_choice) == 4:
        [cyan, magenta, yellow, black] = map(float, users_choice)
        if (0.0 <= cyan <= 1.0) and (0.0 <= magenta <= 1.0) and (0.0 <= yellow <= 1.0) and (0.0 <= black <= 1.0):
            white = 1 - black
            red = 255 * white * (1 - cyan)
            green = 255 * white * (1 - magenta)
            blue = 255 * white * (1 - yellow)

            print(f"Red: {int(red)}")
            print(f"Green: {int(green)}")
            print(f"Blue: {int(blue)}")
        else:
            print("Values not in the specified range!")
    else:
        print("You chose the wrong values for C, M, Y, B!")

    users_choice = input('Choose the level of cyan, magenta, '
                         'yellow, black from 0.0-1.0 or type "exit": ')

