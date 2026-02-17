import random
import string
from abc import abstractmethod,ABC
import nltk
from typing import List, Optional

nltk.download("words")

class PasswordGenerator(ABC):
    ''' base class for generating passwords '''
    
    @abstractmethod
    def generate(self):
        ''' methode to override by subclasses to generate passwords '''
        pass

  
class RandomPasswords(PasswordGenerator):
    '''
    class to generate random passwords that can include numberes and symbols
    '''
    def __init__(self, passlenght: int = 8, hasnumber: bool =False, hasesymbols: bool =False):
        self.passlenght = passlenght
        self.charachters: str = string.ascii_letters
        if hasnumber:
            self.charachters += string.digits
        if hasesymbols:
            self.charachters += string.punctuation
    
    def generate(self):
        '''
        Generate a password from specified characters.
        '''
        return "".join([random.choice(self.charachters) for i in range(self.passlenght)])
    
class MemorablePasswords(PasswordGenerator):
    ''' class to generate password with meaningful words'''
    def __init__(self,
        passlenght: int = 8,
        seperator: str = "-" ,
        capitalize: bool = False,
        words: Optional[List[str]] = None
        ):
        
        if words is None:
            words = nltk.corpus.words.words()
            
        self.passlenght = passlenght
        self.seperator = seperator
        self.capitalize = capitalize
        self.words: List[str] = words

        
    def generate(self):
        """
        Generate a password from a list of vocabulary words.
        """
        
        password = [random.choice(self.words) for i in range(self.passlenght)]
        if self.capitalize:
            password = [word.upper() if random.choice([True,False]) else word.lower() for word in password]
            
        return self.seperator.join(password)
    
class PinCodes(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    
    def __init__(self,passlenght: int):
        self.passlenght = passlenght
    
    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return "".join([random.choice(string.digits) for i in range(self.passlenght)])


def test_random_password_generator():
    randomgen = RandomPasswords(passlenght=8,hasnumber=True,hasesymbols=True)
    password = randomgen.generate()
    print(password)
    assert len(password) == 8
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    memprable_gen = MemorablePasswords(
        passlenght=10,
        seperator="/",
        capitalize=True,
        words=nltk.corpus.words.words())
    
    password = memprable_gen.generate()
    print(password)
    assert len(password.split('/')) == 10
    assert all(word[0].isupper() for word in password.split('/'))


def test_pincode_generator():
    pin_gen = PinCodes(passlenght=16)
    password = pin_gen.generate()
    
    print(password)
    assert len(password) == 16
    assert all(digits in string.digits for digits in password)


def main():
    print("Testing RandomPasswordGenerator:")
    test_random_password_generator()
    print("Testing MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("Testing PinCodeGenerator:")
    test_pincode_generator()



if __name__=="__main__":
    main()