import streamlit as st
from style.style import sit_style

st.set_page_config(layout="wide",initial_sidebar_state="expanded")

st.html(sit_style)

st.html("""
<style>
[data-testid="stSidebar"]{
	background-color: #11567F;
}
[data-testid="stSidebarNavLink"] span{
	color: white;
	# text-decoration-line: underline transparent;
 }

# [data-testid="stSidebarNavLink"] :active span{
#  }

</style>
	""")


st.header("Overview")


st.write("Welcome to the Solution Innovation Team Design Guidelines!")
st.write("This documentation is intended for anyone at Snowflake working on user interfaces with Streamlit.")
st.write("This tool provides ready-to-use code snippets, style guidelines, and reusable components to ensure a consistent look and feel that aligns with SIT’s design standards.")
st.info("Feel free to reach out to the Slack channel #sit-design-requests with any feedback or design requests you have.")
