import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

levi_df = pd.read_csv("C:\\Code\\Miniproject 2\\predicted_data\\levi_future.csv")
koli_df = pd.read_csv("C:\\Code\\Miniproject 2\\predicted_data\\koli_future.csv")
messila_df = pd.read_csv("C:\\Code\\Miniproject 2\\predicted_data\\messila_future.csv")
tahko_df = pd.read_csv("C:\\Code\\Miniproject 2\\predicted_data\\tahko_future.csv")
ruka_df = pd.read_csv("C:\\Code\\Miniproject 2\\predicted_data\\ruka_future.csv")


def plot_snow_depth (df, title):
# Read the CSV file into a DataFrame
    df = df.rename(columns={"0":'Snow Depth (cm)'})
    df['Date']= pd.to_datetime(df['Date'])


    #plt.figure(figsize=(60,10))
    df = df.head(2000)
    
    # Extract x and y data
    x = df['Date']
    y = df['Snow Depth (cm)']

    # Plot the data
    plt.plot(x, y)
    plt.axhline(y = 0, color = 'black', linestyle = '-')
    plt.axhline(y = 20, color = 'red', linestyle = '-')
    plt.axhline(y = 40, color = 'red', linestyle = '-')
    plt.xlabel("Year")
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    
    plt.ylabel("Snow Depth (cm)") 

    plt.ylim(0,100)

    plt.title(title)
    plt.show()


#plot_snow_depth(messila_df, "Messilä")
plot_snow_depth(levi_df, "Levi")
# plot_snow_depth(tahko_df, "Tahko")
# plot_snow_depth(koli_df, "Koli")
#plot_snow_depth(ruka_df, "Ruka")