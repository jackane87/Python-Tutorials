from colorama import init
import termcolor

text = termcolor.colored('Hi There', color='cyan', on_color='on_yellow' , attrs=['bold','underline'])

print(text)

