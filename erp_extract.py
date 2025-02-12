import os

comp_chs = {
    "LPP": ["CPz", "Cz", "Pz"],
    "N170": ["P8", "P7"],
    "N100": ["F4", "FC4", "F3", "FC3"],
    "P100": ["Oz", "O1", "O2"],
    "N200": ["Fz", "FCz", "Cz", "CPz", "Pz"],
    "P200": ["Fz", "FCz", "Cz", "CPz", "Pz"],
    "P300": ["Fz", "FCz", "Cz", "CPz", "Pz"],
    "N400": ["CPz", "CP4", "CP3", "Pz", "P4", "P3"],
    "P600": ["P3", "Pz", "P4"],
    "ELAN": ["F3","F7"],
    "LAN": ["F3","F7"]
}

bids_root = os.environ.get("BIDS_ROOT")

task="UV"
subjects = 'all'
ch_types = ["eeg"]

l_freq = 0.5
h_freq = 35
notch_freq = 50

spatial_filter = "ica"
ica_reject = "autoreject_local"
reject = "autoreject_global"
autoreject_n_interpolate = [2, 4]
ica_decim = 2

epochs_tmin = -0.2
epochs_tmax = 0.8

conditions = ['eerie', 'not_eerie']
contrasts = [('eerie', 'not_eerie')]

run_source_estimation = False
on_rename_missing_events = "ignore"

parallel_backend = "dask"
dask_worker_memory_limit = "2.5G"
n_jobs = 8

if os.environ.get("COMPONENT") == "LAN":
    exclude_subjects = ["nas"] # No  good channels avalaibale for LAN

analyze_channels = comp_chs[os.environ.get("COMPONENT")]
deriv_root = f"/Users/pabu/Documents/ExperimentsData/UncannyValley/derivatives/{os.environ.get('COMPONENT')}"
