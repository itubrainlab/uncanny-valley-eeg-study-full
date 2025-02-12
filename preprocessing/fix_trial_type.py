import os
from bids import BIDSLayout
import pandas

bids_root = os.environ.get("BIDS_ROOT")

layout = BIDSLayout(bids_root).to_df()

files_to_fix = layout[layout["suffix"] == "events"]["path"]

def fix_col_names(file_name):
    with open(file_name) as f:
        newText=f.read().replace('trial_type', 'temporary_field_xyz').replace('label', 'trial_type').replace('temporary_field_xyz', 'label')

    with open(file_name, "w") as f:
       f.write(newText)

files_to_fix.apply(func=fix_col_names)