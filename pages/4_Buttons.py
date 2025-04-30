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

</style>
	""")

st.title("SIT Design System")

st.header("Overview")

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
	tab1, tab2, tab3, tab4 = st.tabs(["Primary Buttons", "Secondary Buttons", "Tertiary Buttons","Destructive Buttons"])
	with tab1:
		st.write("**Primary Buttons:** For the most important action on the page or section. Use only once per screen. Can be paired with secondary buttons when there are multipe calls to action in the same section.")
		col1,col2,col3,col4 = st.columns(4)
		col1.write("**State**")
		col2.write("**Button**")
		col3.write("**Background Color**")
		col4.write("**Text Color**")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top: 7px">Resting</p>""")
		col2.button("Click me", key="p-resting", disabled=True)
		col3.html("""<p style="padding-top:7px">11567F</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Hover</p>""")
		col2.button("Click me", key="p-hover")
		col3.html("""<p style="padding-top:7px">044064</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Clicked</p>""")
		col2.button("Click me", key="p-clicked")
		col3.html("""<p style="padding-top:7px">1B78AE</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		# col1,col2,col3,col4 = st.columns(4)
		# col1.html("""<p style="padding-top:7px">Disabled</p>""")
		# col2.button("Click me", key="p-disabled", disabled=True)
		# col3.html("""<p style="padding-top:7px">389FDA</p>""")
		# col4.html("""<p style="padding-top:7px">FFFFFF 50%</p>""")

		css = """
		<style>
		.st-key-p-resting button{
			color: #FFFFFF !important;
			background-color: #11567F !important;
		}

		.st-key-p-hover button{
			color: #FFFFFF;
			background-color: #044064;
		}

		.st-key-p-clicked button{
			color: #FFFFFF;
			background-color: #1B78AE;
		}
		</style>
		"""
		st.html(css)

		st.write("**Example:**")
		st.button("Click me",key="p-example")
		st.html("""
		<style>
		.st-key-p-example button{
			color: #FFFFFF;
			background-color: #11567F;
		}

		.st-key-p-example:hover button{
			color: #FFFFFF;
			background-color: #044064;
			border-color: transparent;
		}

		.st-key-p-example:active button{
			color: #FFFFFF;
			background-color: #1B78AE;
		}
		.st-key-p-example :focus:not(:active) {
			color: #FFFFFF;
			background-color: #1B78AE;
			border-color: transparent;
		}
		</style>
		""")

		with st.popover("Copy code"):
			st.code('''	
		st.button("Click me",key="p-example")
		st.html("""
		<style>
		.st-key-p-example button{
			color: #FFFFFF;
			background-color: #11567F;
		}

		.st-key-p-example:hover button{
			color: #FFFFFF;
			background-color: #044064;
			border-color: transparent;
		}

		.st-key-p-example:active button{
			color: #FFFFFF;
			background-color: #1B78AE;
		}
		.st-key-p-example :focus:not(:active) {
			color: #FFFFFF;
			background-color: #1B78AE;
			border-color: transparent;
		}
		</style>
		""")''')

	with tab2:
		st.write("**Primary Buttons:** For the most important action on the page or section. Use only once per screen. Can be paired with secondary buttons when there are multipe calls to action in the same section.")
		col1,col2,col3,col4 = st.columns(4)
		col1.write("**State**")
		col2.write("**Button**")
		col3.write("**Outline Color**")
		col4.write("**Text Color**")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top: 7px">Resting</p>""")
		col2.button("Click me", key="s-resting")
		col3.html("""<p style="padding-top:7px">11567F</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Hover</p>""")
		col2.button("Click me", key="s-hover")
		col3.html("""<p style="padding-top:7px">02263B</p>""")
		col4.html("""<p style="padding-top:7px">02263B 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Clicked</p>""")
		col2.button("Click me", key="s-clicked")
		col3.html("""<p style="padding-top:7px">1B78AE</p>""")
		col4.html("""<p style="padding-top:7px">1B78AE 100%</p>""")

		css = """
		<style>
		.st-key-s-resting button{
			color: #11567F;
			border-color: #11567F;
		}

		.st-key-s-hover button{
			color: #02263B;
			border-color: #02263B;
		}

		.st-key-s-clicked button{
			color: #1B78AE;
			border-color: #1B78AE;
		}
		</style>
		"""
		st.html(css)

		st.write("**Example:**")
		st.button("Click me",key="s-example")
		st.html("""
		<style>
		.st-key-s-example button{
			color: #11567F;
			border-color: #11567F;
		}

		.st-key-s-example:hover button{
			color: #02263B;
			border-color: #02263B;
		}

		.st-key-s-example:active button{
			color: #1B78AE;
			border-color: #1B78AE;
			background-color:transparent;
		}
		.st-key-s-example :focus:not(:active) {
			color: #1B78AE;
			border-color: #1B78AE;
			background-color:transparent;
		}
		</style>
		""")

		with st.popover("Copy code"):
			st.code('''	
		st.button("Click me",key="s-example")
		st.html("""
		<style>
		.st-key-s-example button{
			color: #11567F;
			border-color: #11567F;
		}

		.st-key-s-example:hover button{
			color: #02263B;
			border-color: #02263B;
		}

		.st-key-s-example:active button{
			color: #1B78AE;
			border-color: #1B78AE;
			background-color:transparent;
		}
		.st-key-s-example :focus:not(:active) {
			color: #1B78AE;
			border-color: #1B78AE;
			background-color:transparent;
		}
		</style>
		""")''')


	with tab3:
		st.write("**Primary Buttons:** For the most important action on the page or section. Use only once per screen. Can be paired with secondary buttons when there are multipe calls to action in the same section.")
		col1,col2,col3,col4 = st.columns(4)
		col1.write("**State**")
		col2.write("**Button**")
		col3.write("**Outline Color**")
		col4.write("**Text Color**")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top: 7px">Resting</p>""")
		col2.button("Click me", key="t-resting")
		col3.html("""<p style="padding-top:7px">BFC5D3</p>""")
		col4.html("""<p style="padding-top:7px">262730 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Hover</p>""")
		col2.button("Click me", key="t-hover")
		col3.html("""<p style="padding-top:7px">808495</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Clicked</p>""")
		col2.button("Click me", key="t-clicked")
		col3.html("""<p style="padding-top:7px">262730</p>""")
		col4.html("""<p style="padding-top:7px">FFFFFF 100%</p>""")

		css = """
		<style>
		.st-key-t-resting button{
			color: #262730;
			border-color: #BFC5D3;
		}

		.st-key-t-hover button{
			color: #262730;
			border-color: #808495;
		}

		.st-key-t-clicked button{
			color: #262730;
			border-color: #262730;
			background-color:transparent;
		}
		</style>
		"""
		st.html(css)

		st.write("**Example:**")
		st.button("Click me",key="t-example")
		st.html("""
		<style>
		.st-key-t-example button{
			color: #262730;
			border-color: #BFC5D3;
		}

		.st-key-t-example:hover button{
			color: #262730;
			border-color: #808495;
		}

		.st-key-t-example:active button{
			color: #262730;
			border-color: #262730;
			background-color:transparent;
		}
		.st-key-t-example :focus:not(:active) {
			color: #262730;
			border-color: #262730;
			background-color:transparent;
		}
		</style>
		""")

		with st.popover("Copy code"):
			st.code('''	
		st.button("Click me",key="t-example")
		st.html("""
		<style>
		.st-key-t-example button{
			color: #262730;
			border-color: #BFC5D3;
		}

		.st-key-t-example:hover button{
			color: #262730;
			border-color: #808495;
		}

		.st-key-t-example:active button{
			color: #262730;
			border-color: #262730;
			background-color:transparent;
		}
		.st-key-t-example :focus:not(:active) {
			color: #262730;
			border-color: #262730;
			background-color:transparent;
		}
		</style>
		""")''')

	with tab4:
		st.write("**Primary Buttons:** For the most important action on the page or section. Use only once per screen. Can be paired with secondary buttons when there are multipe calls to action in the same section.")
		col1,col2,col3,col4 = st.columns(4)
		col1.write("**State**")
		col2.write("**Button**")
		col3.write("**Background Color**")
		col4.write("**Text Color**")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top: 7px">Resting</p>""")
		col2.button("Click me", key="d-resting")
		col3.html("""<p style="padding-top:7px">FF2B2B</p>""")
		col4.html("""<p style="padding-top:7px">FF2B2B 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Hover</p>""")
		col2.button("Click me", key="d-hover")
		col3.html("""<p style="padding-top:7px">7D353B</p>""")
		col4.html("""<p style="padding-top:7px">7D353B 100%</p>""")

		col1,col2,col3,col4 = st.columns(4)
		col1.html("""<p style="padding-top:7px">Clicked</p>""")
		col2.button("Click me", key="d-clicked")
		col3.html("""<p style="padding-top:7px">FF8C8C</p>""")
		col4.html("""<p style="padding-top:7px">FF8C8C 100%</p>""")

		css = """
		<style>
		.st-key-d-resting button{
			color: #FF2B2B;
			border-color: #FF2B2B;
		}

		.st-key-d-hover button{
			color: #7D353B;
			border-color: #7D353B;
		}

		.st-key-d-clicked button{
			color: #FF8C8C;
			border-color: #FF8C8C;
			background-color:transparent;
		}
		</style>
		"""
		st.html(css)

		st.write("**Example:**")
		st.button("Click me",key="d-example")
		st.html("""
		<style>
		.st-key-d-example button{
			color: #FF2B2B;
			border-color: #FF2B2B;
		}

		.st-key-d-example:hover button{
			color: #7D353B;
			border-color: #7D353B;
		}

		.st-key-d-example:active button{
			color: #FF8C8C;
			border-color: #FF8C8C;
			background-color:transparent;
		}
		.st-key-d-example :focus:not(:active) {
			color: #FF8C8C;
			border-color: #FF8C8C;
			background-color:transparent;
		}
		</style>
		""")

		with st.popover("Copy code"):
			st.code('''	
		st.button("Click me",key="d-example")
		st.html("""
		<style>
		.st-key-d-example button{
			color: #FF2B2B;
			border-color: #FF2B2B;
		}

		.st-key-d-example:hover button{
			color: #7D353B;
			border-color: #7D353B;
		}

		.st-key-d-example:active button{
			color: #FF8C8C;
			border-color: #FF8C8C;
			background-color:transparent;
		}
		.st-key-d-example :focus:not(:active) {
			color: #FF8C8C;
			border-color: #FF8C8C;
			background-color:transparent;
		}
		</style>
		""")''')
