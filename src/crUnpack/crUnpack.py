import cstpw as _cstpw
import crGlobalLevel as _crGlobalLevel

# Module scope config
_environment_config_local = None

# Receive config
def init_crUnpack():
    global _environment_config_local
    _environment_config_local = _crGlobalLevel.environment_config

    script_file_name = _environment_config_local['cstpw']['script_file_name']

    _cstpw.init_cstpw(script_file_name)

def unpack_chm_file():
    _cstpw.cstpw_create_script()
    _cstpw.cstpw_write_script("pause")
    _cstpw.cstpw_run_script(wait = True, new_window = True)