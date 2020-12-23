import argparse
import cow_emulator
import os


def translate(filename):
    with open(filename) as f:
        lines = f.readlines()
    new_lines = []

    filename, file_extension = os.path.splitext(filename)

    if file_extension == ".cow":
        lookup = cow_emulator.command_lookup
        output_filename = filename + ".own"
    elif file_extension == ".own":
        lookup = cow_emulator.get_reverse_commands()
        output_filename = filename + ".cow"
    else:
        raise Exception(f"Expected a '.own' or '.cow' file. Got {filename}")

    for line in lines:
        i = 0
        new_line = ""
        comment1 = line.find(';', )
        if comment1 < 0:
            comment1 = len(line)
        comment2 = line.find('[', )
        if comment2 < 0:
            comment2 = len(line)
        end_line = min(comment1, comment2)

        while i < len(line):
            if (i+3) <= end_line and line[i:i+3] in lookup:
                new_line += lookup[line[i:i+3]]
                i = i+3
            else:
                new_line += line[i]
                i += 1
        new_lines.append(new_line)
    print(f"writing {output_filename}")
    with open(output_filename, 'w') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translating cow files")
    parser.add_argument("file", help="The file that should be translated. If its extension is 'cow' it will"
                                     " be translated to 'own' and vice versa")
    args = parser.parse_args()
    translate(args.file)