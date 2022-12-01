import argparse
from pathlib import Path
from typing import List


class ElfSupply:
    def __init__(self, calory_supplies: str):
        calory_supply_texts = calory_supplies.split("\n")
        self.calory_supplies = map(int, calory_supply_texts)

    def calory_sum(self) -> int:
        return sum(self.calory_supplies)

    def __str__(self):
        return str(self.calory_supplies)


def parse_input_file(input_filename: str) -> List[ElfSupply]:
    input_filepath = Path(__file__).parent / input_filename
    with input_filepath.open("r") as f:
        input_text = f.read()
        input_text_per_elf = input_text.split("\n\n")
        calory_supplies_per_elf = [
            ElfSupply(calory_supplies_text)
            for calory_supplies_text in input_text_per_elf
        ]
        return calory_supplies_per_elf


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the calory supply for a group of elves"
    )
    parser.add_argument(
        "-i",
        "--input_filename",
        type=str,
        default="sample_input.txt",
        help="File name containing the elves' supplies (located in same folder as day1.py)",
    )
    args = parser.parse_args()

    calory_supplies_per_elf = parse_input_file(args.input_filename)
    calory_sum_per_elf = [
        elf_supply.calory_sum() for elf_supply in calory_supplies_per_elf
    ]

    print(f"Maximum supply carried: {max(calory_sum_per_elf)}")


if __name__ == "__main__":
    main()
