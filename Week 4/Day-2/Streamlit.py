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

## Getting Started

First, we’ll create a new Python script and import Streamlit.

- Create a new Python file named first_app.py, then open it with your IDE or text editor.
- Next, import Streamlit.

```py
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
```

- Run your app. A new tab will open in your default browser. It’ll be blank for now. That’s OK.

`streamlit run first_app.py`

Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command.

- You can kill the app at any time by typing Ctrl+c in the terminal.

## Add text and data

### Add a title

Streamlit has a number of ways to add text to your app. Check out our API reference for a complete list.

Let’s add a title to test things out:

`st.title('My first app')`

That’s it! Your app has a title. You can use specific text functions to add content to your app, or you can use `st.write()` and add your own markdown.

### Write a data frame

Along with magic commands, `st.write()` is Streamlit’s "Swiss Army knife". You can pass almost anything to `st.write()`: text, data, Matplotlib figures, Altair charts, and more. Don’t worry, Streamlit will figure it out and render things the right way.

```py
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
```

There are other data specific functions like `st.dataframe()` and `st.table()` that you can also use for displaying data. Check our advanced guides on displaying data to understand when to use these features and how to add colors and styling to your data frames.

## Use magic

You can also write to your app without calling any Streamlit methods. Streamlit supports “magic commands,” which means you don’t have to use st.write() at all! Try replacing the code above with this snippet:

```py
'''
# My first app
Here's our first attempt at using data to create a table:
'''

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
```

Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write(). For more information, refer to the documentation on magic commands.

## Draw charts and maps

Streamlit supports several popular data charting libraries like Matplotlib, Altair, deck.gl, and more. In this section, you’ll add a bar chart, line chart, and a map to your app.

### Draw a line chart

You can easily add a line chart to your app with `st.line_chart()`. We’ll generate a random sample using Numpy and then chart it.

```py
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

### Plot a map

With `st.map()` you can display data points on a map. Let’s use Numpy to generate some sample data and plot it on a map of San Francisco.

```py
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
```

## Add interactivity with widgets

With widgets, Streamlit allows you to bake interactivity directly into your apps with checkboxes, buttons, sliders, and more. Check out our API reference for a full list of interactive widgets.

### Use checkboxes to show/hide data

One use case for checkboxes is to hide or show a specific chart or section in an app. `st.checkbox()` takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement.

```py
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
```

### Use a selectbox for options

Use `st.selectbox` to choose from a series. You can write in the options you want, or pass through an array or data frame column.

Let’s use the `df` data frame we created earlier.

```py
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```

## Lay out your app

For a cleaner look, you can move your widgets into a sidebar. This keeps your app central, while widgets are pinned to the left. Let’s take a look at how you can use `st.sidebar` in your app.

```py
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
```

Most of the elements you can put into your app can also be put into a sidebar using this syntax: `st.sidebar.[element_name]()`. Here are a few examples that show how it’s used: `st.sidebar.markdown()`, `st.sidebar.slider()`, `st.sidebar.line_chart()`.

You can also use `st.columns` to lay out widgets side-by-side, or `st.expander` to conserve space by hiding away large content.

```py
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
```

The only exceptions right now are `st.echo` and `st.spinner`. Rest assured, though, we’re currently working on adding support for those too!

## Show progress

When adding long running computations to an app, you can use `st.progress()` to display status in real time.

First, let’s import time. We’re going to use the `time.sleep()` method to simulate a long running computation:

`import time`

Now, let’s create a progress bar:

```py
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
```

## Share your app

After you’ve built a Streamlit app, it’s time to share it! To show it off to the world you can use Streamlit Cloud to deploy, manage, and share your app. Streamlit Cloud is currently invitation only, so please request an invite and we’ll get you one soon!

It works in 3 simple steps:

- Put your app in a public Github repo (and make sure it has a requirements.txt!)
- Sign into share.streamlit.io
- Click ‘Deploy an app’ and then paste in your GitHub URL

## Interactive Widget

### Button

```py
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
```

### Download Button

```py
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(my_large_df)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
```

### Checkbox

```py
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
```

### Radio Button

```py
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
```

### Select

```py
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
```

### Multiselect

```py
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)
```

### Slider

```py
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

### Range Select

```py
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
```

### Text

```py
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
```

### Number

```py
number = st.number_input('Insert a number')
st.write('The current number is ', number)
```

### Text Area

```py
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (
    ''')
st.write('Sentiment:', run_sentiment_analysis(txt))
```

### Date

```py
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
```

### Time

```py
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
```

### File Upload

```py
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
```

### Add widget to sidebar

```py
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
```

API Cheatsheet [here](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py) or [here](https://docs.streamlit.io/library/api-reference)

## Matplotlib Plot

`st.pyplot`

Display a matplotlib.pyplot figure.

```py
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
```

## Plotly Plot

`st.plotly_chart`

Display an interactive Plotly chart.

```py
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

st.plotly_chart(fig)
```

## App Exercise

Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better. Please come join us on the community forum. We love to hear your questions, ideas, and help you work through your bugs — stop by today!

The first step is to create a new Python script. Let's call it `uber_pickups.py`.

Open `uber_pickups.py` in your favorite IDE or text editor, then add these lines:

```py
import streamlit as st
import pandas as pd
import numpy as np
```

Every good app has a title, so let's add one:

`st.title('Uber pickups in NYC')`

Now it's time to run Streamlit from the command line:

`streamlit run uber_pickups.py`

Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command

## Fetch Data

Now that you have an app, the next thing you'll need to do is fetch the Uber dataset for pickups and drop-offs in New York City.

Let's start by writing a function to load the data. Add this code to your script:

```py
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
```

You'll notice that load_data is a plain old function that downloads some data, puts it in a Pandas dataframe, and converts the date column from text to datetime. The function accepts a single parameter (nrows), which specifies the number of rows that you want to load into the dataframe.

Now let's test the function and review the output. Below your function, add these lines:

```py
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
```

You'll see a few buttons in the upper-right corner of your app asking if you'd like to rerun the app. Choose Always rerun, and you'll see your changes automatically each time you save

## Effortless caching

Try adding @st.cache before the load_data declaration:

```py
@st.cache
def load_data(nrows):
```

Then save the script, and Streamlit will automatically rerun your app. Since this is the first time you’re running the script with @st.cache, you won't see anything change. Let’s tweak your file a little bit more so that you can see the power of caching.

Replace the line data_load_state.text('Loading data...done!') with this:

`data_load_state.text("Done! (using st.cache)")`

Now save. See how the line you added appeared immediately? If you take a step back for a second, this is actually quite amazing. Something magical is happening behind the scenes, and it only takes one line of code to activate it.

## Inspect the raw data

It's always a good idea to take a look at the raw data you're working with before you start working with it. Let's add a subheader and a printout of the raw data to the app:

```py
st.subheader('Raw data')
st.write(data)
```

In the Main concepts guide you learned that st.write will render almost anything you pass to it. In this case, you're passing in a dataframe and it's rendering as an interactive table.

st.write tries to do the right thing based on the data type of the input. If it isn't doing what you expect you can use a specialized command like st.dataframe instead.

## Draw a histogram

Now that you've had a chance to take a look at the dataset and observe what's available, let's take things a step further and draw a histogram to see what Uber's busiest hours are in New York City.

- To start, let's add a subheader just below the raw data section:

`st.subheader('Number of pickups by hour')`

- Use NumPy to generate a histogram that breaks down pickup times binned by hour:

```py
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
```
- Now, let's use Streamlit's st.bar_chart() method to draw this histogram.

`t.bar_chart(hist_values)`

- Save your script. This histogram should show up in your app right away. After a quick review, it looks like the busiest time is 17:00 (5 P.M.).

To draw this diagram we used Streamlit's native bar_chart() method, but it's important to know that Streamlit supports more complex charting libraries like Altair, Bokeh, Plotly, Matplotlib and more.

## Plot data on a map

Using a histogram with Uber's dataset helped us determine what the busiest times are for pickups, but what if we wanted to figure out where pickups were concentrated throughout the city. While you could use a bar chart to show this data, it wouldn't be easy to interpret unless you were intimately familiar with latitudinal and longitudinal coordinates in the city. To show pickup concentration, let's use Streamlit st.map() function to overlay the data on a map of New York City.

- Add a subheader for the section:

`st.subheader('Map of all pickups')`

- Use the st.map() function to plot the data:

`st.map(data)`

- Save your script. The map is fully interactive. Give it a try by panning or zooming in a bit.

After drawing your histogram, you determined that the busiest hour for Uber pickups was 17:00. Let's redraw the map to show the concentration of pickups at 17:00.

- Locate the following code snippet:

```py
st.subheader('Map of all pickups')
st.map(data)
```

- Replace it with:

```py
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
```

- You should see the data update instantly.

To draw this map we used the st.map function that's built into Streamlit, but if you'd like to visualize complex map data, we encourage you to take a look at the st.pydeck_chart.

## Filter results with a slider

In the last section, when you drew the map, the time used to filter results was hardcoded into the script, but what if we wanted to let a reader dynamically filter the data in real time? Using Streamlit's widgets you can. Let's add a slider to the app with the st.slider() method.

- Locate hour_to_filter and replace it with this code snippet:

`hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h`

- Use the slider and watch the map update in real time.

## Use a button to toggle data
Sliders are just one way to dynamically change the composition of your app. Let's use the st.checkbox function to add a checkbox to your app. We'll use this checkbox to show/hide the raw data table at the top of your app.

- Locate these lines:

```py
st.subheader('Raw data')
st.write(data)
```

- Replace these lines with the following code:

```
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
```

## Let's put it all together

That's it, you've made it to the end. Here's the complete script for our interactive app.

```py
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
```
"""