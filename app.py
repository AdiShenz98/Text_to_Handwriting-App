# Core Packages
from attr import dataclass
from requests.sessions import SessionRedirectMixin
import streamlit as st
from streamlit.elements.image import image_to_url
from streamlit.state.session_state import SessionState 
import pywhatkit as kit

# Additional Packages
import requests
import os
import base64



# Page Config

# Formatting and Styling Functions
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def text_to_handwriting(text, save_as = "result.png", rgb = [0,0,0]):
    data = requests.get("https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (text,rgb[0],rgb[1],rgb[2])).content
    return data

def hex2rgb(color):
  hex = color.lstrip('#')
  rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
  return rgb

def img_to_html(data, save_as):
    if save_as == '':
        save_as = 'converted_image.png'
    else:
        save_as = save_as + '.png'
    bin_str = base64.b64encode(data).decode()
    href = f'<p align="right"><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(save_as)}">Download {save_as}</a></p>'
    return href



def main():
    # Loading the CSS styling file
    local_css("style.css")
    
    st.title('Text to handwriting App')
    main_cont = st.beta_container()
    display_cont = st.beta_container()
    Download_opt_cont = st.beta_container()
    
    with main_cont:     
        with st.form('Form 1'):
            txt = st.text_area('Enter Text',max_chars=750)
            txt_conv = '\n\n' + txt

            c1, c2 = st.beta_columns(2)

            with c1:
                color = st.color_picker('Select Font Color',value='#000000')
                rgb = list(hex2rgb(color))
          
        
        with c2:
            if 'b1' not in st.session_state:
                st.session_state.b1 = False
            st.markdown("<br>",unsafe_allow_html=True)
            b1 = st.form_submit_button('Convert')
            if b1:
                st.session_state.b1 = True

            
        
        
    with display_cont:
        with st.form('Form 2'):
            if st.session_state.b1:
                data = text_to_handwriting(txt_conv,rgb=rgb)
                st.subheader('Converted Image')
                st.image(data)
                c1, c2 = st.beta_columns(2)
                with c1:
                    file_name = st.text_input('File name')
                with c2:
                    st.markdown("<br>",unsafe_allow_html=True)
                    submit = st.form_submit_button('Generate Download Link')
                    if submit:            
                        download_link = img_to_html(data, file_name)            
                        st.markdown(download_link,unsafe_allow_html=True)


    
    


if __name__ == '__main__':
    main()