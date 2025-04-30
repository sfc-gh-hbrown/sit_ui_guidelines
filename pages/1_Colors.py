import streamlit as st


st.set_page_config(layout="wide")

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

st.title("SIT Design System")

st.header("Colors")

st.write("**Mid Blue**: Primary Color")

st.html("""
<div class="row">
  <span>#11567F </span>
  <div class='box m_blue' style="background-color:#11567F;"></div>
</div>""")

st.html("""
<div class="grad_row">
	<div class="grad_box" style="background-color:#E6F6FF;">
		<span>
			<span>10</span>
			<span>E6F6FF</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#D4EFFF;">
		<span>
			<span>20</span>
			<span>D4EFFF</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#ACE1FF;">
		<span>
			<span>30</span>
			<span>ACE1FF</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#8ACBF1;">
		<span>
			<span>40</span>
			<span>8ACBF1</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#389FDA;">
		<span>
			<span>50</span>
			<span>389FDA</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#248AC5;">
		<span>
			<span>60</span>
			<span>248AC5</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#1B78AE;">
		<span>
			<span>70</span>
			<span>1B78AE</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#166898;">
		<span>
			<span>80</span>
			<span>166898</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#11567F;">
		<span>
			<span>90</span>
			<span>11567F</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#0A466A;">
		<span>
			<span>100</span>
			<span>0A466A</span>
		</span>
	</div>
</div>
	""")

st.divider()







st.write("**Snowflake Blue**: Secondary Color")

st.html("""
<div class="row">
  <span>#29B5E8 </span>
  <div class='box' style="background-color:#29B5E8;"></div>
</div>""")

st.html("""
<div class="grad_row">
	<div class="grad_box" style="background-color:#E6F7FD;">
		<span>
			<span>10</span>
			<span>E6F7FD</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#D4F0FA;">
		<span>
			<span>20</span>
			<span>D4F0FA</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#BBE6F7;">
		<span>
			<span>30</span>
			<span>BBE6F7</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#A9E1F6;">
		<span>
			<span>40</span>
			<span>A9E1F6</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#96D9F1;">
		<span>
			<span>50</span>
			<span>96D9F1</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#7FD3F1;">
		<span>
			<span>60</span>
			<span>7FD3F1</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#6FCBED;">
		<span>
			<span>70</span>
			<span>6FCBED</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#54C4ED;">
		<span>
			<span>80</span>
			<span>54C4ED</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#29B5E8;">
		<span>
			<span>90</span>
			<span>29B5E8</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#0EA6DE;">
		<span>
			<span>100</span>
			<span>0EA6DE</span>
		</span>
	</div>
</div>
	""")

st.divider()







st.write("**Red**: Destruction Actions Color")

st.html("""
<div class="row">
  <span>#11567F </span>
  <div class='box' style="background-color:#FF2A2B;"></div>
</div>""")

st.html("""
<div class="grad_row">
	<div class="grad_box" style="background-color:#FFF0F0;">
		<span>
			<span>10</span>
			<span>FFF0F0</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FFDEDE;">
		<span>
			<span>20</span>
			<span>FFDEDE</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FFC7C7;">
		<span>
			<span>30</span>
			<span>FFC7C7</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FFABAB;">
		<span>
			<span>40</span>
			<span>FFABAB</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FF8C8C;">
		<span>
			<span>50</span>
			<span>FF8C8C</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FF4B4B;">
		<span>
			<span>60</span>
			<span>FF4B4B</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FF4B4B;">
		<span>
			<span>70</span>
			<span>FF4B4B</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#FF2A2B;">
		<span>
			<span>80</span>
			<span>FF2A2B</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#BD4043;">
		<span>
			<span>90</span>
			<span>BD4043</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#7D353B;">
		<span>
			<span>100</span>
			<span>7D353B</span>
		</span>
	</div>
</div>
	""")

st.divider()







st.write("**Grey**:")

st.html("""
<div class="row">
  <span>#262730 </span>
  <div class='box m_blue' style="background-color:#262730;"></div>
</div>""")

st.html("""
<div class="grad_row">
	<div class="grad_box" style="background-color:#FAFAFA;">
		<span>
			<span>10</span>
			<span>FAFAFA</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#F0F2F6;">
		<span>
			<span>20</span>
			<span>F0F2F6</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#E6EAF1;">
		<span>
			<span>30</span>
			<span>E6EAF1</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#D5DAE5;">
		<span>
			<span>40</span>
			<span>D5DAE5</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#BFC5D3;">
		<span>
			<span>50</span>
			<span>BFC5D3</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#A3A8B8;">
		<span>
			<span>60</span>
			<span>A3A8B8</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#808495;">
		<span>
			<span>70</span>
			<span>808495</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#555867;">
		<span>
			<span>80</span>
			<span>555867</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#262730;">
		<span>
			<span>90</span>
			<span>262730</span>
		</span>
	</div>
	<div class="grad_box" style="background-color:#0E1117;">
		<span>
			<span>100</span>
			<span>0E1117</span>
		</span>
	</div>
</div>
	""")

st.divider()