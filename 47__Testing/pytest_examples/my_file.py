import sys


def parsing_command_line_parameters(is_print=False):
    """
    The function parses the command line parameters and returns the parameter with index 2.
    :return: The command line parameter with index 2
    """
    if is_print:
        print(sys.argv)
    return sys.argv[2]


if __name__ == '__main__':
    parsing_command_line_parameters(is_print=True)


# python my_file.py 1 2 3

# ['my_file.py', '1', '2', '3']
