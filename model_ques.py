import streamlit as st
import pickle
class InvestorProfileModel:
    profiles = {
    'Opportunistic Trend Follower': 0,
    'High-Risk Speculator': 0,
    'Passive Index Investor': 0,
    'Informed Fundamental Investor': 0,
    'Diversified Portfolio Builder': 0,
    'Strategic Value Investor': 0,
    'Retirement Income Planner': 0,
    'Active Swing Trader': 0
}
    # def __init__(self, questions, choices_per_question, profiles):
    #     self.questions = questions
    #     self.choices_per_question = choices_per_question
    #     self.profiles = profiles
    def __init__(self, questions, choices_per_question, profiles=None):
        self.questions = questions
        self.choices_per_question = choices_per_question
    investor_model=pickle.load(open('investor_model.pkl','rb'))

   
    

    # def save_model(self, filename):
    #     with open(filename, 'wb') as file:
    #         pickle.dump(self, file)

    @classmethod
    def load_model(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_user_selection(self, question, choices):
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")

        # Get user selection
        selection = int(input(f"Select an option [1-{len(choices)}]: "))
        return selection

    def update_profiles(self, question_index, selection,profiles):
        # Update profiles based on user selection
        if question_index == 0:  # Example for the first question
            if selection == 1:  # short-term
                self.profiles['Opportunistic Trend Follower'] += 1
                self.profiles['High-Risk Speculator'] += 1
                self.profiles['Active Swing Trader'] += 1
            elif selection == 2:  # medium-term
                self.profiles['Informed Fundamental Investor'] += 1
                self.profiles['Strategic Value Investor'] += 1
            elif selection == 3:  # long-term
                self.profiles['Passive Index Investor'] += 1
                self.profiles['Diversified Portfolio Builder'] += 1
                self.profiles['Retirement Income Planner'] += 1
            elif selection == 4:  # unsure
                self.profiles['Passive Index Investor'] += 1
                self.profiles['Diversified Portfolio Builder'] += 1

        elif question_index == 1:  # Example for the second question
            if selection == 1:  # Very conservative
                self.profiles['Passive Index Investor'] += 1
            elif selection == 2:  # Conservative
                self.profiles['Passive Index Investor'] += 1
                self.profiles['Diversified Portfolio Builder'] += 1
            elif selection == 3:  # Moderate
                self.profiles['Informed Fundamental Investor'] += 1
                self.profiles['Strategic Value Investor'] += 1
            elif selection == 4:  # Aggressive
                self.profiles['Opportunistic Trend Follower'] += 1
                self.profiles['High-Risk Speculator'] += 1
                self.profiles['Active Swing Trader'] += 1
        elif question_index == 2:  # Example for the third question
            if selection == 1:  # Quick returns
               self.profiles['Opportunistic Trend Follower'] += 1
               self.profiles['High-Risk Speculator'] += 1
               self.profiles['Active Swing Trader'] += 1

            elif selection == 2:  # Wait a few years
               self.profiles['Informed Fundamental Investor'] += 1
               self.profiles['Strategic Value Investor'] += 1
               self.profiles['Active Swing Trader'] += 1
            elif selection == 3:  # Wait for a decade or more
               self.profiles['Passive Index Investor'] += 1
               self.profiles['Diversified Portfolio Builder'] += 1
               self.profiles['Retirement Income Planner'] += 1
            elif selection == 4:  # Unsure
               self.profiles['Passive Index Investor'] += 1
               self.profiles['Diversified Portfolio Builder'] += 1
        elif question_index==3:
            if selection == 1:
             self.profiles['Opportunistic Trend Follower'] += 1
             self.profiles['High-Risk Speculator'] += 1
            elif selection == 2:
               self.profiles['Informed Fundamental Investor'] += 1
               self.profiles['Strategic Value Investor'] += 1
               self.profiles['Active Swing Trader'] += 1
            elif selection == 3:
               self.profiles['Passive Index Investor'] += 1
               self.profiles['Diversified Portfolio Builder'] += 1
               self.profiles['Retirement Income Planner'] += 1
            elif selection == 4:
               self.profiles['Passive Index Investor'] += 1
               self.profiles['Diversified Portfolio Builder'] += 1
        elif question_index==4:
            if selection == 1:
             self.profiles['Informed Fundamental Investor'] += 1
             self.profiles['Strategic Value Investor'] += 1
             self.profiles['Retirement Income Planner'] += 1

            elif selection == 2:
             self.profiles['Strategic Value Investor'] += 1
             self.profiles['Opportunistic Trend Follower'] += 1


            elif selection == 3:
             self.profiles['High-Risk Speculator'] += 1
             self.profiles['Active Swing Trader'] += 1
             self.profiles['Diversified Portfolio Builder'] += 1
            elif selection == 4:
               self.profiles['Passive Index Investor'] += 1
               self.profiles['Diversified Portfolio Builder'] += 1

    def run(self):
        for i, question in enumerate(self.questions):
            user_selection = self.get_user_selection(question, self.choices_per_question[i])
            self.update_profiles(i, user_selection)

        # Display top profiles
        top_profiles = sorted(self.profiles.items(), key=lambda x: x[1], reverse=True)[:3]

        print("\nYour top investor profiles:")
        for profile, score in top_profiles:
            print(f"{profile}: {score} points")
        top_profiles = sorted(self.profiles.items(), key=lambda x: x[1], reverse=True)[:3]
        st.write(top_profiles)

        return top_profiles
    def main():
        if st.button('Predict'):
            st.success(run(investor_model.predict()))
        else:
           st.write('error')

    
       
# Example Usage:

questions = [
        "What is your preferred investment horizon?",
        "How would you describe your risk tolerance?",
        "How patient are you with investment returns?",
        "How do you approach budgeting for investments?",
        "What level of profit margin are you comfortable with in your investments?"
        # Add more questions as needed
    ]

choices_per_question = [
        ['Short-term (less than a year)', 'Medium-term (1-5 years)', 'Long-term (5+ years)', "I'm unsure"],
        ['Very conservative', 'Conservative', 'Moderate', 'Aggressive'],
        ["I expect quick returns", "I'm willing to wait a few years", "I'm patient and can wait for a decade or more", "I'm not sure"],
        ["I don't have a specific budget", "I allocate a small percentage of my income", "I have a well-defined budget for investments", "I'm not sure"],
        ["Minimal, but consistent", "Moderate", "High, even with higher risk", "I'm not sure"]
    ]



investor_model = InvestorProfileModel(questions, choices_per_question)
pickle.dump(investor_model,open('investor_model.pkl','wb'))
if __name__=='__main__':
    main()


# import streamlit as st
# import pickle

# class InvestorProfileModel:
#     def __init__(self, questions, choices_per_question, profiles=None):
#         self.questions = questions
#         self.choices_per_question = choices_per_question
#         self.profiles = profiles

#     # Define other methods as needed

# def load_model(filename):
#     with open(filename, 'rb') as file:
#         return pickle.load(file)

# def main():
#     st.title('Investor Profile Questionnaire')

#     # Load the investor model
#     investor_model = load_model('investor_model.pkl')

#     st.write("Please answer the following questions:")

#     # Iterate through questions and get user input
#     for i, question in enumerate(investor_model.questions):
#         user_selection = investor_model.get_user_selection(question, investor_model.choices_per_question[i])
#         investor_model.update_profiles(i, user_selection)

#     # Display the results
#     st.write("\nYour top investor profiles:")
#     top_profiles = investor_model.get_top_profiles()
#     for profile, score in top_profiles:
#         st.write(f"{profile}: {score} points")


# if __name__ == "__main__":
#     main()
