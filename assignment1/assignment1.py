# Task 1 - Hello
def hello():
    return "Hello!"

#Task 2 - Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

#Task 3 - Calculator
def calc(arg1, arg2, operation="multiply"):
    try:
        match operation:
            case "multiply":
                return arg1 * arg2
            case "add":
                return arg1 + arg2
            case "subtract":
                return arg1 - arg2
            case "divide":
                return arg1 / arg2
            case "modulo":
                return arg1 % arg2
            case "int_divide":
                return arg1//arg2
            case "power":
                return arg1 ** arg2
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#Task 4 - Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"Invalid data type: {type}"
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
#Task 5 - Grading System, using *args
def grade(*args):
    try:
        avg = sum(args)/ len(args)
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        else:
            return "Below 60"
    except TypeError:
        return "Invalid data was provided."

#Task 6 - Use a For Loop with a Range
def repeat(string, count):
    result =""
    for _ in range(count):
        result += string
    return result

#Task 7: Student Scores, Using **kwargs
def student_scores(position, **kwargs):
    if position == "best":
        return max(kwargs, key=kwargs.get)
    elif position == "mean":
        return sum(kwargs.values())/ len(kwargs)
    else:
        return "Invalid. Use 'best' or 'mean'." 

#Task 8: Titleize, with String and List Operations
def titleize(param):
    little_words = {"a","on","an","the","of","and","is","in"}
    words = param.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    word =""
    for letter in secret:
        if letter in guess:
            word += letter
        else:
            word +="_"
    return word

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels ="aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        # if the first letter of the word is a vowel, add "ay"
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        #"qu" as a single constant and then add "ay" at the end and removes the two letters from beginning of word
        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "quay")
        else:
            # loop through word if it starts with a consonant
            i = 0
            #using a while loop to locate the vowel in word to then append "ay"
            while i < len(word) and word[i] not in vowels:
                #However, if "q" is followed by "u" then move thpse to the end 
                if word[i] == "q" and i + 1 < len(word) and word[i+1] == "u":
                    i += 2
                    break
                i += 1
            #word[i:] takes the portion of the word starting from the firs vowel
            # word [:i] takes the constants before the first vowel and moves them to the end 
            pig_latin_words.append(word[i:] + word[:i] + "ay")
    return " ".join(pig_latin_words)