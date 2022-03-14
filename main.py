import sys
import time
import json

storingData = False

if storingData == True:
    dictThing = {
        "data" : []
    }

    with open('data.json', 'w') as f:
        json.dump(dictThing, f, indent = 4)

def storeData(char, zero, one, two, three, four, five, six, seven, eight, nine):
    
    cycle = 0

    if cycle >= 10000000:
        cycle = 0

        jsonData = {
                "digit":char,
                "zero":zero,
                "one":one,
                "two":two,
                "three":three,
                "four":four,
                "five":five,
                "six":six,
                "seven":seven,
                "eight":eight,
                "nine":nine
            }

        with open('data.json', 'r') as f:
            fileData = json.load(f)

        fileData["data"].append(jsonData)

        with open('data.json', 'w') as f:
            json.dump(fileData, f, indent = 4)

    else:
        cycle += 1

def main(wholePi, char):

    global zero
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    while char <= 10:
        try: 
            int(wholePi[char])
            if int(wholePi[char]) % 2 == 0:
                if int(wholePi[char]) == 0:
                    zero += 1
                elif int(wholePi[char]) == 2:
                    two += 1
                elif int(wholePi[char]) == 4:
                    four += 1
                elif int(wholePi[char]) == 6:
                    six += 1
                elif int(wholePi[char]) == 8:
                    eight += 1
            else:
                if int(wholePi[char]) == 1:
                    one += 1
                elif int(wholePi[char]) == 3:
                    three += 1
                elif int(wholePi[char]) == 5:
                    five += 1
                elif int(wholePi[char]) == 7:
                    seven += 1
                elif int(wholePi[char]) == 9:
                    nine += 1
        except:
            pass

        # print(char, " | ", wholePi[char])

        char += 1

def run():
    start = time.time()

    with open ("PiDec.txt", "r") as f:
        for x in f:
            wholePi = x.replace(".", "")

    main(wholePi, 0)



    mean = ((zero + one + two + three + four + five + six + seven + eight + nine) / 10)
    deviance = (abs(zero-mean) + abs(one-mean) + abs(two-mean) + abs(three-mean) + abs(four-mean) + abs(five-mean) + abs(six-mean) + abs(seven-mean) + abs(eight-mean) + abs(nine-mean))

    print("Difference compared to mean: Zero: ", zero-mean, " One: ", one-mean, " Two: ", two-mean, " Three: ", three-mean, " Four: ", four-mean, " Five: ", five-mean, " Six: ", six-mean, " Seven: ", seven-mean, " Eight: ", eight-mean, " Nine: ", nine-mean)

    print("Percent from mean: Zero: ", ((zero-mean)/deviance * 100), "%", " One: ", ((one-mean)/deviance * 100), "%", " Two: ", ((two-mean)/deviance * 100), "%", " Three: ", ((three-mean)/deviance * 100), "%", " Four: ", ((four-mean)/deviance * 100), "%", " Five: ", ((five-mean)/deviance * 100), "%", " Six: ", ((six-mean)/deviance * 100), "%", " Seven: ", ((seven-mean)/deviance * 100), "%", " Eight: ", ((eight-mean)/deviance * 100), "%", " Nine: ", ((nine-mean)/deviance * 100), "%")

    print("Total values: Zero: ", zero, " One: ", one, " Two: ", two, " Three: ", three, " Four: ", four, " Five: ", five, " Six: ", six, " Seven: ", seven, " Eight: ", eight, " Nine: ", nine)

    end = time.time()

    print("Program execution time: ", end - start)

if __name__ == "__main__":
    run()

# Percent from normalcy
# Trending towards normalcy?
# 