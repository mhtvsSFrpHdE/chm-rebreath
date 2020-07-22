# 3rd
import os as _os

from pathlib import Path as _plPath  # Path
from os import path as _osPath

# My
import crExceptionSal as _crException
import crLog as _crLog
import crDevInput  # Information used while development

# Module scope config
_message_config_local = None

# Receive config


def init_environment(message_config):
    global _message_config_local

    _message_config_local = message_config

# Create folder if not exist


def crCreateFolder(myFolder):
    folder_exist = False
    if _osPath.exists(myFolder) is False:
        try:
            _os.mkdir(myFolder)
            folder_exist = True
        except:
            error_message = _message_config_local['err']['failed_to_create_output_folder']
            _crLog.crPrintCyan(error_message)
            raise _crException.CrEnvironmentError(error_message)
    # else if myFolder already exist
    else:
        folder_exist = True # TODO: Undocumented behavior, should we actually ignore the folder exist problem?
