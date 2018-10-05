from __future__ import print_function
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time, random, sys, os

def getSavePath(directory, extension):
    if int(sys.version[0]) < 3:
        from tkFileDialog import asksaveasfilename
        from Tkinter import Tk
    else:
        from tkinter.filedialog import asksaveasfilename
        from tkinter import Tk
    master = Tk()
    master.attributes("-topmost", True)
    path = asksaveasfilename(initialdir=directory,filetypes=['MineFriff {*.'+extension+'}'],defaultextension="."+extension,title="Save")
    master.destroy()
    return path

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

stack = []
mc = minecraft.Minecraft()

LEFT = (0, 0, -1)
RIGHT = (0, 0, 1)
UP = (1, 0, 0)
DOWN = (-1, 0, 0)
LAYER_UP = (0, 1, 0)
LAYER_DOWN = (0, -1, 0)

direction = RIGHT
temp_reg = 0
push_mode = int
next_op = "+"

def change_direction(new_dir):
    if new_dir == direction:
            return direction

    elif new_dir == LEFT:
            return LEFT

    elif new_dir == RIGHT:
            return RIGHT

    elif new_dir == DOWN:
            return DOWN

    elif new_dir == UP:
            return UP

    elif new_dir == LAYER_UP:
            return LAYER_UP

    elif new_dir == LAYER_DOWN:
            return LAYER_DOWN

    else:
            raise Exception("Unknown direction")

def next_block(ip):
    return (ip[0] + direction[0], ip[1] + direction[1], ip[2] + direction[2])

def main(start, end):
    global direction, stack, temp_reg, push_mode, next_op
    ip = start
    output = ""
    eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
    if eval_block == block.GLASS.id:
            return

    while eval_block != block.GLASS.id:

        if eval_block.id == block.WOOD_PLANKS.id:
            if eval_block.data == block.WOOD_PLANKS_OAK.data:
                direction = change_direction(LEFT)

            elif eval_block.data == block.WOOD_PLANKS_SPRUCE.data:
                direction = change_direction(RIGHT)

            elif eval_block.data == block.WOOD_PLANKS_BIRCH.data:
                direction = change_direction(UP)

            elif eval_block.data == block.WOOD_PLANKS_JUNGLE.data:
                direction = change_direction(DOWN)

            elif eval_block.data == block.WOOD_PLANKS_DARK_OAK.data:
                direction = change_direction(LAYER_UP)

            elif eval_block.data == block.WOOD_PLANKS_ACACIA.data:
                direction = change_direction(LAYER_DOWN)
                    
        elif eval_block.id == block.WOOL.id:
            if next_op == "*":
                temp_reg *= eval_block.data

            elif next_op == "+":
                temp_reg += eval_block.data

            elif next_op == "/":
                temp_reg /= float(eval_block.data)

            elif next_op == "-":
                temp_reg -= eval_block.data

            next_op = "+"
            

        elif eval_block.id == block.PISTON.id:
            stack.append(push_mode(temp_reg))
            temp_reg = 0


        elif eval_block.id == block.AIR.id:
                pass

        elif eval_block.id == block.WOOD.id:
            if eval_block.data == block.BIRCH_WOOD.data:
                push_mode = chr

            elif eval_block.data == block.JUNGLE_WOOD.data:
                ip = (ip[0] + (direction[0] * (start[0] - end[0])), ip[1] + (direction[1] * (start[1] - end[1])),
                ip[2] + (direction[2] * (start[2] - end[2])))
                eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
                continue

        elif eval_block.id == block.ICE_PACKED.id:
            push_mode = int

        elif eval_block.id == block.FURNACE_INACTIVE.id:
            push_mode = float

        elif eval_block.id == block.SPONGE.id:
            print(stack[-1], end="")
            del stack[-1]

        elif eval_block.id == block.HOPPER.id:
            stack.append(stack[-1])

        elif eval_block.id == block.NETHERRACK.id:
            stack = stack[::-1]

        elif eval_block.id == block.STONE.id:
            if eval_block.data == block.STONE.data:
                stack.append(len(stack))
            elif eval_block.data == block.STONE_DIORITE.data:
                if temp_reg == 0:
                    #Stack operations
                    x, y = stack[-1], stack[-2]
                    if str not in [type(x), type(y)]:
                        del stack[-1]
                        del stack[-1]
                        stack.append(y / x)

                    else:
                        raise Exception("Different types for /")

                else:
                    next_op = "/"

            elif eval_block.data == block.STONE_ANDESITE.data:
                if temp_reg == 0:
                    #Stack operations
                    x, y = stack[-1], stack[-2]
                    if str not in [type(x), type(y)]:
                        del stack[-1]
                        del stack[-1]
                        stack.append(x + y)

                    else:
                        raise Exception("Different types for +")

                else:
                    next_op = "+"

            elif eval_block.data == block.STONE_GRANITE.data:
                if temp_reg == 0:
                    #Stack operations
                    x, y = stack[-1], stack[-2]
                    if str not in [type(x), type(y)]:
                        del stack[-1]
                        del stack[-1]
                        stack.append(y - x)

                    else:
                        raise Exception("Different types for -")

                else:
                    next_op = "-"

        elif eval_block.id == block.SAND.id:
            if temp_reg == 0:
                #Stack operations
                x, y = stack[-1], stack[-2]
                if str not in [type(x), type(y)]:
                    del stack[-1]
                    del stack[-1]
                    stack.append(y % x)

                else:
                    raise Exception("Different types for %")

            else:
                next_op = "%"
                

        elif eval_block.id == block.REDSTONE_LAMP_INACTIVE.id:
            test = stack[-1]
            del stack[-1]

            if test == 0:
                ip = next_block(ip)
                ip = next_block(ip)
                eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
                continue


        elif eval_block.id == block.SLIME_BLOCK.id:
            ip = next_block(ip)
            ip = next_block(ip)
            eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
            continue

        elif eval_block.id == block.HAY_BLOCK.id:
            ip = (ip[0], ip[1], start[2])
            eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
            direction = change_direction(RIGHT)
            continue

        elif eval_block.id == block.BEDROCK.id:
            if len(stack) < 2:
                raise Exception("Not enough values for comparison")
            x, y = stack[-1], stack[-2]
            del stack[-1]
            del stack[-1]

            if x == y:
                stack.append(1)
            else:
                stack.append(0)

        elif eval_block.id == block.DISPENSER.id:
            direction = change_direction(random.choice([LEFT, RIGHT, UP, DOWN]))

        elif eval_block.id == block.DIAMOND_BLOCK.id:
            if len(stack) < 2:
                raise Exception("Not enough values for comparison")
            x, y = stack[-1], stack[-2]
            del stack[-1]
            del stack[-1]

            if x > y:
                stack.append(1)
            else:
                stack.append(0)

        elif eval_block.id == block.COAL_BLOCK.id:
            if len(stack) < 2:
                raise Exception("Not enough values for comparison")
            x, y = stack[-1], stack[-2]
            del stack[-1]
            del stack[-1]

            if x < y:
                stack.append(1)
            else:
                stack.append(0)

        elif eval_block.id == block.DIRT.id:
            if eval_block.data == block.DIRT.data:
                val = stack[-1]
                del stack[-1]
                stack.insert(0, val)

            elif eval_block.data == block.DIRT_PODZOL.data:
                if temp_reg == 0:
                    #Stack operations
                    x, y = stack[-1], stack[-2]
                    if str not in [type(x), type(y)]:
                        del stack[-1]
                        del stack[-1]
                        stack.append(x * y)

                    else:
                        raise Exception("Different types for *")

                else:
                    next_op = "*"

        elif eval_block.id == block.COBBLESTONE.id:
            val = stack[0]
            del stack[0]
            stack.append(val)


        elif eval_block.id == block.END_BRICKS.id:
            ip = (ip[0] - 1, ip[1], start[2])
            eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])
            continue

        elif eval_block.id == block.OBSIDIAN.id:
            stack[-1], stack[-2] = stack[-2], stack[-1]
        ip = next_block(ip)
        eval_block = mc.getBlockWithNBT(ip[0], ip[1], ip[2])

def export():
    start = [169, 56, -596]
    end = [69, 56, -496]
    code = ""

    for x in range(start[0], end[0], -1):
        y = start[1]
        for z in range(start[2], end[2], 1):
            eval_block = mc.getBlockWithNBT(x, y, z)

            if eval_block.id == block.WOOD_PLANKS.id: #Direction change
                if eval_block.data == block.WOOD_PLANKS_OAK.data: #Go left
                    code += "<"

                elif eval_block.data == block.WOOD_PLANKS_SPRUCE.data: #Go right
                    code += ">"

                elif eval_block.data == block.WOOD_PLANKS_BIRCH.data: #Go up
                    code += "^"

                elif eval_block.data == block.WOOD_PLANKS_JUNGLE.data: #Go down
                    code += "v"

                elif eval_block.data == block.WOOD_PLANKS_DARK_OAK.data:
                    code += "!"

                elif eval_block.data == block.WOOD_PLANKS_ACACIA.data:
                    code += "@"
                        
            elif eval_block.id == block.WOOL.id:
                code += "0123456789abcdef"[eval_block.data]
                
            elif eval_block.id == block.PISTON.id:
                code += ","


            elif eval_block.id == block.AIR.id:
                code += " "

            elif eval_block.id == block.WOOD.id:
                if eval_block.data == block.BIRCH_WOOD.data:
                    code += "C"

                elif eval_block.data == block.JUNGLE_WOOD.data:
                    pass
                    

            elif eval_block.id == block.ICE_PACKED.id:
                code += "I"

            elif eval_block.id == block.FURNACE_INACTIVE.id:
                code += "F"

            elif eval_block.id == block.SPONGE.id:
                code += "o"

            elif eval_block.id == block.HOPPER.id:
                code += ":"

            elif eval_block.id == block.NETHERRACK.id:
                code += "r"

            elif eval_block.id == block.STONE.id:
                if eval_block.data == block.STONE.data:
                    code += "l"
                elif eval_block.data == block.STONE_DIORITE.data:
                    code += "/"

                elif eval_block.data == block.STONE_ANDESITE.data:
                    code += "+"

                elif eval_block.data == block.STONE_GRANITE.data:
                    code += "-"

            elif eval_block.id == block.SAND.id:
                code += "%"
                    

            elif eval_block.id == block.REDSTONE_LAMP_INACTIVE.id:
                code += "?"


            elif eval_block.id == block.SLIME_BLOCK.id:
                code += "#"

            elif eval_block.id == block.HAY_BLOCK.id:
                code += "~"

            elif eval_block.id == block.GLASS.id:
                code += ";"

            elif eval_block.id == block.BEDROCK.id:
                code += "="

            elif eval_block.id == block.DISPENSER.id:
                code += "x"

            elif eval_block.id == block.DIAMOND_BLOCK.id:
                code += ")"

            elif eval_block.id == block.COAL_BLOCK.id:
                code += "("

            elif eval_block.id == block.DIRT.id:
                if eval_block.data == block.DIRT.data:
                    code += "]"

                elif eval_block.data == block.DIRT_PODZOL.data:
                    code += "*"

            elif eval_block.id == block.COBBLESTONE.id:
                code += "["


            elif eval_block.id == block.END_BRICKS.id:
                code += "`"

            elif eval_block.id == block.OBSIDIAN.id:
                code += "$"
        code = code.rstrip()
        code += "\n"


    path = getSavePath("", "mf")
    if not path:
        mc.postToChat('Canceled')
        return
    f = open(path, "w")
    f.write(code)
    f.close()
    mc.postToChat('Code saved in '+path)

def _import():
    path = getLoadPath("", "mf")
    if not path:
        mc.postToChat('Canceled')
        return
    f = open(path)
    code = f.read()
    f.close()
    start = [169, 56, -596]
    loc = [169, 56, -596]
    end = [69, 56, -496]
    for letter in code:
        if letter == "<":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_OAK)

        elif letter == ">":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_SPRUCE)

        elif letter == "^":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_BIRCH)

        elif letter == "v":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_JUNGLE)

        elif letter == "o":
            mc.setBlock(loc[0], loc[1], loc[2], block.SPONGE)

        elif letter in "0123456789abcdef":
            mc.setBlock(loc[0], loc[1], loc[2], block.Block(block.WOOL.id,
                "0123456789abcdef".index(letter)))

        elif letter == "r":
            mc.setBlock(loc[0], loc[1], loc[2], block.NETHERRACK)

        elif letter == ",":
            mc.setBlock(loc[0], loc[1], loc[2], block.PISTON)

        elif letter == ".":
            mc.setBlock(loc[0], loc[1], loc[2], block.Block(29))

        elif letter == "l":
            mc.setBlock(loc[0], loc[1], loc[2], block.STONE)

        elif letter == "=":
            mc.setBlock(loc[0], loc[1], loc[2], block.BEDROCK)

        elif letter == ":":
            mc.setBlock(loc[0], loc[1], loc[2], block.HOPPER)

        elif letter == "$":
            mc.setBlock(loc[0], loc[1], loc[2], block.OBSIDIAN)

        elif letter == "#":
            mc.setBlock(loc[0], loc[1], loc[2], block.SLIME_BLOCK)

        elif letter == "?":
            mc.setBlock(loc[0], loc[1], loc[2], block.REDSTONE_LAMP_INACTIVE)

        elif letter == ";":
            mc.setBlock(loc[0], loc[1], loc[2], block.GLASS)

        elif letter == ")":
            mc.setBlock(loc[0], loc[1], loc[2], block.DIAMOND_BLOCK)

        elif letter == "(":
            mc.setBlock(loc[0], loc[1], loc[2], block.COAL_BLOCK)

        elif letter == "*":
            mc.setBlock(loc[0], loc[1], loc[2], block.DIRT_PODZOL)

        elif letter == "/":
            mc.setBlock(loc[0], loc[1], loc[2], block.STONE_DIORITE)

        elif letter == "+":
            mc.setBlock(loc[0], loc[1], loc[2], block.STONE_ANDESITE)

        elif letter == "-":
            mc.setBlock(loc[0], loc[1], loc[2], block.STONE_GRANITE)

        elif letter == "x":
            mc.setBlock(loc[0], loc[1], loc[2], block.DISPENSER)

        elif letter == "~":
            mc.setBlock(loc[0], loc[1], loc[2], block.HAY_BLOCK)

        elif letter == "I":
            mc.setBlock(loc[0], loc[1], loc[2], block.ICE_PACKED)

        elif letter == "C":
            mc.setBlock(loc[0], loc[1], loc[2], block.BIRCH_WOOD)

        elif letter == "F":
            mc.setBlock(loc[0], loc[1], loc[2], block.FURNACE_INACTIVE)

        elif letter == "`":
            mc.setBlock(loc[0], loc[1], loc[2], block.END_BRICKS)

        elif letter == "]":
            mc.setBlock(loc[0], loc[1], loc[2], block.DIRT)

        elif letter == "[":
            mc.setBlock(loc[0], loc[1], loc[2], block.COBBLESTONE)

        elif letter == "!":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_ACACIA)

        elif letter == "@":
            mc.setBlock(loc[0], loc[1], loc[2], block.WOOD_PLANKS_DARK_OAK)

        elif letter == "%":
            mc.setBlock(loc[0], loc[1], loc[2], block.SAND)
        
        if loc[2] == end[2] or letter == "\n":
            loc[2] = start[2]
            loc[0] -= 1
        else:
            loc[2] += 1



if __name__ == "__main__":
    player_pos = mc.player.getPos()
    if len(sys.argv) > 1:
        if sys.argv[1] == "e":
            export()

        elif sys.argv[1] == "i":
            _import()

        elif sys.argv[1] == "s":
            main((169, 56, -596), (69, 56, -497))
    else:
        main((player_pos.x, player_pos.y - 1, player_pos.z), (player_pos.x - 100, player_pos.y,
player_pos.z + 100))
