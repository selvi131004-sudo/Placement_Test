# grammar_questions.py

from app.models import Question

questions = [

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Brave'.",
    "option1":"Coward",
    "option2":"Bold",
    "option3":"Weak",
    "option4":"Lazy",
    "answer":"Bold"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Expand'.",
    "option1":"Increase",
    "option2":"Develop",
    "option3":"Reduce",
    "option4":"Extend",
    "answer":"Reduce"
},

{
    "section":"Grammar",
    "question":"Find the error: 'She do not like coffee.'",
    "option1":"She",
    "option2":"do",
    "option3":"like",
    "option4":"coffee",
    "answer":"do"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"He go to office daily.",
    "option2":"He goes to office daily.",
    "option3":"He going to office daily.",
    "option4":"He gone to office daily.",
    "answer":"He goes to office daily."
},

{
    "section":"Grammar",
    "question":"Choose the correct spelling.",
    "option1":"Enviroment",
    "option2":"Environment",
    "option3":"Envirnoment",
    "option4":"Enviornment",
    "answer":"Environment"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: She _____ singing now.",
    "option1":"is",
    "option2":"are",
    "option3":"was",
    "option4":"be",
    "answer":"is"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Ancient'.",
    "option1":"Old",
    "option2":"Historic",
    "option3":"Modern",
    "option4":"Traditional",
    "answer":"Modern"
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Quick'.",
    "option1":"Slow",
    "option2":"Rapid",
    "option3":"Lazy",
    "option4":"Weak",
    "answer":"Rapid"
},

{
    "section":"Grammar",
    "question":"Find the error: 'They was playing football.'",
    "option1":"They",
    "option2":"was",
    "option3":"playing",
    "option4":"football",
    "answer":"was"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: I have been waiting _____ two hours.",
    "option1":"since",
    "option2":"for",
    "option3":"from",
    "option4":"by",
    "answer":"for"
},

{
    "section":"Grammar",
    "question":"Choose the correct article: _____ apple a day keeps the doctor away.",
    "option1":"A",
    "option2":"An",
    "option3":"The",
    "option4":"No article",
    "answer":"An"
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Huge'.",
    "option1":"Tiny",
    "option2":"Small",
    "option3":"Massive",
    "option4":"Short",
    "answer":"Massive"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Victory'.",
    "option1":"Win",
    "option2":"Success",
    "option3":"Defeat",
    "option4":"Achievement",
    "answer":"Defeat"
},

{
    "section":"Grammar",
    "question":"Find the error: 'He have completed the task.'",
    "option1":"He",
    "option2":"have",
    "option3":"completed",
    "option4":"task",
    "answer":"have"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: If I _____ rich, I would help poor people.",
    "option1":"am",
    "option2":"was",
    "option3":"were",
    "option4":"be",
    "answer":"were"
},

{
    "section":"Grammar",
    "question":"What is the meaning of idiom 'Once in a blue moon'?",
    "option1":"Regularly",
    "option2":"Very rarely",
    "option3":"Daily",
    "option4":"Immediately",
    "answer":"Very rarely"
},

{
    "section":"Grammar",
    "question":"Choose the correct passive voice: 'They completed the work.'",
    "option1":"The work completed by them.",
    "option2":"The work was completed by them.",
    "option3":"The work is completed by them.",
    "option4":"The work has completed.",
    "answer":"The work was completed by them."
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Honest'.",
    "option1":"Truthful",
    "option2":"Clever",
    "option3":"Lazy",
    "option4":"Proud",
    "answer":"Truthful"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Permanent'.",
    "option1":"Stable",
    "option2":"Fixed",
    "option3":"Temporary",
    "option4":"Strong",
    "answer":"Temporary"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: She is good _____ mathematics.",
    "option1":"in",
    "option2":"at",
    "option3":"on",
    "option4":"for",
    "answer":"at"
},

# ---------------- PARAGRAPH QUESTIONS ----------------

{
    "section":"Grammar",
    "question":"Passage: Ravi wakes up early every morning and goes for a walk. He believes exercise keeps him healthy. Question: Why does Ravi go for a walk?",
    "option1":"To meet friends",
    "option2":"To stay healthy",
    "option3":"To play games",
    "option4":"To study",
    "answer":"To stay healthy"
},

{
    "section":"Grammar",
    "question":"Passage: Priya loves reading books during weekends. She visits the library every Saturday. Question: Where does Priya go every Saturday?",
    "option1":"School",
    "option2":"Market",
    "option3":"Library",
    "option4":"Office",
    "answer":"Library"
},

{
    "section":"Grammar",
    "question":"Passage: Arun worked hard for his exams and scored highest marks in class. Question: Why did Arun score highest marks?",
    "option1":"Luck",
    "option2":"Hard work",
    "option3":"Guessing",
    "option4":"Help from friends",
    "answer":"Hard work"
},

{
    "section":"Grammar",
    "question":"Passage: Technology has changed communication. People now connect instantly through mobile phones and internet. Question: What changed communication?",
    "option1":"Transport",
    "option2":"Technology",
    "option3":"Education",
    "option4":"Agriculture",
    "answer":"Technology"
},

{
    "section":"Grammar",
    "question":"Passage: Trees provide oxygen and reduce pollution. Planting more trees helps environment. Question: Why should we plant trees?",
    "option1":"For pollution",
    "option2":"For oxygen and environment",
    "option3":"For cutting",
    "option4":"For roads",
    "answer":"For oxygen and environment"
},

{
    "section":"Grammar",
    "question":"Choose the meaning of idiom 'Hit the nail on the head'.",
    "option1":"Miss the point",
    "option2":"Say exactly right thing",
    "option3":"Do carpentry work",
    "option4":"Get confused",
    "answer":"Say exactly right thing"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"Neither of the boys are present.",
    "option2":"Neither of the boys is present.",
    "option3":"Neither boys are present.",
    "option4":"Neither boys is present.",
    "answer":"Neither of the boys is present."
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Diligent'.",
    "option1":"Lazy",
    "option2":"Hardworking",
    "option3":"Weak",
    "option4":"Careless",
    "answer":"Hardworking"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Optimistic'.",
    "option1":"Positive",
    "option2":"Hopeful",
    "option3":"Pessimistic",
    "option4":"Cheerful",
    "answer":"Pessimistic"
},

{
    "section":"Grammar",
    "question":"Find the error: 'Each of the players have a jersey.'",
    "option1":"Each",
    "option2":"players",
    "option3":"have",
    "option4":"jersey",
    "answer":"have"
},
{
    "section":"Grammar",
    "question":"Choose the synonym of 'Abundant'.",
    "option1":"Scarce",
    "option2":"Plentiful",
    "option3":"Rare",
    "option4":"Empty",
    "answer":"Plentiful"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Generous'.",
    "option1":"Kind",
    "option2":"Helpful",
    "option3":"Selfish",
    "option4":"Polite",
    "answer":"Selfish"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: He insisted _____ paying the bill.",
    "option1":"on",
    "option2":"in",
    "option3":"at",
    "option4":"for",
    "answer":"on"
},

{
    "section":"Grammar",
    "question":"Find the error: 'She did not went to school yesterday.'",
    "option1":"She",
    "option2":"did",
    "option3":"went",
    "option4":"school",
    "answer":"went"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"Everyone have completed the work.",
    "option2":"Everyone has completed the work.",
    "option3":"Everyone completed the work.",
    "option4":"Everyone having completed the work.",
    "answer":"Everyone has completed the work."
},

{
    "section":"Grammar",
    "question":"Choose the meaning of idiom 'Break the ice'.",
    "option1":"To start conversation",
    "option2":"To break something",
    "option3":"To stop talking",
    "option4":"To get angry",
    "answer":"To start conversation"
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Fragile'.",
    "option1":"Strong",
    "option2":"Weak",
    "option3":"Delicate",
    "option4":"Heavy",
    "answer":"Delicate"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Compulsory'.",
    "option1":"Necessary",
    "option2":"Optional",
    "option3":"Important",
    "option4":"Mandatory",
    "answer":"Optional"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: The teacher divided the sweets _____ the children.",
    "option1":"between",
    "option2":"among",
    "option3":"with",
    "option4":"into",
    "answer":"among"
},

{
    "section":"Grammar",
    "question":"Choose the correct spelling.",
    "option1":"Recieve",
    "option2":"Receive",
    "option3":"Receeve",
    "option4":"Receve",
    "answer":"Receive"
},

{
    "section":"Grammar",
    "question":"Find the error: 'Neither Ram nor his friends was present.'",
    "option1":"Neither",
    "option2":"friends",
    "option3":"was",
    "option4":"present",
    "answer":"was"
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Cautious'.",
    "option1":"Careful",
    "option2":"Careless",
    "option3":"Bold",
    "option4":"Fearless",
    "answer":"Careful"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Artificial'.",
    "option1":"Natural",
    "option2":"False",
    "option3":"Fake",
    "option4":"Plastic",
    "answer":"Natural"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: She prefers tea _____ coffee.",
    "option1":"than",
    "option2":"to",
    "option3":"over",
    "option4":"with",
    "answer":"to"
},

{
    "section":"Grammar",
    "question":"Choose the correct passive voice: 'The chef cooked the meal.'",
    "option1":"The meal cooked by chef.",
    "option2":"The meal was cooked by the chef.",
    "option3":"The meal is cooked by chef.",
    "option4":"The chef was cooked the meal.",
    "answer":"The meal was cooked by the chef."
},

{
    "section":"Grammar",
    "question":"Passage: Internet has become an essential part of modern life. People use it for communication, education, shopping and entertainment. Question: What are people using internet for?",
    "option1":"Only shopping",
    "option2":"Only education",
    "option3":"Many activities",
    "option4":"Only games",
    "answer":"Many activities"
},

{
    "section":"Grammar",
    "question":"Passage: Water conservation is important because fresh water resources are limited. Saving water today helps future generations. Question: Why should we conserve water?",
    "option1":"Water is expensive",
    "option2":"Fresh water is limited",
    "option3":"To avoid studies",
    "option4":"For entertainment",
    "answer":"Fresh water is limited"
},

{
    "section":"Grammar",
    "question":"Choose the meaning of idiom 'Under the weather'.",
    "option1":"Feeling sick",
    "option2":"Feeling excited",
    "option3":"Working outside",
    "option4":"Feeling hungry",
    "answer":"Feeling sick"
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Ancient'.",
    "option1":"Modern",
    "option2":"Old",
    "option3":"Future",
    "option4":"Current",
    "answer":"Old"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Expand'.",
    "option1":"Increase",
    "option2":"Spread",
    "option3":"Contract",
    "option4":"Develop",
    "answer":"Contract"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: I am looking forward _____ meeting you.",
    "option1":"for",
    "option2":"to",
    "option3":"with",
    "option4":"on",
    "answer":"to"
},

{
    "section":"Grammar",
    "question":"Find the error: 'The sceneries here are beautiful.'",
    "option1":"The",
    "option2":"sceneries",
    "option3":"are",
    "option4":"beautiful",
    "answer":"sceneries"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"She enjoys to dance.",
    "option2":"She enjoys dancing.",
    "option3":"She enjoy dancing.",
    "option4":"She enjoying dance.",
    "answer":"She enjoys dancing."
},

{
    "section":"Grammar",
    "question":"Choose the synonym of 'Swift'.",
    "option1":"Slow",
    "option2":"Fast",
    "option3":"Weak",
    "option4":"Heavy",
    "answer":"Fast"
},

{
    "section":"Grammar",
    "question":"Choose the antonym of 'Bold'.",
    "option1":"Brave",
    "option2":"Fearless",
    "option3":"Timid",
    "option4":"Strong",
    "answer":"Timid"
},

{
    "section":"Grammar",
    "question":"Choose the meaning of idiom 'Piece of cake'.",
    "option1":"Difficult task",
    "option2":"Easy task",
    "option3":"Delicious food",
    "option4":"Birthday party",
    "answer":"Easy task"
},

{
    "section":"Grammar",
    "question":"Passage: Healthy food gives energy and keeps the body fit. Junk food may cause health problems if eaten regularly. Question: What may happen if junk food is eaten regularly?",
    "option1":"More fitness",
    "option2":"Health problems",
    "option3":"Better sleep",
    "option4":"More energy",
    "answer":"Health problems"
},

{
    "section":"Grammar",
    "question":"Fill in the blank: He is interested _____ learning AI.",
    "option1":"on",
    "option2":"at",
    "option3":"in",
    "option4":"for",
    "answer":"in"
},

{
    "section":"Grammar",
    "question":"Choose the correct spelling.",
    "option1":"Occasion",
    "option2":"Ocassion",
    "option3":"Occassion",
    "option4":"Occesion",
    "answer":"Occasion"
},

{
    "section":"Grammar",
    "question":"Find the error: 'One of the boys are absent.'",
    "option1":"One",
    "option2":"boys",
    "option3":"are",
    "option4":"absent",
    "answer":"are"
},
{
    "section":"Grammar",
    "question":"Choose the correct sentence (Subject-Verb Agreement).",
    "option1":"Each of the students are responsible.",
    "option2":"Each of the students is responsible.",
    "option3":"Each of the students were responsible.",
    "option4":"Each of the students have responsible.",
    "answer":"Each of the students is responsible."
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Tense Usage).",
    "option1":"She has went to school.",
    "option2":"She had went to school.",
    "option3":"She has gone to school.",
    "option4":"She have gone to school.",
    "answer":"She has gone to school."
},

{
    "section":"Grammar",
    "question":"Find the error in the sentence: 'Neither the manager nor the employees was present.'",
    "option1":"Neither",
    "option2":"manager",
    "option3":"was",
    "option4":"present",
    "answer":"was"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Verb Agreement).",
    "option1":"The list of items are missing.",
    "option2":"The list of items is missing.",
    "option3":"The list of items were missing.",
    "option4":"The list of items have missing.",
    "answer":"The list of items is missing."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense usage.",
    "option1":"I am living here since 2020.",
    "option2":"I have lived here since 2020.",
    "option3":"I live here since 2020.",
    "option4":"I lived here since 2020 now.",
    "answer":"I have lived here since 2020."
},

{
    "section":"Grammar",
    "question":"Find the error: 'He don't know the answer.'",
    "option1":"He",
    "option2":"don't",
    "option3":"know",
    "option4":"answer",
    "answer":"don't"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"The data is correct.",
    "option2":"The data are correct.",
    "option3":"The data were corrects.",
    "option4":"The data have correct.",
    "answer":"The data is correct."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense.",
    "option1":"She will goes to college tomorrow.",
    "option2":"She will go to college tomorrow.",
    "option3":"She will went to college tomorrow.",
    "option4":"She going to college tomorrow.",
    "answer":"She will go to college tomorrow."
},

{
    "section":"Grammar",
    "question":"Find the error: 'Everyone have submitted their assignment.'",
    "option1":"Everyone",
    "option2":"have",
    "option3":"submitted",
    "option4":"assignment",
    "answer":"have"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Subject-Verb Agreement).",
    "option1":"The team are winning the match.",
    "option2":"The team is winning the match.",
    "option3":"The team were winning the match.",
    "option4":"The team have winning the match.",
    "answer":"The team is winning the match."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense usage.",
    "option1":"I am knowing him for years.",
    "option2":"I have known him for years.",
    "option3":"I know him for years now.",
    "option4":"I knew him for years now.",
    "answer":"I have known him for years."
},

{
    "section":"Grammar",
    "question":"Find the error: 'She is used to wake up early.'",
    "option1":"She",
    "option2":"is used to",
    "option3":"wake",
    "option4":"early",
    "answer":"wake"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"There is many students in the class.",
    "option2":"There are many students in the class.",
    "option3":"There is many student in the class.",
    "option4":"There are much students in the class.",
    "answer":"There are many students in the class."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense.",
    "option1":"He had finished the work before I came.",
    "option2":"He has finished the work before I came.",
    "option3":"He finishes the work before I came.",
    "option4":"He finish the work before I came.",
    "answer":"He had finished the work before I came."
},

{
    "section":"Grammar",
    "question":"Find the error: 'Neither of the answers are correct.'",
    "option1":"Neither",
    "option2":"answers",
    "option3":"are",
    "option4":"correct",
    "answer":"are"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Verb Agreement).",
    "option1":"The number of students are increasing.",
    "option2":"The number of students is increasing.",
    "option3":"The number of student is increasing.",
    "option4":"The number of students were increasing.",
    "answer":"The number of students is increasing."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense usage.",
    "option1":"By next year, I will complete my course.",
    "option2":"By next year, I will have completed my course.",
    "option3":"By next year, I completed my course.",
    "option4":"By next year, I have complete my course.",
    "answer":"By next year, I will have completed my course."
},

{
    "section":"Grammar",
    "question":"Find the error: 'She do her work carefully every day.'",
    "option1":"She",
    "option2":"do",
    "option3":"work",
    "option4":"carefully",
    "answer":"do"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"The news are interesting.",
    "option2":"The news is interesting.",
    "option3":"The news were interesting.",
    "option4":"The news have interesting.",
    "answer":"The news is interesting."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense.",
    "option1":"I will be working at 5 PM tomorrow.",
    "option2":"I will working at 5 PM tomorrow.",
    "option3":"I will worked at 5 PM tomorrow.",
    "option4":"I working at 5 PM tomorrow.",
    "answer":"I will be working at 5 PM tomorrow."
},

{
    "section":"Grammar",
    "question":"Find the error: 'The committee have decided the matter.'",
    "option1":"The",
    "option2":"committee",
    "option3":"have",
    "option4":"matter",
    "answer":"have"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Subject-Verb Agreement).",
    "option1":"Either of the options are fine.",
    "option2":"Either of the options is fine.",
    "option3":"Either of the option is fine.",
    "option4":"Either options is fine.",
    "answer":"Either of the options is fine."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense usage.",
    "option1":"I had been working here since 2018.",
    "option2":"I have been working here since 2018.",
    "option3":"I am working here since 2018.",
    "option4":"I worked here since 2018 now.",
    "answer":"I have been working here since 2018."
},

{
    "section":"Grammar",
    "question":"Find the error: 'He have been working here for five years.'",
    "option1":"He",
    "option2":"have",
    "option3":"working",
    "option4":"years",
    "answer":"have"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence.",
    "option1":"The furniture are new.",
    "option2":"The furniture is new.",
    "option3":"The furniture were new.",
    "option4":"The furniture have new.",
    "answer":"The furniture is new."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense.",
    "option1":"When I reached, they left.",
    "option2":"When I reached, they had left.",
    "option3":"When I reach, they left.",
    "option4":"When I reached, they have left.",
    "answer":"When I reached, they had left."
},

{
    "section":"Grammar",
    "question":"Find the error: 'The police is investigating the case.'",
    "option1":"The",
    "option2":"police",
    "option3":"is",
    "option4":"case",
    "answer":"is"
},

{
    "section":"Grammar",
    "question":"Choose the correct sentence (Verb Agreement).",
    "option1":"Ten kilometers are a long distance.",
    "option2":"Ten kilometers is a long distance.",
    "option3":"Ten kilometer is a long distance.",
    "option4":"Ten kilometers were long distance.",
    "answer":"Ten kilometers is a long distance."
},

{
    "section":"Grammar",
    "question":"Choose the correct tense usage.",
    "option1":"She has been teaching since 10 years.",
    "option2":"She has been teaching for 10 years.",
    "option3":"She is teaching since 10 years.",
    "option4":"She was teaching since 10 years.",
    "answer":"She has been teaching for 10 years."
},

{
    "section":"Grammar",
    "question":"Find the error: 'Each of the boys have brought their books.'",
    "option1":"Each",
    "option2":"boys",
    "option3":"have",
    "option4":"books",
    "answer":"have"
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

print("Grammar Questions Added Successfully")