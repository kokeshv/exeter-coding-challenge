import pandas as pd
import re
import time
import os, psutil

def replaceWords(text, wordDict):
    check=[]
    frequency = []
    for key in wordDict:
        frequency.append([a.start() for a in re.finditer(key, text)])
        text = text.replace(key, wordDict[key])
    return text,frequency

start=time.time()

french_dic = pd.read_csv('french_dictionary.csv', header=None)
eng_list = french_dic[0].to_list()
french_list = french_dic[1].to_list()
dic = dict(zip(eng_list,french_list))

with open('t8.shakespeare.txt', 'r') as file:
    data = file.read()

str1,frequency = replaceWords(data, dic)
freq = []
for i in range(len(frequency)):
    freq.append(len(frequency[i]))

text_file = open("19990924.kokesh.venkatesh.kcg_college_of_technology/t8.shakespeare.translated.txt", "w")
text_file.write(" %s " % str1)
text_file.close()

Dict=[{'English word':eng, 'French word':french, 'Frequency':fr} for eng,french,fr in zip(eng_list,french_list,freq)]
df = pd.DataFrame (Dict, columns = ['English word','French word','Frequency'])
df.to_csv("19990924.kokesh.venkatesh.kcg_college_of_technology/frequency.csv", index=None)

end = time.time()
t=end - start
mem_file = open("19990924.kokesh.venkatesh.kcg_college_of_technology/performance.txt", "w")
str_1 = "Time to process: " + str(t) + "secs"
str_2 = "Memory used: " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + "mB"
mem_file.write(" %s\n " % str_1)
mem_file.write(" %s " % str_2)
mem_file.close()