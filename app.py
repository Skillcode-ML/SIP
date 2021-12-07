import streamlit as st

pamoun=st.number_input('Monthly Installment', 1)
rate=st.number_input('Rate', 1)
time=st.number_input('Time', 1)
princ=st.number_input('Principal Amount', 1)
month=st.checkbox("In Months")
if month:
    st.write(sip(pamoun, time, rate, princ, False))
else:
    st.write(sip(pamoun, time, rate, princ))

def sip(investment, tenure, interest, amount=0, is_year=True, is_percent=True, show_amount_list=True):
    tenure = tenure*12 if is_year else tenure
    interest = interest/100 if is_percent else interest
    interest /= 12
    amount_every_month = {}
    for month in range(tenure):
        amount = (amount + investment)*(1+interest)
        amount_every_month[month+1] = amount
    return {'Amount @ Maturity': amount, 'Amount every month': amount_every_month} if show_amount_list else {'Amount @ Maturity': amount} 
