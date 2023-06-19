import streamlit as st
import openai

def generate_report(brand, competitors):
    prompt = f"I want you to act like an analysis / auditor. I want you to perform an analysis of {brand} with the following top 5 competitors: {', '.join(competitors)}. I need you to assess the differences and similarities between {brand} and {', '.join(competitors)}. I need you to focus on pricing, market positioning, branding, and messaging. Research the relevant market and analyze each brand to identify key differences and similarities. Present all the information in a detailed report that includes charts, graphs, and tables. Based on all the information, let me know how {brand} can improve and actionable steps we can take to make {brand} be better than {', '.join(competitors)}."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    report = response.choices[0].text.strip()

    return report

# Set OpenAI API key
openai.api_key = "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"

# Streamlit app
def main():
    st.title("Brand Analysis App")

    # User inputs
    brand = st.text_input("Enter your brand")
    num_competitors = st.number_input("Enter the number of competitors (1-5)", min_value=1, max_value=5, step=1)
    competitors = []
    for i in range(num_competitors):
        competitor = st.text_input(f"Enter competitor {i+1}")
        competitors.append(competitor)

    if st.button("Generate Analysis"):
        # Generate the analysis report
        analysis_report = generate_report(brand, competitors)

        # Display the report
        st.subheader("Analysis Report")
        st.write(analysis_report)

if __name__ == "__main__":
    main()
