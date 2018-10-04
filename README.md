# MineFriff - A Blocky Esolang
**MineFriff** brings the joy of traditional esolangs such as `Befunge` and `><>` into the blocky pixelated world of _Minecraft_.  Much like fungoid languages, MineFriff allows code to be set out in a 2D code area, which can range from a 100*100 grid (allowing for 10,000 instructions) to any size of square (or cube).

As aforementioned, MineFriff allows for free-form code to be written in any size cube (meaning that 3D code is allowed).

**MineFriff** comes in three flavours: Strict, Freeform and Textual. _Strict_ MineFriff is contained in a 100 by 100 block grid, and can be exported to a `.mf` file. However, strict MineFriff is only avaliable in the offical MineFriff interpreter world. _Freeform_ MineFriff is avaliable in any world, but is unexportable to an actual file -- code is run using.
```
/py MineFriff
```

_Textual_ MineFriff is a text based ascii version of the blocky esolang, which is avaliable to everyone -- all one needs is the python based MineFriff interpreter.

## Concepts
### Code Box
Like most fungeoidal esolangs, MineFriff has a code box in which the program is placed. In strict MineFriff, this code box is as shown:

![100 * 100 block code grid]()

In freeform MineFriff, this code box is essentially non-existant; programs can take any form they want and can be even 3d.

In textual MineFriff, the code box spans an infinite amount of space, both vertically and horizontally.

### Instruction Pointer (IP)
The _instruction pointer_ is what drives the interpreting of MineFriff programs. It starts in the top left corner of the program (strict and textual) or wherever the player is standing in freeform. It can move left, right, up, down, and in the case of freeform MineFriff, up layers and down layers. In strict MineFriff, when the IP reaches the edge of the code box, the IP "wraps around" to the other side (e.g. if it reaches the far right side, it will go to the far left side and continue). This doesn't in happen in freeform MineFriff, as there isn't any code box to wrap around. This functionality is being worked on for textual MineFriff.

### The Temporary Register
Rather than having literals pushed directly onto the stack, MineFriff has a _temporary register_ (temp reg) in which literals are constructed. This allows for any value to be created without having to worry about impacting the stack. The temp reg can be treated as either an `int`eger, a `char`acter or a `float`.
