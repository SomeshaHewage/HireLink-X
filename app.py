import hashlib
from flask import Flask, render_template, request, session, jsonify
import os
import ml
from werkzeug.utils import secure_filename
from firebasedb import ToDoCollection
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'HireLinkX'

UPLOAD_FOLDER = 'static/uploads'
PROFILE_IMAGE_FOLDER ='static/profile_image'
RESUME_FOLDER ='static/resume'
COVER_LETTER_FOLDER ='static/cover_letter'
UNI_LETTER_FOLDER = 'static/uni_letter'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROFILE_IMAGE_FOLDER'] = PROFILE_IMAGE_FOLDER
app.config['RESUME_FOLDER'] = RESUME_FOLDER
app.config['COVER_LETTER_FOLDER'] = COVER_LETTER_FOLDER
app.config['UNI_LETTER_FOLDER'] = UNI_LETTER_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(PROFILE_IMAGE_FOLDER):
    os.makedirs(PROFILE_IMAGE_FOLDER)
if not os.path.exists(RESUME_FOLDER):
    os.makedirs(RESUME_FOLDER)
if not os.path.exists(COVER_LETTER_FOLDER):
    os.makedirs(COVER_LETTER_FOLDER)
if not os.path.exists(UNI_LETTER_FOLDER):
    os.makedirs(UNI_LETTER_FOLDER)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'hirelinkx@gmail.com'
app.config['MAIL_PASSWORD'] = 'kjfmymsuaiogahiy'

mail = Mail(app)


# Home
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/h_about')
def h_about():
    return render_template("About.html")

@app.route('/h_company')
def h_company():
    return render_template("company.html")

@app.route('/h_services')
def h_services():
    return render_template("services.html")
    
@app.route('/h_vacancy')
def h_vacancy():
    return render_template("vacancy.html")

@app.route('/logincan')
def logincan():
    return render_template("logincan.html")

@app.route('/logincom')
def logincom():
    return render_template("logincom.html")

@app.route('/regcan')
def regcan():
    return render_template("regcan.html")

@app.route('/regcom')
def regcom():
    return render_template("regcom.html")
# Home


# Candidate
@app.route('/candidate_index')
def candidate_index():
    return render_template("./candidate/candidate-index.html")

@app.route('/about')
def about():
    return render_template("./candidate/about.html")

@app.route('/services')
def services():
    return render_template("./candidate/services.html")

@app.route('/company')
def company():
    return render_template("./candidate/company.html")

@app.route('/vacancy')
def vacancy():
    return render_template("./candidate/vacancy.html")

@app.route('/testimonal')
def testimonal():
    return render_template("./candidate/testimonal.html")

@app.route('/contact')
def contact():
    return render_template("./candidate/contact.html")

@app.route('/profile')
def profile():
    return render_template("./candidate/profile.html")

@app.route('/editprofile')
def editprofile():
    return render_template("./candidate/editprofile.html")

@app.route('/chat')
def chat():
    return render_template("./candidate/chat.html")

@app.route('/error')
def error():
    return render_template("./candidate/error.html")
# Candidate


# Compnay
@app.route('/company_index')
def company_index():
    return render_template("./company/company-index.html")

@app.route('/c_about')
def c_about():
    return render_template("./company/about.html")

@app.route('/c_services')
def c_services():
    return render_template("./company/services.html")

@app.route('/c_company')
def c_company():
    return render_template("./company/company.html")

@app.route('/c_vacancy')
def c_vacancy():
    return render_template("./company/vacancy.html")

@app.route('/c_testimonal')
def c_testimonal():
    return render_template("./company/testimonal.html")

@app.route('/c_contact')
def c_contact():
    return render_template("./company/contact.html")

@app.route('/c_profile')
def c_profile():
    return render_template("./company/profile.html")

@app.route('/c_editprofile')
def c_editprofile():
    return render_template("./company/editprofile.html")

@app.route('/c_chat')
def c_chat():
    return render_template("./company/chat.html")

@app.route('/viewapplication')
def viewapplication():
    return render_template("./company/viewapplication.html")
   
# Compnay




@app.route('/applyNow', methods=['POST'])
def applyNow():
    position = request.form["position"]
    company_name = request.form["company_name"]
    company_email = request.form["company_email"]

    candidateUser = session.get('candidateUser') 
    candidateUser_username = session.get('candidateUser_username') 
    candidateUser_phone = session.get('candidateUser_phone') 
    candidateUser_resume_path = session.get('candidateUser_resume_path') 
    candidateUser_uni_letter_path = session.get('candidateUser_uni_letter_path') 
    candidateUser_cover_letter_path = session.get('candidateUser_cover_letter_path') 

  
    dbdata.addTodoItem({
        "position": position,
        "company_name": company_name,
        "company_email": company_email,
        "candidateUser": candidateUser,
        "candidateUser_username": candidateUser_username,
        "candidateUser_phone": candidateUser_phone,
        "candidateUser_resume_path": candidateUser_resume_path,
        "candidateUser_uni_letter_path": candidateUser_uni_letter_path,
        "candidateUser_cover_letter_path": candidateUser_cover_letter_path
    }, "zz_Applycation/")

    return render_template("./candidate/vacancy.html")


@app.route('/load_application', methods=['POST'])
def load_application():
    user_email = session.get('companyUser')
    newdata = dbdata.getTodoItems()
    print(newdata[5])
    # jsonify the data
    jdata = jsonify({"jobs": newdata[5], "loguserdata":user_email})
    # set CORS headers
    jdata.headers.add('Access-Control-Allow-Origin', '*')
    return jdata


@app.route('/add_job', methods=['POST'])
def add_job():
    position = request.form["position"]
    introduction = request.form["introduction"]
    key_res = request.form["key_res"]
    quali = request.form["quali"]
    duration = request.form["duration"]
    loc = request.form["loc"]

    user_email = session.get('companyUser') 
    user_email_user = session.get('companyUser_user') 
  
    dbdata.addTodoItem({
        "position": position,
        "introduction": introduction,
        "key_res": key_res,
        "quali": quali,
        "duration": duration,
        "loc": loc,
        "company_email":user_email,
        "username":user_email_user
    }, "jobs/")

    return render_template("./company/company-index.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    print(file)

    # If the user submits an empty part without selecting a file, the browser will send an empty file name
    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the file with a secure filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        resume_path = file_path  # Replace with your PDF file path
        jobname,score,all_error_type = ml.main(resume_path)
        print(all_error_type)

        return jsonify({"score":score,"all_error_type":all_error_type,"jobname":jobname})


@app.route('/loaddata', methods=['POST'])
def loaddata():
    newdata = dbdata.getTodoItems()
    print(newdata[3])
    # jsonify the data
    jdata = jsonify({"jobs": newdata[3]})
    # set CORS headers
    jdata.headers.add('Access-Control-Allow-Origin', '*')
    return jdata


@app.route('/addFeedback',methods=['POST'])
def addFeedback():
    name = request.form["name"]
    message = request.form["message"]

    dbdata.addTodoItem({
        "name": name,
        "message": message
    }, "Feedback/")
    return render_template("./candidate/testimonal.html")


@app.route('/C_addFeedback',methods=['POST'])
def c_addFeedback():
    name = request.form["name"]
    message = request.form["message"]

    dbdata.addTodoItem({
        "name": name,
        "message": message
    }, "Feedback/")
    return render_template("./company/testimonal.html")


@app.route('/loadFeedback', methods=['POST'])
def loadFeedback():
    newdata = dbdata.getTodoItems()
    print(newdata[2])
    # jsonify the data
    jdata = jsonify({"jobs": newdata[2]})
    # set CORS headers
    jdata.headers.add('Access-Control-Allow-Origin', '*')
    return jdata


@app.route('/contactUs',methods=['POST'])
def contactUs():
    print("email starting")
    to = "ttheruwandi@gmail.com"
    subject = "Contact Us"

    email = request.form["email"]
    name = request.form['name']
    emailbody = request.form['message']

    
    msg = Message(subject=subject,
                  sender="hirelinkx@gmail.com",
                  recipients=[to])
    msg.body = emailbody + "\t\t" + name + "\t\t" + email
    mail.send(msg)
    return render_template("./candidate/contact.html")


@app.route('/c_contactUs',methods=['POST'])
def c_contactUs():
    print("email starting")
    to = "ttheruwandi@gmail.com"
    subject = "Contact Us"

    email = request.form["email"]
    name = request.form['name']
    emailbody = request.form['message']

    
    msg = Message(subject=subject,
                  sender="hirelinkx@gmail.com",
                  recipients=[to])
    msg.body = emailbody + "\t\t" + name + "\t\t" + email
    mail.send(msg)
    return render_template("./company/contact.html")


@app.route('/loadProfile', methods=['POST'])
def loadProfile():
    candidate_email = session.get('candidateUser')  # Getting candidate email from session
    database = dbdata.getTodoItems()

    for candidate_data in database[0].values():
        if candidate_email == candidate_data["email"]:
            jdata = jsonify({"jobs": candidate_data})
            jdata.headers.add('Access-Control-Allow-Origin', '*')
            return jdata

    # If no matching candidate is found, you might want to handle this case accordingly
    return jsonify({"error": "Candidate profile not found"})


@app.route('/c_loadProfile', methods=['POST'])
def c_loadProfile():
    company_email = session.get('companyUser')  # Getting company email from session
    database = dbdata.getTodoItems()

    for company_data in database[1].values():
        if company_email == company_data["email"]:
            jdata = jsonify({"jobs": company_data})
            jdata.headers.add('Access-Control-Allow-Origin', '*')
            return jdata

    # If no matching company is found, you might want to handle this case accordingly
    return jsonify({"error": "Company profile not found"})


@app.route('/editProfile', methods=['POST'])
def editProfile():
    user_email = session.get('candidateUser')  # Getting candidate email from session

    database = dbdata.getTodoItems()

    for n in database[0]:
        if user_email == database[0][n]["email"]:
            emailne = n

            # Fetch existing candidate data
            candidate_data = database[0][n]
   
            if candidate_data:
                # Update only the fields that are provided in the request
                name = request.form.get("name", candidate_data.get("username"))
                phone = request.form.get("phone", candidate_data.get("phone"))
                birthday = request.form.get("birthday", candidate_data.get("birthdate"))
                industry = request.form.get("industry", candidate_data.get("industry"))
                education = request.form.get("education", candidate_data.get("education"))
                experience = request.form.get("experience", candidate_data.get("experience"))
                password = request.form.get("password", candidate_data.get("password"))
                image = request.files.get('profile_image', None)
                resume = request.files.get('resume', None)
                coverLetter = request.files.get('covletter', None)
                uniLetter = request.files.get('uniletter', None)

                    # Hash the password using MD5
                hashed_password = hashlib.md5(password.encode()).hexdigest()

                # Save files if provided
                image_path = candidate_data.get("image_path")
                resume_path = candidate_data.get("resume_path")
                cover_letter_path = candidate_data.get("cover_letter_path")
                uni_letter_path = candidate_data.get("uni_letter_path")

                if image:
                    image_path = os.path.join(app.config['PROFILE_IMAGE_FOLDER'], secure_filename(image.filename))
                    image.save(image_path)
                if resume:
                    resume_path = os.path.join(app.config['RESUME_FOLDER'], secure_filename(resume.filename))
                    resume.save(resume_path)
                if coverLetter:
                    cover_letter_path = os.path.join(app.config['COVER_LETTER_FOLDER'], secure_filename(coverLetter.filename))
                    coverLetter.save(cover_letter_path)
                if uniLetter:
                    uni_letter_path = os.path.join(app.config['UNI_LETTER_FOLDER'], secure_filename(uniLetter.filename))
                    uniLetter.save(uni_letter_path)

                # Prepare data to be stored in the database
                output = {
                    "username": name,
                    "password": hashed_password,
                    "phone": phone,
                    "birthdate": birthday,
                    "industry": industry,
                    "education": education,
                    "experience": experience,
                    "resume_path": resume_path,
                    "cover_letter_path": cover_letter_path,
                    "uni_letter_path": uni_letter_path,
                    "image_path": image_path
                }

                # Update the candidate's data in the database
                dbdata.updateTodoItem(emailne, output)
                return render_template("./candidate/profile.html")
            else:
                # Handle case when candidate data is not found
                return "Candidate data not found", 404


@app.route('/c_editProfile',methods=['POST'])
def c_editProfile():

    user_email = session.get('companyUser')  # Getting candidate email from session

    database = dbdata.getTodoItems()

    for n in database[1]:
        if user_email == database[1][n]["email"]:
            emailne = n

            # Fetch existing candidate data
            candidate_data = database[1][n]
   
            if candidate_data:
                # Update only the fields that are provided in the request
                name = request.form.get("name", candidate_data.get("username"))
                introduction = request.form.get("introduction", candidate_data.get("introduction"))
                password = request.form.get("password", candidate_data.get("password"))
                image = request.files.get('profile-image', None)

    # Hash the password using MD5
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                
                # Save files if provided
                image_path = candidate_data.get("image_path")

                if image:
                    image_path = os.path.join(app.config['PROFILE_IMAGE_FOLDER'], secure_filename(image.filename))
                    image.save(image_path)

                # Prepare data to be stored in the database
                output = {
                    "username": name,
                    "password": hashed_password,
                    "introduction": introduction,
                    "image_path": image_path
                }

                # Update the candidate's data in the database
                dbdata.updateTodoItem2(emailne, output)
                return render_template("./company/profile.html")
            else:
                # Handle case when candidate data is not found
                return "Company data not found", 404


@app.route('/addCandidate', methods=['POST'])
def addCandidate():
    # Extracting data from the form
    image = request.files['image']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    birthdate = request.form['birthdate']
    industry = request.form['industry']
    education = request.form['education']
    experience = request.form['experience']
    resume = request.files['resume']
    coverLetter = request.files['coverLetter']
    uniLetter = request.files['uniLetter']


    # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()


    database = dbdata.getTodoItems()
    check = False


    for n in database[0]:
        if email == database[0][n]["email"]:
            check = False
            break
        else:
            check = True

    if check:
        # Move uploaded files to respective folders
        image_path = os.path.join(app.config['PROFILE_IMAGE_FOLDER'], secure_filename(image.filename))
        resume_path = os.path.join(app.config['RESUME_FOLDER'], secure_filename(resume.filename))
        cover_letter_path = os.path.join(app.config['COVER_LETTER_FOLDER'], secure_filename(coverLetter.filename))
        uni_letter_path = os.path.join(app.config['UNI_LETTER_FOLDER'], secure_filename(uniLetter.filename))

        image.save(image_path)
        resume.save(resume_path)
        coverLetter.save(cover_letter_path)
        uniLetter.save(uni_letter_path)

        # Prepare data to be stored in the database
        candidate_data = {
            "username": username,
            "password": hashed_password,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "industry": industry,
            "education": education,
            "experience": experience,
            "resume_path": resume_path,
            "cover_letter_path": cover_letter_path,
            "uni_letter_path": uni_letter_path,
            "image_path": image_path
        }
        
        # Add candidate data to the database
        dbdata.addTodoItem(candidate_data, "Candidate/")
        return render_template("logincan.html")

    else:
        return render_template("regcan.html", error="This user all ready register")     
        

@app.route('/loginCandidate', methods=['POST'])
def loginCandidate():
    username = request.form["username"]
    password = request.form["password"]

        # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    database = dbdata.getTodoItems()

    for user_data in database[0].values():
        if username == user_data["username"] and hashed_password == user_data["password"]:
            session['candidateUser'] = user_data["email"]
            session['candidateUser_username'] = user_data["username"]
            session['candidateUser_phone'] = user_data["phone"]
            session['candidateUser_resume_path'] = user_data["resume_path"]
            session['candidateUser_uni_letter_path'] = user_data["uni_letter_path"]
            session['candidateUser_cover_letter_path'] = user_data["cover_letter_path"]
            return render_template("./candidate/candidate-index.html")

    # If no matching user is found, return an error message
    return render_template("logincan.html", error="Invalid username or password")


@app.route('/addCompany', methods=['POST'])
def addCompany():
    # Extracting data from the form
    image = request.files["image"]
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    introduction = request.form["introduction"]

       # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    database = dbdata.getTodoItems()
    check = False


    for n in database[1]:
        if email == database[1][n]["email"]:
            check = False
            break
        else:
            check = True

    if check:

        # Move uploaded image to the appropriate folder
        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
            image.save(image_path)
        else:
            # Handle case where no image is uploaded
            # For example, provide a default image path
            image_path = "profile.jpeg"

        # Prepare data to be stored in the database
        company_data = {
            "username": username,
            "password": hashed_password,
            "email": email,
            "introduction": introduction,
            "image_path": image_path
        }

        # Add company data to the database
        dbdata.addTodoItem(company_data, "Company/")

        # Optionally, redirect to a success page or render a template
        return render_template("logincom.html")

    else:
        return render_template("regcom.html", error="This user all ready register")     
        

@app.route('/loginCompany', methods=['POST'])
def loginCompany():
    username = request.form["username"]
    password = request.form["password"]

        # Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    database = dbdata.getTodoItems()

    for company_data in database[1].values():
        if username == company_data["username"] and hashed_password == company_data["password"]:
            session['companyUser'] = company_data["email"]
            session['companyUser_user'] = company_data["username"]
            return render_template("./company/company-index.html")

    # If no matching company is found, return an error message
    return render_template("logincom.html", error="Invalid username or password")


@app.route('/logout')
def logout():
    session.pop('candidateUser', None)
    return render_template("home.html")


@app.route('/c_logout')
def c_logout():
    session.pop('companyUser', None)
    return render_template("home.html")


#new*******

@app.route('/loadCompany', methods=['POST'])
def loadCompany():
    newdata = dbdata.getTodoItems()
    print(newdata[1])
    # jsonify the data
    jdata = jsonify({"jobs": newdata[1]})
    # set CORS headers
    jdata.headers.add('Access-Control-Allow-Origin', '*')
    return jdata

@app.route('/loadCandidate', methods=['POST'])
def loadCandidate():
    newdata = dbdata.getTodoItems()
    loguser = session.get('companyUser')
    print(newdata[4])
    # jsonify the data
    jdata = jsonify({"jobs": newdata[4],"logusert":loguser})
    # set CORS headers
    jdata.headers.add('Access-Control-Allow-Origin', '*')
    return jdata

@app.route('/chatcom', methods=['POST'])
def chatcom():
    name = request.form["name"]
    email = request.form["email"]
    profile = request.form["profile"]
    sender = session.get('candidateUser') 
    return render_template("./candidate/chat.html", name_tx=name, email_tx=email, profile_tx=profile, sender_tx=sender)

@app.route('/chatcan', methods=['POST'])
def chatcan():
    name = request.form["name"]
    email = request.form["email"]
    profile = request.form["profile"]
    sender = session.get('companyUser') 
    return render_template("./company/chat.html", name_tx=name, email_tx=email, profile_tx=profile, sender_tx=sender)

@app.route('/get_profile', methods=['POST'])
def get_profile():
    candidate_email = request.form["proval"] # Getting candidate email from session
    database = dbdata.getTodoItems()

    for candidate_data in database[1].values():
        if candidate_email == candidate_data["email"]:
            jdata = jsonify({"jobs": candidate_data})
            jdata.headers.add('Access-Control-Allow-Origin', '*')
            return jdata

    # If no matching candidate is found, you might want to handle this case accordingly
    return jsonify({"error": "Candidate profile not found"})

@app.route('/get_profile_can', methods=['POST'])
def get_profile_can():
    candidate_email = request.form["proval"] # Getting candidate email from session
    database = dbdata.getTodoItems()

    for candidate_data in database[0].values():
        if candidate_email == candidate_data["email"]:
            jdata = jsonify({"jobs": candidate_data})
            jdata.headers.add('Access-Control-Allow-Origin', '*')
            return jdata

    # If no matching candidate is found, you might want to handle this case accordingly
    return jsonify({"error": "Candidate profile not found"})

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        message = request.form['message']
        sender = request.form['sender']
        receiver = request.form['receiver']
        # profile_img = ""
        # profile_name = ""

        candidate_email = request.form['sender'] # Getting candidate email from session
        database = dbdata.getTodoItems()

        for candidate_data in database[0].values():
            if candidate_email == candidate_data["email"]:
                
               profile_img = candidate_data["image_path"]
               profile_name = candidate_data["username"]

        # Validate input (you can add more validations as needed)
        if not message.strip() or not sender.strip() or not receiver.strip():
            raise ValueError("Missing required fields")

        # Add the message to the chat_messages collection
        dbdata.addTodoItem({"sender": sender, "message": message, "receiver": receiver, "profile_img": profile_img, "profile_name": profile_name}, "z_messages/")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/send_message2', methods=['POST'])
def send_message2():
    try:
        message = request.form['message']
        sender = request.form['sender']
        receiver = request.form['receiver']
        # profile_img = ""
        # profile_name = ""

        candidate_email = request.form['sender'] # Getting candidate email from session
        database = dbdata.getTodoItems()

        for candidate_data in database[1].values():
            if candidate_email == candidate_data["email"]:
                
               profile_img = candidate_data["image_path"]
               profile_name = candidate_data["username"]

        # Validate input (you can add more validations as needed)
        if not message.strip() or not sender.strip() or not receiver.strip():
            raise ValueError("Missing required fields")

        # Add the message to the chat_messages collection
        dbdata.addTodoItem({"sender": sender, "message": message, "receiver": receiver, "profile_img": profile_img, "profile_name": profile_name}, "z_messages/")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    # Retrieve all messages from the chat_messages collection
    messages = dbdata.getTodoItems()
    print(messages[4])
    return jsonify(messages[4])

@app.route('/goVacancy', methods=['POST'])
def goVacancy():
    jobname = request.form["jobname"]
    # jobname = "HR"
    return render_template("./candidate/vacancyfilter.html", jobname=jobname)

if __name__ == '__main__':
    dbdata = ToDoCollection("", "/")
    app.run(debug=True)
