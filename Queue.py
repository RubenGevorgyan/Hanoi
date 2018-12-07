def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def top(stack):
    p = len(stack)
    return stack[p - 1]


def pop(stack):
    if (isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)

    return stack.pop()


def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()


def sortStack(stack):
    tmpStack = createStack()
    while (isEmpty(stack) == False):

        tmp = top(stack)
        pop(stack)


        while (isEmpty(tmpStack) == False and
               int(top(tmpStack)) > int(tmp)):
            push(stack, top(tmpStack))
            pop(tmpStack)

        push(tmpStack, tmp)

    return tmpStack
def main():
    print("Now we are starting sorting algorithm")
    stak=createStack()
    for i in range(0,int(input("How many times do you want to input a number?"))):
        push(stak,input("Input number,please"))
    sorted=sortStack(stak)
    for i in range(0,len(sorted)):
        print(sorted[i]+"\n")
main()