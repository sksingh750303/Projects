# Import audio pyhton librabry
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# function for text to speak


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Enter your Number 1")
num1 = int(input("Enter your Number 1: "))
speak("Enter your Number 2")
num2 = int(input("Enter your Number 2: "))
speak(f"Your numbers is {num1} and {num2} is: ")

print("for Add press 1:")
print("for Substraction press 2:")
print("for multiplication press 3:")
print("for division press 4:")

speak(" for Add press 1:, for Substraction press 2:,  for multiplication press 3:, for division press 4:")
fractionNo = int(input("Enter your fraction Number "))

if fractionNo == 1:
    add = num1+num2
    print(" Your answer is......", add)
    speak(f" Your answer is......{add}")
elif fractionNo == 2:
    sub = num1-num2
    print(" Your answer is......", sub)
    speak(f" Your answer is......{sub}")
elif fractionNo == 3:
    mul = num1*num2
    print(" Your answer is......", mul)
    speak(f" Your answer is......{mul}")
elif fractionNo == 4:
    div = num1/num2
    print(" Your answer is......", div)
    speak(f" Your answer is......{div}")
