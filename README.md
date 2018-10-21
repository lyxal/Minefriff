# MineFriff - A Blocky Esolang
**MineFriff** brings the joy of traditional esolangs such as `Befunge` and `><>` into the blocky pixelated world of _Minecraft_.  Much like fungeoid languages, MineFriff allows code to be set out in a 2D code area, which can range from a 100*100 grid (allowing for 10,000 instructions) to any size of square (or cube).

As aforementioned, MineFriff allows for free-form code to be written in any size cube (meaning that 3D code is allowed).

**MineFriff** comes in three flavours: Strict, Freeform and Textual. _Strict_ MineFriff is contained in a 100 by 100 block grid, and can be exported to a `.mf` file. However, strict MineFriff is only avaliable in the offical MineFriff interpreter world. _Freeform_ MineFriff is avaliable in any world, but is unexportable to an actual file -- code is run using.
```
/py MineFriff
```

_Textual_ MineFriff is a text based ascii version of the blocky esolang, which is avaliable to everyone -- all one needs is the python based MineFriff interpreter.

## Concepts
### Code Box
Like most fungeoidal esolangs, MineFriff has a code box in which the program is placed. In strict MineFriff, this code box is as shown:

![100 * 100 block code grid](https://lh3.googleusercontent.com/tXp9f3xuB_S83ek8RkoznTq1_sIqf2aH-zNH4aiBXxvzJwT58d5r2HStrCprvPhJMj6L9YkVaiSR2khAZeB4an2oDgveBt7zIcBypbxul1-xyhlx2QN4D0tnh3mYctoc64-GU93R6FXWgysyoixHkw6yq1dqAaIZT0bT8EKU_pZSKE-wIzniB_ofbzc-w6vssv4MiiWgcGcaq80jh8DdNK7fRQnOps5OFpOxuKJKJEZkyA1SzEKKPu-xTy9CwDq-AQuob3M0xGWNZEpJdoE4f2VhYqAcSUOCcX8X_TxggFFb-wvrk5F9cnowz2zAbikDHguvf3MfKuEj7xbIOrhQGXJI64NcywYPNv7AWWDnQFdVzjQEM9Z8-CKKBMXabvxN4lIamdjiYM8ssFpVF9KVEGQ0k7DZeNrEGHz1eeWprsDJOqxbDC8duDvqkFCwGuTqzGKxf3e8Ycevm6qFG3VPHEnSuwbF7UZbYe220jT5FrhzbP4ahnmPpvuy7mODhtM6RRpWJqqjq4GMScCV4n3hd_2h1HxHIAj_s4nRfrCnnGgKji8ZThxs959EOBHseMlenT3MDAnzzH31MO_DzPWCsxH7BYDRZJ46hAMlWExQHvNHBmSqpYWPnZcLEEdsIjs=w1186-h741-no)

In freeform MineFriff, this code box is essentially non-existant; programs can take any form they want and can be even 3d.

In textual MineFriff, the code box spans an infinite amount of space, both vertically and horizontally.

### Instruction Pointer (IP)
The _instruction pointer_ is what drives the interpreting of MineFriff programs. It starts in the top left corner of the program (strict and textual) or wherever the player is standing in freeform. It can move left, right, up, down, and in the case of freeform MineFriff, up layers and down layers. In strict MineFriff, when the IP reaches the edge of the code box, the IP "wraps around" to the other side (e.g. if it reaches the far right side, it will go to the far left side and continue). This doesn't in happen in freeform MineFriff, as there isn't any code box to wrap around. This functionality is being worked on for textual MineFriff.

### The Temporary Register
Rather than having literals pushed directly onto the stack, MineFriff has a _temporary register_ (temp reg) in which literals are constructed. This allows for any value to be created without having to worry about impacting the stack. The temp reg can be treated as either an `int`eger, a `char`acter or a `float`.

### The Stack
The stack in MineFriff is like the stack in most other fungeoids -- it can have values pushed to it, it can have stack operations performed, it can be shifted left and right -- all of the usual stuff. However, when popping values from the stack, they are placed back into the temp reg (hence, overwriting the current value), rather than deleted into nowhere.

## Instructions
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
| Go to the start of the next line.                                                                      |         Backtick        | End Bricks                  |
| Treat the temp reg as an integer.                                                                      |         `I`        | Packed Ice                  |
| Treat the temp reg as a character.                                                                     |         `C`        | Birch Wood                  |
| Treat the temp reg as a float.                                                                         |         `F`        | Furnace                     |
| Right shift the stack by 1.                                                                            |         `]`        | Dirt Block                  |
| Left shift the stack by 1.                                                                             |         `[`        | Cobblestone                 |
| Pop `x` and `y` off the stack. Push `y % x` back on.                                                   |         `%`        | Sand (normal)               |
| Start/end a comment                                                                                    |         `{...}`     | N/A                         |
| Delete the last item on the stack (pop it, without saving it)                                                               |         `!`     | N/A                         |


## Example Programs
### Hello World
	C9*8,a*a1,9*c,:a*b1,ffe,ff2,8*a7,a*b1,a*b4,9*c,a*a,ff3,`
	>l?#;o~

![Hello world program in blocks](https://lh3.googleusercontent.com/0OLHfIK0dkMC0Wma5OhB6bTlxaDrmv1FlluEyqnh2wdCJjQK3fJ5ATUycUuixtIAODqi9Ix7P3bJ0FHE2bSJ0xln_1-fy-Fvz4pzGvxnthpH2XfQgKUdewKpCZGjF_JT0Gbz0yG0ypwYBfQRp08VQNb_JKbJRDGjz9Clpbgnk7WjdrsMnEHJAPeAjmoEtIc9k8qAOBm93xpldcUZxUTmBtpYDvvw0zsP0MKUdYLjoPE4DSDFe1RqqtDRt-H7ftrrUOoikdKVTZ7qnBzMFdjhIN9BdKsNJm9yDW7ZZlYhc9KvTaQWvWq_xZJ4ddr56kfwvkWWuAOGmbxsrC5ZfM0xDlMlkZiydVBLEtO8mJNi7QFb4fTkrMDKxbBqUWuCjKJMouHQp1LIPxaJ7WmRKJ693EfDBGfIuB6IHi6bO6lLx6K8JnykUR4hDSft56erMJnh5sObvy5s3-Gxn2QJ7FyDbk6wmCVqy-ZnL_ZwBsQ5hMdBxuU6Hlbzp8CfPVT6wF3cGFruHeDA3xd6DOvUsjzKEutpcKeNztBY-5YoYv3tomol8X0bEQ8fo21LGKLRUBf2iukj_IFpO0YXdkp6cb-jAI4c_-otIaHXz1Cyxyabe44Je7gppZxpiVTLBpUsWyk=w1264-h790-no)
### Fizzbuzz
	0,`
	>I1,+:a*a1,=?;`~             o,aC            <  
	>:f,%?`Ca*c2,:a*b7,7*e,a*c2,:f*7,a*7,oooooooo^
	>:5,%?`Ca*c2,:a*b7,6*b,oooo                  ^
	>:3,%?`Ca*c2,:f*7,a*7,oooo                   ^
	>:o                                          ^ 

![Fizzbuzz program in blocks](https://lh3.googleusercontent.com/9fY3GEMsNFk3bnzmMUUKA0wIxVUsah7l7vnHtszAcLgH7lI6nxrQ5EL9Z51NhViDt-_abKjW4rbZ5ayYw74tDQy2lLG8Ba9n56khZdZOBnkL55Lx7dxytT1C3WpR8yOR9wzIA3bg4OcclQDFdJ1HOQXM89qZeJb65HQpbn5ifWejxhinyCIFaO3xG_Ywnh4Ux0_U8xbSlSiU1ZsseN1xNfoDRnrCGEsKbeKZcd5Uvs37Mk9t7QhuL1ky-gIWdb5tRZZXJJ57-P0XaXH6kj64sgS8ev0cY6Uo3N9m1Dn_TZUhDOgL__DBCIsN5rEqCTXlrvXSEK6eQ7B-P6jFKp_Wc0uUqdw-tZAOpBpMkSDZiGtSXyQ289wwVnNVTsQumohPRwPm596R94-EMCigjN-bjP3nk_NjiRB6eRw8wkmw3OhgJVHlKgp_H0ssa0uV2Zy6R0y4CbeueEqNMK0DDiHXlNDb2_OIWW2lip0QtxKkWHn1ahLZq16-SkJo27oagPIh_lqubt-V3wLfKnl-C8NJrV4tt0ZxioxdxENCcf4uo03PWzIZiC5ezHH3VXbrApO8HdD6OAs31PAie7eyMUoK73mnYldz_WqooOHAYjVBbslfSIktq3GVJagOqtXAr8A=w1264-h790-no)

### 99 bottles of bear
    Ia*a,`
    >I1,-:0,=?;`                                                                                                                                   ~
    >Cff2,ffe,c*9,c*9,a*97,a*b9,ff2,a*a1,d*8,a*b6,ff2,a*b,a*b1,ff2,a*b4,a*a1,a*a1,e*7,ff2,a*a2,a*b1,ff2,a*b5,a*a1,c*9,a*b6,a*b6,a*b1,e*7,ff2,`
    >r:or`
    >lI1,=?`o~
    >Ca,a*46,a*b4,a*a1,a*a1,e*7,ff2,a*a2,a*b1,ff2,a*b5,a*a1,c*9,a*b6,a*b6,a*b1,e*7,ff2,`
    >r:or`
    >lI1,=?`o~
    >Cff2,ffe,a*a,a*b,d*9,a*b1,a*b4,a*97,ff2,a*b6,f*7,ff2,a*b5,a*b5,a*97,e*8,ff2,ffe,a*b,a*b9,a*b1,a*a,ff2,a*a1,a*b,a*b1,ff2,a*a1,a*a7,a*97,c*7,`
    >lI1,=?`o~
    >Ca*46,c*9,c*9,a*97,a*b9,ff2,a*a1,d*8,a*b6,ff2,a*b,a*b1,ff2,a*b4,a*a1,a*a1,e*7,ff2,a*a2,a*b1,ff2,a*b5,a*a1,c*9,a*b6,a*b6,a*b1,e*7,ff2,`
    >r:I1,-or`
    >l1,=?`o~                                                                                                                                  
    >Ca,a,oo                                                                                                                                       ^
--------------
# Installation Instructions for Strict and Freeform MineFriff
You will need the [Raspberry Jam Mod](https://github.com/arpruss/raspberryjammod). The tutorial [here](https://www.instructables.com/id/Python-coding-for-Minecraft/) shows how to install it. Once you have the mod fully installed, drag `MineFriff.py` into the `mcpipy` folder.

# To be Added
- The ability to have input
- More commands
