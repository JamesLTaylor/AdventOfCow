import sys
import argparse
import cow_emulator


def run(args):
    if len(sys.argv) > 0:
        print(f"running Cow script: {args.file}. Format={args.format}. Will stop after {args.stop} steps")

    with open(args.file) as f:
        lines = f.readlines()

    # remove comments
    new_lines = []
    for line in lines:
        index = line.find('[')
        if index >= 0:
            line = line[:index]
        index = line.find(';')
        if index >= 0:
            line = line[:index]
        if len(line) > 0:
            new_lines.append(line)

    prog = "".join(new_lines)
    cow_emulator.run(prog, args.stop, args.format == "cow")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Running Cow files.")
    parser.add_argument("file", help="The file that should be executed.")
    parser.add_argument("--format", "--f", choices=['cow', 'own'], default="cow",
                        help="The format of the file to run. Either a pure cow file or an 'own' format file"
                             "which is slightly human readable cow that make debugging a bit easier.")
    parser.add_argument("--stop", default=10000, type=int, help="The maximum number of steps that should be "
                                                                "executed while the program is running. This is to save "
                                                                "you from infinite loops. Sometimes to the mooing can be "
                                                                "incessant.")
    args = parser.parse_args()
    run(args)
