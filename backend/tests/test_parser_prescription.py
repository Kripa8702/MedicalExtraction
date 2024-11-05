import pytest

from backend.src.parser_prescription import ParserPrescription

@pytest.fixture
def doc_test():
    return '''
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

def test_get_name(doc_test):
    pp = ParserPrescription(doc_test)
    assert pp.get_field("patient_name") == "Marta Sharapova"
    
def test_get_address(doc_test):
    pp = ParserPrescription(doc_test)
    assert pp.get_field("patient_address") == "9 tennis court, new Russia, DC"

def test_get_refill(doc_test):
    pp = ParserPrescription(doc_test)
    assert pp.get_field("refill") == "2 times"