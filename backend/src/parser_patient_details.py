from backend.src.parser_generic import MedicalDocParser
import re

class ParserPatientDetails(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            "patient_name": self.remove_noise_from_name(self.get_field("patient_name")),
            "phone_number": self.get_field("phone_number"),
            "hepatitis_b_vaccination": self.get_field("hepatitis_b_vaccination"),
            "medical_problems": self.get_field("medical_problems")
        }

    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {"pattern": "Patient Information Birth Date\n*(.*)\n", "flags": 0},
            "phone_number": {"pattern": "(\(\d{3}\) \d{3}-\d{4})", "flags": 0},
            "hepatitis_b_vaccination": {"pattern": "Have you had the Hepatitis B vaccination\?.*(Yes|No)\n", "flags": re.DOTALL},
            "medical_problems": {"pattern": "List any Medical Problems \(.*(\)|\}):\n*(.*)\n", "flags": 0}

        }

        pattern_object = pattern_dict.get(field_name)

        if pattern_object:
            pattern = pattern_object["pattern"]
            flags = pattern_object["flags"]
            field = re.findall(pattern, self.text, flags=flags)

            if len(field) > 0:
                if field_name == "medical_problems":
                    return field[0][1].strip()
                return field[0].strip()

    @staticmethod
    def remove_noise_from_name(name):
        date_pattern = "((January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2} \d{4})"
        date = re.findall(date_pattern, name)
        if len(date) > 0:
            return name.replace(date[0][0], "").strip()


if __name__ == "__main__":
    doc_text = '''
    17/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight’
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Casc of Emergency
7 ee
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone

Genera! Medical History

a

a

a ea A CE i a

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?
No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

CO
aa
   '''

    doc_text_2 = '''
  Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020
'''

    obj = ParserPatientDetails(doc_text)
    print(obj.parse())

    obj = ParserPatientDetails(doc_text_2)
    print(obj.parse())
