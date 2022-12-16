from argparse import ArgumentParser, Namespace
from typing import Sequence


def get_all_calories_records_from_file(filename: str) -> Sequence[Sequence[int]]:
    """
    Retrieve the calories records from a file
    """
    all_calories_records = []
    current_calories_records = []

    with open(filename, "r") as input_file:
        for record in input_file:
            record = record.rstrip()

            # Empty line signals that the records for the current elf has finished
            if not record:
                all_calories_records.append(current_calories_records)
                current_calories_records = []
            else:
                calorie_record = int(record)
                current_calories_records.append(calorie_record)

    return all_calories_records


def get_all_calories_records_from_input() -> Sequence[Sequence[int]]:
    """
    Retrieve the calories records from input
    """
    all_calories_records = []
    current_calories_records = []
    while True:
        input_line = input()
        # Both empty line and empty calories records signals that the input finished
        if not input_line and not current_calories_records:
            break

        # Empty line signals that the records for the current elf has finished
        elif not input_line:
            all_calories_records.append(current_calories_records)
            current_calories_records = []
        else:
            current_calories_records.append(int(input_line))

    if not all_calories_records:
        raise RuntimeError("No calories records where supplied!")

    return all_calories_records


def get_command_line_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        metavar="<input_filename>",
        default=None,
        dest="input_filename",
        help="The file to read the calories records from",
    )
    return parser.parse_args()


def main():
    command_line_arguments = get_command_line_arguments()

    if command_line_arguments.input_filename is None:
        elves_calories_records = get_all_calories_records_from_input()
    else:
        elves_calories_records = get_all_calories_records_from_file(
            filename=command_line_arguments.input_filename
        )

    elves_calories_count = [
        sum(elf_calories_count) for elf_calories_count in elves_calories_records
    ]
    best_calories_count = max(elves_calories_count)
    best_calories_count_elf_number = elves_calories_count.index(best_calories_count) + 1
    print(
        f"Elf {best_calories_count_elf_number} carries the most calories: {best_calories_count}"
    )


if __name__ == "__main__":
    main()
