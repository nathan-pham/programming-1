# Filename:     closest_average.py
# Date:         2/18/2022
# Purpose:      number closest to average in a list
# Name:         Nathan Pham


def get_avg(array: list) -> float:
    return sum(array) / len(array)


def closest_average(array: list) -> int:
    """
    get the number closest to an average in a list
    """

    avg = get_avg(array)
    avg_array = [abs(avg - num) for num in array]
    return array[avg_array.index(min(avg_array))]


def main() -> None:
    scores = [78, 66, 89, 77, 43, 95, 98, 92, 90, 67, 99, 82, 65, 72]
    print(f"the number closest to the average {get_avg(scores)} is {closest_average(scores)}")


if __name__ == "__main__":
    main()
