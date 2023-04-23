import os
import sys

for p in ['../spotlight_ext', '../dice_ext']:
    module_path = os.path.abspath(os.path.join(p))
    if module_path not in sys.path:
        sys.path.append(module_path)