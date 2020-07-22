import argparse as _argparse
argument_parser = _argparse.ArgumentParser()

# Simply read command line arguments
# These are code example and common arguments
# add your own on SAL


def _python_arg_parser():
    # Add required arguments
    global argument_parser

    # Version
    argument_parser.add_argument("--version",
                                 help="Show build number or other version information")


_python_arg_parser()
