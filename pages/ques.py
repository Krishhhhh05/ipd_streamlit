import streamlit as st
#from model_ques import InvestorProfileModel  # Assuming your model is in a file called investor_profile_model.py

def main():
    st.title('Investor Profile Questionnaire')

    # # Define your questions and choices here
    # questions = [
    #     "What is your preferred investment horizon?",
    #     "How would you describe your risk tolerance?",
    #     "How patient are you with investment returns?",
    #     "How do you approach budgeting for investments?",
    #     "What level of profit margin are you comfortable with in your investments?"
    # ]

    # choices_per_question = [
    #     ['Short-term (less than a year)', 'Medium-term (1-5 years)', 'Long-term (5+ years)', "I'm unsure"],
    #     ['Very conservative', 'Conservative', 'Moderate', 'Aggressive'],
    #     ["I expect quick returns", "I'm willing to wait a few years", "I'm patient and can wait for a decade or more", "I'm not sure"],
    #     ["I don't have a specific budget", "I allocate a small percentage of my income", "I have a well-defined budget for investments", "I'm not sure"],
    #     ["Minimal, but consistent", "Moderate", "High, even with higher risk", "I'm not sure"]
    # ]

    # # Create an instance of InvestorProfileModel
    # investor_model = InvestorProfileModel(questions, choices_per_question)

    st.write("Please answer the following questions:")

    # Iterate through questions and get user input
    # for i, question in enumerate(questions):
    #     user_selection = investor_model.get_user_selection(question, choices_per_question[i])
    #     investor_model.update_profiles(i, user_selection)

    # # Display the results
    # st.write("\nYour top investor profiles:")
    # top_profiles = investor_model.get_top_profiles()
    # for profile, score in top_profiles:
    #     st.write(f"{profile}: {score} points")


if __name__ == "__main__":
    main()
