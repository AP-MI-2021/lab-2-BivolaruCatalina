def is_palindrome(n):
    '''
    Verifica daca n este palindrom
    :param n: numar intreg
    :return: valoare de adevar in funtie de caz
    '''
    aux=n
    invers=0
    while aux != 0:
       invers=invers*10+aux%10
       aux=aux//10
    if invers == n:
     return True
    else:
     return False

def test_is_palindrome():
    assert is_palindrome(1221) == True
    assert is_palindrome(1321) == False
    assert is_palindrome(131) == True
    assert is_palindrome(12341) == False
    assert is_palindrome(12321) == True

def is_superprime(n):
    '''
    Verifica daca n este superprim
    :param n: numar intreg
    :return: valoare de adevar in functie de caz
    '''
    copie=n
    if n<2:
        return False
    else:
      while copie != 0:
          if copie == 1:
              return False
          for i in range(2, copie//2):
              if n%i == 0:
                  return False
          copie=copie//10
    return True

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(21) == False
    assert is_superprime(73) == True
    assert is_superprime(15) == False
    assert is_superprime(37) == True

def is_antipalindrome(n):
    '''
    Verifica daca n este antipalindrom
    :param n: numar intreg
    :return: valoare de adevar in functie de caz
    '''
    invers = 0
    copie = n
    aux = n
    parametru1 = 0
    parametru2=0
    while aux != 0:
        parametru1 = parametru1+1
        aux = aux//10
    if parametru1%2 == 0:
        while parametru2 < parametru1//2:
            invers = invers*10+copie%10
            copie = copie//10
            parametru2 = parametru2+1
    else:
        while parametru2 < parametru1 // 2:
            invers = invers * 10 + copie % 10
            copie = copie // 10
            parametru2 = parametru2 + 1
        copie = copie//10
    while invers != 0:
        if invers%10 == copie% 10:
            return False
        invers = invers//10
        copie = copie//10
    return True

def test_is_antipalindrome():
    assert is_antipalindrome(25321) == True
    assert is_antipalindrome(25351) == False
    assert is_antipalindrome(2521) == True
    assert is_antipalindrome(2522) == False
    assert is_antipalindrome(1521) == False

def main():
 while True:
        optiune=input('Introduce optiunea: ')
        if optiune == '5':
            nr1 = int(input('Introduceti numarul: '))
            if is_palindrome(nr1):
                print(f'Numarul este palindrom.')
            else:
                print(f'Numarul nu este palindrom.')
            test_is_palindrome()
        elif optiune == '6':
            nr2 = int(input('Introduce numarul: '))
            if is_superprime(nr2):
                print(f'Numarul este superprim.')
            else:
                print(f'Numarul nu este superprim.')
                test_is_superprime()
        elif optiune == '7':
            nr3=int(input('Introduce numarul: '))
            if is_antipalindrome(nr3):
                print(f'Numarul este antipalindrom.')
            else:
                print(f'Numarul nu este antipalindrom')
            test_is_antipalindrome()
        elif optiune == 'x':
            break
main()