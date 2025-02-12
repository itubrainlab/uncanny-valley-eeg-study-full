import os
from bids import BIDSLayout
import pandas

bids_root = os.environ.get("BIDS_ROOT")

bad_channels = {
            "amn": [],
            "aul": ['AF4'],
            "brk": ['P8','AF4','O2'], 
            "dqp": ['CP3','O2','FT7','T7','P3','P7','T8','TP8','P8','Pz','O1','Oz','Cz','AF4'],
            "feg": [],
            "fre": ['C3','FT7','T7','T8','TP7','FT8'],
            "gcm": ['O2','AF4'],
            "gop": [],
            "gry": [],
            "hjk": ['TP7'],
            "ihj": ['AF4','FC3'],
            "jkz": ['T7','F4','AF4'],
            "lks": [],
            "lty": ['P8','O2','AF4'],
            "mno": ['O2','T7','AF4'], 
            "nas": ['F3','P8','AF4','O2'], 
            "nlk": ['AF4','AF3','O1','T7'],
            "pkw": ['Fp1','FCz','O2','AF4'],
            "reh": [],
            "rto": ['AF4'],
            "rxi": ['O2','AF4'],
            "sop": ['AF3','AF4'],
            "uqo": ['C3','O2', 'AF4','F8','P7'],
            "veb": ['O2','AF4'],
            "wdf": ['P8','T7','O2','AF4'],
            "xyl": ['O2'],
            "ytl": ['FT7','T7'],
            "zar": ['AF4','O1'],
            "zhf": ['Fp1','AF4','O2'], 
            "zvj": ['P8','T7','AF4','O2']
        }

layout = BIDSLayout(bids_root).to_df()

files_to_fix = layout[layout["suffix"] == "channels"][["path","subject"]]

def fix_subject_channels(row, bad_channels):
    channels_data=pandas.read_csv(row["path"],sep='\t')
    for bc in bad_channels:
        channels_data.loc[channels_data.name == bc, 'status'] = "bad"
    channels_data.to_csv(row["path"],sep='\t')

files_to_fix.apply(lambda r: fix_subject_channels(r, bad_channels[r['subject']]), axis=1)