import cstpw as _cstpw

# Module scope config
environment_config_local = None

# Receive config
def init_crUnpack(environment_config):
    global environment_config_local
    environment_config_local = environment_config

    script_file_name = environment_config_local['cstpw']['script_file_name']

    _cstpw.init_cstpw(script_file_name)

def unpack_chm_file():
    _cstpw.cstpw_create_script()
    _cstpw.cstpw_write_script("pause")
    _cstpw.cstpw_run_script(wait = True, new_window = True)