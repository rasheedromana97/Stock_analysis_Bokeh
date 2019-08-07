from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file, save

start_time=datetime.datetime(2018,2,1)
end_time=datetime.datetime(2018,2,26)
df=data.DataReader("AAPL","yahoo",start_time,end_time)
#data.DataReader(name="stock symbol",data_source="",starttime,endtime)
#Every company has a stock symbol/ticker. #https://pandas-datareader.readthedocs.io/en/latest/ = for more information
#print(df)
def inc_dec(c,o):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value = "Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"]= (df.Open + df.Close)/2
df["Height"]= abs(df.Close - df.Open)/2
#print(df)

p=figure(x_axis_type='datetime',plot_width=800,plot_height=300,sizing_mode="scale_width")
p.title.text="Candlestick Chart"
p.grid.grid_line_alpha =0.3 #To define the transparency of the grid lines

hours_12=12*60*60*1000
p.segment(df.index,df.High,df.index,df.Low,color="black")
#Syntax: .segment(x value of it's highest point, y value of it's highest point, x of the lower point, y of the lower point)
#X remains the same because we are moving horizontally along the grid.
#Segments are the lines between the rectangles that you see in the grid_line_alpha
#These can be behind the rectangles and infront of them. These lines run like a layer, so if you add this
#code of segment after the rect code then it will be on the triangles, if you add them like this, it will behind.

p.rect(df.index[df.Status=="Increase"],
        df.Middle[df.Status=="Increase"], hours_12,
        df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")

p.rect(df.index[df.Status=="Decrease"],
        df.Middle[df.Status=="Decrease"], hours_12,
        df.Height[df.Status=="Decrease"],fill_color="#FF3333", line_color="black")

output_file("CS.html")
save(p)
