import streamlit as st


from style.style import sit_style

st.set_page_config(layout="wide",initial_sidebar_state="expanded")

st.html(sit_style)

st.header("Overview")

st.html("""
<style>
[data-testid="stSidebar"]{
	background-color: #11567F;
	# margin-right: 100px;
}
[data-testid="stSidebarNavLink"] span{
	color: white;
 }

.row {
    display : flex;
    align-items : center;
    margin-bottom: 15px;
}

.grad_row {
    display : flex;
    align-items : center;
}

.grad_box {
  height: 80px;
  width: 80px;
  border-radius: 8px;
  margin-right: 15px;
  display : inline-block;
  # align-items: center;
  text-align: center;
  padding-top: 10px;
}

.grad_box > span{
  display: inline-flex;
  flex-flow : column nowrap;
  vertical-align: middle;
}

.box {
  height: 20px;
  width: 20px;
  border: 1px solid black;
  border-radius: 4px;
  margin-left : 10px;
}


</style>
	""")