from pyfiglet import figlet_format
from colorama import init
import termcolor

def ascii_msg_generator():
    message = input('What message do you want to print? ')
    msg_color = input('What color would you like the message to be? ').lower()
    if msg_color not in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey'):
        print(termcolor.colored(f'{msg_color.upper()} is not a supported color. The color will be defaulted to green.', color='red'))
        msg_color = 'green'
    text = termcolor.colored(figlet_format(message, font='isometric1'), color=msg_color)
    print(text)

ascii_msg_generator()