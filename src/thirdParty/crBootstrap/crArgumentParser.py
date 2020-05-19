import argparse

# Place some placeholders
commandline_arguments = None

# Simply read command line arguments


def _python_arg_parser():
    global commandline_arguments

    argParser = argparse.ArgumentParser()

    # Input folder(where chm file extracted)
    argParser.add_argument("-i", "--inputFolder",
                           help="Input folder(where chm file extracted)")

    commandline_arguments = argParser.parse_args()

# Preprocess read argument and confirm behavior by specified flags
# the argument should not change by code after preprocess


def _confirm_argument_behavior():
    global commandline_arguments

    # TODO: If there is any boolean argument can override others, they go here
    doNothing = True


def init_argument_parser():
    _python_arg_parser()
    _confirm_argument_behavior()
