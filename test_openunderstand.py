import sys
from os import getcwd
from os.path import join

sys.path.append(join(getcwd(), "openunderstand"))
sys.path.append(join(getcwd(), "openunderstand", "oudb"))
sys.path.append(join(getcwd(), "openunderstand", "utils"))
from openunderstand.ounderstand.openunderstand import *

start_parsing(
    repo_address=join(getcwd(), "benchmark", "hw6test"),
    db_address=getcwd(),
    db_name="hw.udb",
    engine_core="Python3",
    log_address=join(getcwd(), "a.log"),
)
