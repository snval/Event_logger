import argparse
import pathlib

parser = argparse.ArgumentParser(description="Выберем файл и отбразим содержимое")
parser.add_argument('file', type=argparse.FileType('r'), help="Добавьте тимя файла .xtx")
args = parser.parse_args()


with args.file as file2:
    for line in file2:
        print(line.strip())