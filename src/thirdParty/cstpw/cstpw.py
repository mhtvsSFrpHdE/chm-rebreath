import os as _os
import platform as _platform
import subprocess as _subprocess

_cstpw_file_is_opened = False
_cstpw_have_system_info = False
_cstpw_script_file = None
_cstpw_script_file_encoding = None
_cstpw_script_file_name = None  # Full path and pathlib are recommended but NOT required
_cstpw_system_type = None


# Run only once to get system information
def _cstpw_grab_system_info():
    global _cstpw_have_system_info

    if _cstpw_have_system_info == False:
        # Get system information
        global _cstpw_system_type

        _cstpw_system_type = _platform.system()
        _cstpw_have_system_info = True

# Force close script file and ignore errors like file not opened yet


def _cstpw_force_close():
    try:
        _cstpw_script_file.close()
    except:
        pass
    finally:
        _cstpw_file_is_opened = False


# Set necessary information for cstpw
#
# "cp1252" is the default encoding of Microsoft Windows United Status Edition


def init_cstpw(script_file_name, script_file_encoding="cp1252"):
    _cstpw_grab_system_info()

    # Copy script file name
    global _cstpw_script_file_name
    _cstpw_script_file_name = script_file_name

    # Copy script file encoding
    global _cstpw_script_file_encoding
    _cstpw_script_file_encoding = script_file_encoding

    # Reset script status
    _cstpw_force_close()


# Add a line of command to script, auto \n


def _cstpw_add_command(command_text):
    global _cstpw_script_file
    _cstpw_script_file.write("%s\n" % command_text)

# Write some basic command before any other commands
# to prevent some common bug


def _cstpw_initialize_script(chcp_command=False):
    def _cstpw_init_script_for_windows():
        # If you need "chcp 65001" (Unicode mode) or something
        # cmd.exe mostly not able to recognize first character, e.g. UTF-8 BOM
        _cstpw_add_command("gUsJAzrtybEx >nul 2>nul")

        # Then add chcp if needed, 65001 only available on Windows 7 and later
        if chcp_command != False:
            _cstpw_add_command(chcp_command)

        # Always cd into script directory to prevent current working directory missing bug
        # In rare case like double click script from Windows explorer search results
        # then the one being executed will not able to get it's current working directory
        _cstpw_add_command("cd /d %~dp0")

    if _cstpw_system_type == "Windows":
        _cstpw_init_script_for_windows()
    else:
        raise NotImplementedError

# Open script file and record open status


def _cstpw_create_empty_file():
    global _cstpw_script_file
    global _cstpw_file_is_opened

    _cstpw_force_close()

    _cstpw_script_file = open(_cstpw_script_file_name, "w+", encoding=_cstpw_script_file_encoding)
    _cstpw_file_is_opened = True


# Wrapper method for public usage


def cstpw_create_script(chcp_command=False):
    _cstpw_create_empty_file()
    _cstpw_initialize_script(chcp_command)

# Wrapper method for public usage


def cstpw_write_script(command_text):
    _cstpw_add_command(command_text)

# Wrapper method for public usage
#
# wait: wait for the script to execute complete
#
# new_window: run the script in separate console window
#   if wait=False, new_window will be ignored and always behaves as True


def cstpw_run_script(wait=False, new_window=False):
    def _cstpw_run_script_for_windows():
        if wait:
            myCommand = None

            if new_window:
                # This trick run script on a separate console window
                # but still allow to wait
                myCommand = "start /wait %s" % _cstpw_script_file_name
            # if not require new window
            else:
                myCommand = _cstpw_script_file_name

            # If not redirect stderr to null, when click on close window button
            # the python will print a "^C"
            with open(_os.devnull, 'wb') as null_out:
                myProcess = _subprocess.Popen(myCommand, shell=True, stdout=null_out, stderr=null_out)
                myProcess.wait()

        # else if not wait
        else:
            # Simulate a Windows explorer double click
            _os.startfile(_cstpw_script_file_name)

    _cstpw_force_close()

    if _cstpw_system_type == "Windows":
        _cstpw_run_script_for_windows()
    else:
        raise NotImplementedError
