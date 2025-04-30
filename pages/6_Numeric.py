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

st.header("Selections")

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
	tab1, tab3, tab4 = st.tabs(["Number Input", "Date Input","Time Input"])

	with tab1:
		st.write("**Number Input:** For choosing or modifying a specific number value.")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.number_input("Label goes here",key="nmbr_1", value=0)
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.number_input("Label goes here", key="nmbr_2",value=0)
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.number_input("Label goes here", key="nmbr_3",value=0)

		st.html("""<style>
				.st-key-selectr_1 div[data-baseweb="select"] div{
					color: black;
					# background-color: #11567F !important;
					# border-color: #11567F !important;
				}

				.st-key-selectr_2 div[data-baseweb="select"] div{
					color: black;
					background-color: #EAEBEC !important;
				}

				.st-key-nmbr_2 div[data-testid="stNumberInputContainer"] > div > div{
					background-color: #EAEBEC !important;
				}

				.st-key-nmbr_3 div[data-testid="stNumberInputContainer"] {
					border-color: #11567F !important;
				}
				.st-key-nmbr_3 button[data-testid="stNumberInputStepDown"]:hover {
					background-color: #11567F !important;
				}
				.st-key-nmbr_3 button[data-testid="stNumberInputStepUp"]:hover {
					background-color: #11567F !important;
				}

				.st-key-nmbr_3 button[data-testid="stNumberInputStepDown"]:focus:not(:active) {
					background-color: #11567F !important;
				}
				.st-key-nmbr_3 button[data-testid="stNumberInputStepUp"]:focus:not(:active) {
					background-color: #11567F !important;
				}

				</style>""")

		st.write("**Example:**")
		st.number_input("Label goes here", key="example_number_input",value=0)
		st.html("""<style>
		.st-key-example_number_input div[data-baseweb="select"] div{
			color: black;
		}

		.st-key-example_number_input div[data-baseweb="select"]:hover {
			color: black;
			background-color: #EAEBEC !important;
		}

		.st-key-example_number_input div[data-testid="stNumberInputContainer"] > div > div :hover {
			background-color: #EAEBEC !important;
		}

		.st-key-example_number_input div[data-testid="stNumberInputContainer"]:active {
			border-color: #11567F !important;
		}

		.st-key-example_number_input .focused {
			border-color: #11567F !important;
		}

		.st-key-example_number_input button[data-testid="stNumberInputStepDown"]:hover {
			background-color: #11567F !important;
		}
		.st-key-example_number_input button[data-testid="stNumberInputStepUp"]:hover {
			background-color: #11567F !important;
		}

		.st-key-example_number_input button[data-testid="stNumberInputStepDown"]:focus:not(:active) {
			background-color: #11567F !important;
		}
		.st-key-example_number_input button[data-testid="stNumberInputStepUp"]:focus:not(:active) {
			background-color: #11567F !important;
		}

		</style>""")

		with st.popover("Copy code"):
			st.code('''
		st.number_input("Label goes here", key="example_number_input",value=0)
		st.html("""
		<style>
			.st-key-example_number_input div[data-baseweb="select"] div{
				color: black;
			}

			.st-key-example_number_input div[data-baseweb="select"]:hover {
				color: black;
				background-color: #EAEBEC !important;
			}

			.st-key-example_number_input div[data-testid="stNumberInputContainer"] > div > div :hover {
				background-color: #EAEBEC !important;
			}

			.st-key-example_number_input div[data-testid="stNumberInputContainer"]:active {
				border-color: #11567F !important;
			}

			.st-key-example_number_input .focused {
				border-color: #11567F !important;
			}

			.st-key-example_number_input button[data-testid="stNumberInputStepDown"]:hover {
				background-color: #11567F !important;
			}
			.st-key-example_number_input button[data-testid="stNumberInputStepUp"]:hover {
				background-color: #11567F !important;
			}

			.st-key-example_number_input button[data-testid="stNumberInputStepDown"]:focus:not(:active) {
				background-color: #11567F !important;
			}
			.st-key-example_number_input button[data-testid="stNumberInputStepUp"]:focus:not(:active) {
				background-color: #11567F !important;
			}

		</style>""")

				''')

	# with tab2:
	# 	st.write("**Slider:** For choosing a value or range from a fixed set of options.")

	# 	st.write("**Example**")
	# 	st.html("""<style>
	# 			.stSlider div[role="slider"]{
	# 				# padding-bottom: 16px;
	# 				background-color: #11567F !important;
	# 				color: #11567F !important;
	# 			}
	# 			.stSlider div[role="slider"] > div{
	# 				# padding-bottom: 16px;
	# 				color: #11567F !important;
	# 			}

	# 			.stSlider div[data-baseweb="slider"] > div > div{
	# 				# padding-bottom: 16px;
	# 				background-color: #11567F !important;
	# 			}



	# 			</style>""")
	# 	st.slider("Label goes here")



	# 	start_color, end_color = st.select_slider(
	# 	    "Label goes here",
	# 	    options=[
	# 	        "red",
	# 	        "orange",
	# 	        "yellow",
	# 	        "green",
	# 	        "blue",
	# 	        "indigo",
	# 	        "violet",
	# 	    ],
	# 	    value=("red", "blue"),
	# 	)
			# st.radio("",options = ["I agree"], key="radio_1", label_visibility="collapsed")
		

	with tab3:
		st.write("**Date Input:** For choosing a specific date or date range")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.date_input("Label goes here", key="date_1")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.date_input("Label goes here", key="date_2")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.date_input("Label goes here", key="date_3")

		st.html("""<style>
				.st-key-date_1 label{
					# padding-bottom: 100px;
					# background-color: #11567F !important;
					# border-color: #11567F !important;
				}

				.st-key-date_2 div[data-baseweb="base-input"]{
					background-color: #EAEBEC !important;
				}
				.st-key-date_2 div[data-baseweb="input"]{
					background-color: #EAEBEC !important;
				}

				.st-key-date_3 div[data-baseweb="input"]{
					border-color: #11567F !important;
				}

				div[aria-label*="Calendar."] div[aria-label*="Selected."]::after {
					background-color: #11567F !important;
					border-color: #11567F !important;
				}

				div[aria-label*="Calendar."] div[role="gridcell"]:hover::after {
					border-color: #11567F !important;
				}

				</style>""")

		st.write("**Example:**")
		st.date_input("Label goes here", key="example_date_input")
		st.html("""
		<style>

		.st-key-example_date_input div[data-baseweb="base-input"]:hover{
			background-color: #EAEBEC !important;
		}

		.st-key-example_date_input div[data-baseweb="input"]:hover{
			background-color: #EAEBEC !important;
		}

		.st-key-example_date_input div[data-baseweb="input"]:active {
			border-color: #11567F !important;
		}

		.st-key-example_date_input .focused {
			border-color: #11567F !important;
		}

		div[aria-label*="Calendar."] div[aria-label*="Selected."]::after {
			background-color: #11567F !important;
			border-color: #11567F !important;
		}

		div[aria-label*="Calendar."] div[role="gridcell"]:hover::after {
			border-color: #11567F !important;
		}

		</style>""")
		with st.popover("Cope code"):
			st.code('''
		st.date_input("Label goes here", key="example_date_input")
		st.html("""
		<style>
			.st-key-example_date_input div[data-baseweb="base-input"]:hover{
				background-color: #EAEBEC !important;
			}

			.st-key-example_date_input div[data-baseweb="input"]:hover{
				background-color: #EAEBEC !important;
			}

			.st-key-example_date_input div[data-baseweb="input"]:active {
				border-color: #11567F !important;
			}

			div[aria-label*="Calendar."] div[aria-label*="Selected."]::after {
				background-color: #11567F !important;
				border-color: #11567F !important;
			}

			div[aria-label*="Calendar."] div[role="gridcell"]:hover::after {
				border-color: #11567F !important;
			}

		</style>""")''')

	with tab4:
		st.write("**Date Input:** For choosing a specific date or date range")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.time_input("Label goes here", key="time_1")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.time_input("Label goes here", key="time_2")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.time_input("Label goes here", key="time_3")

		st.html("""<style>
				.st-key-date_1 label{
					# padding-bottom: 100px;
					# background-color: #11567F !important;
					# border-color: #11567F !important;
				}

				.st-key-time_2 div[data-baseweb="select"]{
					# background-color: #EAEBEC !important;
				}
				.st-key-time_2 div[data-baseweb="select"] > div{
					background-color: #EAEBEC !important;
				}

				.st-key-time_3 div[data-baseweb="select"] > div {
					border-color: #11567F !important;
				}

				.st-key-time_3 div[data-baseweb="select"] > div:focus {
					border-color: #11567F !important;
				}


				</style>""")
		
		st.write("**Example:**")
		st.time_input("Label goes here", key="example_time_input")
		st.html("""
			<style>
				.st-key-example_time_input div[data-baseweb="select"]:hover{
					# background-color: #EAEBEC !important;
				}
				.st-key-example_time_input div[data-baseweb="select"] > div:hover{
					background-color: #EAEBEC !important;
				}

				.st-key-example_time_input div[data-baseweb="select"] > div:active {
					border-color: #11567F !important;
				}

				.st-key-example_time_input :has(input[aria-expanded="true"]) div[data-baseweb="select"] > div {
					border-color: #11567F !important;
				}
			</style>""")
		with st.popover("Copy Code"):
			st.code('''
				st.time_input("Label goes here", key="example_time_input")
				st.html("""
					<style>
						.st-key-example_time_input div[data-baseweb="select"]:hover{
							# background-color: #EAEBEC !important;
						}
						.st-key-example_time_input div[data-baseweb="select"] > div:hover{
							background-color: #EAEBEC !important;
						}

						.st-key-example_time_input div[data-baseweb="select"] > div:active {
							border-color: #11567F !important;
						}

						.st-key-example_time_input :has(input[aria-expanded="true"]) div[data-baseweb="select"] > div {
							border-color: #11567F !important;
						}
					</style>""")
				''')