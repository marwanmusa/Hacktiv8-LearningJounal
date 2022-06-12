# -*- coding: utf-8 -*-
"""
# Streamlit

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps - so let’s get started!

1. Make sure that you have Python 3.6+ installed.
2. Install Streamlit using PIP and run the ‘hello world’ app:

```sh
pip install streamlit
streamlit hello
```

That’s it! In the next few seconds the sample app will open in a new tab in your default browser.

Still with us? Great! Now make your own app in just 3 more steps:

1. Open a new Python file, import Streamlit, and write some code
2. Run the file with: `streamlit run [filename]`
3. When you’re ready, click `Deploy` from the Streamlit menu to share your app with the world!

Now that you’re set up, let’s dive into more of how Streamlit works and how to build great apps.

## Media and Layout

st.image

Display an image or list of images.

```py
from PIL import Image
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')
```

st.columns

Insert containers laid out as side-by-side columns.

Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

To add elements to the returned containers, you can use "with" notation (preferred) or just call methods directly on the returned object. See examples below.

You can use with notation to insert any element into a column:

```py
col1, col2, col3 = st.columns(3)
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")
```

Or you can just call methods directly in the returned objects:

```py
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
```

st.expander

Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. When collapsed, all that is visible is the provided label.

To add elements to the returned container, you can use "with" notation (preferred) or just call methods directly on the returned object. See examples below.

```py
st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
  st.write('''
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.
  ''')

  st.image("https://static.streamlit.io/examples/dice.jpg")
```

st.container

Insert a multi-element container.

Inserts an invisible container into your app that can be used to hold multiple elements. This allows you to, for example, insert multiple elements into your app out of order.

To add elements to the returned container, you can use "with" notation (preferred) or just call methods directly on the returned object. See examples below.

```py
with st.container():
  st.write("This is inside the container")

  # You can call any Streamlit command, including custom components:
  st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
```

st.set_page_config

Configures the default settings of the page.

```py
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
```

## Multipage Streamlit

We can create multiple apps and navigate across each of them in a main app using a radio button. Let’s see how to do that.

1. Create app1.py and app2.py .

```py
# app1.py
import streamlit as st
def app():
    st.title('APP1')
    st.write('Welcome to app1')
```

```py
# app2.py
import streamlit as st
def app():
    st.title('APP2')
    st.write('Welcome to app2')
```

2. Create a main app app.py and add a navigator using radio or select buttons.

```py
#app.py
import app1
import app2
import streamlit as st
PAGES = {
    "App1": app1,
    "App2": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
```

Now you run the app.py to access and navigate through both the apps.

## Practice Session.

Make your own dashboard using [this](https://www.kaggle.com/peterkmutua/housing-dataset) dataset.

### Deployment

Next, in the project’s root directory, create a file called `runtime.txt` where you’ll specify a Python version for your Heroku app:

```txt
python-3.8.6
```

When you deploy your app, Heroku will automatically detect that it’s a Python application and will use the correct buildpack. If you also provide a runtime.txt, then it’ll pin down the Python version that your app will use.

Next, create a `requirements.txt` file in the project’s root directory where you’ll copy the libraries required to set up your Dash application on a web server:

```py
streamlit
pandas
plotly
```
Now create a file named `setup.sh` with the following content:

```sh
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

Now create a file named `Procfile` with the following content:

`web: sh setup.sh && streamlit run app.py`

This file tells the Heroku index what commands should be executed to start your app.

Next, you’ll need to initialize a Git repository. To do that, go to your project’s root directory and execute the following command:

`$ git init`

This will start a Git repository in h8_dash/. It’ll start tracking all the changes you make to the files in that directory.

However, there are files you don’t want to track using Git. For example, you usually want to remove Python compiled files, the contents of your virtual environment folder, or metadata files such as .DS_Store.

To avoid tracking unnecessary files, create a file called `.gitignore` in the root directory. Then copy the following content in it:

```py
venv
*.pyc
.DS_Store # Only if you are using macOS
```

This will make sure your repository doesn’t track unnecessary files. Now commit your project files:

```sh
$ git add .
$ git commit -m 'Add dashboard files'
```

Finally, you need to create an app in Heroku, push your code there using Git, and start the app in one of Heroku’s free server options. You can do that by running the following commands:

```sh
$ heroku create APP-NAME # Choose a name for your app
$ git push heroku master
$ heroku ps:scale web=1
```

The first command will create a new application on Heroku and an associated Git repository. The second will push the changes to that repository, and the third will start your app in one of Heroku’s free server options.

That’s it! You’ve built and deployed your dashboard. Now you just need to access it to share it with your friends. To access your app, copy https://APP-NAME.herokuapp.com/ in your browser and replace APP-NAME with the name you defined in the previous step.
"""