# Write your code here.

#task 1
print("-------------TASK  #1")
def hello():
    return "Hello!"
print(hello())

#task 2
print("-------------TASK #2")
def greet(name):
    return f"Hello, {name}!"
print(greet("Miriam"))

#task 3
print("-------------TASK #3")
def calc(num1,num2, operation="multiply" ):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "divide":
                return num1/num2
        elif operation == "modulo":
            return num1%num2
        elif operation == "int_divide":
            return num1/num2
        elif operation == "power":
            return num1 ** num2
        else:
            return num1*num2
        
    except ZeroDivisionError:
            return "You can't divide by 0!"
    except Exception as e:
            return f"You can't multiply those values!"

print(calc(5,6))
print(calc(5,6,"add"))
print(calc(5,6,"subtract"))
print(calc(5,0,"divide"))
print(calc(5,'3',"divide"))

#task 4
print("-------------TASK #4")
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "string":
            return str(value)
        elif type == "float":
            return float(value)      
    except Exception as e:
        return f"You can't convert {value} into a {type}"

print(data_type_conversion(1,"float"))
print(data_type_conversion(2,"string"))
print(data_type_conversion(2.99999,"int"))
print(data_type_conversion("dollar","int"))

#task 5
print("-------------TASK #5")
def grade(*args):
    try:
        result = sum(args) / len(args)
        if result >= 90:
            return "A"
        elif result >= 80 <90:
            return "B"
        elif result >=70 <80:
            return "C"
        elif result >=60 <70:
            return "D"
        elif result <60:
            return "F"
    except Exception:
        return "Invalid data was provided"
    
print(grade(100,80,90,78))
print(grade(100,80,90,"g"))

#task 6
print("-------------TASK #6")
def repeat(string, count):
    for i in range(count):
        print(string * i)

print(repeat("hello", 4))

#task 7
print("-------------TASK #7")
def student_scores(str, **kwargs):
    
    print("best or mean:", str)
    print("kwargs:", kwargs)
    
    if str == "best":
        return max(kwargs.values())
    elif str == "mean":
        sum =0
        count =0
        for value in kwargs.values(): 
            sum += value
            count += 1
        if count == 0:
            return "You can't divide by 0!"
        return sum / count
    
print(student_scores("mean",Alice=90, Bob=85, Charlie=78 ))
print(student_scores("best", Alice=90, Bob=85, Charlie=78))

#task 8
print("-------------TASK #8")
def titleize( str ):
    words = str.split()
    for i, word in enumerate(words):
       if i == 0:
           words[i] = word.capitalize()
       elif i == len(words)-1:
           words[i] = word.capitalize()
       elif word not in ["a","on","an","the", "of", "and","is","in"]:
            words[i] = word.capitalize()
    return " ".join(words)        
        
       
print(titleize("the girl with the dragon tattoo"))
print(titleize("to kill a mocking-bird"))
print(titleize("a tale of two cities"))

#task 9
print("-------------TASK #9")
def hangman(secret, guess):
    list_secret = list(secret.lower())
    list_guess = list(guess.lower())
    match = []
    for letter in list_secret:
        if letter in list_guess:
            match.append(letter)
        if letter not in list_guess:
            match.append("_")
    return ''.join(match)
            
    
    
print(hangman("seccret", "aec"))
print(hangman("Montana", "aecm"))

#task 10
print("-------------TASK #10")
def pig_latin(str):
    words = str.split()
    new_words = []
    
    for word in words:
        if word[0] in ["a", "e", "i", "o", "u"]:
            new_words.append(word + "ay")
        elif word[:2] =='qu':
            new_words.append(word[2:]+ "quay")
        else:
            consonants = ""
            while word and word[0] not in ["a", "e", "i", "o", "u"]:
                consonants +=word[0]
                word = word[1:]
            
            new_words.append(word + consonants + "ay")
    return ' '.join(new_words)

        
print(pig_latin("unknown"))
print(pig_latin("tractor"))
print(pig_latin("tractor is on the other side of the road"))
