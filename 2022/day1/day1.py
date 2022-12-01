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
    parser.add_argument(
        "--top",
        type=int,
        default=1,
        help="Number of top X elves to calculate the calories for.",
    )
    args = parser.parse_args()

    calory_supplies_per_elf = parse_input_file(args.input_filename)
    calory_sum_per_elf = [
        elf_supply.calory_sum() for elf_supply in calory_supplies_per_elf
    ]

    sorted_calory_sums = sorted(calory_sum_per_elf, reverse=True)
    top_x_calories = sorted_calory_sums[: args.top]
    print(f"Sum of top {args.top} elves' supplies = {sum(top_x_calories)}")


if __name__ == "__main__":
    main()
