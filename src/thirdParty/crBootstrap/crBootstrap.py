# Prepare everything about logging, config, international
# Result in one line `from crBootstrap import *` in the main method or file

# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
import crLog as _crLog  # NOQA: E402
import crGlobalLevel as _crGlobalLevel

_crGlobalLevel.crLog = _crLog
_crGlobalLevel.crLog.logging.basicConfig(filename="log.txt", level=_crGlobalLevel.crLog.logging.INFO)  # NOQA: E402
_crGlobalLevel.crLog.logging.info("#========= Start =========#")  # NOQA: E402

# Load config
from crConfig import *  # NOQA: E402
