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


st.header("Charts")

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

st.info("These are sample images for ideas, please refer to the 'Colors' page when designing your chart",icon=":material/info:")

with st.container(key="styled_tabs"):
	tab1, tab2, tab3, tab4 = st.tabs(["Area Chart", "Bar Chart", "Line Chart","Scatter Chart"])

	with tab1:
		st.write("**Area Chart**")
		st.image("images/area_chart.png")
	with tab2:
		st.write("**Bar Chart**")
		st.image("images/bar_chart.png")
	with tab3:
		st.write("**Line Chart**")
		st.image("images/line_chart.png")
	with tab4:
		st.write("**Scatter Chart**")
		st.image("images/scatter_chart.png")
