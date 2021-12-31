# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 01:26:10 2021
@author: wynin
"""

#########################################################
# Imports modules
#########################################################

import array
import argparse
import base64
import csv
import numpy as np
import os
import pandas as pd
import sys

from ast import literal_eval

#########################################################
# Functions
#########################################################



maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
        
os.chdir("C:/Users/wynin/Documents/git/ECG_Extract_Wave/data")

extracted_file = "./test.csv"
mycsv = csv.DictReader(open(extracted_file, encoding="utf-8-sig"))
headers = mycsv.fieldnames

for row in mycsv:
    lines = row['RestingECG.Waveform']
    filename = row['__FileName']
    patid = row['RestingECG.PatientDemographics.PatientID']
    date = row['RestingECG.TestDemographics.AcquisitionDate']
    ecg_list = literal_eval(str(lines))

    ## Find 500Hz lead data else 250Hz
    for i in range(len(ecg_list)):
        # lead_data = literal_eval(str(ecg_list[i]))['LeadData']
        # if literal_eval(str(lead_data))[0]['LeadSampleCountTotal']=='5000':
        #     ecg_dict = ecg_list[i]
        # elif literal_eval(str(lead_data))[0]['LeadSampleCountTotal']=='2500':
        #     ecg_dict = ecg_list[i]
        # else:
        #     print("lead count error")
        ecg_dict = ecg_list[i]


    for i in range(len(ecg_list)):
        lead_data = literal_eval(str(ecg_list[i]))['LeadData']
        if literal_eval(str(lead_data))[0]['LeadSampleCountTotal']=='5000':
            ecg_dict = ecg_list[i]
        elif literal_eval(str(lead_data))[0]['LeadSampleCountTotal']=='2500':
            ecg_dict = ecg_list[i]
        else:
            print("lead count error")
        ecg_dict = ecg_list[i]
        
        
# ecg_list[0].get('LeadData',{})[0].get('LeadByteCountTotal',{})



## I

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "I":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])
   
            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict = {'I': lead_vals}

## II

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "II":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['II'] = lead_vals


## V1

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V1":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V1'] = lead_vals

## V2

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V2":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V2'] = lead_vals

    ## V3

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V3":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V3'] = lead_vals

## V4

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V4":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V4'] = lead_vals

## V5

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V5":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])
    
            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V5'] = lead_vals

## V6

    for i in range(len(ecg_dict['LeadData'])):
        if literal_eval(str(ecg_dict['LeadData'][i]))['LeadID'] == "V6":
            raw_wave=ecg_dict['LeadData'][i]['WaveFormData']
            laupb = float(literal_eval(str(ecg_dict['LeadData'][i]))['LeadAmplitudeUnitsPerBit'])

            wave_decoded = base64.b64decode(raw_wave)
            lead_vals = np.array(array.array('h', wave_decoded))
            lead_vals = (lead_vals*laupb).astype(int)

    result_dict['V6'] = lead_vals

    result_dict['III'] = np.subtract(result_dict['II'], result_dict['I']).astype(int)
    result_dict['aVR'] = (np.add(result_dict['I'], result_dict['II'])*(-0.5)).astype(int)
    result_dict['aVL'] = np.subtract(result_dict['I'], 0.5*result_dict['II']).astype(int)
    result_dict['aVF'] = np.subtract(result_dict['II'], 0.5*result_dict['I']).astype(int)

    df = pd.DataFrame.from_dict(result_dict) 

    df.to_csv(patid +"_"+ date.split('-',1)[0] + ".csv", index=False)
        

