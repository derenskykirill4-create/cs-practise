import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    non_empty = [line for line in lines if line.strip() != '']
    valid_records = read_valid(lines)
    total_lines = len(non_empty)
    skipped_count = total_lines - len(valid_records)
    print(len(valid_records))
    print(skipped_count)

    if valid_records:
        avg_temp = average_by_city(valid_records)
        print(f"{avg_temp[warmest_city(valid_records)]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()