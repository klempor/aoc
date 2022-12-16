from argparse import ArgumentParser
from typing import Sequence


def get_all_calories_records_from_file(filename: str) -> Sequence[Sequence[int]]:
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


def get_command_line_arguments():
    parser = ArgumentParser()
    parser.add_argument("input_file", default=None)
    return parser.parse_args()


def main():
    command_line_arguments = get_command_line_arguments()

    if command_line_arguments.input_file is None:
        pass
    else:
        elves_calories_records = get_all_calories_records_from_file(
            command_line_arguments.input_file
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
