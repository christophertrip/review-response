import streamlit as st
import streamlit.components.v1 as components
import openai

st.set_page_config(page_title="Review Response App", page_icon="✍️")

openai.api_key = st.secrets["OPENAI_API"]

st.title('✍️ Review Response')
#type_of_host = st.selectbox('Choose type of Host:', ('Home Stay 🏠', 'Airbnb Experience 🏄‍♂️'), index=0, help="Choose if this is for a Home Stay or for an Airbnb Experience")
# hosts = st.checkbox('Chris & Andrea')
#if type_of_host == "Home Stay 🏠":
#host_name = st.text_input('Host Name', 'Chris, Andrea & Mitchell', placeholder="Host name", label_visibility="collapsed")
host_name = "Chris, Andrea & Mitchell"
#else:
	#host_name = st.text_input('Host Name', placeholder="Host name", label_visibility="collapsed")
guest_name = st.text_input('Guest Name', placeholder="Guest name", label_visibility="collapsed")
guest_review = st.text_area('Guest Review', placeholder="Paste your Guest's review here. AI will automatically detect the language for the reply.", label_visibility="collapsed", height=250)
guest_review = f'"{guest_review}"'
#print (guest_review)

# response_language = st.selectbox('Choose response language:', ('English 🇺🇸', 'Spanish 🇲🇽', 'French 🇫🇷'), index=0)

# Different for Homes and Experiences
#if type_of_host == "Home Stay 🏠":
	#if response_language == "English 🇺🇸":
    		#sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', 'You always have a home here with us in Playa!', placeholder="Custom text", label_visibility="visible", help="Example: _You always have a home here with us!_")
	#elif response_language == "Spanish 🇲🇽":
    		#sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', '¡Siempre tienes un hogar aquí con nosotros en Playa!', placeholder="Custom text", label_visibility="visible", help="Example: _You always have a home here with us!_")
	#else:
    		#sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', 'Vous avez toujours une maison ici avec nous à Playa!', placeholder="Custom text", label_visibility="visible", help="Example: _You always have a home here with us!_")
#else:
    #sign_off_text = st.text_input('Custom text at the end of the response: _(Optional)_', 'Pura Vida! 🇨🇷', placeholder="Custom text", label_visibility="visible", help="Example: _Thanks for coming on the adventure!_")

# Different for Homes and Experiences
#if type_of_host == "Home Stay 🏠":
messages = [{"role": "system", "content": f'Hello wonderful assistant! We are Airbnb hosts. Our names are {host_name}. Each of our guests that stay in our Airbnb rentals leave us a review of their experience. We need you to create a polite response to the guest review. Below is a review from a guest named {guest_name}:\n\n"{guest_review}\n\n We need you to create a polite response to the guest review. Do not create a translation of the guest review. We do not want that. I am going to provide you with directions on how we need the review response to be. Our guests come from all over the world so they create their reviews in different languages. We need you to make the response in the same language as the guest review. The default language for the response is English. Before you create the response to the guest review you need to determine what language the guest review is in. To do this we want you to analyze the guest review and then determine what language most of the words are in. Just because a few words are in a language it does not mean that you create the response in that language but instead you need to determine what language the majority of the words are in! Please make the response 50 words or less. Please address the guest by their name in the response. Please thank the guest for their positive comment. Do not address any negative comments or criticisms. At the end of the response please append the following text — You always have a home here with us in Playa! And sign off with our host names. I have been having issues in the past with you creating the response in the wrong language. Please do not do that. It is very simple to determine what language the guest review is in by determining what language the majority of their words are in. It is extremely important that the response that you create is in the same language as the majority of the word in the guest review. We only need you to create the response only. Thank you!'}]
#else:
   # messages = [{"role": "system", "content": f'I am an Airbnb Experience host named {host_name}. A guest named {guest_name} left the following review. Please create a very polite reply based on their review in {response_language}, in 50 words or less.\n\n"{guest_review}"'}]

# if button clicked then do the with st.spinner
if st.button('Start the Magic  🪄'):

    with st.spinner(f"Creating your Reponse..."): 
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        review_response = f'{response["choices"][0]["message"]["content"]}'
	#review_response = f'{response["choices"][0]["message"]["content"]} — {sign_off_text}'
        #review_response = response["choices"][0]["message"]["content"]
        st.divider()
        st.subheader('Review Response')
        st.code(review_response, language=None)
	
	    st.code(guest_review, language=None)

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
    padding-top: 20px;
    padding-bottom: 20px;
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
