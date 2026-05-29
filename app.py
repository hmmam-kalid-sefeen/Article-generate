import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API
genai.configure(api_key="AIzaSyDu0qj6_ttEpYiO4KxPRz9Lm94iVDVc8Z4")

# تعريف النموذج
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("مولد المحتوى الذكي")

keyword = st.text_input("أدخل الكلمة المفتاحية:")

if st.button("توليد المحتوى"):
    if keyword:
        with st.spinner('جاري إنشاء المحتوى...'):
            try:
                response = model.generate_content(f"اكتب لي عنواناً، وصفاً، هاشتاقات، ومقالاً مفصلاً عن: {keyword}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال كلمة مفتاحية!")
