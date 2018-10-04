|                                                 Command                                                |       Symbol       |  Minecraft Block Equivalent |
|:------------------------------------------------------------------------------------------------------:|:------------------:|:---------------------------:|
| Move the IP left.                                                                                      |         `<`        | Oak Wood Planks             |
| Move the IP right.                                                                                     |         `>`        | Spruce Wood Planks          |
| Move the IP up.                                                                                        |         `^`        | Birch Wood Planks           |
| Move the IP down.                                                                                      |         `v`        | Jungle Wood Planks          |
| Print the top value on the stack.                                                                      |         `o`        | Sponge                      |
| Add a literal to the temp reg.                                                                         | `0123456789abcdef` | Wool (Data gives the value) |
| Reverse the contents of the stack.                                                                     |         `r`        | Netherrack                  |
| Push the temp reg onto the stack and reset it to 0.                                                    |         `,`        | Piston                      |
| Pop the top item from the stack and place it in the temp reg.                                          |         `.`        | Sticky Piston               |
| Push the length of the stack onto the stack.                                                           |         `l`        | Stone                       |
| Pop `x` and `y` off the stack. Push `y == x` back on (1 if true, 0 if false).                          |         `=`        | Bedrock                     |
| Duplicate the top item of the stack.                                                                   |         `:`        | Hopper                      |
| Swap the top two items of the stack.                                                                   |         `$`        | Obsidian                    |
| Skip the next instruction (trampoline).                                                                |         `#`        | Slime Block                 |
| Pop the top value from the stack and skip the next instruction if it is zero (conditional trampoline). |         `?`        | Redstone Lamp (off)         |
| End the program                                                                                        |         `;`        | Glass Block                 |
| Pop `x` and `y` off the stack. Push `y > x` back on (1 if true, 0 if false).                           |         `)`        | Diamond Block               |
| Pop `x` and `y` off the stack. Push `y < x` back on (1 if true, 0 if false).                           |         `(`        | Coal Block                  |
| Pop `x` and `y` off the stack. Push `y * x` back on.                                                   |         `*`        | Podzol                      |
| Pop `x` and `y` off the stack. Push `y / x` back on.                                                   |         `/`        | Diorite (raw)               |
| Pop `x` and `y` off the stack. Push `y + x` back on.                                                   |         `+`        | Andesite (raw)              |
| Pop `x` and `y` off the stack. Push `y - x` back on.                                                   |         `-`        | Granite (raw)               |
| Change the direction of the IP to a random direction.                                                  |         `x`        | Dispenser                   |
| Go back to the start of the current line in the same direction.                                        |         `~`        | Hay Block                   |
| Go to the start of the next line.                                                                      |        `\``        | End Bricks                  |
| Treat the temp reg as an integer.                                                                      |         `I`        | Packed Ice                  |
| Treat the temp reg as a character.                                                                     |         `C`        | Birch Wood                  |
| Treat the temp reg as a float.                                                                         |         `F`        | Furnace                     |
| Right shift the stack by 1.                                                                            |         `]`        | Dirt Block                  |
| Left shift the stack by 1.                                                                             |         `[`        | Cobblestone                 |
| Pop `x` and `y` off the stack. Push `y % x` back on.                                                   |         `%`        | Sand (normal)               |
