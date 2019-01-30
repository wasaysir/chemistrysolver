import roman
import re
# It goes:Atomic Symbol: Atomic Number, Element Name, Root, Atomic Weight, Column, Row, Multivalence, *Ionic Charges]

Element = {
         'H': [1, 'Hydrogen', 'hydr', 1, 1, 1, False, 1],
         'He': [2, 'Helium', 'hel', 4, 8, 1, False, 0],
         'Li': [3, 'Lithium', True, 7, 1, 2, False, 1],
         'Be': [4, 'Beryllium', True, 9, 2, 2, False, 2],
         'B': [5, 'Boron', 'bor', 11, 2, 3, False, 3],
         'C': [6, 'Carbon', 'carb', 12, 2, 4, False, 4],
         'N': [7, 'Nitrogen', 'nitr', 14, 2, 5, False, -3],
         'O': [8, 'Oxygen', 'ox', 16, 2, 6, False, -2],
         'F': [9, 'Fluorine', 'fluor', 19, 2, 7, False, -1],
         'Ne': [10, 'Neon', 'ne', 20, 2, 8, False, 0],
         'Na': [11, 'Sodium', True, 23, 3, 1, False, 1],
         'Mg': [12, 'Magnesium', True, 24, 3, 2, False, 2],
         'Al': [13, 'Aluminum', True, 27, 3, 3, False, 3],
         'Si': [14, 'Silicon', True, 28, 3, 4, False, 4],
         'P': [15, 'Phosphorus', 'phosph', 31, 3, 5, False, -3],
         'S': [16, 'Sulfur', 'sulf', 32, 3, 6, False, -2],
         'Cl': [17, 'Chlorine', 'chlor', 35, 3, 7, False, -1],
         'Ar': [18, 'Argon', 'arg', 40, 3, 8, False, 0],
         'K': [19, 'Potassium', True, 39, 4, 1, False, 1],
         'Ca': [20, 'Calcium', True, 40, 4, 2, False, 2],
         'Sc': [21, 'Scandium', True, 45, 4, 9, False, 3],
         'Ti': [22, 'Titanium', True, 48, 4, 9, True, [4, 3]],
         'V': [23, 'Vanadium', True, 51, 4, 9, True, [5, 4]],
         'Cr': [24, 'Chromium', True, 52, 4, 9, True, [3, 2]],
         'Mn': [25, 'Manganese', True, 55, 4, 9, True, [2, 3, 4]],
         'Fe': [26, 'Iron', True, 56, 4, 9, True, [3, 2]],
         'Co': [27, 'Cobalt', True, 59, 4, 9, True, [2, 3]],
         'Ni': [28, 'Nickel', True, 59, 4, 9, True, [2, 3]],
         'Cu': [29, 'Copper', True, 64, 4, 9, True, [2, 1]],
         'Zn': [30, 'Zinc', True, 65, 4, 9, False, 2],
         'Ga': [31, 'Gallium', True, 70, 4, 3, False, 3],
         'Ge': [32, 'Germanium', True, 73, 4, 4, False, 4],
         'As': [33, 'Arsenic', 'arsen', 75, 4, 5, False, -3],
         'Se': [34, 'Selenium', 'selen', 79, 4, 6, False, -2],
         'Br': [35, 'Bromine', 'brom', 80, 4, 7, False, -1],
         'Kr': [36, 'Krypton', 'krypt', 84, 4, 8, False, 0],
         'Rb': [37, 'Rubidium', True, 86, 5, 1, False, 1],
         'Sr': [38, 'Strontium', True, 88, 5, 2, False, 2],
         'Y': [39, 'Yttrium', True, 89, 5, 9, False, 3],
         'Zr': [40, 'Zirconium', True, 91, 5, 9, False, 4],
         'Nb': [41, 'Niobium', True, 93, 5, 9, True, [3, 5]],
         'Mo': [42, 'Molybdenum', True, 96, 5, 9, True, [2, 3]],
         'Tc': [43, 'Technetium', True, 98, 5, 9, False, 7],
         'Ru': [44, 'Ruthenium', True, 101, 5, 9, True, [3, 4]],
         'Rh': [45, 'Rhodium', True, 103, 5, 9, True, [3, 4]],
         'Pd': [46, 'Palladium', True, 106, 5, 9, True, [2, 4]],
         'Ag': [47, 'Silver', True, 108, 5, 9, False, 1],
         'Cd': [48, 'Cadmium', True, 112, 5, 9, False, 2],
         'In': [49, 'Indium', True, 115, 5, 3, False, 3],
         'Sn': [50, 'Tin', True, 119, 5, 4, True, [4, 2]],
         'Sb': [51, 'Antimony', True, 122, 5, 5, True, [3, 5]],
         'Te': [52, 'Tellurium', True, 128, 5, 6, False, -2],
         'I': [53, 'Iodine', True, 127, 5, 7, False, -1],
         'Xe': [54, 'Xenon', True, 131, 5, 8, False, 0],
         'Cs': [55, 'Cesium', True, 133, 6, 1, False, 1],
         'Ba': [56, 'Barium', True, 137, 6, 2, False, 2],
         'La': [57, 'Lanthanum', True, 139, 6, 9, False, 3],
         'Ce': [58, 'Cerium', True, 140, 6, 9, True, [3, 4]],
         'Pr': [59, 'Praseodymium', True, 141, 6, 9, True, [3, 4]],
         'Nd': [60, 'Neodymium', True, 144, 6, 9, False, 3],
         'Pm': [61, 'Promethium', True, 145, 6, 9, False, 3],
         'Sm': [62, 'Samarium', True, 150, 6, 9, True, [3, 4]],
         'Eu': [63, 'Europium', True, 152, 6, 9, True, [3, 2]],
         'Gd': [64, 'Gadolinium', True, 157, 6, 9, False, 3],
         'Tb': [65, 'Terbium', True, 159, 6, 9, True, [3, 4]],
         'Dy': [66, 'Dysprosium', True, 163, 6, 9, False, 3],
         'Ho': [67, 'Holmium', True, 165, 6, 9, False, 3],
         'Er': [68, 'Erbium', True, 167, 6, 9, False, 3],
         'Tm': [69, 'Thulium', True, 169, 6, 9, True, [3, 2]],
         'Yb': [70, 'Ytturbium', True, 173, 6, 9, True, [3, 2]],
         'Lu': [71, 'Lutetium', True, 175, 6, 9, False, 3],
         'Hf': [72, 'Hafnium', True, 179, 6, 9, False, 4],
         'Ta': [73, 'Tantalum', True, 181, 6, 9, False, 5],
         'W': [74, 'Tungsten', True, 184, 6, 9, False, 6],
         'Re': [75, 'Rhenium', True, 186, 6, 9, True, [4, 7]],
         'Os': [76, 'Osmium', True, 190, 6, 9, True, [3, 4]],
         'Ir': [77, 'Iridium', True, 192, 6, 9, True, [3, 4]],
         'Pt': [78, 'Platinum', True, 195, 6, 9, True, [4, 2]],
         'Au': [79, 'Gold', True, 197, 6, 9, True, [3, 1]],
         'Hg': [80, 'Mercury', True, 201, 6, 9, True, [2, 1]],
         'Tl': [81, 'Thalium', True, 204, 6, 3, True, [1, 3]],
         'Pb': [82, 'Lead', True, 207, 6, 4, True, [2, 4]],
         'Bi': [83, 'Bismuth', True, 209, 6, 5, True, [3, 5]],
         'Po': [84, 'Polonium', True, 209, 6, 6, True, [2, 4]],
         'At': [85, 'Astatine', True, 210, 6, 7, False, -1],
         'Rn': [86, 'Radon', True, 222, 6, 8, False, 0],
         'Fr': [87, 'Francium', True, 223, 7, 1, False, 1],
         'Ra': [88, 'Radum', True, 226, 7, 2, False, 2],
         'Ac': [89, 'Actinium', True, 227, 7, 9, False, 3],
         'Th': [90, 'Thorium', True, 232, 7, 9, False, 4],
         'Pa': [91, 'Protactinium', True, 231, 7, 9, True, [5, 4]],
         'U': [92, 'Uranium', True, 238, 7, 9, True, [6, 4, 5]]}

Element_names = {
    'Hydrogen':  'H',
    'hel':  'He',
    'Lithium':  'Li',
    'Beryllium':  'Be',
    'bor':  'B',
    'carb':  'C',
    'nitr':  'N',
    'ox':  'O',
    'fluor':  'F',
    'ne':  'Ne',
    'Sodium':  'Na',
    'Magnesium':  'Mg',
    'Aluminum':  'Al',
    'Silicon':  'Si',
    'phosph':  'P',
    'sulf':  'S',
    'chlor':  'Cl',
    'arg':  'Ar',
    'Potassium':  'K',
    'Calcium':  'Ca',
    'Scandium':  'Sc',
    'Titanium':  'Ti',
    'Vanadium':  'V',
    'Chromium':  'Cr',
    'Manganese':  'Mn',
    'Iron':  'Fe',
    'Cobalt':  'Co',
    'Nickel':  'Ni',
    'Copper':  'Cu',
    'Zinc':  'Zn',
    'Gallium':  'Ga',
    'Germanium':  'Ge',
    'arsen':  'As',
    'selen':  'Se',
    'brom':  'Br',
    'krypt':  'Kr',
    'Rubidium':  'Rb',
    'Strontium':  'Sr',
    'Yttrium':  'Y',
    'Zirconium':  'Zr',
    'Niobium':  'Nb',
    'Molybdenum':  'Mo',
    'Technetium':  'Tc',
    'Ruthenium':  'Ru',
    'Rhodium':  'Rh',
    'Palladium':  'Pd',
    'Silver':  'Ag',
    'Cadmium':  'Cd',
    'Indium':  'In',
    'Tin':  'Sn',
    'Antimony':  'Sb',
    'Tellurium':  'Te',
    'Iodine':  'I',
    'Xenon':  'Xe',
    'Cesium':  'Cs',
    'Barium':  'Ba',
    'Lanthanum':  'La',
    'Cerium':  'Ce',
    'Praseodymium':  'Pr',
    'Neodymium':  'Nd',
    'Promethium':  'Pm',
    'Samarium':  'Sm',
    'Europium':  'Eu',
    'Gadolinium':  'Gd',
    'Terbium':  'Tb',
    'Dysprosium':  'Dy',
    'Holmium':  'Ho',
    'Erbium':  'Er',
    'Thulium':  'Tm',
    'Ytturbium':  'Yb',
    'Lutetium':  'Lu',
    'Hafnium':  'Hf',
    'Tantalum':  'Ta',
    'Tungsten':  'W',
    'Rhenium':  'Re',
    'Osmium':  'Os',
    'Iridium':  'Ir',
    'Platinum':  'Pt',
    'Gold':  'Au',
    'Mercury':  'Hg',
    'Thalium':  'Tl',
    'Lead':  'Pb',
    'Bismuth':  'Bi',
    'Polonium':  'Po',
    'Astatine':  'At',
    'Radon':  'Rn',
    'Francium':  'Fr',
    'Radum':  'Ra',
    'Actinium':  'Ac',
    'Thorium':  'Th',
    'Protactinium':  'Pa',
    'Uranium':  'U'
}

polyatomic_ions = {
    'Ammonium': ['NH4', 1],
    'hydroxide': ['OH', -1],
    'nitrite': ['NO2', -1],
    'nitrate': ['NO3', -1],
    'chlorate': ['ClO3', -1],
    'cyanide': ['CN', -1],
    'carbonate': ['CO3', -2],
    'sulfite': ['SO3', -2],
    'sulfate': ['SO4', -2],
    'bisulfate': ['HSO4', -1],
    'phosphate': ['PO4', -3],
    'bicarbonate': ['HCO3', -1],
    'perchlorate': ['ClO4', -1],
    'chlorate': ['ClO3', -1],
    'chlorite': ['ClO2', -1],
    'hypochlorite': ['ClO', -1],
    'acetate': ['C2H3O2', -1],
    'dichromate': ['Cr2O7', -2],
    'chromate': ['CrO4', -1]
}

polyatomic_formula = {
    "NH4": "Ammonium",
    "OH": "hydroxide",
    "NO2": "nitrite",
    "NO3": "nitrate",
    "ClO3": "chlorate",
    "CN": "cyanide",
    "CO3": "carbonate",
    "SO3": "sulfite",
    "SO4": "sulfate",
    "HSO4": "bisulfate",
    "PO4": "phosphate",
    "HCO3": "bicarbonate",
    "ClO4": "perchlorate",
    "ClO2": "chlorite",
    "ClO": "hypochlorite",
    "C2H3O2": "acetate",
    "Cr2O7": "dichromate",
    "CrO4": "chromate"
}

prefixes = ['mono', 'di', 'tri', 'tetra', 'penta', 'hexa', 'hepta', 'octa']

prefixes_shortened = ['mon', 'di', 'tri', 'tetr', 'pent', 'hex', 'hept', 'oct']

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    if(lcm/x==1):
        if(lcm/y==1):
            return('','')
        return('',int(lcm/y))
    if(lcm/y==1):
        return(int(lcm/x),'')
    return(int(lcm/x),int(lcm/y))


def ionic():
    ionic_choice = str(input('Is it F: Finding a compound from its name or N: Naming a compound \n').upper())
    if (ionic_choice=='F'):
        print(ionic_compound())
        return
    if (ionic_choice=='N'):
        print(ionic_naming())
        return


def ionic_compound():
    compound_name = str(input('What is the name of the compound without any roman numerals?\n'))
    individual_compounds = str.split(compound_name)
    anion = individual_compounds[0]
    cation_ide = individual_compounds[1]
    cation = cation_ide[:-3]
    polyatomic = False
    ammonium_anion = polyatomic_ions.get(anion, False)
    polyatomic_cation = polyatomic_ions.get(cation_ide, False)
    if ammonium_anion or polyatomic_cation:
        polyatomic = True
    if ammonium_anion:
        anion_symbol = polyatomic_ions.get(anion, '')[0]
        anion_multivalence = False
        if not polyatomic_cation:
            cation_symbol = Element_names.get(cation, '')
    if polyatomic_cation:
        if not ammonium_anion:
            anion_symbol = Element_names.get(anion, '')
            anion_multivalence = Element.get(anion_symbol, '')
            anion_multivalence = anion_multivalence[6]
        cation_symbol = polyatomic_ions.get(cation_ide, '')[0]
    if not polyatomic:
        anion_symbol = Element_names.get(anion, '')
        cation_symbol = Element_names.get(cation, '')
        anion_multivalence = Element.get(anion_symbol, '')
        anion_multivalence = anion_multivalence[6]
    if anion_multivalence:
        roman_numerals = str(input('What is the roman numeral attached to the anion? \n'))
        anion_charge = roman.fromRoman(roman_numerals)
        if polyatomic:
            cation_charge = abs(polyatomic_ions.get(cation_ide, '')[1])
        else:
            cation_charge = abs(Element.get(cation_symbol,'')[7])
        atoms_needed = lcm(anion_charge,cation_charge)
        atoms_needed = [str(atoms_needed[0]),str(atoms_needed[1])]
        if polyatomic:
            chemical_formula=str(anion_symbol)+atoms_needed[0]+'('+str(cation_symbol)+')'+atoms_needed[1]
        else:
            chemical_formula=str(anion_symbol)+atoms_needed[0]+str(cation_symbol)+atoms_needed[1]
        #Changing Subscripts Format
        return chemical_formula.replace('0','\u2080').replace('1','\u2081').replace('2','\u2082').replace('3','\u2083').replace('4','\u2084').replace('5','\u2085').replace('6','\u2086').replace('7','\u2087').replace('8','\u2088').replace('9','\u2089')
    else:
        if polyatomic :
            if ammonium_anion:
                anion_charge=1
            else:
                anion_charge=abs(Element.get(anion_symbol,'')[7])
            if polyatomic_cation:
                cation_charge=abs(polyatomic_ions.get(cation_ide,'')[1])
            else:
                cation_charge=abs(Element.get(cation_symbol,'')[7])
            atoms_needed=lcm(anion_charge,cation_charge)
            atoms_needed=[str(atoms_needed[0]),str(atoms_needed[1])]
            if ammonium_anion:
                if polyatomic_cation:
                    chemical_formula='('+str(anion_symbol)+')'+atoms_needed[0]+'('+str(cation_symbol)+')'+atoms_needed[1]
                else:
                    chemical_formula='('+str(anion_symbol)+')'+atoms_needed[0]+str(cation_symbol)+atoms_needed[1]
            else:
                chemical_formula=str(anion_symbol)+atoms_needed[0]+'('+str(cation_symbol)+')'+atoms_needed[1]
            #Changing Subscripts Format
            return chemical_formula.replace('0','\u2080').replace('1','\u2081').replace('2','\u2082').replace('3','\u2083').replace('4','\u2084').replace('5','\u2085').replace('6','\u2086').replace('7','\u2087').replace('8','\u2088').replace('9','\u2089')
        else:
            anion_charge=abs(Element.get(anion_symbol,'')[7])
            cation_charge=abs(Element.get(cation_symbol,'')[7])
            atoms_needed=lcm(anion_charge,cation_charge)
            atoms_needed=[str(atoms_needed[0]),str(atoms_needed[1])]
            chemical_formula=str(anion_symbol)+atoms_needed[0]+str(cation_symbol)+atoms_needed[1]
            #Changing Subscripts Format
            return chemical_formula.replace('0','\u2080').replace('1','\u2081').replace('2','\u2082').replace('3','\u2083').replace('4','\u2084').replace('5','\u2085').replace('6','\u2086').replace('7','\u2087').replace('8','\u2088').replace('9','\u2089')


def ionic_naming():
    polyatomic=False
    compound=str(input('What is the chemical formula for the compound ('
                       'with brackets around polyatomic ions and for subscripts just place the number) \n'))
    if '(' in compound:
        polyatomic=True
    if not polyatomic:
        chemicals = re.sub(r"[^A-Za-z]+", '', compound)
        split_compound = re.findall('[A-Z][^A-Z]*', chemicals)
        cation = Element.get(split_compound[1], '')
        anion_multivalence = Element.get(split_compound[0], '')[6]
        cation = cation[2]
        cation_ide = cation + 'ide'
        anion = Element.get(split_compound[0], '')[1]
        if not anion_multivalence:
            compound_name = anion + ' ' + cation_ide
            return compound_name
        else:
            different_elements = re.findall('[A-Z][^A-Z]*', compound)
            subscripts_array = [0, 1]
            for i in range(0,2):
                subscripts_array[i] = re.sub("\D", '', different_elements[i])
                if subscripts_array[i] == '':
                    subscripts_array[i] = 1
                else:
                    subscripts_array[i] = int(subscripts_array[i])
            cation_charge = abs(int(Element.get(split_compound[1], '')[7]))
            anion_charge = int((cation_charge*subscripts_array[1])/subscripts_array[0])
            roman_translation = roman.toRoman(anion_charge)
            compound_name = anion + ' (' + roman_translation + ') ' + cation_ide
            return compound_name

    if polyatomic:
        component_one = compound.split(')')[0]
        if(compound[0] == '('):
            anion = 'Ammonium'
            component_two = compound.split(')')[1]
            component_two = re.sub(r"[^A-Za-z]+", '', component_two)
            cation = Element.get(component_two, '')[2]
            cation_ide = cation + 'ide'
            return anion + ' ' + cation_ide
        else:
            component_two = compound.split('(')[0]
            anion_symbol = re.sub(r"[^A-Za-z]+", '', component_two)
            anion = Element.get(anion_symbol, '')
            anion_name = anion[1]
            anion_multivalence = anion[6]
            component_one = component_one.split('(')[1]
            polyatomic_ion = polyatomic_formula.get(component_one, '')
            cation = polyatomic_ion
            if anion_multivalence:
                cation_charge = polyatomic_ions.get(cation, '')[1]
                if compound[-1] == ')':
                    cation_subscript = 1
                else:
                    cation_subscript = compound.split(')')[1]
                    cation_subscript = re.sub("\D", "", cation_subscript)
                    if not cation_subscript == '':
                        cation_subscript = int(cation_subscript)
                    else:
                        cation_subscript = 1
                anion_subscript = re.sub("\D", "", component_two)
                if not anion_subscript == '':
                    anion_subscript = int(anion_subscript)
                else:
                    anion_subscript = 1
                anion_charge = abs(int((cation_charge * cation_subscript) / anion_subscript))
                roman_translation = roman.toRoman(anion_charge)
                compound_name = anion_name + ' (' + roman_translation + ') ' + cation
                return compound_name
            else:
                return anion_name + ' ' + cation


def covalent():
    problemkey = str(input('Is the problem either covalent [N]aming or writing the [F]ormulas? \n')).upper()
    if problemkey == 'N':
        print(covalent_naming())
    if problemkey == 'F':
        print(covalent_compound())


def covalent_compound():
    compound = str(input('What is the formula of the compound? \n'))
    chemicals = re.sub(r"[^A-Za-z]+", '', compound)
    split_compound = re.findall("[A-Z][^A-Z]*", chemicals)
    first_element_name = Element.get(split_compound[0], '')[1]
    second_element_name = Element.get(split_compound[1], '')[2].lower()
    different_elements = re.findall('[A-Z][^A-Z]*', compound)
    subscripts_array = ['', '']
    for i in range(0, 2):
        subscripts_array[i] = re.sub("\D", "", different_elements[i])
        if subscripts_array[i] == '':
            subscripts_array[i] = 1
        else:
            subscripts_array[i] = int(subscripts_array[i])
    if first_element_name[0].lower() in "aeiou":
        first_element_subscript = prefixes_shortened[int(subscripts_array[0])-1]
    else:
        first_element_subscript = prefixes[int(subscripts_array[0])-1]
    if second_element_name[0].lower() in "aeiou":
        second_element_subscript = prefixes_shortened[int(subscripts_array[1])-1]
    else:
        second_element_subscript = prefixes[int(subscripts_array[1])-1]
    if(subscripts_array[0] == 1):
        compound_name = first_element_name + ' ' + second_element_subscript + second_element_name
    else:
        compound_name = first_element_subscript.capitalize() + (first_element_name.lower()) + ' ' + second_element_subscript + second_element_name + 'ide'
    return compound_name


def covalent_naming():
    compound = str(input('What is the name of the compound? \n'))
    chemical = compound.split()
    chemical_1_full = chemical[0].lower()
    chemical_1_short = chemical[0].lower()
    chemical_2_full = chemical[1].lower()
    chemical_2_short = chemical[1].lower()
    element_1_subscript = 1
    element_2_subscript = 1
    for j in range(len(prefixes)):
        i = prefixes[j]
        prefix_length = len(i)
        if i in chemical_1_full[0:prefix_length]:
            chemical_1_full = chemical_1_full[prefix_length:]
            element_1_subscript = j+1
        if i in chemical_2_full[0:prefix_length]:
            chemical_2_full = chemical_2_full[prefix_length:]
            element_2_subscript = j+1
    for j in range(len(prefixes_shortened)):
        i = prefixes_shortened[j]
        prefix_length = len(i)
        if i in chemical_1_short[0:prefix_length]:
            chemical_1_short = chemical_1_short[prefix_length:]
            element_1_subscript = j+1
        if i in chemical_2_short[0:prefix_length]:
            chemical_2_short = chemical_2_short[prefix_length:]
            element_2_subscript = j+1
    second_element_name = chemical_2_full[:-3]
    second_element_name_short = chemical_2_short[:-3]
    first_element_name = Element_names.get(chemical_1_full.capitalize(), '')
    second_element_name = Element_names.get(second_element_name, '')
    first_element_name_short = Element_names.get(chemical_1_short.capitalize(), '')
    second_element_name_short = Element_names.get(second_element_name_short, '')
    if not first_element_name == '':
        first_element = first_element_name
    else:
        first_element = first_element_name_short

    if not second_element_name == '':
        second_element = second_element_name
    else:
        second_element = second_element_name_short
    if element_1_subscript == 1:
        if element_2_subscript ==1:
            compound_formula = first_element + second_element + str(element_2_subscript)
        else:
            compound_formula = first_element + second_element
    else:
        if element_2_subscript==1:
            compound_formula = first_element + str(element_1_subscript) + second_element
        else:
            compound_formula = first_element + str(element_1_subscript) + second_element + str(element_2_subscript)
    return compound_formula.replace('0','\u2080').replace('1','\u2081').replace('2','\u2082').replace('3','\u2083').replace('4','\u2084').replace('5','\u2085').replace('6','\u2086').replace('7','\u2087').replace('8','\u2088').replace('9','\u2089')



def pH():
    compound = str(input('[N]aming or [F]ormula? \n')).upper()
    if compound == 'F':
        pH_formula()
    if compound == 'N':
        ph_naming()

def pH_formula():
    compound_naming = str(input('What is the compound name? \n'))
    base = False
    acid = False
    binary = False
    oxyacid = False
    if 'OH' in compound_naming:
        base = True
    else:
        acid = True
    if acid:
        if 'O' in compound_naming:
            oxyacid = True
        else:
            binary = True
    if binary:
        acid = re.sub(r"[^A-Za-z]+", '', compound_naming)
        acid.replace('(', '').replace(')', '')
        acid = re.sub(r"H", '', acid)
        polyatomic_ion = polyatomic_formula.get(acid, '')
        element = Element.get(acid, '')[2]
        cation = ''
        if polyatomic_ion == '':
            cation = element
        else:
            cation = polyatomic_ion
        if cation[-3:] == 'ide':
            compound_name = 'Hydro' + cation[:-3] + 'ic acid'
        else:
            compound_name = 'Hydro' + cation + 'ic acid'
    if oxyacid:
        try:
            acid = compound_naming.split('(')[1]
            acid = acid.split(')')[0]
        except:
            acid = compound_naming[1:]
            while acid[0].isdigit():
                acid = acid[1:]
        polyatomic_ion = polyatomic_formula.get(acid, '')
        if polyatomic_ion[-3:] == 'ate':
            polyatomic_ion = polyatomic_ion[:-3] + 'ic'
        elif polyatomic_ion[-3:] == 'ite':
            polyatomic_ion = polyatomic_ion[:-3] + 'ous'
        compound_name = polyatomic_ion.capitalize() + ' acid'
    if base:
        base = re.sub(r"[^A-Za-z]+", '', compound_naming)
        base.replace('(', '').replace(')', '')
        base = re.sub(r"OH", '', base)
        base_name = Element.get(base, '')[1]
        compound_name = base_name + ' hydroxide'
    return compound_name


def pH_naming():
    compound_name = str(input('What is the name of the compound? If multivalent do not add the roman numerals\n'))
    acid = False
    if compound_name[-4:] == 'acid':
        acid = True
    element_name = compound_name.split()[0]
    if acid:
        if element_name[:5] == 'Hydro':
            element_name = element_name[5:-2]
            element = Element_names.get(element_name, '')
            element_charge = abs(Element.get(element, '')[7])
            if element_charge == 1:
                compound_formula = 'H' + element
            else:
                compound_formula = 'H' + element
            return compound_formula
        else:
            if element_name[-2:] == 'ic':
                element_name = element_name[:-2].lower() + 'ate'
            else:
                element_name = element_name[:-3].lower() + 'ite'
            polyatomic_ion_info = polyatomic_ions.get(element_name, '')
            polyatomic_ion_formula = polyatomic_ion_info[0]
            polyatomic_ion_charge = abs(polyatomic_ion_info[1])
            if polyatomic_ion_charge == 1:
                compound_formula = 'H' + polyatomic_ion_formula
            else:
                compound_formula = 'H' + str(polyatomic_ion_charge) + polyatomic_ion_formula

    else:
        base_name = compound_name.split()[0]
        roman_numerals = str(input('If there ar roman numerals put them here or else put n \n')).upper()
        Element_name = Element_names.get(base_name, '')
        if roman_numerals == 'N':
            Element_charge = Element.get(Element_name, '')[7]
            Element_charge = Element.get(Element_name, '')[7]
        else:
            Element_charge = roman.fromRoman(roman_numerals)
        if Element_charge == 1:
            compound_formula = Element_name + 'OH'
        else:
            compound_formula = Element_name + '(OH)' + str(Element_charge)

    return compound_formula.replace('0', '\u2080').replace('1', '\u2081').replace('2', '\u2082').replace('3', '\u2083').replace('4', '\u2084').replace('5', '\u2085').replace('6', '\u2086').replace('7', '\u2087').replace('8', '\u2088').replace('9', '\u2089')

def main():
    print("Booted up")
    print("What seems to be the problem today?")
    problemkey = str(input("Press the key for the problem you have: \n [A]cids and Bases/pH \n [C]ovalent Bonds \n [E]quation \n [I]onic Charge \n [R]eaction \n [U]nknown \n")).upper()
    if problemkey == 'A':
        pH()
    if(problemkey=='C'):
        covalent()
    if(problemkey=='E'):
        equation()
    if(problemkey=='I'):
        ionic()
    if(problemkey=='R'):
        reaction()
    if(problemkey=='U'):
        problemtype()

print(pH_naming())