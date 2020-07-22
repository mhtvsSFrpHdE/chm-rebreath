# Read any potential input from user or runtime config
# To confirm what's the purpose of this startup

import crLog as _crLog


# TODO: If there is any boolean argument can override others, they go here
# Preprocess read argument and confirm behavior by specified flags
# the argument should not change by code after preprocess


class _RuntimeInput:
    useConfigFile = False

    configFile = None
    inputFolder = None
    outputFolder = None

    def __init__(self, commandline_arguments):
        if commandline_arguments.configFile is not None:
            self.useConfigFile = True
            self.configFile = commandline_arguments.configFile

            _crLog.crPrintCyan("Running in config as arguments mode")
            _crLog.crPrintCyan(self.configFile)

        self.inputFolder = commandline_arguments.inputFolder
        self.outputFolder = commandline_arguments.outputFolder


def get_runtime_input(commandline_arguments):
    return _RuntimeInput(commandline_arguments)
