def calculate_volume_label():
    height = float(input("Enter the height of the object in cm: "))
    width = float(input("Enter the width of the object in cm: "))
    depth = float(input("Enter the depth of the object in cm: "))

    volume = height * width * depth

    if volume <= 10:
        return "Extra Small"
    elif volume <= 25:
        return "Small"
    elif volume <= 75:
        return "Medium"
    elif volume <= 100:
        return "Large"
    elif volume <= 250:
        return "Extra Large"
    else:
        return "Extra-Extra Large"


# Example usage
label = calculate_volume_label()
print(label)
