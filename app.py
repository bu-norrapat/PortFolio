from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.context_processor
def inject_lang():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    return {'lang': lang}

@app.route('/')
def home():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    response = render_template('home.html', page_title='Home', lang=lang)
    response = make_response(response)
    response.set_cookie('lang', lang, max_age=60*60*24*30)
    return response

@app.route('/project')
def project():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    projects = [
        {
            'title': 'A Simple shop app',
            'image' : 'Images/dota2shop.png',
            'link': 'https://github.com/bu-norrapat/dota2shop.git',
            'description': 'Description : As a First year Student this is my very first Project',
            'whatilearn': 'What I learn : basic Python,SQL,VScode',
            'about' : 'About : A simple shop app that Start With a Registeration,Log in,how many items each user have bought',
            'description_th': 'คำอธิบาย : ในฐานะนักศึกษาชั้นปีที่ 1 นี่คือโปรเจกต์แรกของผม',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : Python พื้นฐาน, SQL, VS Code',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : เว็บแอปร้านค้าขนาดเล็กที่เริ่มจากการสมัครสมาชิก เข้าสู่ระบบ และนับจำนวนรายการที่ผู้ใช้แต่ละคนซื้อ',
        },
        {
            'title': 'Arduino Project',
            'image' : 'Images/Arduino.jpg',
            'link': 'https://github.com/bu-norrapat/esp32-fan-project.git',
            'description': 'Description : Learning ESP32 and other components',
            'whatilearn': 'What I learn : IoT devices , c++ , Blynk Cloud',
            'about' : 'About : This Particular Project is About Controlling a Fan based on temparature higher Temp Higher Fan Speed and send temperature data to Blynk Cloud',
            'description_th': 'คำอธิบาย : เรียนรู้เกี่ยวกับ ESP32 และอุปกรณ์ต่าง ๆ',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : อุปกรณ์ IoT, C++, Blynk Cloud',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : การควบคุมพัดลมตามอุณหภูมิ โดยอุณหภูมิสูงขึ้น พัดลมจะหมุนเร็วขึ้น และส่งข้อมูลอุณหภูมิไปยัง Blynk Cloud',
        },
        {
            'title': 'FINDCAM Item Finder using Vision Ai',
            'image' : 'Images/Findcam.png',
            'link': 'https://www.youtube.com/watch?v=1nRZWKHHlf0',
            'description': 'Description : My team and I tackle a Proposition From a Company',
            'whatilearn': 'What I learn : Vision Ai, Team Work',
            'about' : 'About : My Role in this Project is ai tester. testing various Ai model and trying to improve Ai performance',
            'description_th': 'คำอธิบาย : ผมและทีมรับโจทย์จากบริษัทหนึ่ง',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : Vision AI, การทำงานเป็นทีม',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมในโปรเจกต์นี้คือ AI Tester ทดสอบโมเดล AI ต่าง ๆ และพยายามปรับปรุงประสิทธิภาพของ AI',
        },
        {
            'title': 'UNISYNC Email',
            'image' : 'Images/Unisync2.png',
            'link': 'https://github.com/bu-norrapat/BuEmailSystem',
            'description': 'Description : My team and I Making an Email Webapp',
            'whatilearn': 'What I learn : Team Work,Cloud microsoft azure database,Visual Studio',
            'about' : 'About : My Role in this Project is Full Stack Dev. Building backend and Manage SQL database ##NOTE this website is no longer available due to microsoftazure database expiration',
            'description_th': 'คำอธิบาย : ผมและทีม สร้างเว็บแอปอีเมล',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การทำงานเป็นทีม, Cloud Microsoft Azure Database, Visual Studio',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมคือ Full Stack Developer พัฒนาบางส่วนของระบบหลังบ้านและจัดการฐานข้อมูล SQL ###หมายเหตุเว็บไซต์นี้ไม่สามารถใช้งานได้อีกต่อไปเนื่องจากวันหมดอายุของฐานข้อมูล Microsoft Azure',
        },
        {
            'title': 'Xocial Demo',
            'image' : 'Images/Xocialdemo.png',
            'link': 'put link here',
            'description': 'Description : My team and I making a Xocial webapp mock up',
            'whatilearn': 'What I learn : Team Work,Front End Dev,UX/UI Design',
            'about' : 'About : My Role in this Project is Front-end Developer Designing UX/UI',
            'description_th': 'คำอธิบาย : ผมและทีม สร้าง mock up ของเว็บแอป Xocial',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การทำงานเป็นทีม, Front-end Development, UX/UI Design',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมคือ Front-end Developer รับผิดชอบการออกแบบ UX/UI',
        },
        {
            'title': 'Pentest Report',
            'image' : 'Images/pentest.png',
            'link': 'put link here',
            'description': 'Description : My team and I do a vulnerabilities assesment report',
            'whatilearn': 'What I learn : Team Work , pentesting , Kali Linux',
            'about' : 'About : My Role in this Project is Vulnerability Validator. Reproducing Found vulnerability of machines found in offsec',
            'description_th': 'คำอธิบาย : ผมและทีม ทำรายงานประเมินช่องโหว่ความปลอดภัย',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การทำงานเป็นทีม, การเจาะระบบ, Kali Linux',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมคือ Vulnerability Validator ทำการยืนยันช่องโหว่ที่พบบนเครื่องต่างๆใน Offsec',
        },
        {
            'title': 'Data Visualization',
            'image' : 'Images/Data.png',
            'link': 'https://www.youtube.com/watch?v=B2VgVg-wk00',
            'description': 'Description : My team and I do a data visualization report',
            'whatilearn': 'What I learn : Team Work , presenting , Power BI, Davinci Resolve',
            'about' : 'About : My Role in this Project is data visualizer and editing presentation video',
            'description_th': 'คำอธิบาย : ผมและทีม ทำรายงานนำเสนอข้อมูลเป็นกราฟรูปภาพ',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การทำงานเป็นทีม, การนำเสนอ, Power BI, Davinci Resolve',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมคือ data visualizer และ ตัดต่อวิดีโอที่ใช้นำเสนอ',
        },
        {
            'title': 'Movie Ticket',
            'image' : 'Images/Movie.png',
            'link': 'https://github.com/bu-norrapat/CinemaProj',
            'description': 'Description : My team and I do a Movie ticket booking',
            'whatilearn': 'What I learn : Team Work , css , html',
            'about' : 'About : My Role in this Project is full stack dev i learned basic html from this project',
            'description_th': 'คำอธิบาย : ผมและทีม ทำเว็ปแอปการจองตั๋วหนัง',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การทำงานเป็นทีม , css , html',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : บทบาทของผมคือ full stack dev ผมได้เรียนรู้พื้นฐาน html จากโปรเจกนี้',
        },
        {
            'title': 'The PortFolio Itself',
            'image' : 'Images/Port.png',
            'link': 'https://github.com/bu-norrapat/PortFolio',
            'description': 'Description : I make my own PortFolio Website',
            'whatilearn': 'What I learn : File Management , Time Management',
            'about' : 'About : My very first portfolio website !! i learned a lot about file management if i manage my file i would save a lot of time.',
            'description_th': 'คำอธิบาย : ผมาสร้างเว็บพอร์ตโฟลิโอของผมเอง',
            'whatilearn_th': 'สิ่งที่ผมได้เรียนรู้ : การจัดการไฟล์ และ เวลา',
            'about_th' : 'เกี่ยวกับโปรเจกต์ : เว็ปพอร์ตโฟลิโอเว็ปแรกของผมเอง !! ผมได้เรียนรู้แล้วว่าถ้าผมจัดการไฟล์ให้ดีผมจะประหยัดเวลาได้เยอะมาก',
        },
    ]
    response = render_template('project.html', page_title='Project', projects=projects, lang=lang)
    response = make_response(response)
    response.set_cookie('lang', lang, max_age=60*60*24*30)
    return response

@app.route('/activity')
def activity():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    activities = [
        {
            'title': 'mini CTF , career expo 2026',
            'image': 'Images/activity1.jpg',
            'description': 'Attended career expo 2026 and BU Cyber Fortress',
            'description_detail': 'At Career Expo i have learned about the experience of being an intern from many intern in the expo. And Crack some Flags in mini CTF with my friend in the picture',
            'description_th': 'เข้าร่วม Career Expo 2026 และ BU Cyber Fortress',
            'description_detail_th': 'ณ Career Expo ผมได้เรียนรู้เกี่ยวกับ ประสบการณ์ทำงานของการฝึกงานจากพี่ๆที่ฝึกงานกับบริษัทในงาน และ เข้าร่วมเล่น CTF กับเพื่อนในรูป',
        },
        {
            'title': 'IT Empowering Day',
            'image': 'Images/ITday.jpg',
            'description': 'Attended IT Empowering Day : in the era of Ai',
            'description_detail': 'At IT Empowering Day it is similiar to the previous Career Expo but this time there is a guest speaker talking about Ai and How Ai is changing the world i have learn a lot about the impact of ai to many industry around the globe',
            'description_th': 'เข้าร่วม IT Empowering Day : in the era AI',
            'description_detail_th': 'ณ IT Empowering Day มันคล้ายๆกับ Career Expo ก่อนหน้านี้ แต่มีแขกรับเชิญมาร่วมพูดให้ความรู้เกี่ยวกับ AI AI เปลี่ยนแปลงโลกยังไงและAi ส่งผลกระทบต่ออุตสาหกรรมทั่วโลกอย่างไรบ้าง ',
        }
    ]
    response = render_template('activity.html', page_title='Activity', activities=activities, lang=lang)
    response = make_response(response)
    response.set_cookie('lang', lang, max_age=60*60*24*30)
    return response

@app.route('/certificates')
def certificates():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    certificates = [
        {
            'title': 'Guided Learning Project Management',
            'image': 'Images/eCertificate1.pdf',
            'description': 'My Professional certification document.',
            'description_th': 'เอกสารรับรองของผม',
        },
        {
            'title': 'Cloud Infrastucture 2025 (AI associate)',
            'image': 'Images/eCertificate2.pdf',
            'description': 'My Professional certification document.',
            'description_th': 'เอกสารรับรองของผม',
        },
        {
            'title': 'Data Platform 2025',
            'image': 'Images/eCertificate3.pdf',
            'description': 'My Professional certification document.',
            'description_th': 'เอกสารรับรองของผม',
        },
        {
            'title': 'Siebel CRM',
            'image': 'Images/eCertificate4.pdf',
            'description': 'My Professional certification document.',
            'description_th': 'เอกสารรับรองของผม',
        },
        {
            'title': 'Cloud Infrastucture 2025 (Foundations associate)',
            'image': 'Images/eCertificate5.pdf',
            'description': 'My Professional certification document.',
            'description_th': 'เอกสารรับรองของผม',
        }
    ]
    response = render_template('cert.html', page_title='Certification', certificates=certificates, lang=lang)
    response = make_response(response)
    response.set_cookie('lang', lang, max_age=60*60*24*30)
    return response

@app.route('/about')
def about():
    lang = request.args.get('lang') or request.cookies.get('lang', 'en')
    response = render_template('about.html', page_title='About Me', lang=lang)
    response = make_response(response)
    response.set_cookie('lang', lang, max_age=60*60*24*30)
    return response

if __name__ == '__main__':
    app.run(debug=True)
