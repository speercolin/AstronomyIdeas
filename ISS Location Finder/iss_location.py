# Importing the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Link to the ISS coordinates api
link = "http://api.open-notify.org/iss-now.json"

# Converting the link into a Pandas data frame
df = pd.read_json(link)

# Filtering data
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

# Dropping unnecessary data
df = df.drop(['index', 'message'], axis=1)

# Setting background image
background = mpimg.imread('world_map.jpg')

# Creating plot using Seaborn
sns.scatterplot(x='latitude', y='longitude', data=df, s=50, color='red')

# Displaying the plot using matplotlib
plt.imshow(background, extent=[-90, 90, -180, 180], aspect='auto')
plt.show()
