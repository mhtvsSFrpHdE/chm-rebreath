# Read any potential input from user or runtime config
# To confirm what's the purpose of this startup

import crExceptionSal as _crException
import crGlobalLevel as _crGlobalLevel

_message_config_local = None

# TODO: If there is any boolean argument can override others, they go here
# Preprocess read argument and confirm behavior by specified flags
# the argument should not change by code after preprocess


class _RuntimeInput:
    def __init__(self, commandline_arguments):
        # Create variable

        # Config file as argument
        self.configFileAsArgument = False
        # Related data
        self.configFile = None

        # Unpack chm file or folder mode(already unpacked)
        self.useChmFile = False
        self.useUnpackedFolder = False
        # Related data
        self.inputChm = None
        self.inputFolder = None

        # Where to save output
        self.outputFolder = None

        # Fill variable
        #
        #
        #
        # When these happen,
        # show information only and exit(no need to parse other argument)
        if commandline_arguments.version:
            return

        # If specified config file as argument
        if commandline_arguments.configFile is not None:
            self.configFileAsArgument = True
            self.configFile = commandline_arguments.configFile

            # No need to parse other argument
            return

        # Other argument

        # inputChm
        if commandline_arguments.inputChm is not None:
            self.useChmFile = True
            self.inputChm = commandline_arguments.inputChm
        # inputFolder(if chm already unpacked)
        elif commandline_arguments.inputFolder is not None:
            self.useUnpackedFolder = True
            self.inputFolder = commandline_arguments.inputFolder
        # Input not found
        else:
            error_message = _message_config_local['err']['wrong_run_argument'] + _message_config_local['err']['input_not_provided']
            _crGlobalLevel.crLog.crPrintCyan(error_message)
            raise _crException.CrRunArgumentError(error_message)

        # outputFolder(required)
        if commandline_arguments.outputFolder is not None:
            self.outputFolder = commandline_arguments.outputFolder
        else:
            error_message = _message_config_local['err']['wrong_run_argument'] + 'outputFolder'
            _crGlobalLevel.crLog.crPrintCyan(error_message)
            raise _crException.CrRunArgumentError(error_message)


def get_runtime_input(commandline_arguments):
    return _RuntimeInput(commandline_arguments)


def init_input_sal():
    global _message_config_local
    _message_config_local = _crGlobalLevel.message_config
