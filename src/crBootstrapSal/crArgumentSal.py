from crArgument import *

# Read command line arguments


def _my_arg_parser():
    # Set required arguments
    global argument_parser

    # TODO: Add more arguments

    myArgs = None
    # Collect arguments
    try:
        myArgs = argument_parser.parse_args()
    except:
        raise

    return myArgs


# Export argument for later use
commandline_arguments = _my_arg_parser()
