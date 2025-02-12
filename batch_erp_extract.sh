#!/bin/bash

export BIDS_ROOT=/path/to/dataset
export COMPONENT=LPP; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=N170; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=N100; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=P100; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=N200; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=P200; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=P300; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=N400; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=N400; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=P600; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=ELAN; mne_bids_pipeline --config=erp_extract.py
export COMPONENT=LAN; mne_bids_pipeline --config=erp_extract.py