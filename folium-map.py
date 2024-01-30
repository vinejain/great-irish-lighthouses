# Ireland map
#!pip install folium
#!pip install branca
import folium
from folium import IFrame
import branca
import pandas as pd

# initialing folium base map for Ireland
# Make an empty map
#m = folium.Map(location=[53.350496, -6.239456], zoom_start=7, tiles='Stamen Toner', max_bounds=True, scrollWheelZoom = False)
m = folium.Map(location=[53.350496, -6.239456], zoom_start=7, tiles='OpenStreetMap', max_bounds=True, scrollWheelZoom = False)

# reading dataset
data = pd.read_csv('data.csv')

# frame url popup function
def get_frame(url,width,height):
      html = """ 
                <!doctype html>
            <html>
            <iframe id="myIFrame" width="{}" height="{}" src={}""".format(width,height,url) + """ frameborder="0"></iframe>
            <script type="text/javascript">
            var resizeIFrame = function(event) {
                var loc = document.location;
                if (event.origin != loc.protocol + '//' + loc.host) return;

                var myIFrame = document.getElementById('myIFrame');
                if (myIFrame) {
                    myIFrame.style.height = event.data.h + "px";
                    myIFrame.style.width  = event.data.w + "px";
                }
            };
            if (window.addEventListener) {
                window.addEventListener("message", resizeIFrame, false);
            } else if (window.attachEvent) {
                window.attachEvent("onmessage", resizeIFrame);
            }
            </script>
            </html>"""
      return html


for i in range(0,len(data)):

  width, height = 900, 500
  html = get_frame(data.iloc[i]['url'], width, height)
  iframe = IFrame(html=html , width=width, height=height)
  popup  = folium.Popup(iframe, parse_html = True)
  folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']],  icon=folium.Icon(color='black', icon='anchor', prefix='fa'), 
                popup=popup).add_to(m)


title_html = '''
             <h1 align="left" style="color:red"><b>The Great Irish Lighthouses</b></h1>
             <h4><a target="_blank" rel="noopener noreferrer" href="https://github.com/vinejain/great-irish-lighthouses">(view code)</a></h4>
             <body style="background-color:black;">
             '''
m.get_root().html.add_child(folium.Element(title_html))

# Save it as html
m.save('great-irish-lighthouses.html')
m

# from google.colab import files
# files.download('312_markers_on_folium_map1.html') 