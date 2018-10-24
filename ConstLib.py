LEFT = (-1, 0, 0)
RIGHT = (1, 0, 0)
UP = (0, -1, 0)
DOWN = (0, 1, 0)
UP_LAYER = (0, 0, 1)
DOWN_LAYER = (0, 0, -1)

COMMAND_LEFT = "<"
COMMAND_RIGHT = ">"
COMMAND_UP = "^"
COMMAND_DOWN = "v"

OUTPUT = "o"
LITERAL = "0123456789abcdef"
REVERSE = "r"
PUSH = ","
POP = "."
DELETE = "!"
LENGTH = "l"
EQUALS = "="
DUPLICATE = ":"
SWAP_TOP = "$"
TRAMPOLINE = "#"
CONDITIONAL = "?"
END_PROG = ";"
GREATER_THAN = ")"
LESS_THAN = "("
MULTIPLY = "*"
DIVIDE = "/"
ADD = "+"
SUBTRACT = "-"
RANDOM = "x"
RETURN = "~"
PUSH_CHR = "C"
PUSH_INT = "I"
PUSH_FLOAT = "F"
NEXT_LINE = "`"
R_SHIFT = "]"
L_SHIFT = "["
INPUT = "i"
MODULUS = "%"
JUMP = '"'
COMMENT_START = "{"
COMMENT_END = "}"
PEAK_UP = "U"
PEAK_DOWN = "D"
PEAK_LEFT = "L"
PEAK_RIGHT = "R"
PRINT = "p"

class PEAK_DIR:
    UP = (0, -1, 0)
    DOWN = (0, 1, 0)
    LEFT = (-1, 0, 0)
    RIGHT = (1, 0, 0)
    NONE = (0, 0, 0)
