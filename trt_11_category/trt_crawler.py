
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_context(url):
    try:
        context = ""
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        element = soup.find("div", attrs={'class': 'editorPart blackle'})
        p_nodes = element.find_all("p")
        for p_node in p_nodes:
            context += p_node.text + " "
        return " ".join(context.split())
    except:
        return ""

######################################################

MAIN_URL = "https://www.trthaber.com/"
URL = "https://www.trthaber.com/haber/guncel/"
category = "guncel"

min_page_no = 1
max_page_no = 100

title_list = []
context_list = [] # text
category_list = []  # label

for page_no in range(min_page_no, max_page_no + 1):
    print("page_no: ", page_no)

    page = requests.get(URL + str(page_no) + ".sayfa.html")
    soup = BeautifulSoup(page.content, 'html.parser')

    elements = soup.find_all("div", attrs={'class': 'row'})
    #print(len(elements))
    for node in elements:
        link_nodes = node.find_all("a", attrs={"class": "cat-page-small-item"})
        for link_node in link_nodes:
            #print("title: ", link_node['title'])
            #print("link: ", MAIN_URL + link_node["href"])
            # get context
            context = get_context(MAIN_URL + link_node["href"])
            #print("context: ", context)
            #print("*"*30)

            # save
            title_list.append(" ".join(link_node['title'].split()))
            context_list.append(context)
            category_list.append(category)

df = pd.DataFrame(zip(title_list, context_list, category_list), columns=["title", "context", "category"])
df.to_excel(category + ".xlsx", encoding="utf-8")


"""
import pandas as pd

# ekonomi
# spor
# kültür-sanat
# sağlık
# teknoloji
# eğitim

df_ekonomi = pd.read_excel("ekonomi.xlsx")
df_spor = pd.read_excel("spor.xlsx")
df_kultur_sanat = pd.read_excel("kultur_sanat.xlsx")
df_saglik = pd.read_excel("saglik.xlsx")
df_bilim_teknoloji = pd.read_excel("bilim_teknoloji.xlsx")
df_egitim = pd.read_excel("egitim.xlsx")

dfs = [df_ekonomi, df_spor, df_kultur_sanat, df_saglik, df_bilim_teknoloji, df_egitim]

df_out = pd.concat(dfs)
print(df_out)
print(df_out.columns)
print(len(df_out))

df_out.to_excel("trt_6_category.xlsx", encoding="utf-8")
"""

"""
import pandas as pd

df_bilim_teknoloji = pd.read_excel("bilim_teknoloji.xlsx")
df_dunya = pd.read_excel("dunya.xlsx")
df_egitim = pd.read_excel("egitim.xlsx")
df_ekonomi = pd.read_excel("ekonomi.xlsx")
df_guncel = pd.read_excel("guncel.xlsx")
df_gundem = pd.read_excel("gundem.xlsx")
df_kultur_sanat = pd.read_excel("kultur_sanat.xlsx")
df_saglik = pd.read_excel("saglik.xlsx")
df_spor = pd.read_excel("spor.xlsx")
df_turkiye = pd.read_excel("turkiye.xlsx")
df_yasam = pd.read_excel("yasam.xlsx")

dfs = [df_bilim_teknoloji,
       df_dunya,
       df_egitim,
       df_ekonomi,
       df_guncel,
       df_gundem,
       df_kultur_sanat,
       df_saglik,
       df_spor,
       df_turkiye,
       df_yasam
       ]

df_out = pd.concat(dfs)
print(df_out)
print(df_out.columns)
print(len(df_out))

df_out.to_excel("trt_11_category.xlsx", encoding="utf-8")
"""
