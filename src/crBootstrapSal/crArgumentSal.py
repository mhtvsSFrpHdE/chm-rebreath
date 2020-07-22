from crArgument import *

# Add project specified command line arguments


def _my_arg_parser():
    # Set required arguments
    global argument_parser

    # Use config file to fill arguments
    argument_parser.add_argument("-c", "--configFile",
                                help="Ignore any other argument and use config to fill runtime input")

    # Input folder(where chm file already extracted)
    argument_parser.add_argument("-i", "--inputFolder",
                                 help="Input folder(where chm file already extracted)")
    # Output folder
    argument_parser.add_argument("-o", "--outputFolder",
                                 help="Output folder")

    # TODO: Add more arguments

# Request parse arguments
# If failed to get arguments, software will do nothing and exit
# If no arguments are given, software should print version information,
# but till now the software were uncompleted.


def _request_arguments_parse():
    myArgs = None
    # Collect arguments
    try:
        myArgs = argument_parser.parse_args()
    except:
        raise

    return myArgs


# Run code
_my_arg_parser()

# Export argument for later use
commandline_arguments = _request_arguments_parse()
