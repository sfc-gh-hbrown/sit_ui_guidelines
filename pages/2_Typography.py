import streamlit as st


st.set_page_config(layout="wide")

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
[data-testid="stPopoverButton"]{
	color: #262730;
	border-color: #BFC5D3;
}

[data-testid="stPopoverButton"]:hover {
	color: #262730;
	border-color: #808495;
}

[data-testid="stPopoverButton"]:active{
	color: #262730;
	border-color: #262730;
	background-color:transparent;
}
[data-testid="stPopoverButton"]:focus:not(:active) {
	color: #262730;
	border-color: #262730;
	background-color:transparent;
}

</style>
	""")

st.title("SIT Design System")
st.header("Typography")

st.write("Streamlit apps have the font **Source Sans Pro** by default. However, fonts can be customized for Streamlit and other frameworks if needed.")
st.write("Here is a recommended Streamlity typeface library with font sizes and styles using the default font:")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:44px"><b> App Title - 44 Bold </b></p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:44px"><b> App Title - 44 Bold </b></p>""")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:36px"><b> Header - 36 Bold </b></p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:36px"><b> Header - 36 Bold </b></p>""")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:24px; font-family:'Source Sans Pro Semibold', sans-serif;"> Subheader - 24 SemiBold</p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:24px; font-family:'Source Sans Pro Semibold', sans-serif;"> Subheader - 24 SemiBold</p>""")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:20px; font-family:'Source Sans Pro Semibold', sans-serif;"> Section Titles - 20 SemiBold</p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:24px; font-family:'Source Sans Pro Semibold', sans-serif;"> Subheader - 24 SemiBold</p>""")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:16px">Body - 16 regular</p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:16px">Body - 16 regular</p>""")

with st.expander("", expanded=True):
	st.html("""<p style="font-size:14px">Labels - 14 regular</p>""")
	with st.popover("Copy code"):
		st.code("""<p style="font-size:14px">Labels - 14 regular</p>""")