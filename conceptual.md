### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Unlike Javascript, Python is a "high level" language, is dynamic, and runs on servers as opposed to how javascript runs in the browser. It is used for data science, machine learning, making servers, etc.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
One way to to try to get a missing key is to use .get(key, default_key). In this method, if the key is not in the dictionary, the default_key will be returned, avoiding an error. Similarly, setdefault(key, def_value) will work the same way, but the default key is added to the dictionary if the key is missing. 

- What is a unit test?
A unit test will test an individualy functionality of the code, usually a function or methond.
- What is an integration test?
An integration test will test how the compnents work together
- What is the role of web application framework, like Flask?
A web application framework has built in functions and classes which help handle browser interaction - handle web requests, produce dynamic HTML, handle forms, cookies, and connects to backend.
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

URL Querys are usually used when return extra info, or when handling forms. URL parameters should be the main subjuect of the page.

- How do you collect data from a URL placeholder parameter using Flask?
A variable is set up in the URL route, and passed as a parameter in the route function.

- How do you collect data from the query string using Flask?
Use flask import request, then set a variable in the function to the query string using request.args. *ex* "/search?term=word"  term = request.args["term"]
- How do you collect data from the body of the request using Flask?
I think this is asking for request.form? save that to a variable to be saved in database
- What is a cookie and what kinds of things are they commonly used for?
A cookie is a name/string value pair used to store bits of data on the browser

- What is the session object in Flask?
The session object in Flask is a dictionary that can't be modified and is "serialized" with a key.
- What does Flask's `jsonify()` do?
jsonify turns data into JSON
