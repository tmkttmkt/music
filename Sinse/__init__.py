import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# カレントディレクトリをsys.pathに追加
if current_dir not in sys.path:
    sys.path.append(current_dir)

from .sinse import *
print("utils package is being imported")
