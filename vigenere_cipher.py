""" Class """

class VigenereCipher:
    """ Vigenere Cipher class """
    def __init__(self, keyword):
        """ Init cipher, set keyword to cipher """
        self.keyword = keyword.upper()

    def _code(self, text, combine_func):
        """ Universal method for decoding and encoding """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for letter,k in zip(text, keyword):
            combined.append(combine_func(letter,k))
        return "".join(combined)

    def encode(self, plaintext):
        """ Encoding method """
        return self._code(plaintext, self.combine_character)

    def decode(self, ciphertext):
        """ Decoding method """
        return self._code(ciphertext, self.separate_character)

    @staticmethod
    def separate_character(cypher, keyword):
        """ Separates character getting row from intersection sell and col"""
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    @staticmethod
    def combine_character(plain, keyword):
        """ Combines two characters first is row second in column """
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    def extend_keyword(self, number):
        """ Ectends keyword if too short of shortens if too long """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]
