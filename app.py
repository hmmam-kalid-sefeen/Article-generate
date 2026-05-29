import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API الخاص بـ Gemini
genai.configure(api_key="AIzaSyA9lXNaZd-8qk7YFnkbky2mTOP_lZqi8gY")

# اختيار النموذج
model = genai.GenerativeModel('gemini-pro')

st.title("مولد المحتوى الذكي (بواسطة Gemini)")

keyword = st.text_input("أدخل الكلمة المفتاحية:")

if st.button("توليد المحتوى"):
    if keyword:
        with st.spinner('جاري إنشاء المحتوى...'):
            try:
                # إرسال الطلب لـ Gemini
                prompt = f"اكتب لي عنواناً جذاباً، وصفاً قصيراً، هاشتاقات مناسبة، ومقالاً مفصلاً عن موضوع: {keyword}. يرجى الكتابة باللغة العربية."
                response = model.generate_content(prompt)
                
                # عرض النتيجة
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("الرجاء إدخال كلمة!")
