# CodingBat: Recursion 1


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def bunnyEars(n):
    if n == 0:
        return 0
    return 2 + bunnyEars(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def bunnyEars2(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)


def triangle(n):
    if n == 0:
        return 0
    return n + triangle(n-1)


def sumDigits(n):
    if n == 0:
        return 0

    return (n % 10) + sumDigits(int(n/10))


def count7(n):
    if n < 10:
        if n % 10 == 7:
            return 1
        else:
            return 0
    elif n % 10 == 7:
        return 1 + count7(int(n/10))
    else:
        return count7(int(n/10))


def count8(n):
    if n == 0:
        return 0
    k = int(n/10)
    if n % 10 == 8:
        if (k) % 10 == 8:
            return 2 + count8(k)
        return 1 + count8(k)
    return count8(k)


def powerN(base, n):
    if n == 0:
        return 1
    return base * powerN(base, n-1)


def countX(s):
    if s == '':
        return 0
    if s[0] == 'x':
        return 1 + countX(s[1:])
    return countX(s[1:])


def countHi(s):
    if s == '':
        return 0
    if s[:2] == 'hi':
        return 1 + countHi(s[2:])
    return countHi(s[1:])


def changeXY(s):
    if s == '':
        return s
    if s[0] == 'x':
        return 'y' + changeXY(s[1:])
    return s[0] + changeXY(s[1:])


def changePi(s):
    if s == '':
        return s

    if s[:2] == 'pi':
        return '3.14' + changePi(s[2:])
    return s[0] + changePi(s[1:])


def noX(s):
    if s == '':
        return s
    if s[0] == 'x':
        return noX(s[1:])
    return s[0] + noX(s[1:])


def array6(nums, index):
    if index >= len(nums):
        return False
    if nums[index] == 6:
        return True
    return array6(nums, index+1)


def array11(nums, index):
    if index >= len(nums):
        return 0
    if nums[index] == 11:
        return 1 + array11(nums, index+1)
    return array11(nums, index+1)


def array220(nums, index):
    if index >= len(nums)-1:
        return False
    if (nums[index] * 10) == nums[index+1]:
        return True
    return array220(nums, index+1)


def allStar(s):
    if len(s) <= 1:
        return s
    return s[0] + '*' + allStar(s[1:])


def pairStar(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + '*' + pairStar(s[1:])
    return s[0] + pairStar(s[1:])


def endX(s):
    if s == '':
        return s
    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    return s[0] + endX(s[1:])


def countPairs(s):
    if len(s) <= 2:
        return 0
    if s[0] == s[2]:
        return 1 + countPairs(s[1:])
    return countPairs(s[1:])


def countAbc(s):
    if s == '':
        return 0
    if s[:3] == 'abc' or s[:3] == 'aba':
        return 1 + countAbc(s[3:])
    return countAbc(s[1:])


def stringClean(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return stringClean(s[1:])
    return s[0] + stringClean(s[1:])


def countHi2(s):
    if s == '':
        return 0
    if s[:3] == 'xhi':
        return countHi2(s[3:])
    elif s[:2] == 'hi':
        return 1 + countHi2(s[2:])
    return countHi2(s[1:])


def parenBit(s):
    if s == '':
        return s
    if s[0] == '(':
        if s[-1] == ')':
            return s
        else:
            return parenBit(s[:-1])
    return parenBit(s[1:])


def nestParen(s):
    if len(s) <= 1:
        return True
    if s[0] == '('and s[-1] == ')':
        return nestParen(s[1:-1])
    else:
        return False


def strCount(s, sub):
    if s == '' or sub == '':
        return 0
    if s[:len(sub)] == sub:
        return 1 + strCount(s[len(sub):], sub)
    return strCount(s[1:], sub)


def strCopies(s, sub, n):
    if len(s) < len(sub):
        return n == 0
    if s[:len(sub)] == sub:
        return strCopies(s[len(sub):], sub, n-1)
    else:
        return strCopies(s[1:], sub, n)


def strDist(s, sub):
    if s == '' or sub == '':
        return 0
    if s[:len(sub)] == sub and s[-len(sub):]:
        return len(s)
    return strDist(s[1:-1], sub)


def main():
    print('Factorial:')
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))

    print('BunnyEars:')
    print(bunnyEars(0))
    print(bunnyEars(1))
    print(bunnyEars(2))

    print('Fibonacci:')
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))

    print('BunnyEars2:')
    print(bunnyEars2(0))
    print(bunnyEars2(1))
    print(bunnyEars2(2))

    print('Triangle:')
    print(triangle(0))
    print(triangle(1))
    print(triangle(2))

    print('sumDigits:')
    print(sumDigits(126))
    print(sumDigits(49))
    print(sumDigits(12))

    print('Count7:')
    print(count7(717))
    print(count7(7))
    print(count7(123))

    print('Count8:')
    print(count8(8))
    print(count8(818))
    print(count8(8818))

    print('powerN:')
    print(powerN(3, 1))
    print(powerN(3, 2))
    print(powerN(3, 3))

    print('countX:')
    print(countX('xxhixx'))
    print(countX('xhixhix'))
    print(countX('hi'))

    print('countHi:')
    print(countHi('xxhixx'))
    print(countHi('xhixhix'))
    print(countHi('hi'))

    print('changeXY:')
    print(changeXY('codex'))
    print(changeXY('xxhixx'))
    print(changeXY('xhixhix'))

    print('changePi:')
    print(changePi('xpix'))
    print(changePi('pipi'))
    print(changePi('pip'))

    print('noX:')
    print(noX('xaxb'))
    print(noX('abc'))
    print(noX('xx'))

    print('array6:')
    print(array6([1, 6, 4], 0))
    print(array6([1, 4], 0))
    print(array6([6], 0))

    print('array11:')
    print(array11([1, 2, 11], 0))
    print(array11([11, 11], 0))
    print(array11([1, 2, 3, 4], 0))

    print('array220:')
    print(array220([1, 2, 20], 0))
    print(array220([3, 30], 0))
    print(array220([3], 0))

    print('allStar:')
    print(allStar('hello'))
    print(allStar('abc'))
    print(allStar('ab'))

    print('pairStar:')
    print(pairStar('hello'))
    print(pairStar('xxyy'))
    print(pairStar('aaaa'))

    print('endX:')
    print(endX('xxre'))
    print(endX('xxhixx'))
    print(endX('xhixhix'))

    print('countPairs:')
    print(countPairs('axa'))
    print(countPairs('axax'))
    print(countPairs('axbx'))

    print('countAbc:')
    print(countAbc('abc'))
    print(countAbc('abcxxabc'))
    print(countAbc('abaxxaba'))

    print('stringClean:')
    print(stringClean('yyzzza'))
    print(stringClean('abbbcdd'))
    print(stringClean('Hello'))

    print('CountHi2:')
    print(countHi2('ahixhi'))
    print(countHi2('ahibhi'))
    print(countHi2('xhixhi'))

    print('parenBit:')
    print(parenBit('xyz(abc)123'))
    print(parenBit('x(hello)'))
    print(parenBit('(xy)1'))

    print('NestParen:')
    print(nestParen('(())'))
    print(nestParen('(())'))
    print(nestParen('(((x))'))

    print('strCount:')
    print(strCount('catcowcat', 'cat'))
    print(strCount('catcowcat', 'cow'))
    print(strCount('catcowcat', 'dog'))

    print('strCopies:')
    print(strCopies('catcowcat', 'cat', 2))
    print(strCopies('catcowcat', 'cow', 2))
    print(strCopies('catcowcat', 'cow', 1))

    print('strDist:')
    print(strDist('catcowcat', 'cat'))
    print(strDist('catcowcat', 'cow'))
    print(strDist('cccatcowcatxx', 'cat'))


if __name__ == '__main__':
    main()
