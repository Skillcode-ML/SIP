import streamlit as st

st.write("Monthly SIP Calculator")

st.write("Monthly Installment")
pamoun_sli=st.slider(label="",min_value=1, max_value=10000, step=1)
pamoun_enter=st.number_input('',1)

st.write("Selected Amount:")
        if pamoun_enter==1:
           st.write(pamoun_sli)
        else:
           st.write(pamoun_enter)
    
st.write("Rate")
rate_enter=st.number_input('', 1)
rate_sli=st.slider(label="",min_value=1, max_value=100, step=1)

st.write("Selected Rate:")
        if rate_enter==1:
            st.write(rate_sli)
        else:
            st.write(rate_enter)

st.write("Time")
time_enter=st.number_input('', 1)
time_sli=st.slider(label="",min_value=1, max_value=100, step=1)

st.write("Selected Time:")
        if time_enter==1:
            st.write(time_sli)
        else:
            st.write(time_enter)
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

if month:
    st.write(sip(pamoun, time, rate, princ, False))
else:
    st.write(sip(pamoun, time, rate, princ))
