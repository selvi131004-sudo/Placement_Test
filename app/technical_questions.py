# technical_questions.py

from app.models import Question

questions = [

{
    "section":"Technical",
    "question":"Which data structure follows FIFO principle?",
    "option1":"Stack",
    "option2":"Queue",
    "option3":"Tree",
    "option4":"Graph",
    "answer":"Queue"
},

{
    "section":"Technical",
    "question":"Which keyword is used to define a function in Python?",
    "option1":"function",
    "option2":"define",
    "option3":"def",
    "option4":"fun",
    "answer":"def"
},

{
    "section":"Technical",
    "question":"Which SQL command is used to retrieve data?",
    "option1":"GET",
    "option2":"SELECT",
    "option3":"SHOW",
    "option4":"FETCH",
    "answer":"SELECT"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used to insert an image?",
    "option1":"<image>",
    "option2":"<img>",
    "option3":"<pic>",
    "option4":"<src>",
    "answer":"<img>"
},

{
    "section":"Technical",
    "question":"Which protocol is used for secure communication over internet?",
    "option1":"HTTP",
    "option2":"FTP",
    "option3":"HTTPS",
    "option4":"SMTP",
    "answer":"HTTPS"
},

{
    "section":"Technical",
    "question":"Which data structure follows LIFO principle?",
    "option1":"Queue",
    "option2":"Array",
    "option3":"Stack",
    "option4":"Linked List",
    "answer":"Stack"
},

{
    "section":"Technical",
    "question":"What does CPU stand for?",
    "option1":"Central Process Unit",
    "option2":"Central Processing Unit",
    "option3":"Computer Processing Unit",
    "option4":"Control Processing Unit",
    "answer":"Central Processing Unit"
},

{
    "section":"Technical",
    "question":"Which language is mainly used for web page structure?",
    "option1":"CSS",
    "option2":"HTML",
    "option3":"Python",
    "option4":"Java",
    "answer":"HTML"
},

{
    "section":"Technical",
    "question":"Which company developed Java?",
    "option1":"Google",
    "option2":"Microsoft",
    "option3":"Sun Microsystems",
    "option4":"Apple",
    "answer":"Sun Microsystems"
},

{
    "section":"Technical",
    "question":"Which database is used by Django by default?",
    "option1":"MySQL",
    "option2":"Oracle",
    "option3":"SQLite",
    "option4":"MongoDB",
    "answer":"SQLite"
},

{
    "section":"Technical",
    "question":"Which symbol is used for comments in Python?",
    "option1":"//",
    "option2":"#",
    "option3":"<!-- -->",
    "option4":"**",
    "answer":"#"
},

{
    "section":"Technical",
    "question":"What is the extension of Python file?",
    "option1":".java",
    "option2":".html",
    "option3":".py",
    "option4":".css",
    "answer":".py"
},

{
    "section":"Technical",
    "question":"Which tag is used for paragraph in HTML?",
    "option1":"<h1>",
    "option2":"<div>",
    "option3":"<p>",
    "option4":"<span>",
    "answer":"<p>"
},

{
    "section":"Technical",
    "question":"Which operator is used for exponent in Python?",
    "option1":"^",
    "option2":"**",
    "option3":"//",
    "option4":"%",
    "answer":"**"
},

{
    "section":"Technical",
    "question":"Which data type is immutable in Python?",
    "option1":"List",
    "option2":"Dictionary",
    "option3":"Set",
    "option4":"Tuple",
    "answer":"Tuple"
},

{
    "section":"Technical",
    "question":"Which keyword is used for loop in Python?",
    "option1":"repeat",
    "option2":"loop",
    "option3":"for",
    "option4":"iterate",
    "answer":"for"
},

{
    "section":"Technical",
    "question":"What does RAM stand for?",
    "option1":"Read Access Memory",
    "option2":"Random Access Memory",
    "option3":"Run Access Memory",
    "option4":"Rapid Access Memory",
    "answer":"Random Access Memory"
},

{
    "section":"Technical",
    "question":"Which layer of OSI model handles routing?",
    "option1":"Transport",
    "option2":"Application",
    "option3":"Network",
    "option4":"Session",
    "answer":"Network"
},

{
    "section":"Technical",
    "question":"Which CSS property is used to change text color?",
    "option1":"font-color",
    "option2":"text-color",
    "option3":"color",
    "option4":"background-color",
    "answer":"color"
},

{
    "section":"Technical",
    "question":"Which method is used to add element in Python list?",
    "option1":"push()",
    "option2":"insert()",
    "option3":"append()",
    "option4":"add()",
    "answer":"append()"
},

{
    "section":"Technical",
    "question":"Which keyword is used for inheritance in Java?",
    "option1":"inherit",
    "option2":"extends",
    "option3":"implements",
    "option4":"inherits",
    "answer":"extends"
},

{
    "section":"Technical",
    "question":"Which SQL clause is used to filter records?",
    "option1":"ORDER BY",
    "option2":"GROUP BY",
    "option3":"WHERE",
    "option4":"FILTER",
    "answer":"WHERE"
},

{
    "section":"Technical",
    "question":"Which protocol is used to send emails?",
    "option1":"HTTP",
    "option2":"SMTP",
    "option3":"FTP",
    "option4":"TCP",
    "answer":"SMTP"
},

{
    "section":"Technical",
    "question":"Which function is used to get input in Python?",
    "option1":"input()",
    "option2":"scan()",
    "option3":"get()",
    "option4":"read()",
    "answer":"input()"
},

{
    "section":"Technical",
    "question":"Which symbol is used for ID selector in CSS?",
    "option1":"#",
    "option2":".",
    "option3":"*",
    "option4":"@",
    "answer":"#"
},

{
    "section":"Technical",
    "question":"Which language is used for styling web pages?",
    "option1":"HTML",
    "option2":"CSS",
    "option3":"Python",
    "option4":"C",
    "answer":"CSS"
},

{
    "section":"Technical",
    "question":"Which normal form removes partial dependency?",
    "option1":"1NF",
    "option2":"2NF",
    "option3":"3NF",
    "option4":"BCNF",
    "answer":"2NF"
},

{
    "section":"Technical",
    "question":"Which command is used to delete table in SQL?",
    "option1":"REMOVE",
    "option2":"DELETE",
    "option3":"DROP",
    "option4":"CLEAR",
    "answer":"DROP"
},

{
    "section":"Technical",
    "question":"Which keyword is used to create object in Java?",
    "option1":"class",
    "option2":"new",
    "option3":"create",
    "option4":"object",
    "answer":"new"
},

{
    "section":"Technical",
    "question":"Which topology uses central hub?",
    "option1":"Bus",
    "option2":"Ring",
    "option3":"Star",
    "option4":"Mesh",
    "answer":"Star"
},
{
    "section":"Technical",
    "question":"Which keyword is used to stop loop in Python?",
    "option1":"stop",
    "option2":"exit",
    "option3":"break",
    "option4":"continue",
    "answer":"break"
},

{
    "section":"Technical",
    "question":"Which protocol is used to transfer files?",
    "option1":"HTTP",
    "option2":"FTP",
    "option3":"SMTP",
    "option4":"TCP",
    "answer":"FTP"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used to create table row?",
    "option1":"<td>",
    "option2":"<tr>",
    "option3":"<th>",
    "option4":"<table>",
    "answer":"<tr>"
},

{
    "section":"Technical",
    "question":"Which Python collection stores key-value pairs?",
    "option1":"List",
    "option2":"Tuple",
    "option3":"Dictionary",
    "option4":"Set",
    "answer":"Dictionary"
},

{
    "section":"Technical",
    "question":"Which sorting algorithm has best average complexity?",
    "option1":"Bubble Sort",
    "option2":"Selection Sort",
    "option3":"Merge Sort",
    "option4":"Insertion Sort",
    "answer":"Merge Sort"
},

{
    "section":"Technical",
    "question":"Which device connects different networks?",
    "option1":"Switch",
    "option2":"Hub",
    "option3":"Router",
    "option4":"Repeater",
    "answer":"Router"
},

{
    "section":"Technical",
    "question":"Which keyword is used to create class in Python?",
    "option1":"define",
    "option2":"class",
    "option3":"object",
    "option4":"struct",
    "answer":"class"
},

{
    "section":"Technical",
    "question":"Which SQL function is used to count records?",
    "option1":"SUM()",
    "option2":"TOTAL()",
    "option3":"COUNT()",
    "option4":"NUMBER()",
    "answer":"COUNT()"
},

{
    "section":"Technical",
    "question":"Which HTTP method is used to send data?",
    "option1":"GET",
    "option2":"POST",
    "option3":"FETCH",
    "option4":"CONNECT",
    "answer":"POST"
},

{
    "section":"Technical",
    "question":"Which data structure uses nodes connected by pointers?",
    "option1":"Array",
    "option2":"Stack",
    "option3":"Linked List",
    "option4":"Queue",
    "answer":"Linked List"
},

{
    "section":"Technical",
    "question":"Which operator is used for comparison in Python?",
    "option1":"=",
    "option2":"==",
    "option3":"!=",
    "option4":"//",
    "answer":"=="
},

{
    "section":"Technical",
    "question":"Which command is used to insert data in SQL?",
    "option1":"ADD",
    "option2":"INSERT",
    "option3":"UPDATE",
    "option4":"PUT",
    "answer":"INSERT"
},

{
    "section":"Technical",
    "question":"Which memory is temporary?",
    "option1":"ROM",
    "option2":"Hard Disk",
    "option3":"RAM",
    "option4":"DVD",
    "answer":"RAM"
},

{
    "section":"Technical",
    "question":"Which tag is used for line break in HTML?",
    "option1":"<break>",
    "option2":"<lb>",
    "option3":"<br>",
    "option4":"<hr>",
    "answer":"<br>"
},

{
    "section":"Technical",
    "question":"Which keyword is used for conditional statement in Python?",
    "option1":"loop",
    "option2":"if",
    "option3":"switch",
    "option4":"case",
    "answer":"if"
},

{
    "section":"Technical",
    "question":"Which CSS property changes background color?",
    "option1":"bgcolor",
    "option2":"background",
    "option3":"background-color",
    "option4":"color",
    "answer":"background-color"
},

{
    "section":"Technical",
    "question":"Which normal form removes transitive dependency?",
    "option1":"1NF",
    "option2":"2NF",
    "option3":"3NF",
    "option4":"4NF",
    "answer":"3NF"
},

{
    "section":"Technical",
    "question":"Which keyword is used to inherit class in Python?",
    "option1":"inherits",
    "option2":"extends",
    "option3":"super",
    "option4":"class Child(Parent)",
    "answer":"class Child(Parent)"
},

{
    "section":"Technical",
    "question":"Which network topology forms closed loop?",
    "option1":"Star",
    "option2":"Bus",
    "option3":"Ring",
    "option4":"Tree",
    "answer":"Ring"
},

{
    "section":"Technical",
    "question":"Which function converts string to integer in Python?",
    "option1":"str()",
    "option2":"float()",
    "option3":"int()",
    "option4":"char()",
    "answer":"int()"
},

{
    "section":"Technical",
    "question":"Which SQL clause sorts records?",
    "option1":"SORT BY",
    "option2":"GROUP BY",
    "option3":"ORDER BY",
    "option4":"FILTER BY",
    "answer":"ORDER BY"
},

{
    "section":"Technical",
    "question":"Which protocol is used for receiving email?",
    "option1":"SMTP",
    "option2":"POP3",
    "option3":"FTP",
    "option4":"HTTP",
    "answer":"POP3"
},

{
    "section":"Technical",
    "question":"Which loop executes at least once?",
    "option1":"for",
    "option2":"while",
    "option3":"do while",
    "option4":"nested",
    "answer":"do while"
},

{
    "section":"Technical",
    "question":"Which HTML tag creates ordered list?",
    "option1":"<ul>",
    "option2":"<li>",
    "option3":"<ol>",
    "option4":"<list>",
    "answer":"<ol>"
},

{
    "section":"Technical",
    "question":"Which symbol is used for class selector in CSS?",
    "option1":"#",
    "option2":".",
    "option3":"*",
    "option4":"@",
    "answer":"."
},

{
    "section":"Technical",
    "question":"Which searching algorithm requires sorted array?",
    "option1":"Linear Search",
    "option2":"Binary Search",
    "option3":"Depth Search",
    "option4":"Tree Search",
    "answer":"Binary Search"
},

{
    "section":"Technical",
    "question":"Which key uniquely identifies record in database?",
    "option1":"Foreign Key",
    "option2":"Alternate Key",
    "option3":"Primary Key",
    "option4":"Candidate Key",
    "answer":"Primary Key"
},

{
    "section":"Technical",
    "question":"Which method removes element from Python list?",
    "option1":"delete()",
    "option2":"remove()",
    "option3":"clear()",
    "option4":"erase()",
    "answer":"remove()"
},

{
    "section":"Technical",
    "question":"Which layer of OSI model handles encryption?",
    "option1":"Session",
    "option2":"Presentation",
    "option3":"Transport",
    "option4":"Application",
    "answer":"Presentation"
},

{
    "section":"Technical",
    "question":"Which Java keyword is used for inheritance?",
    "option1":"inherits",
    "option2":"extends",
    "option3":"implements",
    "option4":"super",
    "answer":"extends"
},
{
    "section":"Technical",
    "question":"Which operator is used for logical AND in Python?",
    "option1":"&&",
    "option2":"and",
    "option3":"&",
    "option4":"AND",
    "answer":"and"
},

{
    "section":"Technical",
    "question":"Which SQL statement is used to update data?",
    "option1":"MODIFY",
    "option2":"CHANGE",
    "option3":"UPDATE",
    "option4":"ALTER",
    "answer":"UPDATE"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used to create hyperlink?",
    "option1":"<a>",
    "option2":"<link>",
    "option3":"<href>",
    "option4":"<url>",
    "answer":"<a>"
},

{
    "section":"Technical",
    "question":"Which data structure is used in recursion?",
    "option1":"Queue",
    "option2":"Tree",
    "option3":"Stack",
    "option4":"Array",
    "answer":"Stack"
},

{
    "section":"Technical",
    "question":"Which protocol is used for web browsing?",
    "option1":"FTP",
    "option2":"HTTP",
    "option3":"SMTP",
    "option4":"POP3",
    "answer":"HTTP"
},

{
    "section":"Technical",
    "question":"Which Python keyword is used to handle exceptions?",
    "option1":"check",
    "option2":"error",
    "option3":"try",
    "option4":"catch",
    "answer":"try"
},

{
    "section":"Technical",
    "question":"Which SQL command removes all records but keeps table?",
    "option1":"DELETE",
    "option2":"DROP",
    "option3":"TRUNCATE",
    "option4":"REMOVE",
    "answer":"TRUNCATE"
},

{
    "section":"Technical",
    "question":"Which CSS property changes font size?",
    "option1":"font-style",
    "option2":"text-size",
    "option3":"font-size",
    "option4":"size",
    "answer":"font-size"
},

{
    "section":"Technical",
    "question":"Which memory stores BIOS?",
    "option1":"RAM",
    "option2":"ROM",
    "option3":"Cache",
    "option4":"Register",
    "answer":"ROM"
},

{
    "section":"Technical",
    "question":"Which Python function returns length of list?",
    "option1":"size()",
    "option2":"count()",
    "option3":"length()",
    "option4":"len()",
    "answer":"len()"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used for largest heading?",
    "option1":"<head>",
    "option2":"<h6>",
    "option3":"<h1>",
    "option4":"<title>",
    "answer":"<h1>"
},

{
    "section":"Technical",
    "question":"Which network device filters data using MAC address?",
    "option1":"Router",
    "option2":"Switch",
    "option3":"Hub",
    "option4":"Gateway",
    "answer":"Switch"
},

{
    "section":"Technical",
    "question":"Which Python datatype stores unique values?",
    "option1":"List",
    "option2":"Tuple",
    "option3":"Dictionary",
    "option4":"Set",
    "answer":"Set"
},

{
    "section":"Technical",
    "question":"Which SQL clause groups records?",
    "option1":"ORDER BY",
    "option2":"WHERE",
    "option3":"GROUP BY",
    "option4":"SORT BY",
    "answer":"GROUP BY"
},

{
    "section":"Technical",
    "question":"Which topology is most reliable?",
    "option1":"Bus",
    "option2":"Ring",
    "option3":"Mesh",
    "option4":"Star",
    "answer":"Mesh"
},

{
    "section":"Technical",
    "question":"Which keyword is used to define constructor in Java?",
    "option1":"create",
    "option2":"init",
    "option3":"constructor",
    "option4":"Class name",
    "answer":"Class name"
},

{
    "section":"Technical",
    "question":"Which layer of OSI model handles error detection?",
    "option1":"Data Link",
    "option2":"Application",
    "option3":"Session",
    "option4":"Transport",
    "answer":"Data Link"
},

{
    "section":"Technical",
    "question":"Which Python operator performs floor division?",
    "option1":"/",
    "option2":"%",
    "option3":"//",
    "option4":"**",
    "answer":"//"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used to create form?",
    "option1":"<input>",
    "option2":"<form>",
    "option3":"<table>",
    "option4":"<body>",
    "answer":"<form>"
},

{
    "section":"Technical",
    "question":"Which command is used to remove table permanently in SQL?",
    "option1":"DELETE",
    "option2":"REMOVE",
    "option3":"DROP",
    "option4":"CLEAR",
    "answer":"DROP"
},

{
    "section":"Technical",
    "question":"Which algorithm technique divides problem into subproblems?",
    "option1":"Backtracking",
    "option2":"Greedy",
    "option3":"Divide and Conquer",
    "option4":"Branching",
    "answer":"Divide and Conquer"
},

{
    "section":"Technical",
    "question":"Which Python keyword is used to import modules?",
    "option1":"using",
    "option2":"include",
    "option3":"import",
    "option4":"require",
    "answer":"import"
},

{
    "section":"Technical",
    "question":"Which database language is used to define structure?",
    "option1":"DML",
    "option2":"DDL",
    "option3":"DCL",
    "option4":"TCL",
    "answer":"DDL"
},

{
    "section":"Technical",
    "question":"Which CSS property aligns text?",
    "option1":"align",
    "option2":"text-align",
    "option3":"font-align",
    "option4":"position",
    "answer":"text-align"
},

{
    "section":"Technical",
    "question":"Which type of testing checks complete system?",
    "option1":"Unit Testing",
    "option2":"Integration Testing",
    "option3":"System Testing",
    "option4":"Alpha Testing",
    "answer":"System Testing"
},

{
    "section":"Technical",
    "question":"Which Python function converts integer to string?",
    "option1":"char()",
    "option2":"string()",
    "option3":"str()",
    "option4":"text()",
    "answer":"str()"
},

{
    "section":"Technical",
    "question":"Which layer of TCP/IP model corresponds to OSI transport layer?",
    "option1":"Internet",
    "option2":"Application",
    "option3":"Transport",
    "option4":"Network Access",
    "answer":"Transport"
},

{
    "section":"Technical",
    "question":"Which HTML tag is used for inserting video?",
    "option1":"<movie>",
    "option2":"<media>",
    "option3":"<video>",
    "option4":"<mp4>",
    "answer":"<video>"
},

{
    "section":"Technical",
    "question":"Which SQL constraint prevents null values?",
    "option1":"UNIQUE",
    "option2":"CHECK",
    "option3":"NOT NULL",
    "option4":"DEFAULT",
    "answer":"NOT NULL"
},

{
    "section":"Technical",
    "question":"Which traversal method visits root first?",
    "option1":"Inorder",
    "option2":"Postorder",
    "option3":"Preorder",
    "option4":"Levelorder",
    "answer":"Preorder"
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

print("Technical Questions Added Successfully")