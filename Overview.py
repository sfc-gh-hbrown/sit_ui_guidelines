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

st.write("Welcome to the SIT Design Guidelines! This documentation is intended for anyone at Snowflake working on user interfaces with Streamlit, React, or other frameworks.")

st.write("Here you will find guidance on how to use UI components, user experience and user interface best practices, links to design and icon libraries, and how to request help from the SIT Design Team.")

st.info("Feel free to reach out to the Slack channel #sit-design-requests with any feedback or design requests you have.")
