import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
import src