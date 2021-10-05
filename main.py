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
    Verifica daca un numar este superprim
    :param n: numar intreg
    :return: valoare de adevar in functie de caz
    '''
    copie=n
    if n<2:
        return False
    elif n%2 == 0:
        return False
    else:
      while copie != 0:
          for i in range(3, copie//2):
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

ShouldRun=True
while ShouldRun:
        optiune=input('Introduce numarul problemei: ')
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
                print(f'Numarul este superprim')
            else:
                print(f'Numarul nu este superprim')
            test_is_superprime()
        elif optiune == 'x':
            ShouldRun=False
