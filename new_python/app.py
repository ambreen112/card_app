import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64 string
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def main():
    st.set_page_config(page_title="ID Card Generator", page_icon="📛", layout="centered")

    # Inject Custom CSS for Background and Styling
    custom_css = """
        <style>
            /* Set background color */
            body {
                background-color: #e6f0ff !important;
            }
            /* Apply background color to the main content */
            .stApp {
                background-color: #e6f0ff;
            }
            
            /* Customizing the sidebar */
            [data-testid="stSidebar"] {
                background-color: #d9e6f2;
            }
            
            /* Styling the ID Card */
            .id-card {
                border: 4px solid #004080;
                padding: 15px;
                width: 300px;
                text-align: center;
                border-radius: 15px;
                background: white;
                color: black;
                font-family: Arial, sans-serif;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
            }

            /* Text formatting */
            .id-card h3 {
                margin: 5px 0;
                font-size: 20px;
                color: #004080;
                text-decoration: underline;
            }
            .id-card p {
                margin: 5px 0;
                font-size: 16px;
                color: #004080;
            }

            /* Profile image styling */
            .profile-img {
                border-radius: 50%;
                border: 3px solid #004080;
            }

            /* School Logo Styling */
            .school-logo {
                width: 80px;
                height: auto;
                margin-bottom: 10px;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title("📛 School ID Card Generator")
    
    # Sidebar info
    st.sidebar.markdown(
        "<h2 style='color: #004080;'>About</h2>"
        "<p style='font-size: 16px; text-align: justify;'>"
        "This app allows you to create a school ID card by uploading a school logo, a student's photo, and entering details."
        "</p>",
        unsafe_allow_html=True
    )

    # Upload School Logo
    school_logo_file = st.file_uploader("🏫 Upload School Logo", type=["jpg", "png", "jpeg"])

    # Upload Student Photo
    uploaded_file = st.file_uploader("📷 Upload Student's Photo", type=["jpg", "png", "jpeg"])
    
    # Enter details
    student_Fname = st.text_input("Student First Name")
    student_Lname = st.text_input("Student Last Name")
    grade = st.text_input("Grade/Class")
    section = st.text_input("Section")
    school_name = st.text_input("School Name")
    id_number = st.text_input("ID No.")

    if uploaded_file and student_Fname and student_Lname and grade and school_name:
        image = Image.open(uploaded_file)
        image_base64 = image_to_base64(image)

        # Convert School Logo to Base64 (if uploaded)
        school_logo_base64 = ""
        if school_logo_file:
            school_logo = Image.open(school_logo_file)
            school_logo_base64 = image_to_base64(school_logo)

        st.subheader("🆔 Generated School ID Card")

        # Display the ID card
        st.markdown(
            f"""
            <div class="id-card">
                {"<img src='data:image/png;base64," + school_logo_base64 + "' class='school-logo'>" if school_logo_base64 else ""}
                <h3>{student_Fname} {student_Lname}</h3>
                <p><strong>Grade:</strong> {grade}</p>
                <p><strong>Section:</strong> {section}</p>
                <p><strong>ID No.:</strong> {id_number}</p>
                <p><strong>School:</strong> {school_name}</p>
                <img src="data:image/png;base64,{image_base64}" width="100" class="profile-img">
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
