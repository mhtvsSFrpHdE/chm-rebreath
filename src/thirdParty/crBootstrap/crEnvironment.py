# 3rd
import os

from pathlib import Path as plPath  # Path
from os import path as osPath

# My
from crExceptionSal import *
from crLogHeader import *
import crDevInput  # Information used while development

# Module scope config
message_config_local = None

# Receive config


def init_environment(message_config):
    global message_config_local

    message_config_local = message_config

# Create folder if not exist


def crCreateFolder(myFolder):
    folder_exist = False
    if osPath.exists(myFolder) is False:
        try:
            os.mkdir(myFolder)
            folder_exist = True
        except:
            error_message = message_config_local['err']['failed_to_create_output_folder']
            crPrintCyan(error_message)
            raise CrEnvironmentError(error_message)
    # else if myFolder already exist
    else:
        folder_exist = True # TODO: What's this? Undocumented behavior