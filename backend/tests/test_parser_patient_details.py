import pytest

from backend.src.parser_patient_details import ParserPatientDetails
@pytest.fixture
def pp1():
    doc_text =  '''
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

    pp = ParserPatientDetails(doc_text)
    return pp.parse()

@pytest.fixture
def pp2():
    doct_text =  '''
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

    pp = ParserPatientDetails(doct_text)
    return pp.parse()


def test_get_name(pp1, pp2):
    assert pp1["patient_name"] == "Kathy Crawford"
    assert pp2["patient_name"] == "Jerry Lucas"

def test_get_phone(pp1, pp2):
    assert pp1["phone_number"] == "(737) 988-0851"
    assert pp2["phone_number"] == "(279) 920-8204"

def test_hepatitis_b_vaccination(pp1, pp2):
    assert pp1["hepatitis_b_vaccination"] == "No"
    assert pp2["hepatitis_b_vaccination"] == "Yes"


def test_get_medical_problems(pp1, pp2):
    assert pp1["medical_problems"] == "Migraine"
    assert pp2["medical_problems"] == "N/A"
