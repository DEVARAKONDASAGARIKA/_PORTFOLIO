# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import requests
# import os
# from dotenv import load_dotenv
# import json
# import logging

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)

# load_dotenv()

# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# app = Flask(__name__, 
#             static_folder=FRONTEND_DIR,
#             static_url_path='')
# CORS(app)

# # API Keys
# GROQ_API_KEY = os.getenv('GROQ_API_KEY')
# HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
# GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# # Debug: Check if API keys are loaded
# print("=" * 50)
# print("API KEY STATUS:")
# print(f"GROQ_API_KEY: {'✅ Loaded' if GROQ_API_KEY else '❌ Not found'}")
# if GROQ_API_KEY:
#     print(f"GROQ_API_KEY starts with: {GROQ_API_KEY[:8]}...")
# print("=" * 50)

# # Portfolio context
# PORTFOLIO_CONTEXT = """
# You are a helpful assistant for Sagarika's portfolio website. 
# Sagarika is a 4th-year B.Tech CSE student at IIT Bhubaneswar with CGPA 6.77.
# She scored 92.9% in 12th grade and 10/10 in 10th grade.

# Skills: C, C++, Python, HTML, CSS, JavaScript, Next.js, MySQL, Git

# Experience: 
# - Research Intern at IIT Bhubaneswar (May-Jul 2025) under Prof. Sukantha Panda
# - Developed AHRC Research Dashboard using Next.js with Twilio authentication
# - Integrated real-time API communication for Tube Well Automation

# Projects:
# 1. Multi-Class Flower Species Classification - 75.89% accuracy using Random Forest
# 2. TCP Congestion Control Simulation - Analyzed Tahoe, Reno, Cubic
# 3. Interactive Portfolio Website - This site with LLM chatbot
# 4. Hospital Management System - MySQL, HTML, CSS, JS

# Keep responses concise, friendly, and professional.
# """

# # Serve frontend
# @app.route('/')
# def serve_index():
#     return send_from_directory(FRONTEND_DIR, 'index.html')

# @app.route('/<path:filename>')
# def serve_static(filename):
#     return send_from_directory(FRONTEND_DIR, filename)

# @app.route('/health')
# def health():
#     return jsonify({'status': 'healthy', 'message': 'Server is running!'})

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.json
#         user_message = data.get('message', '').strip()
        
#         if not user_message:
#             return jsonify({'error': 'Empty message'}), 400
        
#         print(f"\n📨 Received message: {user_message}")
        
#         # Try Groq API first
#         response = None
        
#         if GROQ_API_KEY:
#             print("🔄 Trying Groq API...")
#             try:
#                 response = call_groq_api(user_message)
#                 if response:
#                     print("✅ Groq API responded successfully!")
#                 else:
#                     print("❌ Groq API returned no response")
#             except Exception as e:
#                 print(f"❌ Groq API error: {str(e)}")
#         else:
#             print("⚠️ No Groq API key found")
        
#         # If Groq fails, try Hugging Face
#         if not response and HUGGINGFACE_TOKEN:
#             print("🔄 Trying Hugging Face API...")
#             try:
#                 response = call_huggingface_api(user_message)
#                 if response:
#                     print("✅ Hugging Face API responded successfully!")
#                 else:
#                     print("❌ Hugging Face API returned no response")
#             except Exception as e:
#                 print(f"❌ Hugging Face API error: {str(e)}")
        
#         # If both fail, use fallback
#         if not response:
#             print("🔄 Using fallback response")
#             response = generate_fallback_response(user_message)
        
#         print(f"📤 Response: {response[:100]}...")
#         return jsonify({'response': response})
        
#     except Exception as e:
#         print(f"❌ Error in chat endpoint: {str(e)}")
#         return jsonify({'response': "I'm having trouble connecting. Please try again!"}), 500

# def call_groq_api(message):
#     try:
#         url = "https://api.groq.com/openai/v1/chat/completions"
#         headers = {
#             "Authorization": f"Bearer {GROQ_API_KEY}",
#             "Content-Type": "application/json"
#         }
        
#         # Try different models if one doesn't work
#         models = ["mixtral-8x7b-32768", "llama2-70b-4096", "gemma-7b-it"]
        
#         for model in models:
#             try:
#                 payload = {
#                     "model": model,
#                     "messages": [
#                         {"role": "system", "content": PORTFOLIO_CONTEXT},
#                         {"role": "user", "content": message}
#                     ],
#                     "temperature": 0.7,
#                     "max_tokens": 500
#                 }
                
#                 print(f"  Trying model: {model}")
#                 response = requests.post(url, json=payload, headers=headers, timeout=30)
                
#                 if response.status_code == 200:
#                     data = response.json()
#                     return data['choices'][0]['message']['content']
#                 else:
#                     print(f"  Model {model} failed: {response.status_code}")
                    
#             except Exception as e:
#                 print(f"  Model {model} error: {str(e)}")
#                 continue
        
#         return None
            
#     except Exception as e:
#         print(f"Groq API Exception: {str(e)}")
#         return None

# def call_huggingface_api(message):
#     try:
#         url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
#         headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
#         payload = {
#             "inputs": f"{PORTFOLIO_CONTEXT}\n\nUser: {message}\nAssistant:",
#             "parameters": {"max_new_tokens": 500, "temperature": 0.7}
#         }
#         response = requests.post(url, json=payload, headers=headers, timeout=10)
#         if response.status_code == 200:
#             data = response.json()
#             if isinstance(data, list) and len(data) > 0:
#                 generated = data[0]['generated_text']
#                 # Extract only the assistant's response
#                 if "Assistant:" in generated:
#                     return generated.split("Assistant:")[-1].strip()
#                 return generated.strip()
#         return None
#     except Exception as e:
#         print(f"Hugging Face API error: {str(e)}")
#         return None

# def generate_fallback_response(message):
#     msg = message.lower()
    
#     # EDUCATION
#     if any(word in msg for word in ['education', 'study', 'college', 'university', 'academic', 'grade', 'class', 'board', 'percentage', 'cgpa', 'gpa', '12th', '10th', 'school', 'iit', 'bhubaneswar', 'intermediate', 'ssc']):
#         return "📚 My education journey:\n\n• IIT Bhubaneswar: B.Tech CSE (2022-2026) - CGPA: 6.77\n• 12th Grade (Intermediate): 92.9% (Sri Chaitanya, 2020-2022)\n• 10th Grade (SSC): 10/10 (Sri Chaitanya, 2020)\n\nI'm currently in my 4th year, graduating in 2026!"
    
#     # SKILLS
#     elif any(word in msg for word in ['skill', 'know', 'language', 'technologies', 'framework', 'frontend', 'backend', 'database', 'tools']):
#         return "💻 My technical skills include:\n\n• Languages: C, C++, Python\n• Web Technologies: HTML, CSS, JavaScript, Next.js\n• Databases: MySQL\n• Tools: Git, MS Excel, LTspice, Logism, Blender"
    
#     # PROJECTS
#     elif any(word in msg for word in ['project', 'work', 'built', 'create', 'developed', 'build', 'classifier', 'classification', 'simulation', 'management', 'portfolio', 'hospital', 'tcp', 'flower']):
#         return "🚀 Here are my key projects:\n\n1. Multi-Class Flower Species Classification (75.89% accuracy using Random Forest)\n2. TCP Congestion Control Simulation (Analyzed Tahoe, Reno, Cubic)\n3. Hospital Management System (MySQL, HTML, CSS, JS)\n4. Interactive Portfolio Website (HTML, CSS, JS, Python Flask, LLM Chatbot)\n\nWhich project would you like to know more about?"
    
#     # INTERNSHIP
#     elif any(word in msg for word in ['intern', 'experience', 'internship', 'research', 'professor', 'panda', 'dashboard', 'twilio', 'automation', 'ahrc']):
#         return "🎯 I interned at IIT Bhubaneswar (May-Jul 2025) under Prof. Sukantha Panda:\n\n• Developed AHRC Research Dashboard using Next.js\n• Implemented Twilio OTP-based secure authentication\n• Integrated real-time API communication for Tube Well Automation\n• Worked in a 3-member collaborative team"
    
#     # CONTACT
#     elif any(word in msg for word in ['contact', 'email', 'linkedin', 'reach', 'github', 'mail', 'connect']):
#         return "📬 Connect with me:\n\n• LinkedIn: linkedin.com/in/sagarika-devarakonda-298125278/\n• GitHub: github.com/DEVARAKONDASAGARIKA\n• Email: sagarikadevarakonda2004@gmail.com"
    
#     # COURSES
#     elif any(word in msg for word in ['course', 'subject', 'curriculum', 'syllabus', 'dsa', 'os', 'dbms', 'cn', 'ml']):
#         return "📖 Key courses I've taken:\n\n• Data Structures and Algorithms (DSA)\n• Operating Systems (OS)\n• Database Management Systems (DBMS)\n• Computer Networks (CN)\n• Machine Learning (ML)\n• Network and System Security\n• Entrepreneurship and Business Management"
    
#     # ACTIVITIES
#     elif any(word in msg for word in ['hobby', 'interest', 'sport', 'activity', 'badminton', 'volleyball', 'basketball', 'nss', 'volunteer', 'wissenaire']):
#         return "🏅 Beyond coding, I enjoy:\n\n• Sports: Badminton (NSO Team), Volleyball, Throwball, Basketball, Lawn Tennis, Table Tennis\n• Volunteering with NSS (National Service Scheme)\n• Event organizing as Associate at Wissenaire Fest, IIT Bhubaneswar"
    
#     # RESUME
#     elif any(word in msg for word in ['resume', 'cv', 'curriculum']):
#         return "📄 You can download my resume here:\n\nhttps://drive.google.com/file/d/1e4_pTcGp9pkwCS1YcnrVF7So-DzSvWRr/view?usp=sharing"
    
#     # DEFAULT
#     else:
#         return "🌟 I'd love to tell you about Sagarika! Feel free to ask about:\n\n• Education (CGPA, percentages, schools)\n• Skills & Technologies\n• Projects & Work\n• Experience & Internships\n• Courses & Subjects\n• Hobbies & Activities\n• Contact Information\n• Resume\n\nWhat would you like to know?"

# if __name__ == '__main__':
#     print(f"\n📁 Frontend directory: {FRONTEND_DIR}")
#     print(f"📄 Files in frontend: {os.listdir(FRONTEND_DIR) if os.path.exists(FRONTEND_DIR) else 'Directory not found'}")
#     print("\n🚀 Starting Flask server...")
#     app.run(debug=True, port=5000)









from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

app = Flask(__name__, 
            static_folder=FRONTEND_DIR,
            static_url_path='')
CORS(app)

# API Keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Debug: Check if API keys are loaded
print("=" * 50)
print("API KEY STATUS:")
print(f"GROQ_API_KEY: {'✅ Loaded' if GROQ_API_KEY else '❌ Not found'}")
if GROQ_API_KEY:
    print(f"GROQ_API_KEY starts with: {GROQ_API_KEY[:8]}...")
print("=" * 50)

# Portfolio context
PORTFOLIO_CONTEXT = """
You are a helpful assistant for Sagarika's portfolio website. 
Sagarika is a 4th-year B.Tech CSE student at IIT Bhubaneswar with CGPA 6.77.
She scored 92.9% in 12th grade and 10/10 in 10th grade.

Skills: C, C++, Python, HTML, CSS, JavaScript, Next.js, MySQL, Git

Experience: 
- Research Intern at IIT Bhubaneswar (May-Jul 2025) under Prof. Sukantha Panda
- Developed AHRC Research Dashboard using Next.js with Twilio authentication
- Integrated real-time API communication for Tube Well Automation

Projects:
1. Multi-Class Flower Species Classification - 75.89% accuracy using Random Forest
2. TCP Congestion Control Simulation - Analyzed Tahoe, Reno, Cubic
3. Interactive Portfolio Website - This site with LLM chatbot
4. Hospital Management System - MySQL, HTML, CSS, JS

Keep responses concise, friendly, and professional.
"""

# Serve frontend
@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Server is running!'})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        print(f"\n📨 Received message: {user_message}")
        
        # Try Groq API first
        response = None
        
        if GROQ_API_KEY:
            print("🔄 Trying Groq API...")
            try:
                response = call_groq_api(user_message)
                if response:
                    print("✅ Groq API responded successfully!")
                else:
                    print("❌ Groq API returned no response")
            except Exception as e:
                print(f"❌ Groq API error: {str(e)}")
        else:
            print("⚠️ No Groq API key found")
        
        # If Groq fails, use fallback
        if not response:
            print("🔄 Using fallback response")
            response = generate_fallback_response(user_message)
        
        print(f"📤 Response: {response[:100]}...")
        return jsonify({'response': response})
        
    except Exception as e:
        print(f"❌ Error in chat endpoint: {str(e)}")
        return jsonify({'response': "I'm having trouble connecting. Please try again!"}), 500

def call_groq_api(message):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # CORRECT MODELS FROM YOUR LIST
        models = [
            "llama-3.3-70b-versatile",        # Best quality, most capable
            "llama-3.1-8b-instant",           # Fastest, good for chat
            "meta-llama/llama-4-scout-17b-16e-instruct",  # Latest Llama 4
            "qwen/qwen3-32b",                 # Good reasoning capabilities
            "openai/gpt-oss-120b",            # OpenAI compatible
        ]
        
        for model in models:
            try:
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": PORTFOLIO_CONTEXT},
                        {"role": "user", "content": message}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500,
                    "top_p": 0.9
                }
                
                print(f"  Trying model: {model}")
                response = requests.post(url, json=payload, headers=headers, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data['choices'][0]['message']['content']
                    print(f"  ✅ Model {model} succeeded!")
                    return ai_response
                else:
                    print(f"  ❌ Model {model} failed: {response.status_code}")
                    print(f"     Response: {response.text[:200]}")
                    
            except Exception as e:
                print(f"  ⚠️ Model {model} error: {str(e)}")
                continue
        
        return None
            
    except Exception as e:
        print(f"❌ Groq API Exception: {str(e)}")
        return None

def generate_fallback_response(message):
    msg = message.lower()
    
    # EDUCATION
    if any(word in msg for word in ['education', 'study', 'college', 'university', 'academic', 'grade', 'class', 'board', 'percentage', 'cgpa', 'gpa', '12th', '10th', 'school', 'iit', 'bhubaneswar', 'intermediate', 'ssc']):
        return "📚 My education journey:\n\n• IIT Bhubaneswar: B.Tech CSE (2022-2026) - CGPA: 6.77\n• 12th Grade (Intermediate): 92.9% (Sri Chaitanya, 2020-2022)\n• 10th Grade (SSC): 10/10 (Sri Chaitanya, 2020)\n\nI'm currently in my 4th year, graduating in 2026!"
    
    # SKILLS
    elif any(word in msg for word in ['skill', 'know', 'language', 'technologies', 'framework', 'frontend', 'backend', 'database', 'tools']):
        return "💻 My technical skills include:\n\n• Languages: C, C++, Python\n• Web Technologies: HTML, CSS, JavaScript, Next.js\n• Databases: MySQL\n• Tools: Git, MS Excel, LTspice, Logism, Blender"
    
    # PROJECTS
    elif any(word in msg for word in ['project', 'work', 'built', 'create', 'developed', 'build', 'classifier', 'classification', 'simulation', 'management', 'portfolio', 'hospital', 'tcp', 'flower']):
        return "🚀 Here are my key projects:\n\n1. Multi-Class Flower Species Classification (75.89% accuracy using Random Forest)\n2. TCP Congestion Control Simulation (Analyzed Tahoe, Reno, Cubic)\n3. Hospital Management System (MySQL, HTML, CSS, JS)\n4. Interactive Portfolio Website (HTML, CSS, JS, Python Flask, LLM Chatbot)\n\nWhich project would you like to know more about?"
    
    # INTERNSHIP
    elif any(word in msg for word in ['intern', 'experience', 'internship', 'research', 'professor', 'panda', 'dashboard', 'twilio', 'automation', 'ahrc']):
        return "🎯 I interned at IIT Bhubaneswar (May-Jul 2025) under Prof. Sukantha Panda:\n\n• Developed AHRC Research Dashboard using Next.js\n• Implemented Twilio OTP-based secure authentication\n• Integrated real-time API communication for Tube Well Automation\n• Worked in a 3-member collaborative team"
    
    # CONTACT
    elif any(word in msg for word in ['contact', 'email', 'linkedin', 'reach', 'github', 'mail', 'connect']):
        return "📬 Connect with me:\n\n• LinkedIn: linkedin.com/in/sagarika-devarakonda-298125278/\n• GitHub: github.com/DEVARAKONDASAGARIKA\n• Email: sagarikadevarakonda2004@gmail.com"
    
    # COURSES
    elif any(word in msg for word in ['course', 'subject', 'curriculum', 'syllabus', 'dsa', 'os', 'dbms', 'cn', 'ml']):
        return "📖 Key courses I've taken:\n\n• Data Structures and Algorithms (DSA)\n• Operating Systems (OS)\n• Database Management Systems (DBMS)\n• Computer Networks (CN)\n• Machine Learning (ML)\n• Network and System Security\n• Entrepreneurship and Business Management"
    
    # ACTIVITIES & RESPONSIBILITIES
    elif any(word in msg for word in ['responsibility', 'responsibilities', 'position', 'role', 'hobby', 'interest', 'sport', 'activity', 'badminton', 'volleyball', 'basketball', 'nss', 'volunteer', 'wissenaire']):
        return "🏅 My responsibilities & activities:\n\n• Associate at Wissenaire Fest: Promoted events, engaged crowds, volunteered at workshops\n• Volunteer at NSS (National Service Scheme)\n• Sports: Badminton (NSO Team), Volleyball, Throwball, Basketball, Lawn Tennis, Table Tennis"
    
    # RESUME
    elif any(word in msg for word in ['resume', 'cv', 'curriculum']):
        return "📄 You can download my resume here:\n\nhttps://drive.google.com/file/d/1e4_pTcGp9pkwCS1YcnrVF7So-DzSvWRr/view?usp=sharing"
    
    # DEFAULT
    else:
        return "🌟 I'd love to tell you about Sagarika! Feel free to ask about:\n\n• Education (CGPA, percentages, schools)\n• Skills & Technologies\n• Projects & Work\n• Experience & Internships\n• Courses & Subjects\n• Hobbies & Activities\n• Contact Information\n• Resume\n\nWhat would you like to know?"

if __name__ == '__main__':
    print(f"\n📁 Frontend directory: {FRONTEND_DIR}")
    print(f"📄 Files in frontend: {os.listdir(FRONTEND_DIR) if os.path.exists(FRONTEND_DIR) else 'Directory not found'}")
    print("\n🚀 Starting Flask server...")
    app.run(debug=True, port=5000)