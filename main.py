#!/usr/bin/env python3

import disease_data, diseases

# where to read the raw disease occurence data from
disease_data.path = 'ADULT.xlsx'

# where to save the cleaned version
disease_data.clean_path = 'cleaned.xlsx'

# read data
diseases.data = disease_data.read()

dfs = []
# for each disease
for disease in diseases.types:
    # clean the associated data and arrange according to criteria in GAN Experiment Instructions_Google Datasets.docx
    # place each clean disease dataframe in a list
    dfs.append(diseases.arrange_disease(disease))
    disease.partition_tract_nos = diseases.partition_tract_nos(disease)


breakpoint()
# wirte the combined clean dataframes
# disease_data.write_clean(dfs)
