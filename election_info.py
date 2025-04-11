import streamlit as st

# 📌 Mapping of states to their election calendar URLs
state_election_urls = {
    "Alabama": "https://www.sos.alabama.gov/alabama-votes/election-information",
    "Alaska": "https://www.elections.alaska.gov/",
    "Arizona": "https://azsos.gov/elections",
    "Arkansas": "https://www.sos.arkansas.gov/elections",
    "California": "https://www.sos.ca.gov/elections",
    "Tennessee": "https://sos.tn.gov/elections/calendar",
    # Add more states as needed
}

# 🔍 Function to get the election calendar URL
def get_election_calendar_url(state_name):
    return state_election_urls.get(
        state_name.title(),
        "❌ Election calendar URL not found for the specified state."
    )

# 🖥️ Streamlit App UI
st.title("🗳️ Local Election Calendar Finder")

state_options = sorted(state_election_urls.keys())
selected_state = st.selectbox("Select your U.S. state:", state_options)

if selected_state:
    url = get_election_calendar_url(selected_state)
    st.success(f"Here's the election calendar for {selected_state}:")
    st.markdown(f"[Click here to view it]({url})")
