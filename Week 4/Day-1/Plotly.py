# -*- coding: utf-8 -*-
"""
Plotly

Plotly Express is a new high-level Python visualization library: it’s a wrapper for Plotly.py that exposes a simple syntax for complex charts. Inspired by Seaborn and ggplot2, it was specifically designed to have a terse, consistent and easy-to-learn API: with just a single import, you can make richly interactive plots in just a single function call, including faceting, maps, animations, and trendlines. It comes with on-board datasets, color scales and themes, and just like Plotly.py, Plotly Express is totally free: with its permissive open-source MIT license, you can use it however you like (yes, even in commercial products!). Best of all, Plotly Express is fully compatible with the rest of Plotly ecosystem: use it in your Dash apps, export your figures to almost any file format using Orca, or edit them in a GUI with the JupyterLab Chart Editor!

If you’re the TL;DR type, just `pip install plotly` and head on over to our walkthrough notebook or gallery or reference documentation to start playing around, otherwise read on for an overview of what makes Plotly Express special.

## Quick and easy data visualization with Plotly Express

Once you import Plotly Express (aka `px`), most plots are made with just one function call that accepts a [tidy Pandas data frame](http://www.jeannicholashould.com/tidy-data-in-python.html), and a simple description of the plot you want to make. For example if you want a simple scatter plot, it’s just `px.scatter(data, x="column_name", y="column_name")`. Here’s an example with the [Gapminder dataset](https://www.gapminder.org/tools/#$state$time$value=2007;;&chart-type=bubbles) – which comes built-in! – showing life expectancy vs GPD per capita by country for 2007:
"""

import plotly.express as px
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")

"""If you want to break that down by continent, you can color your points with the `color` argument and `px` takes care of the details:"""

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent")

"""Each point here is a country, so maybe we want to scale the points by the country population… no problem: there’s an arg for that too!

"""

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60)

"""Curious about which point is which country? Add a `hover_name` and you can easily identify any point: never again wonder “what *is* that outlier?”... just mouse over the point you're interested in!"""

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60, hover_name="country")

"""You could facet your plots, just as easily as coloring your points with `facet_col="continent"`, and let's make the x-axis logarithmic to see things more clearly."""

px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60,
          hover_name="country", facet_col="continent", log_x=True)

"""Maybe you're interested in more than just 2007 and you want to see how this chart evolved over time. You can animate it by setting `animation_frame="year"` and `animation_group="country"` to identify which circles match which ones across frames. In this final version, let's tweak some of the display here, as text like "gdpPercap" is kind of ugly even though it's the name of our data frame column. We can provide prettier `labels` that get applied throughout the figure, in legends, axis titles and hovers. We can also provide some manual bounds so the animation looks nice throughout:"""

px.scatter(gapminder, x="gdpPercap", y="lifeExp",size="pop", size_max=60, color="continent", hover_name="country",
           animation_frame="year", animation_group="country", log_x=True, range_x=[100,100000], range_y=[25,90],
           labels=dict(pop="Population", gdpPercap="GDP per Capita", lifeExp="Life Expectancy"))

"""Because this is geographic data, we can also represent it as an animated map, which makes it clear that `px` can make way more than just scatterplots, and that this dataset is missing data for the former Soviet Union."""

px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year",
              color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")

"""## Visualize Distributions

A major part of data exploration is understanding the distribution of values in a dataset, and how those distributions relate to each other. Plotly Express includes a number of functions to do just that.
Visualize univariate distributions with histograms, box-and-whisker or violin plots:
"""

tips = px.data.tips()

px.histogram(tips, x="total_bill", y="tip", histfunc="sum", color="smoker")

px.box(tips, x="total_bill", y="day", orientation="h", color="smoker", notched=True,
       category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]})

px.violin(tips, y="tip", x="smoker", color="sex", box=True, points="all")

"""You can also visualize bivariate distributions with marginal rugs, histograms, boxes or violins, and you can add trendlines too. px even helpfully adds the line's equation and R² in the hover box for you! It uses `statsmodels` under the hood to do either Ordinary Least Squares (OLS) regression or Locally Weighted Scatterplot Smoothing (LOWESS)."""

px.scatter(tips, x="total_bill", y="tip", color="smoker", trendline="ols", marginal_x="violin", marginal_y="box")

"""## Color scales and sequences

You’ll notice some nice color scales in some of the plots above. Plotly Express. The px.colors module contains a number of useful scales and sequences: qualitative, sequential, diverging, cyclical, and all your favourite open-source bundles: ColorBrewer, cmocean and Carto. We’ve also included some functions to make browsable swatches for your enjoyment
"""

px.colors.qualitative.swatches()

px.colors.sequential.swatches()

"""## Interactive Multidimensional Visualization, in one line of Python

Scatterplot matrices (SPLOMS), parallel coordinates, and a flavour of parallel sets we call parallel categories. With these, you can visualize entire datasets in a single plot for data exploration. Check out these one-liners and the interactions they enable, right in your Jupyter notebook:

"""

iris = px.data.iris()
px.scatter_matrix(iris, dimensions=['sepal_width', 'sepal_length', 'petal_width', 'petal_length'],
                  color='species')

px.parallel_coordinates(iris, color='species_id', color_continuous_scale=['red', 'green', 'blue'])

px.parallel_categories(tips, color='size', color_continuous_scale=px.colors.sequential.Inferno)

"""## More Basic Examples"""

import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()
df.head()

"""Once we imported the libraries and the dataset, we can begin to try the basic functions to display plots. Below there is an example of a scatterplot that shows the relationship between the width and the length of the sepals. With the function scatter from the module of Plotly Express, we can easily build the graph specifying the necessary arguments for the DataFrame object, the variable in the x-axis and the variable in the y-axis.

"""

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

"""A more elaborate scatterplot can be built including the species and the petal length as information. Each of the three species is represented by a different colour, while the size of the dots is proportional to the petal length. The result is this gorgeous graph:"""

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     size='petal_length', hover_data=['petal_width'])
fig.show()

"""But if do we want to have an overview of all the features in the dataset? A simple scatterplot is not enough. A 3D scatterplot is a solution to this problem. In this three-dimensional plot, I included five dimensions:
- 1st dimension: sepal length in the x-axis
- 2nd dimension: petal length in the y-axis
- 3rd dimension: petal width in the z-axis
- 4th dimension: different colours corresponds to different species
- 5th dimension: the size of dots is proportional to the sepal width

"""

fig = px.scatter_3d(df, x="sepal_length", y="petal_length", z="petal_width", 
                    color="species",size='sepal_width')
fig.show()

"""Another way to have a nice representation of the relationship between each couple of features is to use the function scatter_matrix:"""

fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
fig.show()

"""After we saw the relationship between the features, we may be interested in look at the distribution of these features. A simple way to have insights about the distribution of the values of a particular feature is to display a boxplot. From this graphical tool, you can observe many patterns at once: the variance, the median, the first and third quantile, the outliers.

"""

fig = px.box(df, y="sepal_width")
fig.show()

"""Thanks to the interactive boxplot provided by the plotly.express module, it’s possible to have a visualization of the specific values corresponding to the minimum and maximum, the first, second and third quantile. Below I also included the information of the three species, specifying the y variable:"""

fig = px.box(df, x="species", y="sepal_width",color="species")
fig.show()

"""To have more complete information about the distribution of the data, we also need the histogram. It represents the distribution of the frequency of each value of a specific numeric variable. Each bin counts how many time that specific value appears. There are many possible aggregate functions, such as sum and average, not only count. Using the function px.histogram() is possible to visualize the frequency distribution of the sepal width feature:"""

fig = px.histogram(df, x="sepal_width")
fig.show()

"""As before, I would like to show the differences between species in one feature. It’s possible by producing several histograms for the different values of the sepal width. Each colour represents one of three species. There are also functions that overlay the histograms and reduce the opacity to be able to see the three histograms at the same time, even if they have common values."""

fig = px.histogram(df, x="sepal_width", color="species")
fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.75)
fig.show()

"""With the function histogram, it’s possible to build also bar plots. We can count the number of observations for each of the three species:

"""

fig = px.histogram(df, x='species', y='sepal_width', histfunc='count', height=300,
                    title='Histogram Chart')
fig.show()

"""Indeed, the dataset collects 50 samples for each species. Plotly Express offers other tools that combine more plots together. In this case, we can combine a scatterplot with a boxplot for each feature included:"""

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="box",
           marginal_x="box", trendline="ols", template="simple_white")
fig.show()

"""Or we can see at once the scatterplot and the histograms:"""

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="histogram",
           marginal_x="histogram", trendline="ols", template="simple_white")
fig.show()

"""There are many ways to export the figures on your local PC. The more intuitive method is to click the camera bottom at the top of the graph.

## Example on Coronavirus Data
"""

import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/covid_19_data.csv')
df.head()

"""### Choropleth Maps

Spread of the Coronavirus Globally Over Time. This is an animated choropleth which shows where the coronavirus has spread in the month of February 2020.
"""

fig = px.choropleth(df, 
                    locations="Country/Region", 
                    locationmode = "country names",
                    color="Confirmed", 
                    hover_name="Country/Region", 
                    animation_frame="ObservationDate"
                   )

fig.update_layout(
    title_text = 'Spread of Coronavirus',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))
    
fig.show()

"""### Pie Charts

Proportion of Confirmed Cases by Country
"""

fig = px.pie(df, values = 'Confirmed', names='Country/Region', height=600)
fig.update_traces(textposition='inside', textinfo='percent+label')

fig.update_layout(
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig.show()

"""### Bar Graphs

Total Number of Confirmed Cases Over Time
"""

bar_data = df.groupby(['Country/Region', 'ObservationDate'])['Confirmed', 'Deaths', 'Recovered'].sum().reset_index().sort_values('ObservationDate', ascending=True)

fig = px.bar(bar_data, x="ObservationDate", y="Confirmed", color='Country/Region', text = 'Confirmed', orientation='v', height=600,
             title='Cases')
fig.show()

"""- There was a major spike on February 13th, due to a new method of reclassifying confirmed cases
- It started to plateau, but because of the release of the members on the Diamond Cruise Ship, you could see an increasing number of countries with cases towards the end of February. This may suggest that the spread of the virus is far from plateauing.

Total Number of Deaths Over Time
"""

fig = px.bar(bar_data, x="ObservationDate", y="Deaths", color='Country/Region', text = 'Deaths', orientation='v', height=600,
             title='Deaths')
fig.show()

"""Total Number of Recovered Cases Over Time"""

fig = px.bar(bar_data, x="ObservationDate", y="Recovered", color='Country/Region', text = 'Recovered', orientation='v', height=600,
             title='Recovered')
fig.show()

"""The number of deaths and recovered cases are lagging indicators, so we should see some numbers racking up in other countries as the weeks go by.

### Line Graph
"""

line_data = df.groupby('ObservationObservationDate').sum().reset_index()

line_data = line_data.melt(id_vars='ObservationDate', 
                 value_vars=['Confirmed', 
                             'Recovered', 
                             'Deaths'], 
                 var_name='Ratio', 
                 value_name='Value')

fig = px.line(line_data, x="ObservationDate", y="Value", color='Ratio', 
              title='Confirmed cases, Recovered cases, and Death Over Time')
fig.show()

"""This is a consolidated representation of the bar graphs shown above. Ideally, we would like to see the red line and blue line converge and pass each other.

### Treemaps

Treemaps are a similar representation to pie charts in that it represents proportions.
"""

fig = px.treemap(df_countries, path=['Country/Region'], values='Confirmed', height=600, width=1000)

fig.update_layout(
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig.show()