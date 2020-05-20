import argparse as _argparse


# Simply read command line arguments
# These are code example and common arguments
# add your own on SAL


def _python_arg_parser(argParser):
    # Input folder(where chm file extracted)
    argParser.add_argument("-i", "--inputFolder",
                           help="Input folder(where chm file extracted)")

    return argParser.parse_args()

# Preprocess read argument and confirm behavior by specified flags
# the argument should not change by code after preprocess


def _confirm_argument_behavior(commandline_arguments):
    # TODO: If there is any boolean argument can override others, they go here

    return commandline_arguments


def _init_argument_parser(argParser):
    parsedArgs = _python_arg_parser(argParser)
    parsedArgs = _confirm_argument_behavior(parsedArgs)

    return parsedArgs


# Export argument for later use
argument_parser = _argparse.ArgumentParser()
commandline_arguments = _init_argument_parser(argument_parser)
