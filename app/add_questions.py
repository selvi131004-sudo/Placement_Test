from app.models import Question

questions = [

# ---------------- APTITUDE ----------------

{
    "section":"Aptitude",
    "question":"2 + 2 = ?",
    "option1":"2",
    "option2":"3",
    "option3":"4",
    "option4":"5",
    "answer":"4"
},

{
    "section":"Aptitude",
    "question":"10 + 5 = ?",
    "option1":"12",
    "option2":"15",
    "option3":"20",
    "option4":"25",
    "answer":"15"
},

{
    "section":"Aptitude",
    "question":"15 - 5 = ?",
    "option1":"5",
    "option2":"10",
    "option3":"15",
    "option4":"20",
    "answer":"10"
},

{
    "section":"Aptitude",
    "question":"5 x 5 = ?",
    "option1":"10",
    "option2":"15",
    "option3":"25",
    "option4":"30",
    "answer":"25"
},

{
    "section":"Aptitude",
    "question":"20 / 4 = ?",
    "option1":"2",
    "option2":"4",
    "option3":"5",
    "option4":"6",
    "answer":"5"
},

{
    "section":"Aptitude",
    "question":"Square root of 64?",
    "option1":"6",
    "option2":"7",
    "option3":"8",
    "option4":"9",
    "answer":"8"
},

{
    "section":"Aptitude",
    "question":"50% of 200?",
    "option1":"50",
    "option2":"100",
    "option3":"150",
    "option4":"200",
    "answer":"100"
},

{
    "section":"Aptitude",
    "question":"25 + 25 = ?",
    "option1":"25",
    "option2":"40",
    "option3":"50",
    "option4":"60",
    "answer":"50"
},

{
    "section":"Aptitude",
    "question":"100 - 20 = ?",
    "option1":"70",
    "option2":"80",
    "option3":"90",
    "option4":"100",
    "answer":"80"
},

{
    "section":"Aptitude",
    "question":"12 x 2 = ?",
    "option1":"22",
    "option2":"24",
    "option3":"26",
    "option4":"28",
    "answer":"24"
},

# ---------------- TECHNICAL ----------------

{
    "section":"Technical",
    "question":"Python is a ?",
    "option1":"Programming Language",
    "option2":"Database",
    "option3":"Browser",
    "option4":"Operating System",
    "answer":"Programming Language"
},

{
    "section":"Technical",
    "question":"HTML stands for?",
    "option1":"Hyper Text Markup Language",
    "option2":"High Text Machine Language",
    "option3":"Home Tool Markup Language",
    "option4":"None",
    "answer":"Hyper Text Markup Language"
},

{
    "section":"Technical",
    "question":"CSS is used for?",
    "option1":"Styling",
    "option2":"Database",
    "option3":"Server",
    "option4":"Hardware",
    "answer":"Styling"
},

{
    "section":"Technical",
    "question":"JavaScript is used for?",
    "option1":"Frontend",
    "option2":"Cooking",
    "option3":"Painting",
    "option4":"Typing",
    "answer":"Frontend"
},

{
    "section":"Technical",
    "question":"SQL is used for?",
    "option1":"Database",
    "option2":"Gaming",
    "option3":"Editing",
    "option4":"Drawing",
    "answer":"Database"
},

{
    "section":"Technical",
    "question":"Which is backend framework?",
    "option1":"Django",
    "option2":"HTML",
    "option3":"CSS",
    "option4":"Bootstrap",
    "answer":"Django"
},

{
    "section":"Technical",
    "question":"Which symbol used for comments in Python?",
    "option1":"//",
    "option2":"#",
    "option3":"<!-- -->",
    "option4":"**",
    "answer":"#"
},

{
    "section":"Technical",
    "question":"Which company created Python?",
    "option1":"Google",
    "option2":"Microsoft",
    "option3":"Guido van Rossum",
    "option4":"Apple",
    "answer":"Guido van Rossum"
},

{
    "section":"Technical",
    "question":"Which tag used for paragraph in HTML?",
    "option1":"<h1>",
    "option2":"<div>",
    "option3":"<p>",
    "option4":"<span>",
    "answer":"<p>"
},

{
    "section":"Technical",
    "question":"Which database used in Django by default?",
    "option1":"MySQL",
    "option2":"SQLite",
    "option3":"Oracle",
    "option4":"MongoDB",
    "answer":"SQLite"
},

# ---------------- GRAMMAR ----------------

{
    "section":"Grammar",
    "question":"Choose correct sentence",
    "option1":"He go to school",
    "option2":"He goes to school",
    "option3":"He going school",
    "option4":"He gone school",
    "answer":"He goes to school"
},

{
    "section":"Grammar",
    "question":"Past tense of go?",
    "option1":"Gone",
    "option2":"Went",
    "option3":"Going",
    "option4":"Goes",
    "answer":"Went"
},

{
    "section":"Grammar",
    "question":"Choose noun",
    "option1":"Run",
    "option2":"Beautiful",
    "option3":"Book",
    "option4":"Quickly",
    "answer":"Book"
},

{
    "section":"Grammar",
    "question":"Choose verb",
    "option1":"Dance",
    "option2":"Blue",
    "option3":"Chair",
    "option4":"Soft",
    "answer":"Dance"
},

{
    "section":"Grammar",
    "question":"Synonym of Happy?",
    "option1":"Sad",
    "option2":"Joyful",
    "option3":"Angry",
    "option4":"Cry",
    "answer":"Joyful"
},

{
    "section":"Grammar",
    "question":"Antonym of Big?",
    "option1":"Large",
    "option2":"Huge",
    "option3":"Small",
    "option4":"Tall",
    "answer":"Small"
},

{
    "section":"Grammar",
    "question":"Choose adjective",
    "option1":"Quickly",
    "option2":"Beautiful",
    "option3":"Run",
    "option4":"Jump",
    "answer":"Beautiful"
},

{
    "section":"Grammar",
    "question":"Plural of child?",
    "option1":"Childs",
    "option2":"Children",
    "option3":"Childes",
    "option4":"Child",
    "answer":"Children"
},

{
    "section":"Grammar",
    "question":"Choose correct article",
    "option1":"a apple",
    "option2":"an apple",
    "option3":"the apple",
    "option4":"apple",
    "answer":"an apple"
},

{
    "section":"Grammar",
    "question":"Opposite of fast?",
    "option1":"Quick",
    "option2":"Rapid",
    "option3":"Slow",
    "option4":"Speed",
    "answer":"Slow"
}

]

for q in questions:

    Question.objects.create(
        section=q['section'],
        question=q['question'],
        option1=q['option1'],
        option2=q['option2'],
        option3=q['option3'],
        option4=q['option4'],
        answer=q['answer']
    )

print("Questions Added Successfully")