# Liquid Measurement Class
import sys
class LM:
    # Class variables
    lmdict= ' '
    from_unit = ' '
    to_unit = ' '
    qty = 0
    from_value = ' '
    to_value = ' '
    converted_value = ' '
    result = ' '
    # Class methods
    @classmethod
    def dispatcher(cls): # Controls the sequence of operations
        try:
            cls.load_lmdict('lmdict')
        except:
            print("Not able to load LM dictionary.")
            return
        try:
            cls.read_input()
        except:
            print("Problem reading client input.")
            return
        try:
            cls.parse_input()
        except:
            print("Problem parsing client input.")
            return
        try:
            cls.convert()
        except:
            print("Problem converting from_units to to_units.")
            return
        try:
            cls.format()
        except:
            print("Problem formatting output.")
            return
        try:
            cls.output()
        except:
            print("Problem writing formatted output.")
            return
        return
    @classmethod
    def convert(cls): #  the from_units to to_units, multiplied by quantity of from_units
        # Method of conversion is to divide the number of cc's corresponding to the from_unit
        # by the number of cc's corresponding to the to_unit
        # then multiply by the quantity
        try:
            from_ = cls.lmdict[cls.from_unit]
        except:
            print("From_unit "+cls.from_unit+" not supported in the LM dictionary.")
            return
        try:
            to_ = cls.lmdict[cls.to_unit]
        except:
            print("To_unit "+cls.to_unit+" not supported in the LM dictionary.")
            return
        try:
            cls.converted_value = (from_/to_)*cls.qty
        except:
            print("Problem during division of from by to.")
            return
        return
    @classmethod
    def read_input(cls):
        cls.from_unit = input("Enter unit to be converted. (E.g. 'cup')")
        cls.to_unit =   input("Enter target unit. (E.g. 'fluid ounce')")
        cls.qty =       float(input("Enter quantity to be converted."))
        return
    @classmethod
    def parse_input(cls):
        try:
            cls.from_value = cls.lmdict[cls.from_unit]
        except:
            print(cls.from_unit+" not found in conversion dictionary.")
        try:
            cls.to_value = cls.lmdict[cls.to_unit]
        except:
            print(cls.to_unit+ " not found in conversion dictionary.")
        if (type(cls.qty) == 'integer' or type(cls.qty) == 'floating point') == None:
                print("Quantity must be an integer or floating point number.")
        return
    @classmethod
    def format(cls):
        if cls.qty > 1.0:
            cls.result = str(cls.qty)+" units of "+cls.from_unit+"s is "+str(cls.converted_value)+" units of "+cls.to_unit+"s."
        else:
            cls.result = str(cls.qty)+" unit of "+cls.from_unit+" is "+str(cls.converted_value)+" unit(s) of "+cls.to_unit+"s."
        return
    @classmethod
    def output(cls):
        print(cls.result)
        return
    @classmethod
    def load_lmdict(cls,dict_name):
       import json
       f = open(dict_name+'.json')
       data = json.load(f)
       cls.lmdict = data[dict_name]
       for entry in cls.lmdict: print(entry,cls.lmdict[entry])
       return

# ********************************
if __name__ == '__main__':
    while True:

        LM.dispatcher()
        yn = input("Other values to convert? (y/n)")
        if yn == 'y': LM.dispatcher()
        elif yn == 'n': sys.exit()
        else: print("Please answer either 'y' or 'n'")


