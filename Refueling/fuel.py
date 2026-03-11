def main():
    while True:
        try:
            input_fraction = input("Fraction: ")
            fuel_gauge = gauge(input_fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    
    print(fuel_gauge)


def convert(fraction):
    if fraction.count("/") != 1:
        raise ValueError("Invalid input")

    fraction = fraction.split("/")
    X = int(fraction[0])
    Y = int(fraction[1])

    if Y == 0:
        raise ValueError("Denominator cannot be zero")
    if X > Y:
        raise ValueError("Numerator cannot be greater than denominator")

    percentage = (X/Y) * 100

    return percentage


def gauge(percentage):
    converted_percentage = convert(percentage)

    if converted_percentage<= 1:
        return "E"
    elif converted_percentage >= 99:
        return "F"
    else:
        return f"{converted_percentage:.0f}%"


if __name__ == "__main__":
    main()
