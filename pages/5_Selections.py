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
	tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Checkbox", "Radio Button", "Toggle","Select Box","Multi-Select Box","Pills","Segmented Controls"])

	with tab1:
		st.write("**Checkbox:** For choosing one or more options from a list. When used alone, users can make a binary choice(checked or unchecked). When used in a group, users can choose multiple options from a list.")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Button**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.checkbox("I agree", key="check_1")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.checkbox("I agree", key="check_2")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.checkbox("I agree", key="check_3", value=True)
			st.html("""<style>

				.st-key-check_2 span{
					background-color: #EAEBEC;
				}

				.stCheckbox :has(input[aria-checked="true"]) span{
					background-color: #11567F !important;
					border-color: #11567F !important;
				}

				</style>""")

		st.write("**Example:**")
		st.checkbox("I agree with your terms", key="checkbox_example")
		st.html("""<style>

				.st-key-checkbox_example :has(input[aria-checked="true"]) span{
					background-color: #11567F !important;
					border-color: #11567F !important;
				}

				</style>""")

		with st.popover("Copy code"):
			st.write("Style all checkboxes")
			st.code('''
				st.html("""
				<style>
					.stCheckbox :has(input[aria-checked="true"]) span{
						background-color: #11567F !important;
						border-color: #11567F !important;
					}
				</style>""")
				''')

			st.write("Style one checkbox")
			st.code('''
				st.checkbox("I agree with your terms", key="checkbox_example")
				st.html("""
				<style>
					.st-key-checkbox_example :has(input[aria-checked="true"]) span{
						background-color: #11567F !important;
						border-color: #11567F !important;
					}
				</style>""")
				''')
	with tab2:
		st.write("**Radio Button:** For choosing one option from a list. When the space is limited use a dropdown menu instead.")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Button**")

		state,button,__ = st.columns((2,3,10))

		with state:
			st.write("Resting")
			st.write("Clicked")
		with button:
			st.radio("",options = ["Dollar","Pound"], key="radio_3", label_visibility="collapsed", index=1)
			st.html("""<style>

				.st-key-radio_3 label{
					padding-bottom: 16px;
					# background-color: #11567F !important;
					# border-color: #11567F !important;
				}

				.st-key-radio_3 label:has(input[tabindex="0"]) > div:first-child{
					background-color: #11567F !important;
				}

				</style>""")
			# st.radio("",options = ["I agree"], key="radio_1", label_visibility="collapsed")
			pass

		st.write("**Example:**")
		st.radio("Choose an option",options=["One","Two","Three"],key="radio_example")
		st.html("""
			<style>
				.st-key-radio_example label:has(input[tabindex="0"]) > div:first-child{
					background-color: #11567F !important;
				}
			</style>""")

		with st.popover("Copy code"):
			st.write("Style all Radios")
			st.code('''
			st.html("""
			<style>
				.stRadio label:has(input[tabindex="0"]) > div:first-child{
					background-color: #11567F !important;
				}
			</style>""")
				''')
			st.write("Style one Radio")
			st.code('''
			st.radio("Choose an option",options=["One","Two","Three"],key="radio_example")
			st.html("""
			<style>
				.st-key-radio_example label:has(input[tabindex="0"]) > div:first-child{
					background-color: #11567F !important;
				}
			</style>""")
				''')

	with tab3:
		st.write("**Toggle:** For choosing between two opposing states.")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Button**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.toggle("I agree", key="agree_1")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.toggle("I agree", key="agree_2")
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.toggle("I agree", key="agree_3", value=True)

		st.html("""<style>
				.st-key-agree_3 label{
					padding-bottom: 16px;
					# background-color: #11567F !important;
					# border-color: #11567F !important;
				}

				.st-key-agree_2 label > div:first-child{
					background-color: #EAEBEC !important;
				}
				.stCheckbox label:has(input[aria-checked="true"]) > div:first-child{
					background-color: #11567F !important;
				}

				</style>""")

		st.write("**Example:**")
		
		st.toggle("I agree to your demands", value=True, key="example_toggle")
		st.html("""<style>
				.st-key-example_toggle label:has(input[aria-checked="true"]) > div:first-child{
					background-color: #11567F !important;
				}
				</style>""")

		with st.popover("Copy code"):
			st.write("Style all toggles")
			st.code('''
				st.html("""
				<style>
					.stCheckbox label:has(input[aria-checked="true"]) > div:first-child{
						background-color: #11567F !important;
					}
				</style>""")
				''')
			st.write("Style one toggle")
			st.code('''
				st.toggle("I agree to your demands", value=True, key="example_toggle")
				st.html("""
				<style>
					.st-key-example_toggle label:has(input[aria-checked="true"]) > div:first-child{
						background-color: #11567F !important;
					}
				</style>""")
				''')

	with tab4:
		st.write("**Select Box:** For choosing one option from a list in a compact space")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Resting")
		with button:
			st.selectbox("Label goes here",["English","French","Spanish"], key="selectr_1",index=None)
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Hover")
		with button:
			st.selectbox("Label goes here",["English","French","Spanish"], key="selectr_2",index=None)
		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("Clicked")
		with button:
			st.selectbox("Label goes here",["English","French","Spanish"], key="selectr_3",index=None)

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

				.st-key-selectr_3 div[data-baseweb="select"] div{
					color: black;
					border-color: #11567F !important;
				}

				</style>""")

		st.write("**Example:**")
		st.selectbox("Label goes here",["English","French","Spanish"], key="example_selectbox",index=None)
		st.html("""<style>
		.st-key-example_selectbox div[data-baseweb="select"] div{
			color: black;
		}

		.st-key-example_selectbox div[data-baseweb="select"] div:hover{
			color: black;
			background-color: #EAEBEC !important;
		}

		.st-key-example_selectbox div[data-baseweb="select"] div:active {
			color: black;
			border-color: #11567F !important;
		}

		.st-key-example_selectbox :has(input[aria-expanded="true"]) div[data-baseweb="select"] div{
			color: black;
			border-color: #11567F !important;
		}

				</style>""")

		with st.popover("Copy code"):
			st.code('''
		st.selectbox("Label goes here",["English","French","Spanish"], key="example_selectbox",index=None)
		st.html("""
		<style>
			.st-key-example_selectbox div[data-baseweb="select"] div{
				color: black;
			}

			.st-key-example_selectbox div[data-baseweb="select"] div:hover{
				color: black;
				background-color: #EAEBEC !important;
			}

			.st-key-example_selectbox div[data-baseweb="select"] div:active {
				color: black;
				border-color: #11567F !important;
			}

			.st-key-example_selectbox :has(input[aria-expanded="true"]) div[data-baseweb="select"] div{
				color: black;
				border-color: #11567F !important;
			}

		</style>""")
				''')
		with tab5:
			st.write("**Multi Select Box:** For choosing one or more options from a list in a compact space")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("**State**")
			with button:
				st.write("**Component**")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Resting")
			with button:
				st.selectbox("Label goes here",["English","French","Spanish"], key="m_selectr_1",index=None)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Hover")
			with button:
				st.selectbox("Label goes here",["English","French","Spanish"], key="m_selectr_2",index=None)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Clicked")
			with button:
				st.multiselect("Label goes here",["English","French","Spanish"], key="m_selectr_3")

			st.html("""<style>
					.st-key-m_selectr_1 div[data-baseweb="select"] div{
						color: black;
						# background-color: #11567F !important;
						# border-color: #11567F !important;
					}

					.st-key-m_selectr_2 div[data-baseweb="select"] div{
						color: black;
						background-color: #EAEBEC !important;
					}

					.st-key-m_selectr_3 div[data-baseweb="select"] div{
						color: black;
						border-color: #11567F !important;
					}

					.st-key-m_selectr_3 span[role="button"]{
						color: white;
						background-color: #11567F !important;
					}

					</style>""")

			st.write("**Example:**")
			st.multiselect("Label goes here",["English","French","Spanish"], key="example_multiselect")
			st.html("""<style>
			.st-key-example_multiselect div[data-baseweb="select"] div{
				color: black;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}

			.st-key-example_multiselect div[data-baseweb="select"] div:hover{
				color: black;
				background-color: #EAEBEC !important;
			}


			.st-key-example_multiselect div[data-baseweb="select"] div:active{
				color: black;
				border-color: #11567F !important;
			}

			.st-key-example_multiselect div[data-baseweb="select"] div:active{
				color: black;
				border-color: #11567F !important;
			}

			.st-key-example_multiselect :has(input[aria-expanded="true"]) div[data-baseweb="select"] div{
				color: black;
				border-color: #11567F !important;
			}

			.st-key-example_multiselect span[role="button"]{
				color: white;
				background-color: #11567F !important;
			}

			</style>""")


			with st.popover("Copy code"):
				st.code('''
			st.multiselect("Label goes here",["English","French","Spanish"], key="example_multiselect")
			st.html("""
			<style>
				.st-key-example_multiselect div[data-baseweb="select"] div{
					color: black;
				}

				.st-key-example_multiselect div[data-baseweb="select"] div:hover{
					color: black;
					background-color: #EAEBEC !important;
				}


				.st-key-example_multiselect div[data-baseweb="select"] div:active{
					color: black;
					border-color: #11567F !important;
				}

				.st-key-example_multiselect div[data-baseweb="select"] div:active{
					color: black;
					border-color: #11567F !important;
				}

				.st-key-example_multiselect :has(input[aria-expanded="true"]) div[data-baseweb="select"] div{
					color: black;
					border-color: #11567F !important;
				}

				.st-key-example_multiselect span[role="button"]{
					color: white;
					background-color: #11567F !important;
				}

			</style>""")
						''')
		with tab6:
			st.write("**Pills:** For choosing or displaying compact options like tags, filters, or statuses.")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("**State**")
			with button:
				st.write("**Component**")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Resting")
			with button:
				st.button("Click Me", key="m_b_1",disabled=True)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Hover")
			with button:
				st.button("Click Me", key="m_b_2",disabled=True)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Clicked")
			with button:
				st.button("Click Me", key="m_b_3",disabled=True)



			st.html("""<style>
			.st-key-m_b_1 button{
				color: black !important;
				border-radius: 20px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			.st-key-m_b_2 button{
				color: #11567F !important;
				border-color: #11567F !important;
				border-radius: 20px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			.st-key-m_b_3 button{
				background-color: #D4EFFF !important;
				color: #11567F !important;
				border-color: #11567F !important;
				border-radius: 20px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			</style>""")

			st.write("**Example**")

			st.pills("Example",["Comedy","Action","Thriller","Drama"],selection_mode="multi", default=["Action","Drama"], key="pill_example")

			st.html("""
				<style>
				.st-key-pill_example button:hover {
					color: #11567F;
					border-color: #11567F;
				}
				.st-key-pill_example button[kind*="Active"]{
					background-color: #D4EFFF;
					color: #11567F;
					border-color: #11567F;
				}
				</style>
				""")

			with st.popover("Copy code"):
				st.code('''
					st.pills("Example",["Comedy","Action","Thriller","Drama"],selection_mode="multi", default=["Action","Drama"], key="pill_example")

					st.html("""
						<style>
						.st-key-pill_example button:hover {
							color: #11567F;
							border-color: #11567F;
						}
						.st-key-pill_example button[kind*="Active"]{
							background-color: #D4EFFF;
							color: #11567F;
							border-color: #11567F;
						}
						</style>
						""")
					''')
		with tab7:
			st.write("**Segmented Controls:** For toggling between a small number of mutually exclusive options.")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("**State**")
			with button:
				st.write("**Component**")

			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Resting")
			with button:
				st.button("Click Me", key="sc_b_1",disabled=True)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Hover")
			with button:
				st.button("Click Me", key="sc_b_2",disabled=True)
			state,button,__ = st.columns((2,2,10))

			with state:
				st.write("Clicked")
			with button:
				st.button("Click Me", key="sc_b_3",disabled=True)



			st.html("""<style>
			.st-key-sc_b_1 button{
				color: black !important;
				border-radius: 1px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			.st-key-sc_b_2 button{
				color: #11567F !important;
				border-color: #11567F !important;
				border-radius: 1px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			.st-key-sc_b_3 button{
				background-color: #D4EFFF !important;
				color: #11567F !important;
				border-color: #11567F !important;
				border-radius: 1px;
				# background-color: #11567F !important;
				# border-color: #11567F !important;
			}
			</style>""")

			st.write("**Example**")

			st.segmented_control("Example",["Comedy","Action","Thriller","Drama"],selection_mode="multi", default=["Action","Drama"], key="segcontrol_example")

			st.html("""
				<style>
				.st-key-segcontrol_example button:hover {
					color: #11567F;
					border-color: #11567F;
				}
				.st-key-segcontrol_example button[kind*="Active"]{
					background-color: #D4EFFF;
					color: #11567F;
					border-color: #11567F;
				}
				</style>
				""")

			with st.popover("Copy code"):
				st.code('''
					st.segmented_control("Example",["Comedy","Action","Thriller","Drama"],selection_mode="multi", default=["Action","Drama"], key="segcontrol_example")

					st.html("""
						<style>
						.st-key-segcontrol_example button:hover {
							color: #11567F;
							border-color: #11567F;
						}
						.st-key-segcontrol_example button[kind*="Active"]{
							background-color: #D4EFFF;
							color: #11567F;
							border-color: #11567F;
						}
						</style>
						""")
					''')