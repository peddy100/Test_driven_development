"""
Authors: Matthew O'Malley-Nichols, Pedram Jarahzedah, Devin Fahnestock
Description: Tasks for our group project
"""

# Function 1


def str_to_num(num_str: str):
    """Takes a str representing a num and converts it to an number"""
    map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }
    if num_str in map.keys():
        return map[num_str]
    return None


def conv_int(int_str: str, sign: int):
    """Converts a string representing an int to an int"""
    result = 0
    power = 0
    for num in int_str[::-1]:
        result += str_to_num(num) * (10 ** power)
        power += 1
    return sign * result


def conv_float(left_num_str: str, right_num_str: str, sign: int):
    """Converts a str representing a float to a float"""
    result = 0.0
    left_power = 0
    right_power = -1
    for num in left_num_str[::-1]:
        if not num.isdecimal():
            return None
        left = str_to_num(num) * (10 ** left_power)
        result += left
        left_power += 1
    for num in right_num_str:
        if not num.isdecimal():
            return None
        right = str_to_num(num) * (10 ** right_power)
        right = round(right, abs(right_power))
        result += right
        result = round(result, abs(right_power))
        right_power -= 1
    return sign * result


def conv_hex(hex_str: str, sign: int):
    """Converts a str representing a hex to an int"""
    result = 0
    power = 0
    for num in hex_str[::-1]:
        if str_to_num(num) is not None:
            result += str_to_num(num) * (16 ** power)
            power += 1
            continue
        return None
    return sign * result


def conv_num_failure(num_str) -> bool:
    """Failure conditions for conv_num"""
    if not isinstance(num_str, str):
        return True
    if num_str.count(".") > 1:
        return True
    if num_str.count("-") > 1:
        return True
    if num_str.count("-") == 1:
        if not num_str[0] == "-":
            return True
    if len(num_str) == 0:
        return True
    return False


def remove_num_sign(num_str_param: str) -> tuple:
    """Finds the sign of a number"""
    num_str = str(num_str_param).lower()
    sign = 1
    if num_str[0] == "-":
        sign = -1
        num_str = num_str[1::]
    return num_str, sign


def is_hex(num_str: str) -> bool:
    """Returns T/F depending on if num string is hexadecimal"""
    if num_str.count("0x") > 0:
        return num_str[:2] == "0x"
    return False


def remove_hex_prefix(num_str_param: str) -> str:
    """Removes the hex prefix for num_str"""
    num_str = str(num_str_param)
    return num_str[2::]


def is_float(num_str: str) -> bool:
    """Returns T/F depending on if num string is a float"""
    return num_str.count(".") == 1


def conv_num(num_str_param):
    """Takes in a str representing a num, converts it to base 10,
       and returns it."""
    if conv_num_failure(num_str_param):
        return None
    num_str, sign = remove_num_sign(num_str_param)
    if is_hex(num_str):
        num_str = remove_hex_prefix(num_str)
        return conv_hex(num_str, sign)
    if is_float(num_str):
        split_num_str = num_str.split('.')
        return conv_float(split_num_str[0], split_num_str[1], sign)
    if num_str.isdecimal():
        return conv_int(num_str, sign)
    return None

# Function 2


def is_leap_year(year: int) -> bool:
    """Receives an int representing a year and returns True if year is a
    leap year and false if not a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def days_in_year(year: int) -> int:
    """Receives an int representing the year and returns an int representing
    the number of days in that year"""
    if is_leap_year(year):
        return 366
    return 365


def days_in_month(year: int, month: int) -> int:
    """Receives two ints representing the year and month and returns an
    int representing the number days in that month"""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    return 28


def my_datetime(num_sec: int) -> str:
    """Takes in an int representing the num of secs since the epoch,
      and returns it as a string formatted as MM-DD-YYYY"""
    year = 1970
    day = 1
    month = 1
    seconds_in_day = 86400

    while num_sec >= seconds_in_day:
        days_in_current_year = days_in_year(year)
        days_in_current_month = days_in_month(year, month)

        if num_sec >= days_in_current_year * seconds_in_day:
            num_sec -= days_in_current_year * seconds_in_day
            year += 1
        elif num_sec >= days_in_current_month * seconds_in_day:
            num_sec -= days_in_current_month * seconds_in_day
            month += 1
        else:
            day = 1 + num_sec // seconds_in_day
            num_sec %= seconds_in_day

    return f"{month:02d}-{day:02d}-{year}"

# Function 3


def convert_to_hex(num: int):
    """This Function takes a number and converts it to a hex string value."""
    hexmap = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    return hexmap[num]


def create_hex_array(num: int):
    """This function takes a number and returns a inverse array of each Hex values as strings."""
    hex = []
    if num == 0:
        hex.append(convert_to_hex(0))
        hex.append(convert_to_hex(0))
    while num > 0:
        hex.append(convert_to_hex(num % 16))
        num //= 16
    if len(hex) % 2 != 0:
        hex.append(convert_to_hex(0))
    return hex


def conv_endian(num: int, endian='big'):
    """Takes in an int as num and converts it to a hexadecimal num.
    The endian type is determined by the flag endian. Returns a string."""
    hexstr = ""
    if num < 0:
        num = abs(num)
        hexstr += "-"
    hex = create_hex_array(num)
    if endian == 'little':
        spacer = False
        while len(hex) > 0:
            if spacer:
                hexstr += " "
            hexstr += hex.pop(1)
            hexstr += hex.pop(0)
            spacer = True
    elif endian == 'big':
        spacer = False
        while len(hex) > 0:
            if spacer:
                hexstr += " "
            hexstr += hex.pop()
            hexstr += hex.pop()
            spacer = True
    else:
        return None

    return hexstr
