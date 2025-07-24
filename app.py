# careerme_app.py
import streamlit as st

# Dữ liệu gợi ý ngành theo MBTI
mbti_suggestions = {
    "INTJ": ["Kỹ sư phần mềm", "Nhà phân tích dữ liệu", "Nhà khoa học"],
    "INFP": ["Nhà tâm lý học", "Nhà văn", "Nhân sự"],
    "ESTP": ["Marketing", "Quản lý sự kiện", "Bán hàng"],
    "ISFJ": ["Y tá", "Giáo viên", "Chăm sóc khách hàng"]
}

# Câu hỏi MBTI (ví dụ)
questions = [
    {"text": "Bạn thích làm việc một mình hơn là làm việc nhóm?", "type": "I"},
    {"text": "Bạn tin vào trực giác hơn là thực tế?", "type": "N"},
    {"text": "Bạn thường quyết định dựa vào cảm xúc hơn là lý trí?", "type": "F"},
    {"text": "Bạn thích mọi thứ có kế hoạch hơn là linh hoạt?", "type": "J"}
]

# Bắt đầu Streamlit App
st.title("🧭 CareerMe - Ứng dụng Định hướng Nghề nghiệp")
st.write("Trắc nghiệm MBTI đơn giản giúp bạn hiểu rõ bản thân và định hướng nghề nghiệp.")

answers = []

# Hiển thị câu hỏi và thu thập câu trả lời
for q in questions:
    agree = st.radio(q["text"], ["Đồng ý", "Không đồng ý"], key=q["text"])
    if agree == "Đồng ý":
        answers.append(q["type"])
    else:
        # Nếu không đồng ý thì lấy ký tự đối lập
        opposite = {
            "I": "E", "N": "S", "F": "T", "J": "P"
        }
        answers.append(opposite[q["type"]])

# Kết quả
if st.button("🎯 Xem kết quả MBTI và Gợi ý ngành"):
    mbti_result = ''.join(answers)
    st.subheader(f"Kết quả MBTI của bạn là: *{mbti_result}*")

    suggestions = mbti_suggestions.get(mbti_result, ["Đang cập nhật ngành phù hợp..."])
    st.markdown("### 🛠 Ngành nghề gợi ý:")
    for job in suggestions:
        st.write(f"- {job}")