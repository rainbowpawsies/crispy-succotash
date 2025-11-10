from colorama import Back, Fore, Style

#Asking the user to input.
word = input(
    f"{Style.BRIGHT}Ukrainian Noun Declensor {Style.NORMAL}by rainbowpawsies \n"
    f"{Style.NORMAL}{Fore.RED}NB!{Fore.RESET}This tool is currently in alpha, and it does not account for many exeptions. \n For further notes and help, type {Style.BRIGHT}help{Style.NORMAL}\n"
    f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}"
)

# The four words that would be exceptions for the third declension type
type_3_exceptions = ['кров', 'любов', 'ніч', 'піч']
masculine_exceptions = ['тато', 'дядько', 'суддя', 'дідько']
vowels = ['а', 'е', 'є', 'и', 'і', 'о', 'у', 'ю', 'я']

# Deafault cases. Declaration in the beginning is to later use the functions as global.
# Nominative declaration happens here, unlike for other cases.
nominative = word
genitive = ""
dative = ""
accusative = ""
instrumental = ""
locative = ""
vocative = ""

# A function to remove the first vowel from a word.
def remove_first_vowel(word):
    vowels = "ауеєиіїоуюя"
    for i, char in enumerate(word):
        if char in vowels:
            return word[:i] + word[i+1:]
    return word  # Return the original word if no vowels are found

# A function to soften the last consonant of a word if applicable.
# This is used in declenstion type I, both hard and mixed subtypes.
def consonant_softening(word):
    softening_map = {
        'д': 'дж',
        'т': 'ч',
        'з': 'ж',
        'с': 'ш',
        'л': 'ль',
        'н': 'нь',
        'р': 'рь',
        'к': 'ц',
        'г': 'ж',
        'х': 'ш'
    }
    if word[-1] in softening_map:
        return word[:-1] + softening_map[word[-1]]
    else:
        return word

# Checking for correct script usage
def check_for_script(word):
    for char in word:
        if char in "йцукенгшщзхїєждлорпавіфячсмитьбюґЙЦУКЕНГШЩЗХЇЄЖДЛОРПАВІФЯЧСМИТЬБЮҐ'":
            continue
        else:
            return False
    return True

# Determining the gender of the noun
def gender(word):
    if word[-1:] == 'а' or word[-1:] == 'я' or word[-4:] == 'ість':
        return 'feminine'
    elif (word[-1:] not in vowels) or (word in masculine_exceptions):
        return 'masculine'
    elif (word[-1:] == 'о' and word not in masculine_exceptions) or word[-1:] == 'е' or (word[-1] == 'я' and len(word) >= 3 and word[-2] == word[-3]):
        return 'neuter'    
    else:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Rainbow. {Back.RESET}{Fore.RESET}\n Check if your word is in singular form.")
        return None

# Determining declension type to futher proceed with declension
def declension_type(word):
    if (gender(word) in ['feminine', 'masculine'] and word[-1:] not in ['а', 'я']) or (gender(word) == 'neuter' and word[-2:] == 'ще'):
        return "II" # Second declension type
    elif (word[-4:] == 'ість') or (word[-2:] == "'я") or (word in type_3_exceptions):
        return "III"  # Third declension type
    elif word[-1:] == 'а' or word[-1:] == 'я':
        return "I" # First declension type
    else:
        return "IV" # Fourth declension type
    
# The declension function for type I
def declension_type1(word):
    global genitive, dative, accusative, instrumental, locative, vocative
    # Subtype determination
    if word[-1] in ['я','ю','є','ї','ь']: # Any of the soft subtypes
        if word[-2] in vowels: # Soft II
            genitive = word[:-1] + 'ї'; 
            dative = word[:-1] + 'ї'; 
            accusative = word[:-1] + 'ю'; 
            instrumental = word[:-1] + 'єю'; 
            locative = word[:-1] + 'ї'; 
            vocative = word[:-1] + 'є'
        else: # Soft I
            genitive = word[:-1] + 'і'; 
            dative = word[:-1] + 'і'; 
            accusative = word[:-1] + 'ю'; 
            instrumental = word[:-1] + 'ею'; 
            locative = word[:-1] + 'і'; 
            vocative = word[:-1] + 'е'
    elif word [-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
        genitive = word[:-1] + 'і'; 
        dative = consonant_softening(word[:-1]) + 'і'; 
        accusative = word[:-1] + 'у'; 
        instrumental = word[:-1] + 'ею'; 
        locative = consonant_softening(word[:-1]) + 'і'; 
        vocative = word[:-1] + 'є'
    else: # Hard subtype
        genitive = word[:-1] + 'и'; 
        dative = consonant_softening(word[:-1]) + 'і'; 
        accusative = word[:-1] + 'у'; 
        instrumental = word[:-1] + 'ою'; 
        locative = consonant_softening(word[:-1]) + 'і'; 
        vocative = word[:-1] + 'о'

# Asking the user about the meaning category of the noun for declension type II.
# This is required since unlike other declension types, type II has different endings based on the meaning of the noun, and not only on its ending.
def ask_type2_category():
    response = input(
        f"{Style.NORMAL}The noun is of declension type II! We will need to know a bit more... \n"
        f"{Style.BRIGHT}Do you consider this noun to fall under one of these categories:{Style.NORMAL} \n"
        f"names of persons and beings:{Style.DIM} applicant, кінь, комар, Дмитро, {Style.NORMAL}\n" 
        f"names of specific objects that can be counted:{Style.DIM} зошит, ніж, олівець,{Style.NORMAL}\n"
        f"proper names of settlements:{Style.DIM} Ужгород, Тернопіль,{Style.NORMAL}\n"
        f"names of water bodies with a stressed ending:{Style.DIM} Дніпро, Донець{Style.NORMAL}\n"
        f"names of length, area, weight, volume, time intervals:{Style.DIM} метр, грам, тиждень (but also рік, вік),{Style.NORMAL}\n"
        f"nouns-terms:{Style.DIM} атом, квадрат, відмінок {Style.NORMAL}\n"
        f"names of buildings and their parts:{Style.DIM} коридор, гараж.{Style.NORMAL}\n"
        f"{Style.BRIGHT}Type 'yes' if the noun fits any category, otherwise type 'no': {Style.NORMAL}"
    )
    if response in {'yes', 'Yes', 'YES', 'так', 'Так', 'ТАК'}:
        return True
    elif response in {'no', 'No', 'NO', 'ні', 'Ні', 'НІ'}:
        return False
    else:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Echo. {Back.RESET}{Fore.RESET}\n (Please answer with 'yes' or 'no'. This can be in Ukrainian as well.)")
        return ask_type2_category()

# The declension logic for type II. It is separated from the main function to allow easier testing.
def declension_type2_logic(word, is_a_category):
    global genitive, dative, accusative, instrumental, locative, vocative
    if is_a_category:
        if word[-1] in ['й','ь']: # Any of the soft subtypes
            if word[-1] == 'й': # Soft II
                genitive = word[:-1] + 'ю'; 
                dative = word[:-1] + 'ю'; 
                accusative = word; 
                instrumental = word[:-1] + 'єм'; 
                locative = word[:-1] + 'ю'; 
                vocative = word[:-1] + 'ю'
            else: # Soft I
                genitive = (remove_first_vowel(word))[:-1] + 'я' ; 
                dative = (remove_first_vowel(word))[:-1] + 'ю'; 
                accusative = word; 
                instrumental = (remove_first_vowel(word))[:-1] + 'ем'; 
                locative = (remove_first_vowel(word))[:-1] + 'ю'; 
                vocative = word
        elif word[-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
            genitive = word + 'а'; 
            dative = word + 'у';
            accusative = word; 
            instrumental = word + 'ем'; 
            locative = word + 'і'; 
            vocative = word
        else: # Hard subtype
            genitive = remove_first_vowel(word) + 'а'; 
            dative = remove_first_vowel(word) + 'у'; 
            accusative = word; 
            instrumental = word + 'ом'; 
            locative = remove_first_vowel(word) + 'у'; 
            vocative = word + 'е'
    else:
        if word[-1] in ['й','ь']: # Any of the soft subtypes
            if word[-1] == 'й': # Soft II
                genitive = word[:-1] + 'ю'; 
                dative = word[:-1] + 'ю'; 
                accusative = word; 
                instrumental = word[:-1] + 'єм'; 
                locative = word[:-1] + 'ю'; 
                vocative = word[:-1] + 'ю'
            else: # Soft I
                genitive = (remove_first_vowel(word))[:-1] + 'я' ; 
                dative = (remove_first_vowel(word))[:-1] + 'ю'; 
                accusative = word; 
                instrumental = (remove_first_vowel(word))[:-1] + 'ем'; 
                locative = (remove_first_vowel(word))[:-1] + 'ю'; 
                vocative = word
        elif word[-2] in ['ш', 'ж', 'ч', 'щ', 'ц']: # Mixed subtype
            genitive = word + 'у'; 
            dative = word + 'у';
            accusative = word; 
            instrumental = word + 'ем'; 
            locative = word + 'і'; 
            vocative = word
        else: # Hard subtype
            genitive = word + 'у'; 
            dative = word + 'у'; 
            accusative = word + "а"; 
            instrumental = word + 'ом'; 
            locative = word + 'у'; 
            vocative = word + 'у'

# The combined function for declension type II
def declension_type2(word):
    is_a_category = ask_type2_category()
    declension_type2_logic(word, is_a_category)

# The declension function for type III
def declension_type3(word):
    global genitive, dative, accusative, instrumental, locative, vocative
    # Subtype determination
    if word[-1] in ['я','ю','є','ї','ь']: # Any of the soft subtypes
        if word[-2] in vowels: # Soft II
            genitive = word[:-1] + 'ї'; 
            dative = word[:-1] + 'ї'; 
            accusative = word[:-1] + 'ю'; 
            instrumental = word[:-1] + 'єю'; 
            locative = word[:-1] + 'ї'; 
            vocative = word[:-1] + 'є'
        else: # Soft I
            genitive = word[:-1] + 'і'; 
            dative = word[:-1] + 'і'; 
            accusative = word[:-1] + 'ю'; 
            instrumental = word[:-1] + 'ею'; 
            locative = word[:-1] + 'і'; 
            vocative = word[:-1] + 'е'
    elif word == 'мати': # Exception
        genitive = 'матері'; 
        dative = 'матері'; 
        accusative = 'матір'; 
        instrumental = "матір'ю"; 
        locative = 'матері'; 
        word[:-1] + 'мати, мамо, матінко'
   
# The declension function for type IV
def declension_type4(word):
    global genitive, dative, accusative, instrumental, locative, vocative
    # Subtype determination
    if word[-1] == "'я": # The 'ije' words in Proto-Slavic
        genitive = word[:-2] + 'ені' if word != "сім'я" else word[:-1] + 'ї'; 
        dative = word[:-2] + 'ені'; 
        accusative = word; 
        instrumental = word[:-2] + 'енем'; 
        locative = word[:-2] + 'ені'; 
        vocative = word
    elif word[-1] == 'а' or word[-1] == 'я': # Ending in 'а' or 'я'
        genitive = word + 'ти'; 
        dative = 'ті'; 
        accusative = word; 
        instrumental = word + 'м'; 
        locative = word + 'ті'; 
        vocative = word

# Printing the results. This is the actual part of the code.
is_cyrillic = check_for_script(word)
while not is_cyrillic or len(word) < 2 or word == "6" or word == "help":
    if word == "6":
        print(f"{Back.RED}{Fore.WHITE}ABORTED.{Back.RESET}{Fore.RESET}\n (You have exited the program).")
        break
    elif word == "help":
        print(
            f"{Style.NORMAL}{Back.MAGENTA}{Fore.WHITE}==== HELP MENU ===={Back.RESET}{Fore.RESET} \n"
            f"{Style.DIM}Ukrainian Noun Declensor v. Alpha 0.11.10.1 from November 10, 2025{Style.NORMAL}\n"
            f"— To use this tool, simply enter a Ukrainian noun in Cyrillic script. \n"
            f"— The program will determine the gender and the declension type of the noun. \n"
            f"— To exit the program, type '6' and press Enter. \n")
        word = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
    elif not is_cyrillic:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Carrot. {Back.RESET}{Fore.RESET}\n (Please enter a word in Cyrillic script).")
        word = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(word)
    elif len(word) < 2:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Shorty. {Back.RESET}{Fore.RESET}\n (Please enter a noun with at least 2 letters).")
        word = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(word)
else:
    while gender(word) is None:
        word = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(word)
        if not is_cyrillic or len(word) < 2 or word == "6" or word == "help":
            break
    if declension_type(word) == "I":
        declension_type1(word)
    elif declension_type(word) == "II":
        declension_type2(word)
    elif declension_type(word) == "III":
        declension_type3(word)
    elif declension_type(word) == "IV":
        declension_type4(word)
    else:
        print(f"{Back.RED}{Fore.WHITE}Error! Code: Riverside. {Back.RESET}{Fore.RESET}\n (No declension type selected).")
        word = input(f"{Style.BRIGHT}Enter a noun down below: \n {Style.DIM}")
        is_cyrillic = check_for_script(word)
    print(
        f"{Style.NORMAL}==== WORD: {word} ==== \n"
        f"— Gender: {gender(word)}\n"
        f"==== DECLENSION TYPE {declension_type(word)} ==== \n"
        f"Nominative (Називний): {nominative}\n" 
        f"Genetive (Родовий): {genitive}\n" 
        f"Dative (Давальний): {dative}\n" 
        f"Accusative (Звинувальний): {accusative}\n" 
        f"Instrumental (Орудний): {instrumental}\n" 
        f"Locative (Місцевий): на/в {locative}\n" 
        f"Vocative (Кличний): {vocative}\n")