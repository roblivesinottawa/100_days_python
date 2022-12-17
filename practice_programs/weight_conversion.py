unit  = input("select 'k' for kilos or 'l' for pounds: >>> ").lower()
weight = float(input("enter weight: >>> "))

def weight_conversion(_unit=unit, _weight=weight):
    if _unit == 'l':
        converted = _weight * 0.45
        return f"you are {converted} kilos."
    else:
        converted = _weight / 0.45
        return f"you are {converted} pounds."


print(weight_conversion())