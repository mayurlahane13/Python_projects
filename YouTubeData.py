import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import requests
from bs4 import BeautifulSoup
df = pd.read_csv('INvideos.csv')
grouped= df.groupby(['category_id'])['video_id'].count().reset_index(name='frequency')

url = 'https://techpostplus.com/youtube-video-categories-list-faqs-and-solutions/'

html = requests.get(url)
html = html.text
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')
category_list = []
for tr in table_rows:
    td = tr.find_all('td')
    data = [i.text for i in td ]
    category_list.append(data)
category_list.pop()
temp_df = pd.DataFrame(category_list, columns=['category_id','category','description'])
temp_df.drop(columns= 'description',inplace = True)
temp_df['category_id'] = pd.to_numeric(temp_df['category_id'])
grouped['category_id'] = pd.to_numeric(grouped['category_id'])
joined_df = pd.merge(temp_df,grouped, on = 'category_id')

x = joined_df['category']
y = joined_df['frequency']
plt.bar(x,y)
plt.xticks(x,rotation = 'vertical',size = 8)
plt.xlabel('YouTube Categories')
plt.ylabel('Number of videos Trended in 2017-2018')
plt.title('Videos Trended on YouTube in India in 2017-18')
plt.show()

# tags_dict = {}
# a = df['tags'].str.split('|')
# current_tag = ''
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         current_tag = a[i][j]
#         if current_tag in tags_dict.keys():
#             tags_dict[current_tag] +=1
#         else:
#             tags_dict[current_tag] = 1
# print(len(tags_dict))
# plt.figure()
# plt.hist(df['views'])
# plt.title('Views for trending videos 2017-18')
# plt.xlabel('Views')
# plt.show()