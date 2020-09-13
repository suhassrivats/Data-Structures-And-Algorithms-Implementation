# Implement a stack using an array

# import maxsize from sys module used to return -infinite when stack is empty
from sys import maxsize


def create_stack():
    '''Function to create a stack. It initializes size of stack as 0'''
    stack = []
    return stack


def push(stack, item):
    '''Function to add an item to stack. It increases size by 1 '''
    stack.append(item)
    print(item + ' pushed to stack')


def pop(stack):
    '''Function to remove an item from stack. It decreases size by 1'''
    if is_empty(stack):
        return str(-maxsize - 1)
    print()
    return stack.pop()


def peek(stack):
    '''Function to return the top from stack without removing it '''
    if is_empty(stack):
        return str(-maxsize-1)
    print(stack[len(stack)-1])
    return stack[len(stack)-1]


def is_empty(stack):
    '''Stack is empty when size is zero'''
    return len(stack) == 0


####### Driver function #########
stack = create_stack()
push(stack, str(10))
push(stack, str(11))
push(stack, str(12))
peek(stack)
print(pop(stack) + " popped from stack")
print(pop(stack) + " popped from stack")
# print(pop(stack) + " popped from stack")
# print(pop(stack) + " popped from stack")
print(is_empty(stack))
peek(stack)
