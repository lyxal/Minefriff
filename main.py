import random
import ConstLib
import sys

stack = []
temp_reg = 0
direction = ConstLib.RIGHT
ip = (0, 0, 0)
push_mode = int
next_op = "+"

def getLoadPath(directory, extension):
    if int(sys.version[0]) < 3:
        from tkFileDialog import askopenfilename
        from Tkinter import Tk
    else:
        from tkinter.filedialog import askopenfilename
        from tkinter import Tk
    master = Tk()
    master.attributes("-topmost", True)
    path = askopenfilename(initialdir=directory,filetypes=['MineFriff {*.'+extension+'}'],title="Open")
    master.destroy()
    return path

def gridify(code):
    grid = []
    temp_line = []
    for line in code.split("\n"):
        temp_line += line
        grid.append(temp_line[::])
        temp_line = []

    return grid

def next_cmd(ip):
    factor_x = 0
    factor_y = 0
    while is_empty(ip[0] + direction[0] + factor_x,
                   ip[1] + direction[1] + factor_y):
        factor_x += direction[0]
        factor_y += direction[1]
        
    return (ip[0] + direction[0] + factor_x,
            ip[1] + direction[1] + factor_y,
            ip[2] + direction[2])

def is_empty(x, y):
    try:
        c = g[y][x]
        return False
    except IndexError:
        return True
def run(grid):
    global stack, temp_reg, direction, ip, push_mode, next_op
    
    cmd = grid[ip[1]][ip[0]]

    while cmd != ConstLib.END_PROG:
        if cmd == ConstLib.COMMAND_LEFT:
            direction = ConstLib.LEFT

        elif cmd == ConstLib.COMMAND_RIGHT:
            direction = ConstLib.RIGHT

        elif cmd == ConstLib.COMMAND_DOWN:
            direction = ConstLib.DOWN

        elif cmd == ConstLib.COMMAND_UP:
            direction = ConstLib.UP

        elif cmd in ConstLib.LITERAL:
            if next_op == "*":
                temp_reg *= int(cmd, base=16)
            elif next_op == "+":
                temp_reg += int(cmd, base=16)
            elif next_op == "-":
                temp_reg -= int(cmd, base=16)
            elif next_op == "/":
                temp_reg /= int(cmd, base=16)
            elif next_op == "%":
                temp_reg %= int(cmd, base=16)
            next_op = "+"
            

        elif cmd == ConstLib.PUSH:
            stack.append(push_mode(temp_reg))
            temp_reg = 0

        elif cmd == ConstLib.PRINT:
            print(stack[-1], end="")
            del stack[-1]

        elif cmd == ConstLib.INPUT:
            txt = input()
            for char in txt:
                stack.append(char)

        elif cmd == ConstLib.POP:
            del stack[-1]

        elif cmd == ConstLib.REVERSE:
            stack = stack[::-1]

        elif cmd == ConstLib.DUPLICATE:
            stack.append(stack[-1])

        elif cmd == ConstLib.LENGTH:
            stack.append(len(stack))

        elif cmd == ConstLib.RETURN:
            ip = (0, ip[1], ip[2])
            cmd = grid[ip[1]][ip[0]]
            continue

        elif cmd == ConstLib.TRAMPOLINE:
            ip = next_cmd(ip)
            ip = next_cmd(ip)
            cmd = grid[ip[1]][ip[0]]
            continue

        elif cmd == ConstLib.CONDITIONAL:
            test = stack[-1]
            del stack[-1]
            
            if test == 0:
                ip = next_cmd(ip)
                ip = next_cmd(ip)
                cmd = grid[ip[1]][ip[0]]
                continue

        elif cmd == ConstLib.PUSH_CHR:
            push_mode = chr

        elif cmd == ConstLib.PUSH_INT:
            push_mode = int

        elif cmd == ConstLib.PUSH_FLOAT:
            push_mode = float

        elif cmd == ConstLib.MULTIPLY:
            if temp_reg == 0:
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]

                    stack.append(x * y)
                else:
                    raise Exception("Types for multiplication are different")
            else:
                next_op = "*"

        elif cmd == ConstLib.ADD:
            if temp_reg == 0:
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]

                    stack.append(x + y)
                else:
                    raise Exception("Types for addition are different")
            else:
                next_op = "+"


        elif cmd == ConstLib.SUBTRACT:
            if temp_reg == 0:
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]

                    stack.append(y - x)
                else:
                    raise Exception("Types for subtraction are different")
            else:
                next_op = "-"

        elif cmd == ConstLib.DIVIDE:
            if temp_reg == 0:
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]

                    stack.append(y / x)
                else:
                    raise Exception("Types for divison are different")
            else:
                next_op = "/"

        elif cmd == ConstLib.MODULUS:
            if temp_reg == 0:
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]

                    stack.append(y % x)
                else:
                    raise Exception("Types for modulus are different")
            else:
                next_op = "%"

        
        elif cmd == ConstLib.NEXT_LINE:
            ip = (0, ip[1] + 1, ip[2])
            cmd = grid[ip[1]][ip[0]]
            continue

        elif cmd == ConstLib.EQUALS:
            if len(stack) >= 2:
                left, right = stack[-1], stack[-2]
                del stack[-1]; del stack[-1]
                if left == right:
                    stack.append(1)
                else:
                    stack.append(0)
            else:
                raise Exception("Not enough values for comparison for =")
            
        ip = next_cmd(ip)
        #print(stack, cmd)
        cmd = grid[ip[1]][ip[0]]

if __name__ == '__main__':
    pre_stack = input("Enter values to pre-populate stack: ")
    for letter in pre_stack:
        stack.append(letter)
    code = open(getLoadPath("", ".mf")).read()
    g = gridify(code)
    run(g)
