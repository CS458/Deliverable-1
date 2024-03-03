# Run The Server
- Requirements:
  - Python 3.10
- Go to `./`
- Run `pip install -r requirements.txt`
  - To run the application with google authentication feature, please add a `google consumer_key` and `consumer_secret` to the variables in `./settings/app.py.` By adding `http://127.0.0.1:5000/google/authorized` as an authorized redirect URL.
- Run `python main.py`
- If the server runs successfully, you may visit [the page](http://127.0.0.1:5000/).
- To run the tests, gp to `./test/blackbox/`, and tun `python main.py`

# Design Pattern 
- For this project we are using MVC (Model-View-Controller) design.
- Controllers are located in `./controllers.py`
- Modesl are located in `./models.py`
- `./Views/` contain views.
