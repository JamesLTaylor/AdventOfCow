import argparse
import cow_emulator


def run(file, code_format, max_steps, mem_init=None, debug=False):
    """
    Convert the file into a list of commands and run it.

    :param mem_init:
    :param file:
    :param code_format:
    :param max_steps:
    :param debug:
    :return:
    """
    print(f"running Cow script: {file}. Format={code_format}. Will stop after {max_steps} steps")

    with open(file) as f:
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
    prog = prog.replace(' ', '')
    prog = prog.replace('\n', '')
    prog_list = []
    i = 0
    while i < len(prog):
        cmd = prog[i: i + 3]
        prog_list.append(cmd)
        i += 3

    cow_emulator.run(prog_list, max_steps, code_format == "cow", mem_init, debug)


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
    run(args.file, args.format, args.stop)
