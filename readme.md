(readme.md is a draft/WIP)

# Flask Chat App - (Learn To Use Flask)

My first attempts at building with Flask. Very basic chat app using flask_socketio, jinja2 templates, et al...

## Getting Started

- To run the app, clone the repo, follow the steps for creating a virtuaenv, install the dependencies.
- To use the chat open two tabs (both to localhost:5000) and start chatting with yourself!
- CSS, layout, login --> TODO

### Steps to Build

- Create Env
  `python3 -m venv <name-of-venv>`

- Run venv
  `source ./venv/bin/activate`

- Upgrade pip (opitonal)
  ` pip install --upgrade pip`

- Install dependencies
  `pip3 install flask flask_sqlalchemy flask_assets flask_session flask_socketio`

- Create directories and files (or clone):
  `touch __init__.py && mkdir templates && touch templates/base.html && touch index.html && mkdir static && touch static/css/styles.css`

## SQLAlchemy notes:

- To add the database tables:
  `python3`
  `from app import db`
  `db.create_all()`

- To drop tables:
  `python3`
  `from app import db`
  `db.drop_all()`

- To query:
- `python3`
  `from app import User`
  `User.query.all()`

### Tailwind config (optional - css lib, requires node):

- `npx tailwindcss build -i static/css/main.css -o static/css/main.css`

- `pip install -r requirements.txt` to install flask packages
- `npm install` to install npm packages from package.json

- In one terminal run npm run dev to run Tailwind in JIT watch mode during development - this will start real time compilation of styles used in your HTML templates

- In second terminal run python run.py to start the Flask development server (debug mode is ON). As you add/remove Tailwind classes in HTML templates, the watcher running in step 3 will automatically regenerate your app\static\main.css file which is picked up the flask server running in step 4.

### Prerequisites

- python3
- pip3
- virtualenv
- node

### Installing

- TODO

## Deployment

- TODO

#### Tailwind/CSS

- When ready for production, kill the Flask development server in step 3 and run npm run build:prod to prepare CSS build ready for production

## Built With

- TODO

## Contributing

Feel free...

## License

## Acknowledgments

- TODO
