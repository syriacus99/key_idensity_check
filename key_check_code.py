number = '0123456789'
lower_letter = 'abcdefghijklmnopqrstuvwxyz'
upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
specific_symbol = '`~!@#$%^&*()-_=+[{]};:\'"<,.>/?\\| '


class key_check:
    def __init__(self, key):
        self.__idensity_number = bool()
        self.__idensity_lletter = bool()
        self.__idensity_uletter = bool()
        self.__idensity_spesymbol = bool()
        self.__key_level = 0
        self.__message = str()
        self.__key_length = 0
        self.__key = key
        self.idensity_check()


    def idensity_check(self):
        level_count = 0
        length_count = 0
        for i in self.__key:
            length_count += 1
            if i in number:
                self.__idensity_number = True
            if i in lower_letter:
                self.__idensity_lletter = True
            if i in upper_letter:
                self.__idensity_uletter = True
            if i in specific_symbol:
                self.__idensity_spesymbol = True
        if self.__idensity_spesymbol == True:
            level_count += 1
        if self.__idensity_uletter == True:
            level_count += 1
        if self.__idensity_lletter == True:
            level_count += 1
        if self.__idensity_number == True:
            level_count += 1
        self.__key_level = level_count
        self.__key_length = length_count
        if self.__key_length <= 8:
            self.__message += 'length of key is too short.\n'
        if self.__key_length >= 18:
            self.__message += 'length of key is too long.\n'
        if self.__key_level <= 2:
            self.__message += 'Please include at least three of the lowercase,' \
                             ' uppercase, numeric, and special characters\n'
        if self.__message == '':
             self.__message = 'good key.'
        if self.__message != None:
            print(self.print_key_message())
    def print_key(self):
        return self.__key
    def print_key_level(self):
        return self.__key_level
    def print_key_message(self):
        return self.__message
    def print_key_length(self):
        return self.__key_length
    def print_key_include(self):
        message = 'include'
        if self.__idensity_number == True:
            message += ' number'
        if self.__idensity_lletter == True:
            message += ' low case letter'
        if self.__idensity_uletter == True:
            #print(" upper case letter", end='')
            message += ' upper case letter'
        if self.__idensity_spesymbol ==True:
            #print(" specific symbol", end='')
            message += ' specific symbol'
        if self.__key_level == 1:
            #print(" none", end='')
            message += ' none'
        #print(".")
        message += '.'
        return message



if __name__ == '__main__':
    key = str(input("key:"))
    obj_key = key_check(key)
    obj_key.print_key_include()
    #print(obj_key.print_key())
    # print(obj_key.print_key_include())

