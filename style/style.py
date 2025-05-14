sit_style = """
	<style>
	
	div[data-testid="stApp"]{
	    background-color: #24323D;
	    }

	header[data-testid="stHeader"]{
		color: white;
	    height:150px;
	    border: 1px solid #ffffff;
	    border-radius: 32px 32px 0px 0px;
	    background-color: #29B5E8;
	    background-size: cover;                    
	    background-repeat: no-repeat;
	    background-position: center center;
	    text-align: center;
	    margin-left:2rem;
	    margin-top: 2rem;
	    margin-right:2rem;
	    padding-top: 1rem;
	    font-size: 60px;
	    z-index: 3;
	    }

	header[data-testid="stHeader"]:after{
		vertical-align: middle !important;
		content: "SIT Design System";
	}

	[data-testid="stSidebar"] { 
		color: white;
	    background-color: #11567f;
	    max-width: 244px;
	    z-index: 4;
	    border-right: 1px solid #ffffff;
	    #border: 1px solid #ffffff;
	    }
	    
	# [data-testid="stSidebarCollapsedControl"]{
	#     visibility:hidden;
	#     }
	div[data-testid="stDecoration"]{
	    visibility:hidden;
	    }

	div[data-testid="stAppViewContainer"]{
	    background-color: #ffffff;
	    padding-top: 5rem;
	    margin-right:2rem;
	    margin-top:2rem;
	    margin-left:2rem;
	    margin-bottom:2rem;
	    border-radius:2rem;
	    border: 1px solid #ffffff;
	    box-shadow: 4px 4px 4px 1px rgba(64, 64, 64, .25);
	    z-index: 1;
	    }
</style>"""