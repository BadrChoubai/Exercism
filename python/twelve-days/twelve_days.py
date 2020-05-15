VERSES: list = [
    "twelve Drummers Drumming,",
    "eleven Pipers Piping,",
    "ten Lords-a-Leaping,",
    "nine Ladies Dancing,",
    "eight Maids-a-Milking,",
    "seven Swans-a-Swimming,",
    "six Geese-a-Laying,",
    "five Gold Rings,",
    "four Calling Birds,",
    "three French Hens,",
    "two Turtle Doves,",
    "a Partridge in a Pear Tree.",
]

ORDINAL: dict = {
    12: "twelfth",
    11: "eleventh",
    10: "tenth",
    9: "ninth",
    8: "eighth",
    7: "seventh",
    6: "sixth",
    5: "fifth",
    4: "fourth",
    3: "third",
    2: "second",
    1: "first"
}


def build_verse(day: int) -> str:
    '''build_verse
    Given an integer value `day`, constructs and returns a string comprised of values from VERSES
    and ORDINAL.
    '''
    verse = f'On the {ORDINAL[day]} day of Christmas my true love gave to me: '
    first_day = f'{" and " if day != 1 else ""}{VERSES[-1]}'
    verse += " ".join(VERSES[12-day:-1]) + first_day
    return verse


def recite(start_verse: int, end_verse: int) -> list:
    '''recite
    This function returns a list comprehension that iterates over a range for
    the values of start_verse and end_verse + 1. // The end value for range is exclusive hence the '+1'.

    For each iteration the value is assigned to a function call to `build_verse()`.
    '''
    return [build_verse(i) for i in range(start_verse, end_verse+1)]
