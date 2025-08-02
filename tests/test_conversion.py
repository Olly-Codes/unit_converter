from unit_converter.conversion import convert_length, convert_weight, convert_temp 

def test_convert_length():
    mm_to_cm = convert_length(5, "mm", "cm")
    mile_to_yard = convert_length(30, "mile", "yard")

    assert mm_to_cm == 0.5
    assert mile_to_yard == 52800

def test_convert_weight():
    kg_to_pounds = convert_weight(20, "kg", "pounds")
    g_to_ounces = convert_weight(600, "g", "ounces")

    assert kg_to_pounds == 44.09
    assert g_to_ounces == 21.16

def test_convert_temp():
    c_to_c = convert_temp(20, "C", "C")
    c_to_f = convert_temp(35, "C", "F")
    k_to_c = convert_temp(105, "K", "C")

    assert c_to_c == 20.0
    assert c_to_f == 95.0
    assert k_to_c == -168.15