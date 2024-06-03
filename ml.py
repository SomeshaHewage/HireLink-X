import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from joblib import dump, load
import pandas as pd
import fitz
import numpy as np
import random
import language_tool_python
import re
from sklearn.preprocessing import LabelEncoder

# Initialize LanguageTool for grammar and spelling checking
tool = language_tool_python.LanguageTool('en-UK')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Apply the softmax function to convert scores into probabilities
def softmax(x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum(axis=1, keepdims=True)

def read_pdf_mupdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf_document:
        total_pages = pdf_document.page_count
        for page_num in range(total_pages):
            page = pdf_document[page_num]
            text += page.get_text()

    return text

def find_job(resume_text):

    df = pd.read_csv('UpdatedResumeDataSet.csv')
    le = LabelEncoder()
    df['Category'] = le.fit_transform(df['Category'])

    userInput = {

    'Resume':resume_text

    }
    df = pd.DataFrame([userInput])

    df['Resume'] = df['Resume'].apply(lambda x:x.lower())
    for i in range(len(df)):
        lw=[]
        for j in df['Resume'][i].split():
            if len(j)>=3:
                lw.append(j)
        df['Resume'][i]=" ".join(lw)
    ps = list(";?.:!,")
    df['Resume'] = df['Resume']

    for p in ps:
        df['Resume'] = df['Resume'].str.replace(p, '')
    
    df['Resume'] = df['Resume'].str.replace("    ", " ")
    df['Resume'] = df['Resume'].str.replace('"', '')
    df['Resume'] = df['Resume'].apply(lambda x: x.replace('\t', ' '))
    df['Resume'] = df['Resume'].str.replace("'s", "")
    df['Resume'] = df['Resume'].apply(lambda x: x.replace('\n', ' '))

    wl = WordNetLemmatizer()
    nr = len(df)
    lis = []
    for r in range(0, nr):
        ll = []
        t = df.loc[r]['Resume']
        tw = str(t).split(" ")
        for w in tw:
            ll.append(wl.lemmatize(w, pos="v"))
        lt = " ".join(ll)
        lis.append(lt)
    df['Resume'] = lis
    sw = list(stopwords.words('english'))
    for s in sw:
        rs = r"\b" + s + r"\b"
        df['Resume'] = df['Resume'].str.replace(rs, '')
    
    cv = load(open("cv2.pickel", 'rb'))
    testdata = cv.transform(df['Resume']).toarray()

    model = load(open("DT2.pickel", 'rb'))

    predictions = model.predict(testdata)
    jobname = le.inverse_transform(predictions)

    print(jobname)
    # # Print the result
    # print("Maximum Percentage:", prediction_percentages)
    return jobname[0]

def check_spelling_and_grammar(text):
    # Check for spelling and grammar errors
    matches = tool.check(text)
    errors = [(match.ruleId, match.message, match.replacements, match.context) for match in matches]
    return errors

def check_content_accuracy(resume_text):
    # Define regular expressions for common information patterns
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    # Search for email and phone number patterns
    emails = re.findall(email_pattern, resume_text)
    phones = re.findall(phone_pattern, resume_text)

    # Check if email and phone number are present
    errors = []
    if not emails:
        errors.append("Email address is missing.")
    if not phones:
        errors.append("Phone number is missing.")

    return errors

def check_incomplete_information(resume_text):
    # Define sections to check for completeness
    sections_to_check = ["contact information", "career objective", "education", "work experience", "skills"]

    # Check if any of the sections are missing
    errors = []
    for section in sections_to_check:
        if section.lower() not in resume_text.lower():
            errors.append(f"Missing section: {section}")

    return errors

def check_repetitive_language(resume_text):
    # Analyze text for repetitive language
    words = resume_text.split()
    word_counts = {}
    repetitive_words = []

    # Count occurrences of each word
    for word in words:
        word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

    # Identify words that are repeated more than once
    for word, count in word_counts.items():
        if count > 1:
            repetitive_words.append(word)

    return repetitive_words

def check_inconsistent_language(resume_text):
    # Check for inconsistencies in language or terminology used
    # This can be a manual review or specific checks based on domain knowledge
   
    return []

def check_overcrowded_layout(resume_text):
    # Placeholder for demonstration
    # In a real implementation, you could analyze the layout for readability
    return []

def check_irrelevant_information(resume_text):
    # Placeholder for demonstration
    # In a real implementation, you could define criteria for relevance and check against them
    return []

def calculate_error_score(errors):
    # Define weights for different types of errors
    weights = {
        "spelling_and_grammar": 1,  # Adjust weights based on severity or importance
        "content_accuracy": 2,
        "incomplete_information": 3,
        "repetitive_language": 1,
        # Add weights for other error types as needed
    }

    # Calculate error score
    error_score = 0
    for error_type, _ in errors:
        error_score += weights.get(error_type, 0)

    return error_score

def find_error(resume_text):
    # Example usage
    errors = []
    error_score = 0
    all_error_type = ""

    # Check spelling and grammar
    errors.extend(("spelling_and_grammar", error) for error in check_spelling_and_grammar(resume_text))

    # Check content accuracy
    errors.extend(("content_accuracy", error) for error in check_content_accuracy(resume_text))

    # Check incomplete information
    errors.extend(("incomplete_information", error) for error in check_incomplete_information(resume_text))

    # Check repetitive language
    repetitive_words = check_repetitive_language(resume_text)
    if repetitive_words:
        errors.append(("repetitive_language", "Repetitive words or phrases: " + ', '.join(repetitive_words)))

    # Check inconsistent language
    errors.extend(("inconsistent_language", error) for error in check_inconsistent_language(resume_text))

    # Check overcrowded layout
    errors.extend(("overcrowded_layout", error) for error in check_overcrowded_layout(resume_text))

    # Check irrelevant information
    errors.extend(("irrelevant_information", error) for error in check_irrelevant_information(resume_text))

    if errors:
        print("Errors found in the resume:")
        for error_type, error_message in errors:
            print(f"{error_type.capitalize()}: {error_message}")
            all_error_type += f"{error_type.capitalize()}: {error_message}\n\n"
        
        # Calculate error score
        error_score = 100-calculate_error_score(errors)
        print(f"\nError Score: {error_score}")
    else:
        print("No errors found in the resume.")
    
    return error_score,all_error_type

def main(resume_path):
    resume_text = read_pdf_mupdf(resume_path)
    jobname = find_job(resume_text)
    error_score,all_error_type = find_error(resume_text)
    return jobname,error_score,all_error_type


#main("static/uploads/Copy_of_Black_White_Minimalist_CV_Resume.pdf")