from colorama import Back, Fore, Style
import unicodedata

x = input(
    f"{Style.BRIGHT}Ukrainian Noun Declensor {Style.NORMAL}by rainbowpawsies \n"
    f"{Style.NORMAL}{Fore.RED}NB!{Fore.RESET}This tool is currently in alpha, and it does not account for many exeptions. \n For further notes and help, type {Style.BRIGHT}help{Style.NORMAL}\n"
    f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}"
)

# The four words that would be exceptions for the third declension type
type_3_exceptions = ['кров', 'любов', 'ніч', 'піч']
masculine_exceptions = ['тато', 'дядько', 'суддя', 'дідько']
vowels = ['а', 'е', 'є', 'и', 'і', 'о', 'у', 'ю', 'я']

# Deafault cases
nominative = ""
genitive = ""
dative = ""
accusative = ""
instrumental = ""
locative = ""
vocative = ""

def remove_first_vowel(x):
    vowels = "ауеєиіїоуюя"
    for i, char in enumerate(x):
        if char in vowels:
            return x[:i] + x[i+1:]
    return x  # Return the original word if no vowels are found

# Checking for correct script usage
def check_for_script(x):
    for char in x:
        if unicodedata.name(char).startswith('CYRILLIC'):
            continue
        else:
            return False
    return True

# Determining the gender of the noun
def gender(x):
    if x[-1:] == 'а' or x[-1:] == 'я' or x[-4:] == 'ість':
        return 'feminine'
    elif (x[-1:] not in vowels) or (x in masculine_exceptions):
        return 'masculine'
    elif (x[-1:] == 'о' and x not in masculine_exceptions) or x[-1:] == 'е' or (x[-1] == 'я' and len(x) >= 3 and x[-2] == x[-3]):
        return 'neuter'    
    else:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Rainbow. {Back.RESET}{Fore.RESET}\n")
        return None


# Determining declension type
def declension_type(x):
    if (gender(x) in ['feminine', 'masculine'] and x[-1:] not in ['а', 'я']) or (gender(x) == 'neuter' and x[-2:] == 'ще'):
        return "II" # Second declension type
    elif (x[-4:] == 'ість') or (x[-2:] == "'я") or (x in type_3_exceptions):
        return "III"  # Third declension type
    elif x[-1:] == 'а' or x[-1:] == 'я':
        return "I" # First declension type
    else:
        return "IV" # Fourth declension type
    
def declension_type1(x):
    global nominative, genitive, dative, accusative, instrumental, locative, vocative
    nominative = x
    # Subtype determination
    if x[-1] in ['я','ю','є','ї','ь']: # Any of the soft subtypes
        if x[-2] in vowels: # Soft II
            genitive = x[:-1] + 'ї'; dative = x[:-1] + 'ї'; accusative = x[:-1] + 'ю'; instrumental = x[:-1] + 'єю'; locative = x[:-1] + 'ї'; vocative = x[:-1] + 'є'
        else: # Soft I
            genitive = x[:-1] + 'і'; dative = x[:-1] + 'і'; accusative = x[:-1] + 'ю'; instrumental = x[:-1] + 'ею'; locative = x[:-1] + 'і'; vocative = x[:-1] + 'е'
    elif x [-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
        genitive = x[:-1] + 'і'; dative = x[:-1] + 'і'; accusative = x[:-1] + 'у'; instrumental = x[:-1] + 'ею'; locative = x[:-1] + 'і'; vocative = x[:-1] + 'є'
    else: # Hard subtype
        genitive = x[:-1] + 'и'; dative = x[:-1] + 'і'; accusative = x[:-1] + 'у'; instrumental = x[:-1] + 'ою'; locative = x[:-1] + 'і'; vocative = x[:-1] + 'о'

def ask_type2_category():
    response = input(
        f"{Style.NORMAL}The noun is of declension type II! We will need to know a bit more... \n"
        f"{Style.BRIGHT}Do you consider this noun to fall under one of these categories:{Style.NORMAL} \n"
        f"names of persons and beings:{Style.DIM} applicant, horse, mosquito, Dmitry, {Style.NORMAL}\n" 
        f"names of specific objects that can be counted:{Style.DIM} notebook, knife, pencil,{Style.NORMAL}\n"
        f"proper names of settlements:{Style.DIM} Uzhhorod, Ternopil,{Style.NORMAL}\n"
        f"names of water bodies with a stressed ending:{Style.DIM} Dnieper, Donets,{Style.NORMAL}\n"
        f"names of length, area, weight, volume, time intervals:{Style.DIM} meter, gram, week (but also year, age),{Style.NORMAL}\n"
        f"nouns-terms:{Style.DIM} atom, square, case {Style.NORMAL}\n"
        f"names of buildings and their parts:{Style.DIM} greenhouse, corridor, garage.{Style.NORMAL}\n"
        f"{Style.BRIGHT}Type 'yes' if the noun fits any category, otherwise type 'no': {Style.NORMAL}"
    ).lower()
    return response == "yes"

def declension_type2_logic(x, is_a_category):
    global nominative, genitive, dative, accusative, instrumental, locative, vocative
    nominative = x
    if is_a_category:
        if x[-1] in ['й','ь']: # Any of the soft subtypes
            if x[-1] == 'й': # Soft II
                genitive = x[:-1] + 'ю'; dative = x[:-1] + 'ю'; accusative = x; instrumental = x[:-1] + 'єм'; locative = x[:-1] + 'ю'; vocative = x[:-1] + 'ю'
            else: # Soft I
                genitive = (remove_first_vowel(x))[:-1] + 'я' ; dative = (remove_first_vowel(x))[:-1] + 'ю'; accusative = x; instrumental = (remove_first_vowel(x))[:-1] + 'ем'; locative = (remove_first_vowel(x))[:-1] + 'ю'; vocative = x
        elif x[-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
            genitive = x + 'а'; dative = x + 'у'; accusative = x; instrumental = x + 'ем'; locative = x + 'і'; vocative = x
        else: # Hard subtype
            genitive = x + 'а'; dative = x + 'у'; accusative = x; instrumental = x + 'ом'; locative = x + 'у'; vocative = x + 'е'
    else:
        if x[-1] in ['й','ь']: # Any of the soft subtypes
            if x[-1] == 'й': # Soft II
                genitive = x[:-1] + 'ю'; dative = x[:-1] + 'ю'; accusative = x; instrumental = x[:-1] + 'єм'; locative = x[:-1] + 'ю'; vocative = x[:-1] + 'ю'
            else: # Soft I
                genitive = (remove_first_vowel(x))[:-1] + 'я' ; dative = (remove_first_vowel(x))[:-1] + 'ю'; accusative = x; instrumental = (remove_first_vowel(x))[:-1] + 'ем'; locative = (remove_first_vowel(x))[:-1] + 'ю'; vocative = x
        elif x[-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
            genitive = x + 'у'; dative = x + 'у'; accusative = x; instrumental = x + 'ем'; locative = x + 'і'; vocative = x
        else: # Hard subtype
            genitive = x + 'у'; dative = x + 'у'; accusative = x + "а"; instrumental = x + 'ом'; locative = x + 'у'; vocative = x + 'у'

def declension_type2(x):
    is_a_category = ask_type2_category()
    declension_type2_logic(x, is_a_category)

def declension_type3(x):
    global nominative, genitive, dative, accusative, instrumental, locative, vocative
    nominative = x
    # Subtype determination
    if x[-1] in ['я','ю','є','ї','ь']: # Any of the soft subtypes
        if x[-2] in vowels: # Soft II
            genitive = x[:-1] + 'ї'; dative = x[:-1] + 'ї'; accusative = x[:-1] + 'ю'; instrumental = x[:-1] + 'єю'; locative = x[:-1] + 'ї'; vocative = x[:-1] + 'є'
        else: # Soft I
            genitive = x[:-1] + 'і'; dative = x[:-1] + 'і'; accusative = x[:-1] + 'ю'; instrumental = x[:-1] + 'ею'; locative = x[:-1] + 'і'; vocative = x[:-1] + 'е'
    elif x == 'мати': # Exception
        genitive = 'матері'; dative = 'матері'; accusative = 'матір'; instrumental = "матір'ю"; locative = 'матері'; x[:-1] + 'мати, мамо, матінко'
   
def declension_type4(x):
    global nominative, genitive, dative, accusative, instrumental, locative, vocative
    nominative = x
    # Subtype determination
    if x[-1] == "'я": # The 'ije' words in Proto-Slavic
        genitive = x[:-2] + 'ені' if x != "сім'я" else x[:-1] + 'ї'; dative = x[:-2] + 'ені'; accusative = x; instrumental = x[:-2] + 'енем'; locative = x[:-2] + 'ені'; vocative = x
    elif x[-1] == 'а' or x[-1] == 'я': # Ending in 'а' or 'я'
        genitive = x + 'ти'; dative = 'ті'; accusative = x; instrumental = x + 'м'; locative = x + 'ті'; vocative = x

# Printing the results
is_cyrillic = check_for_script(x)
while not is_cyrillic or len(x) < 2 or x == "621" or x == "help":
    if x == "621":
        print(f"{Back.RED}{Fore.WHITE}ABORTED.{Back.RESET}{Fore.RESET}\n (You have exited the program).")
        break
    elif x == "help":
        print(
            f"{Style.NORMAL}{Back.MAGENTA}{Fore.WHITE}==== HELP MENU ===={Back.RESET}{Fore.RESET} \n"
            f"{Style.DIM}Ukrainian Noun Declensor v. Alpha 0.10.27.1 from October 27, 2025{Style.NORMAL}\n"
            f"— To use this tool, simply enter a Ukrainian noun in Cyrillic script. \n"
            f"— The program will determine the gender and the declension type of the noun. \n"
            f"— To exit the program, type '621' and press Enter. \n")
        x = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
    elif not is_cyrillic:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Carrot. {Back.RESET}{Fore.RESET}\n (Please enter a word in Cyrillic script).")
        x = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(x)
    elif len(x) < 2:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Shorty. {Back.RESET}{Fore.RESET}\n (Please enter a noun with at least 2 letters).")
        x = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(x)
else:
    while gender(x) is None:
        x = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(x)
        if not is_cyrillic or len(x) < 2 or x == "621" or x == "help":
            break
    if declension_type(x) == "I":
        declension_type1(x)
    elif declension_type(x) == "II":
        declension_type2(x)
    elif declension_type(x) == "III":
        declension_type3(x)
    elif declension_type(x) == "IV":
        declension_type4(x)
    else:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Riverside. {Back.RESET}{Fore.RESET}\n (No declension type selected).")
        x = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(x)
    print(
        f"{Style.NORMAL}==== WORD: {x} ==== \n"
        f"— Gender: {gender(x)}\n"
        f"==== DECLENSION TYPE {declension_type(x)} ==== \n"
        f"Nominative (Називний): {nominative}\n Genetive (Родовий): {genitive}\n Dative (Давальний): {dative}\n Accusative (Звинувальний): {accusative}\n Instrumental (Орудний): {instrumental}\n Locative (Місцевий): {locative}\n Vocative (Кличний): {vocative}\n")