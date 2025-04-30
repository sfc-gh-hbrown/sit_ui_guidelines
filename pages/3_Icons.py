import streamlit as st
import base64

st.set_page_config(layout="wide")

def get_image(path):
	file_ = open(path, "rb")
	contents = file_.read()
	image_bytes = base64.b64encode(contents).decode("utf-8")
	file_.close()
	return image_bytes

st.html("""<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=favorite" />""")

st.html("""
<style>
[data-testid="stSidebar"]{
	background-color: #11567F;
}
[data-testid="stSidebarNavLink"] span{
	color: white;
	# text-decoration-line: underline transparent;
 }
.icon{
	padding-left: 30px;
	padding-right: 30px;
	height: 60px;
}
.vl {
  margin-right: 20px;
  border-left: 1px solid lightgrey;
  height: 60px;
}
.icons {
	display: flex;
	align-items:center;
}
# [data-testid="stSidebarNavLink"] :active span{
#  }


[data-testid="stBaseLinkButton-secondary"] {
	color: #FFFFFF;
	background-color: #11567F;
}

[data-testid="stBaseLinkButton-secondary"]:hover {
	color: #FFFFFF;
	background-color: #044064;
	border-color: transparent;
}

[data-testid="stBaseLinkButton-secondary"]:active {
	color: #FFFFFF;
	background-color: #1B78AE;
}
[data-testid="stBaseLinkButton-secondary"]:focus:not(:active) {
	color: #FFFFFF;
	background-color: #1B78AE;
	border-color: transparent;
}

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
st.header("Icons")

st.write("**Material Icons:** Open source icon library created by Google. Use one single icon style when adding icons to your interface. Pick the outline or solid icon style but avoid mixing them.")

st.link_button("Material Icons", url='https://fonts.google.com/icons')
# Inject custom CSS

file_ = open("images/favorite.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


st.html(f"""<div class="icons">
	<img class="icon" src="data:image/png;base64,{get_image("images/bookmark.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/favorite.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/star.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/info.png")}">
	<div class="vl"></span>
	<img class="icon" src="data:image/png;base64,{get_image("images/bookmark_filled.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/favorite_filled.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/star_filled.png")}">
	<img class="icon" src="data:image/png;base64,{get_image("images/info_filled.png")}">
	</div>""")
st.html("""<div class="icons">
	<p style="padding-left:200px;">Outline Icons</p><p style="padding-left:400px;">Solid Icons</p>
	</div>""")
st.divider()
st.html("""<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">""")




st.write("**Example**")
text, ex, __ = st.columns((2,3,20))
text.html("""<p style="padding-top:7px">Button</p>""")
ex.button(":material/power_settings_new: Click Me")
text, ex, __ = st.columns((2,3,20))
text.html("""<p style="padding-top:0px">Page</p>""")
ex.write(":material/Timelapse: Page one")
text, ex, __ = st.columns((2,5,20))
text.html("""<p style="padding-top:15px">Status</p>""")
ex.success(":material/Info: Sample Text Goes Here")
text, ex, __ = st.columns((2,3,20))
text.html("""<p style="padding-top:0px">Text</p>""")
ex.write("Text goes here :material/Help:")

with st.popover("Copy Code"):
	st.code("""
st.write("**Example**")
text, ex, __ = st.columns((2,3,20))
text.write("Button")
ex.button(":material/power_settings_new: Click Me")
text, ex, __ = st.columns((2,3,20))
text.write("Page")
ex.write(":material/Timelapse: Page one")
text, ex, __ = st.columns((2,3,20))
text.write("Status")
ex.success(":material/Info: Sample Text Goes Here")
text, ex, __ = st.columns((2,3,20))
text.write("Text")
ex.write("Text goes here :material/Help:")""")