print("This is a Dynamic Calculator")
print("Type expressions like:  2+3*4-6/2")
print("Type 'q' to quit.\n")

while True:
    expression = input("Enter expression: ")
    if expression.lower() == "q":
        print("Calculator closed.")
        break
    box = []
    num = ""
    for i in expression:
        if i.isdigit():
            num += i
        else:
            box.append(int(num))
            box.append(i)
            num = ""
    box.append(int(num))

    i = 0 
    while i < len(box):
        if box[i] == "/":
            r = box[i - 1] / box[i + 1]
            box[i-1:i+2] = [r]
            i -= 1
        elif box[i] == "*":
            r = box[i - 1] * box[i + 1]
            box[i - 1 : i + 2] = [r]
            i -= 1
        i+=1

    i = 0 
    while i < len(box):
        if box[i] == "+":
            r = box[i - 1] + box[i + 1]
            box[i-1: i + 2] = [r]
            i -=1
        elif box[i] == "-":
            r = box[i - 1] - box[i + 1]
            box[i - 1 : i + 2] = [r]
            i -=1
        i+=1
    print("Answer is :", box[0])        
        