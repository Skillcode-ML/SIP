import streamlit as st

st.write("Monthly SIP Calculator")

st.write("Monthly Installment")
pamoun_sli=st.slider(label="Monthly Intallment",min_value=1, max_value=10000, step=1)
pamoun_enter=st.number_input('Monthly',1)

if pamoun_enter==1:
   sm=(pamoun_sli)
else:
   sm=(pamoun_enter)
st.write("Selected Amount:",sm)
    
st.write("Rate")
rate_enter=st.number_input('Rate', 1)
rate_sli=st.slider(label="Rate",min_value=1, max_value=100, step=1)

if rate_enter==1:
   sr=(rate_sli)
else:
   sr=(rate_enter)
st.write("Selected Rate:",sr)

st.write("Time")
time_enter=st.number_input('Time', 1)
time_sli=st.slider(label="Time",min_value=1, max_value=100, step=1)

if time_enter==1:
   stt=(time_sli)
else:
   stt=(time_enter)
st.write("Selected Time:")
month=st.checkbox("In Months")

princ=st.number_input('Principal Amount', 1)

show_list=st.checkbox("Show Monthly Details")

def sip(investment, tenure, interest, amount=0, is_year=True, is_percent=True, show_amount_list=show_list):
    tenure = tenure*12 if is_year else tenure
    interest = interest/100 if is_percent else interest
    interest /= 12
    amount_every_month = {}
    for month in range(tenure):
        amount = (amount + investment)*(1+interest)
        amount_every_month[month+1] = amount
    return {'Amount @ Maturity': amount, 'Amount every month': amount_every_month} if show_amount_list else {'Amount @ Maturity': amount} 

st.write("Total Investment = ", stt*sm)
st.write("Total Gains = ", amount-(stt*sm))
if month:
    st.write(sip(pamoun, time, rate, princ, False))
else:
    st.write(sip(pamoun, time, rate, princ))


