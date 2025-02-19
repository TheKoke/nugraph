import os


NAME2CHARGE = {
    'p' :   1, 'd' :   1, 't' :   1,
    'h' :   1, 'he':   2, 'li':   3, 'be':   4, 'b' :   5, 'c' :   6,
    'n' :   7, 'o' :   8, 'f' :   9, 'ne':  10, 'na':  11, 'mg':  12,
    'al':  13, 'si':  14, 'p' :  15, 's' :  16, 'cl':  17, 'ar':  18,
    'k' :  19, 'ca':  20, 'sc':  21, 'ti':  22, 'v' :  23, 'cr':  24,
    'mn':  25, 'fe':  26, 'co':  27, 'ni':  28, 'cu':  29, 'zr':  30,
    'ga':  31, 'ge':  32, 'as':  33, 'se':  34, 'br':  35, 'kr':  36,
    'rb':  37, 'sr':  38, 'y' :  39, 'zr':  40, 'nb':  41, 'mo':  42,
    'tc':  43, 'ru':  44, 'rh':  45, 'pd':  46, 'ag':  47, 'cd':  48,
    'in':  49, 'sn':  50, 'sb':  51, 'te':  52, 'i' :  53, 'xe':  54,
    'cs':  55, 'ba':  56, 'la':  57, 'ce':  58, 'pr':  59, 'nd':  60,
    'pm':  61, 'sm':  62, 'eu':  63, 'gd':  64, 'tb':  65, 'dy':  66,
    'ho':  67, 'er':  68, 'tm':  69, 'yb':  70, 'lu':  71, 'hf':  72,
    'ta':  73, 'w' :  74, 're':  75, 'os':  76, 'ir':  77, 'pt':  78,
    'au':  79, 'hg':  80, 'tl':  81, 'pb':  82, 'bi':  83, 'po':  84,
    'at':  85, 'rn':  86, 'fr':  87, 'ra':  88, 'ac':  89, 'th':  90,
    'pa':  91, 'u' :  92, 'np':  93, 'pu':  94, 'am':  95, 'cm':  96,
    'bk':  97, 'cf':  98, 'es':  99, 'fm': 100, 'md': 101, 'no': 102,
    'lr': 103, 'rf': 104, 'db': 105, 'sg': 106, 'bh': 107, 'hs': 108,
    'mt': 109, 'ds': 110, 'rg': 111, 'cn': 112, 'nh': 113, 'fl': 114,
    'mc': 115, 'lv': 116, 'ts': 117, 'og': 118
}

CHARGE2NAME = {
    0  :  'n',
    1  :  'H', 2  : 'He', 3  : 'Li', 4  : 'Be', 5  :  'B', 6  :  'C',
    7  :  'N', 8  :  'O', 9  :  'F', 10 : 'Ne', 11 : 'Na', 12 : 'Mg',
    13 : 'Al', 14 : 'Si', 15 :  'P', 16 :  'S', 17 : 'Cl', 18 : 'Ar',
    19 :  'K', 20 : 'Ca', 21 : 'Sc', 22 : 'Ti', 23 :  'V', 24 : 'Cr',
    25 : 'Mn', 26 : 'Fe', 27 : 'Co', 28 : 'Ni', 29 : 'Cu', 30 : 'Zr',
    31 : 'Ga', 32 : 'Ge', 33 : 'As', 34 : 'Se', 35 : 'Br', 36 : 'Kr',
    37 : 'Rb', 38 : 'Sr', 39 :  'Y', 40 : 'Zr', 41 : 'Nb', 42 : 'Mo',
    43 : 'Tc', 44 : 'Ru', 45 : 'Rh', 46 : 'Pd', 47 : 'Ag', 48 : 'Cd',
    49 : 'In', 50 : 'Sn', 51 : 'Sb', 52 : 'Te', 53 :  'I', 54 : 'Xe',
    55 : 'Cs', 56 : 'Ba', 57 : 'La', 58 : 'Ce', 59 : 'Pr', 60 : 'Nd',
    61 : 'Pm', 62 : 'Sm', 63 : 'Eu', 64 : 'Gd', 65 : 'Tb', 66 : 'Dy',
    67 : 'Ho', 68 : 'Er', 69 : 'Tm', 70 : 'Yb', 71 : 'Lu', 72 : 'Hf',
    73 : 'Ta', 74 :  'W', 75 : 'Re', 76 : 'Os', 77 : 'Ir', 78 : 'Pt',
    79 : 'Au', 80 : 'Hg', 81 : 'Tl', 82 : 'Pb', 83 : 'Bi', 84 : 'Po',
    85 : 'At', 86 : 'Rn', 87 : 'Fr', 88 : 'Ra', 89 : 'Ac', 90 : 'Th',
    91 : 'Pa', 92 :  'U', 93 : 'Np', 94 : 'Pu', 95 : 'Am', 96 : 'Cm',
    97 : 'Bk', 98 : 'Cf', 99 : 'Es', 100: 'Fm', 101: 'Md', 102: 'No',
    103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs',
    109: 'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl',
    115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'
}


class ENSDFParser:

    @staticmethod
    def is_exist(z: int, a: int) -> bool:
        try:
            mass_excess = ENSDFParser.mass_excees(z, a)
            return True
        except:
            return False

    @staticmethod
    def mass_excees(z: int, a: int) -> float:
        file = ENSDFParser.find_file(z)
        name = f'{a}{CHARGE2NAME[z]}'

    @staticmethod
    def states(z: int, a: int) -> list[tuple[float, list[float], list[bool], list[str], float]]:
        file = ENSDFParser.find_file(z)
        name = f'{a}{CHARGE2NAME[z]}'

    @staticmethod
    def discharges(z: int, a: int) -> list[tuple[float, float]]:
        file = ENSDFParser.find_file(z)
        name = f'{a}{CHARGE2NAME[z]}'
    
    @staticmethod
    def find_file(z: int) -> str:
        directory = 'ensdf'

        directories = os.listdir()
        if directory not in directories:
            raise RuntimeError('No downloaded datas from ESNDF.')
        
        name = f'{z}{CHARGE2NAME[z]}.txt'

        files = os.listdir()
        if name not in files:
            raise RuntimeError(f'No downloaded ENSDF files for z={z}')
        
        return directory + '/' + name


if __name__ == '__main__':
    pass
