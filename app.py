import streamlit as st


st.set_page_config(layout="wide")
st.title("Monthly SIP Calculator")

col1, col2 = st.beta_columns((2,1))

with col1:
    num_am=st.number_input(label='mon',min_Value=1,max_value=10000, key='hel')
    num_am.setValue=st.slider(label="Monthly Intallment",min_value=1, max_value=10000, step=1)



with col2:
    




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
    return {'Amount @ Maturity': amount, 'Total Investment' : stt*sm, 'Total Gains':amount-(stt*sm), 'Amount every month': amount_every_month} if show_amount_list else {'Amount @ Maturity': amount,'Total Investment' : stt*sm, 'Total Gains':amount-(stt*sm)} 

if month:
    st.write(sip(sm, stt, sr, princ, False))
else:
    st.write(sip(sm, stt, sr, princ))


