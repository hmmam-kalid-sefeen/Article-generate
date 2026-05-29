import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API الخاص بـ Gemini
# تأكد من استبدال 'ضع_مفتاحك_هنا' بمفتاحك الحقيقي
genai.configure(api_key="AIzaSyA9lXNaZd-8qk7YFnkbky2mTOP_lZqi8gY")

# اختيار النموذج المحدث
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("مولد المحتوى الذكي (بواسطة Gemini)")

# مربع الإدخال
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
