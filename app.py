import streamlit as st
import streamlit.components.v1 as components
import openai

st.set_page_config(page_title="Review Response App", page_icon="✍️")

openai.api_key = st.secrets["OPENAI_API"]

st.title('✍️ Review Response')
type_of_host = st.selectbox('Choose type of Host:', ('Home Stay 🏠', 'Airbnb Experience 🏄‍♂️'), index=0, help="Choose if this is for a Home Stay or for an Airbnb Experience")
host_name = st.text_input('Host Name', placeholder="Host name", label_visibility="collapsed")
guest_name = st.text_input('Guest Name', placeholder="Guest name", label_visibility="collapsed")
guest_review = st.text_area('Guest Review', placeholder="Paste your Guest's review here.", label_visibility="collapsed", height=150)

# Different for Homes and Experiences
if type_of_host == "Home Stay 🏠":
    sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', placeholder="Custom text", label_visibility="visible", help="Example: _You always have a home here with us!_")
else:
    sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', placeholder="Custom text", label_visibility="visible", help="Example: _Thanks for coming on the adventure!_")

response_language = st.selectbox('Choose response language:', ('English 🇺🇸', 'Spanish 🇪🇸', 'French 🇫🇷'), index=0)

# Different for Homes and Experiences
if type_of_host == "Home Stay 🏠":
    messages = [{"role": "system", "content": f'We are Airbnb hosts named {host_name}. We just had one of our guests named {guest_name} leave a very polite review. Please create a very polite reply based on their review in {response_language}, in 50 words or less.\n\n"{guest_review}"'}]
else:
    messages = [{"role": "system", "content": f'I am an Airbnb Experience host named {host_name}. A guest named {guest_name} left the following review. Please create a very polite reply based on their review in {response_language}, in 50 words or less.\n\n"{guest_review}"'}]

# if button clicked then do the with st.spinner
if st.button('Start the Magic  🪄'):

    with st.spinner(f"Creating your Reponse..."): 
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        review_response = f'{response["choices"][0]["message"]["content"]} {sign_off_text}'
        #review_response = response["choices"][0]["message"]["content"]
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
    padding-top: 50px;
    padding-bottom: 50px;
}

span#MainMenu {
    display: none;
}

.stActionButton {
    display: none;
}

.viewerBadge_link__1S137 {
    display: none!important;
}

a.viewerBadge_container__1QSob {
    display: none!important;
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
    setTimeout(function () {
        //alert('Its been 5 seconds');
        streamlitDoc.getElementsByTagName("footer")[0].innerHTML = "Provided by <a href='https://airbnbconsulting.com' target='_blank' class='css-z3au9t egzxvld2'>Bnb Consulting</a>";
    
    // Find the div element with the specified class
var divElement = streamlitDoc.querySelector('.viewerBadge_link__1S137');\
alert('It exists! 1');

// Check if the element exists
if (divElement) {
  // Add the style attribute with the value "display: none;"
  alert('It exists! 2');
  divElement.style.display = 'none';
}
//}, 5000);
    
    });
</script>
'''
components.html(html_string)
st.markdown(html_string, unsafe_allow_html=True)
