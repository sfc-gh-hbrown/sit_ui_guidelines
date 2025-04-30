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

st.header("Chat")


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
	tab1, tab2 = st.tabs(["Chat Input", "Chat Message"])

	with tab1:
		st.write("**Chat Input:** For submitting content in a chat")

		state,button,__ = st.columns((2,2,10))

		with state:
			st.write("**State**")
		with button:
			st.write("**Component**")

		state,button,__ = st.columns((2,3,10))

		with state:
			st.write("Resting")
		with button:
			st.chat_input("Placeholder text", key="chat_1", accept_file=True)
		state,button,__ = st.columns((2,3,10))

		with state:
			st.write("Hover")
		with button:
			st.chat_input("Placeholder text", key="chat_2", accept_file=True)		
		state,button,__ = st.columns((2,3,10))

		with state:
			st.write("Clicked")
		with button:
			st.chat_input("Placeholder text", key="chat_3", accept_file=True)



		st.html("""<style>
		.st-key-chat_2 > div > div {
			background-color:#EAEBEC !important;
		}
		.st-key-chat_2 > div > div > div > div  {
			background-color:#EAEBEC !important;
		}
		.st-key-chat_3 > div > div {
			border-color:#11567F !important;
		}
		</style>""")

		st.write("**Example:**")
		
		st.chat_input("Placeholder text", key="example_chat_input", accept_file=True)
		st.html("""<style>
		.st-key-example_chat_input > div > div:hover {
			background-color:#EAEBEC !important;
		}
		.st-key-example_chat_input > div > div > div > div:hover {
			background-color:#EAEBEC !important;
		}
		.st-key-example_chat_input > div > div:active {
			border-color:#11567F !important;
		}

		.st-key-example_chat_input > div > div :focus:not(:active) {
			border-color:#11567F !important;
		}
		</style>""")

	with tab2:
		st.write("**Chat Message:** For insterting a chat message")

		with st.container(key="human_message"):
			message = st.chat_message("human", avatar=":material/face:")
			message.write("Hey lets get started with some inspo on what this data can do!")

		with st.container(key="chatbot_message"):
			message = st.chat_message("assistant", avatar=":material/robot_2:")
			message.write("Great idea! Check out this code:")
			message.code("""
					import streamlit as st
					import pandads as pd
					import numpy as np

					#create a DataFrame with random data
					df = pd.DataFrame(np.random.randn(10,5),columslist(‘ABCDE’))

					#Display the DataFrame in Streamlit

				""")

		st.html("""<style>
		.st-key-human_message div[data-testid="stChatMessage"]{
			background-color:transparent !important;
		}
		.st-key-human_message div[data-testid="stChatMessageAvatarCustom"]{
			color: white;
			background-color:#11567F !important;
			border-radius: 20px;
		}
		.st-key-human_message span[data-testid="stIconMaterial"] {
			color: white;		
			}

		.st-key-chatbot_message div[data-testid="stChatMessage"]{
			background-color:transparent !important;
		}
		.st-key-chatbot_message div[data-testid="stChatMessageAvatarCustom"]{
			color: white;
			background-color:#29B5E8 !important;
			border-radius: 20px;
		}
		.st-key-chatbot_message span[data-testid="stIconMaterial"] {
			color: white;		
			}
		</style>""")

		with st.popover("Copy code"):
			st.code('''
			with st.container(key="human_message"):
				message = st.chat_message("human", avatar=":material/face:")
				message.write("Hey lets get started with some inspo on what this data can do!")

			with st.container(key="chatbot_message"):
				message = st.chat_message("assistant", avatar=":material/robot_2:")
				message.write("Great idea! Check out this code:")
				message.code("""
						import streamlit as st
						import pandads as pd
						import numpy as np

						#create a DataFrame with random data
						df = pd.DataFrame(np.random.randn(10,5),columslist(‘ABCDE’))

						#Display the DataFrame in Streamlit

					""")

			st.html("""
			<style>
				.st-key-human_message div[data-testid="stChatMessage"]{
					background-color:transparent !important;
				}
				.st-key-human_message div[data-testid="stChatMessageAvatarCustom"]{
					color: white;
					background-color:#11567F !important;
					border-radius: 20px;
				}
				.st-key-human_message span[data-testid="stIconMaterial"] {
					color: white;		
					}

				.st-key-chatbot_message div[data-testid="stChatMessage"]{
					background-color:transparent !important;
				}
				.st-key-chatbot_message div[data-testid="stChatMessageAvatarCustom"]{
					color: white;
					background-color:#29B5E8 !important;
					border-radius: 20px;
				}
				.st-key-chatbot_message span[data-testid="stIconMaterial"] {
					color: white;		
					}
			</style>""")
				''')
