BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

#KB[Kilobyte] -> All Conversion

def kb_to_mb(x: float) -> None:
    mb = x/1024
    print(f"{RED}{BOLD}{x}{RESET} KB ={YELLOW}{BOLD}{mb:.2f}{RESET} MB")
    return None



# a = 1024
# b = kb_to_mb(a)
# print(b)

def kb_to_gb(x: float) -> None:
    gb = x/pow(1024, 2)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{gb:.2f}{RESET} GB")
    return None


# a = 1024
# b = kb_to_gb(a)
# print(b)

def kb_to_tb(x: float) -> None:
    tb = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{tb:.2f}{RESET} TB")
    return None


# a = 3072
# b = kb_to_tb(a)
# print(b)

def kb_to_pb(x: float) -> None:
    pb = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{pb:.2f}{RESET} PB")
    return None


def kb_to_eb(x: float)-> None:
    eb = x/pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{eb:.2f}{RESET} EB")
    return None


def kb_to_zb(x: float)->None:
    zb = x/pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{zb:.2f}{RESET} ZB")
    return None


def kb_to_yb(x: float) ->None:
    yb = x/pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{yb:.2f}{RESET} YB")
    return None


def kb_to_bb(x: float)->None:
    bb = x/pow(1024,8)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{bb:.2f}{RESET} BB")
    return None


def kb_to_geb(x: float)->None:
    GEB = x/pow(1024,9)
    print(f"{RED}{BOLD}{x}{RESET} KB ={GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#MB[MegaByte] -> All Conversion

def mb_to_kb(x: float)->None:
    kb = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{kb:.2f}{RESET} KB")
    return None


def mb_to_gb(x: float)-> None:
    gb = x/1024
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{gb:.2f}{RESET} GB")
    return None


def mb_to_tb(x: float)-> None:
    TB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def mb_to_pb(x: float)-> None:
    PB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def mb_to_eb(x: float)->None:
    EB = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def mb_to_zb(x: float)-> None:
    ZB = x/pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def mb_to_yb(x: float) -> None:
    YB = x/pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def mb_to_bb(x: float)->None:
    BB = x/pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def mb_to_geb(x: float)->None:
    GEB = x/pow(1024,8)
    print(f"{RED}{BOLD}{x}{RESET} MB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#GB[GigaByte] ->  All Conversion
def gb_to_kb(x: float) ->None:
    kb = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{kb:.2f}{RESET} KB")
    return None


def gb_to_mb(x: float) -> None:
    MB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def gb_to_tb(x: float)-> None:
    TB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def gb_to_pb(x: float)-> None:
    PB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def gb_to_eb(x: float)-> None:
    EB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def gb_to_zb(x: float)->None:
    ZB = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def gb_to_yb(x: float)-> None:
    YB = x/pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def gb_to_bb(x: float)->None:
    BB = x/pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None
    

def gb_to_geb(x: float)-> None:
    EB = x/pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} GB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


#TB[TeraByte] -> All Conversion

def tb_to_kb(x: float)-> None:
    KB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def tb_to_mb(x: float)-> None:
    MB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def tb_to_gb(x: float)-> None:
    GB = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def tb_to_pb(x: float)-> None:
    PB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def tb_to_eb(x: float)-> None:
    EB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def tb_to_zb(x: float)-> None:
    ZB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def tb_to_yb(x: float)-> None:
    YB = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def tb_to_bb(x: float)-> None:
    BB = x/pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def tb_to_geb(x: float)-> None:
    GEB = x/pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} TB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#PB[PetaByte] -> All Conversion
def pb_to_kb(x: float)-> None:
    KB = x*pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def pb_to_mb(x: float)-> None:
    MB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def pb_to_gb(x: float)-> None:
    GB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def pb_to_tb(x: float)-> None:
    TB = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def pb_to_eb(x: float)-> None:
    EB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def pb_to_zb(x: float)-> None:
    ZB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def pb_to_yb(x: float)-> None:
    YB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def pb_to_bb(x: float)-> None:
    BB = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def pb_to_geb(x: float)-> None:
    GEB = x/pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} PB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


# EB[ExaByte] -> All Conversion
def eb_to_kb(x: float)-> None:
    KB = x*pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def eb_to_mb(x: float)-> None:
    MB = x*pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def eb_to_gb(x: float)-> None:
    GB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def eb_to_tb(x: float)-> None:
    TB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{TB:.2f}{RESET} PB")
    return None


def eb_to_pb(x: float)-> None:
    PB = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def eb_to_zb(x: float)-> None:
    ZB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def eb_to_yb(x: float)-> None:
    YB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def eb_to_bb(x: float)-> None:
    BB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def eb_to_geb(x: float)-> None:
    GEB = x/pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} EB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#ZB[ZettaByte] -> All Conversion
def zb_to_kb(x: float)-> None:  #ZB -> KB
    KB = x*pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def zb_to_mb(x: float)-> None:
    MB = x*pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def zb_to_gb(x: float)-> None:
    GB = x*pow(1024, 4)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def zb_to_tb(x: float)-> None:
    TB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def zb_to_pb(x: float)-> None:
    PB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def zb_to_eb(x: float)-> None:
    EB = x*pow(1024, 1)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def zb_to_yb(x: float)-> None:
    YB = x/pow(1024, 1)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def zb_to_bb(x: float)-> None:
    BB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def zb_to_geb(x: float)-> None:
    GEB = x/pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#YB[YottaByte] -> All Conversion

def yb_to_kb(x: float)-> None:
    KB = x*pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def yb_to_mb(x: float)-> None:
    MB = x*pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def yb_to_gb(x: float)-> None:
    GB = x*pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None
    

def yb_to_tb(x: float)-> None:
    TB = x*pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def yb_to_pb(x: float)-> None:
    PB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def yb_to_eb(x: float)-> None:
    EB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def yb_to_zb(x: float)-> None:
    ZB = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def yb_to_bb(x: float)-> None:
    BB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None


def yb_to_geb(x: float)-> None:
    GEB = x/pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} ZB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#BB[BrontoByte] -> All Conversion
def bb_to_kb(x: float)-> None:
    KB = x*pow(1024,8)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def bb_to_mb(x: float)-> None:
    MB = x*pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None


def bb_to_gb(x: float)-> None:
    GB = x*pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def bb_to_tb(x: float)-> None:
    TB = x*pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def bb_to_pb(x: float)-> None:
    PB = x*pow(1024,4)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None


def bb_to_eb(x: float)-> None:
    EB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{EB:.2f}{RESET} EB")
    return None


def bb_to_zb(x: float)-> None:
    ZB = x*pow(1024,2)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def bb_to_yb(x: float)-> None:
    YB = x*pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{YB:.2f}{RESET} YB")
    return None


def bb_to_geb(x: float)-> None:
    GEB = x/pow(1024,1)
    print(f"{RED}{BOLD}{x}{RESET} BB = {GREEN}{BOLD}{GEB:.2f}{RESET} GEB")
    return None


#GEB[GeopByte] -> All Conversion
def geb_to_kb(x: float)-> None:
    KB = x*pow(1024,9)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{KB:.2f}{RESET} KB")
    return None


def geb_to_mb(x: float)-> None:
    MB = x*pow(1024,8)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{MB:.2f}{RESET} MB")
    return None

def geb_to_gb(x: float)-> None:
    GB = x*pow(1024,7)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{GB:.2f}{RESET} GB")
    return None


def geb_to_tb(x: float)-> None:
    TB = x*pow(1024,6)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{TB:.2f}{RESET} TB")
    return None


def geb_to_pb(x: float)-> None:
    PB = x*pow(1024,5)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{PB:.2f}{RESET} PB")
    return None

def geb_to_eb(x: float)-> None:
    EB = x* pow(1024, 4)
    print(f"{RED} {BOLD} {x} {RESET} GEB = {GREEN} {BOLD} {EB:.2f} {RESET} EB")
    return None


def geb_to_zb(x: float)-> None:
    ZB = x*pow(1024,3)
    print(f"{RED}{BOLD}{x}{RESET} GEB = {GREEN}{BOLD}{ZB:.2f}{RESET} ZB")
    return None


def geb_to_yb(x: float)-> None:
    YB = x*pow(1024,2)
    print(f"{RED} {BOLD} {x} {RESET} GEB = {GREEN} {BOLD} {YB:.2f} {RESET} YB")
    return None


def geb_to_bb(x: float)-> None:
    BB = x*pow(1024, 1)
    print(f"{RED}{BOLD}{x}{RESET}GEB = {GREEN}{BOLD}{BB:.2f}{RESET} BB")
    return None










































