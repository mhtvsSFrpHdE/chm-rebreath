import argparse as _argparse
argument_parser = _argparse.ArgumentParser()

# Simply read command line arguments
# These are code example and common arguments
# add your own on SAL


def _python_arg_parser():
    # Add required arguments
    global argument_parser

    # Input folder(where chm file already extracted)
    argument_parser.add_argument("-i", "--inputFolder",
                                 help="Input folder(where chm file already extracted)")
    # Output folder
    argument_parser.add_argument("-o", "--outputFolder",
                                 help="Output folder")


_python_arg_parser()
