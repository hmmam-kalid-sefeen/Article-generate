import streamlit as st
import google.generativeai as genai

# إعداد المفتاح من إعدادات Streamlit السرية
# تأكد أن الاسم في Secrets هو GEMINI_API_KEY
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["AIzaSyDu0qj6_ttEpYiO4KxPRz9Lm94iVDVc8Z4"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("مفتاح API غير موجود في إعدادات Secrets. الرجاء إضافته.")
    st.stop()

st.title("مولد المحتوى الذكي")

keyword = st.text_input("أدخل الكلمة المفتاحية:")

if st.button("توليد المحتوى"):
    if keyword:
        with st.spinner('جاري التوليد...'):
            try:
                response = model.generate_content(f"اكتب مقالاً مفصلاً عن: {keyword}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال كلمة مفتاحية!")
