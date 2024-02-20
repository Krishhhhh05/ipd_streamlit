import streamlit as st
import pickle



xg_reg=pickle.load(open('xg_reg.pkl','rb'))

def classify(num):
    if num:
        return num 
    
    else:
        return 'wrong'
def main():
    st.title("True Risk Tolerance")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">True risk tolerance</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Linear Regression','Logistic Regression','SVM']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    age=st.slider('Select age ',20.0 , 100.0)
    edu=st.slider('Select education ', 1.0, 5.0)
    married=st.slider('Select married', 1.0, 2.0)
    kids=st.slider('Select kids', 0.0, 7.0)
    lifecl=st.slider('Select lifecl', 1.0, 6.0)
    occat=st.slider('Select occat', 0.0, 4.0)
    income=st.slider('Select income', 0.0, 60000000.0)
    risk=st.slider('Select risk', 0.0, 4.0)
    wsaved=st.slider('Select wsaved ', 1.0, 3.0)
    spendmor=st.slider('Select spendmor', 0.0, 5.0)
    networth=st.slider('Select networth', 0.0, 10000000000.0)
    inputs = [[age, edu, married, kids, lifecl, occat, income, risk, wsaved, spendmor, networth]]

    if st.button('Predict'):
        st.success(classify(xg_reg.predict(inputs)))

        
        


if __name__=='__main__':
    main()