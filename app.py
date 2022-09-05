

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from encoding import encoding

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
st.title("Hotel Customer Bookings")


nationality = st.selectbox('Nationality', df['Nationality'].unique())
age = st.number_input('age')
DaysSinceCreation = st.number_input('DaysSinceCreation')
AverageLeadTime = st.number_input('AverageLeadTime')
LodgingRevenue= st.number_input('LodgingRevenue')
OtherRevenue= st.number_input('OtherRevenue')
BookingsCanceled= st.number_input('BookingsCanceled')
BookingsNoShowed= st.number_input('BookingsNoShowed')
PersonsNights= st.number_input('PersonsNights')
RoomNights= st.number_input('RoomNights')
DaysSinceLastStay= st.number_input('DaysSinceLastStay')
DaysSinceFirstStay= st.number_input('DaysSinceFirstStay')
DistributionChannel = st.selectbox('DistributionChannel',df['DistributionChannel'].unique())
market = st.selectbox('MarketSegment',df['MarketSegment'].unique())
SRHighFloor    = st.selectbox('SRHighFloor',[0, 1])
SRLowFloor = st.selectbox('SRLowFloor',[0, 1])
SRAccessibleRoom  = st.selectbox('SRAccessibleRoom',[0, 1])
SRMediumFloor = st.selectbox('SRMediumFloor',[0, 1])
SRBathtub = st.selectbox('SRBathtub',[0, 1])
SRShower    = st.selectbox('SRShower',[0, 1])
SRCrib= st.selectbox('SRCrib',[0, 1])
SRKingSizeBed= st.selectbox('SRKingSizeBed',[0, 1])
SRTwinBed= st.selectbox('SRTwinBed',[0, 1])
SRNearElevator= st.selectbox('SRNearElevator',[0, 1])
SRAwayFromElevator= st.selectbox('SRAwayFromElevator',[0, 1])
SRNoAlcoholInMiniBar= st.selectbox('SRNoAlcoholInMiniBar',[0, 1])
SRQuietRoom= st.selectbox('SRQuietRoom',[0, 1])


print(str(nationality))
if st.button('Predict Number of Customer CheckedIN'):
    input_df = pd.DataFrame(
        {'Nationality': [encoding(str(nationality))], 'Age': [age], 'DaysSinceCreation': [DaysSinceCreation],
         'AverageLeadTime': [AverageLeadTime], 'LodgingRevenue': [LodgingRevenue], 'OtherRevenue': [OtherRevenue],
         'BookingsCanceled': [BookingsCanceled], 'BookingsNoShowed': [BookingsNoShowed],
         'PersonsNights': [PersonsNights], 'RoomNights': [RoomNights], 'DaysSinceLastStay': [DaysSinceLastStay],
         'DaysSinceFirstStay': [DaysSinceFirstStay], 'DistributionChannel': [DistributionChannel], 'MarketSegment': [market],
         'SRHighFloor': [SRHighFloor], 'SRLowFloor': [SRLowFloor], 'SRAccessibleRoom': [SRAccessibleRoom],
         'SRMediumFloor': [SRMediumFloor], 'SRBathtub': [SRBathtub], 'SRShower': [SRShower], 'SRCrib': [SRCrib],
         'SRKingSizeBed': [SRKingSizeBed], 'SRTwinBed': [SRTwinBed], 'SRNearElevator': [SRNearElevator],
         'SRAwayFromElevator': [SRAwayFromElevator], 'SRNoAlcoholInMiniBar': [SRNoAlcoholInMiniBar],
         'SRQuietRoom': [SRQuietRoom]}
    )
    st.title(pipe.predict(input_df))