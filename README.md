# Data Analysis of the 2023 EEG Study of the Origins of the Uncanny Valley Phenomenon

This project contains all the necessary scripts to replicate the results of the paper: [TBD]

The dataset is available on Zenodo at https://zenodo.org/records/14864689

To procedure to run the complete analysis is:
1. Download the dataset from Zenodo
2. Set the BIDS_ROOT environmental variable to the dataset path and, set the bids_root variable to the correct path in the Python notebooks
3. Install all the necessary libraries defined in the requirements.txt file
4. Edit the BIDS_ROOT variable in the batch_erp_extract.sh
5. Execute the preprocessing/fix_trial_type.py script
6. Execute the batch_erp_extract.sh script
7. Open and execute the group_analysis python notebook
8. Open and execute the single_subject_analysis python notebook
