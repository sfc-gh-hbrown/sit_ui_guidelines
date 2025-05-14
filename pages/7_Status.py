import streamlit as st
import time

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


st.header("Status")


css = """
<style>
    /* This is the main container for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-list"]{
    background:transparent;
}
/*Every tab is a button element*/
.st-key-styled_tabs button{
    # width:33%;
    # border-radius:10px;
}

/*Styles the selected tab*/
.st-key-styled_tabs button[aria-selected="true"]{
    # background-color:#eaeaea;
}
.st-key-styled_tabs button[aria-selected="true"] p{
    color:#11567F;
    # font-weight:bold;
}

/* This is the bottom ruler for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-border"]{
    # background-color:blue;
}

/* This highlights selected tab*/
.st-key-styled_tabs div[data-baseweb="tab-highlight"]{
    background-color:darkgrey;
    # height:7px;
}

/* This is the bottom ruler for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-border"]{
    # background-color:blue;
}

/* This is the body of the tab content*/
.st-key-styled_tabs div[data-baseweb="tab-panel"]{
    # background-color:#eaeaea;
}
</style>"""
st.html(css)


with st.container(key="styled_tabs"):
	tab1, tab2 = st.tabs(["Call Outs", "Progress Bar"])

	with tab1:
		st.write("**Call Outs:** For highlighting important information or feedback.")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Success")
		with button:
			st.success("Sample text goes here",icon=":material/check_circle:")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Info")
		with button:
			st.info("Sample text goes here",icon=":material/info:")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Warning")
		with button:
			st.warning("Sample text goes here",icon=":material/warning:")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Error")
		with button:
			st.error("Sample text goes here",icon=":material/info:")

		with st.popover("Copy Code"):
			st.code('''
				st.success("Sample text goes here",icon=":material/check_circle:")
				st.info("Sample text goes here",icon=":material/info:")
				st.warning("Sample text goes here",icon=":material/warning:")
				st.error("Sample text goes here",icon=":material/info:")
				''')

	with tab2:
		st.write("**Progress Bar:** For representing the completion of a task")

		st.write("**Example**")

		st.progress(60,text="Uploading")

		st.html("""
			<style>
				.stProgress > div > div > div > div{
					background-color: #11567F;
				}
			</style>
			""")
		with st.popover("Copy Code"):
			st.code('''
				st.progress(60,text="Uploading")
				st.html("""
					<style>
						.stProgress > div > div > div > div{
							background-color: #11567F;
						}
					</style>
					""")''')



