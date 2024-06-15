import streamlit as st
import streamlit.components.v1 as components
# import openai
from openai import OpenAI
from langdetect import detect
import pycountry

st.set_page_config(page_title="Review Response App", page_icon="✍️")

# Set up the OpenAI API key
openai_api_key = st.secrets["OPENAI_API"]["api_key"]
client = OpenAI(api_key=openai_api_key)

# Function to detect GUest review language, provide language code and then return the full name of the language
def detect_language_full_name(guest_review):
    try:
        lang_code = detect(guest_review)
        if lang_code:
            # Get the full name of the most probable language
            lang_full_name = pycountry.languages.get(alpha_2=lang_code)
            #lang_full_name = Language.get_name(lang_code)
            return lang_full_name.name
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

st.title('✍️ Review Response')

#host_name = "Chris & Andrea"

guest_name = st.text_input('Guest Name', placeholder="Guest name", label_visibility="collapsed")
guest_review = st.text_area('Guest Review', placeholder="Paste your Guest's review here. AI will automatically detect the language for the reply.", label_visibility="collapsed", height=250)
guest_review = f'"{guest_review}"'

#Language detection
lang_full_name = detect_language_full_name(guest_review)

messages = [{"role": "system", "content": f'Hello wonderful assistant! We are Airbnb hosts. Each of our guests that stay in our Airbnb rentals leave us a review of their experience. A guest named {guest_name} left the following review:\n\n"{guest_review}"\n\nPlease create a very polite reply based on their review in {lang_full_name}, in 75 words or less. Please address the guest by their name in the response. Please thank the guest for each positive comment or remark. It is important that you do not respond to any criticisms from the guest in your response! At the end of the response please sign off by appending the following text "You always have a home here with us in Playa!".\n\nThank you! and nothing else.'}]

# if button clicked then do the with st.spinner
if st.button('Start the Magic  🪄'):

    with st.spinner(f"Creating your Reponse..."): 
	    response = client.chat.completions.create(model="gpt-4o", messages=messages)
	    review_response = f'{response.choices[0].message.content}'
	    st.divider()
	    st.subheader('Review Response')
	    st.code(review_response, language=None)

################################### Define your JavaScript ########################################

html_string='''
<style>
code.language-plaintext {
    white-space: normal!important;
    opacity: 0;
  	animation: fade-in 2s ease-in-out forwards;
    }

    @keyframes fade-in {
		from { opacity: 0; }
		to { opacity: 1; }
		}

.block-container {
    padding-top: 30px;
    padding-bottom: 20px;
}

.st-emotion-cache-h4xjwg {
    display: none;
}

span#MainMenu {
    display: none;
}

.stActionButton {
    display: none;
}

.css-14xtw13.e8zbici0 {
    display: none;
}

.viewerBadge_link__1S137 {
    display: none!important;
}

a.viewerBadge_container__1QSob {
    display: none!important;
}

.viewerBadge_link__1S137 {
display: none;
visibility:hidden
}

/*
footer {
margin-bottom: 20px;
visibility: hidden;
}

footer:after {
visibility: visible;
content: 'Made with ❤️';
display: block;
position: relative;
margin-bottom: 20px;
}
*/
</style>

<script>
const streamlitDoc = window.parent.document;
document.addEventListener("DOMContentLoaded", function(event){
        //alert('Its been 5 seconds');
        streamlitDoc.getElementsByTagName("footer")[0].innerHTML = "Provided by <a href='https://airbnbconsulting.com' target='_blank' class='css-z3au9t egzxvld2'>Bnb Consulting</a>";
    });
</script>
'''
components.html(html_string)
st.markdown(html_string, unsafe_allow_html=True)
