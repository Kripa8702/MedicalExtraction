from backend.src.parser_generic import MedicalDocParser
import re

class ParserPrescription(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)   
        
    def parse(self):
        return {
            "patient_name": self.get_field("patient_name"),
            "patient_address": self.get_field("patient_address"),
            "medicine": self.get_field("medicine"),
            "directions": self.get_field("directions"),
            "refill": self.get_field("refill")
        }
        
    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {"pattern": "Name:(.*)Date", "flags": 0},
            "patient_address": {"pattern": "Address: (.*)\n", "flags": 0},
            "medicine": {"pattern": "Address: [^\n]*(.*)Directions", "flags": re.DOTALL},
            "directions": {"pattern": "Directions:(.*)Refill", "flags": re.DOTALL},
            "refill": {"pattern": "Refill:(.*)", "flags": 0}
        }
        
        pattern_object = pattern_dict.get(field_name)
        
        if pattern_object:
            pattern = pattern_object["pattern"]
            flags = pattern_object["flags"]
            field = re.findall(pattern, self.text, flags=flags)
            if len(field) > 0: 
                return field[0].strip()
        

if __name__ == "__main__":
    doc_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222

    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    K

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''
    obj = ParserPrescription(doc_text)
    print(obj.parse())

    