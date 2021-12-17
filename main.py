import pandas as pd
import streamlit as st

#COBA DISPLAY DATA NEGARA DULU YG BISA DI INPUT SEBELOM INPUT NAMA NEGARANYA
import json
f = open("D:\\COOLYEAH\\Prokom\\UAS\\kode_negara_lengkap.json")
file_json = json.load(f)
df_xsl = pd.read_excel(
    "D:\\COOLYEAH\\Prokom\\UAS\\produksiminyakmentah.xlsx")
df_json = pd.DataFrame.from_dict(file_json, orient='columns')

st.title("Grafik dan Hasil Produksi Minyak Pada Negara di Dunia")
st.image("https://tse1.mm.bing.net/th?id=OIP.YUhFLbjzWPiw7YaBz1zXUAHaEK&pid=Api&P=0&w=339&h=191",width=500)
listnih= list[""]
listbaru = []
listnih2 = []
change_country = []
for x in listnih(df_xsl['country_code']):
    if x not in listnih(df_json['alpha-3']):
        listbaru.append(x)
for x in listbaru:
    df_xsl = df_xsl[df_xsl.country_code != x]
daftarnegara = []
for x in list(df_xsl['country_code']):
    if x not in daftarnegara:
        daftarnegara.append(x)
import matplotlib.pyplot as plt
inputan = st.selectbox("Silahkan masukkan kode Negara yang ingin dicari = ", daftarnegara)
dfbaru=df_xsl.loc[df_xsl['country_code'] == inputan.upper()]

#Pemunculan Grafik
fig,ax = plt.subplots()
ax.plot(dfbaru['Year'],dfbaru['Production'], color='red')
ax.set_xlabel ('Tahun', fontsize = 14)
ax.set_ylabel ('produksi', fontsize = 12)
st.pyplot(fig)
# UNTUK NAMA NEGARA PAKE TOLERANSI HURUF BESAR HURUF KECIL SEMENTARA

#B
daftartahun = []
for x in list(df_xsl['Year']):
    if x not in daftartahun:
        daftartahun.append(x)
T = st.selectbox("Masukkan tahun produksi = ", daftartahun)
B = st.number_input("Masukkan banyak negara untuk ditampilkan = ",min_value=1, max_value=len(daftarnegara))

df1 = df_xsl.loc[df_xsl['Year'] == T]
df1 = df1.sort_values(by=['Production'], ascending=False)
dfm = df1[:B]

i = 0
i = i+2
fig1,ax=plt.subplots()
ax.barh(dfm['country_code'], dfm['Production'], color='mediumorchid')
st.pyplot(fig1)

#3
jumlah = []

B1 = st.number_input("Masukkan banyak negara untuk ditampilkan jumlah kumulatifnya = ", min_value= 0, max_value=len(daftarnegara))
for x in list(df_xsl['country_code']):
    if x in listnih2:
        continue
    if x not in listnih2:
        listnih2.append(x)

for x in listnih2 :
    i = df_xsl.loc[df_xsl['country_code'] == x , 'Production'].sum()
    jumlah.append(i)

df2 =pd.DataFrame(list(zip(listnih2,jumlah)), columns=['country_code','jumlah'])
df2 = df2.sort_values(by=['jumlah'], ascending =False)
dft = df2[:B1]
fig2,ax= plt.subplots()
ax.barh(dft['country_code'], dft['jumlah'], color='indigo')
st.pyplot(fig2)

#4
produksi_total = df1[:1].iloc[0]['Production']
country_codes = df1[:1].iloc[0]['country_code']
negara = ("")
region = ("")
subregion = ("")

for x in range(len(df_json)):
    if list(df_json['alpha-3'])[x] == country_codes:
        negara = list(df_json['name'])[x]
        region = list(df_json['region'])[x]
        subregion = list(df_json['sub-region'])[x]

st.markdown(f"Negara dengan total jumlah produksi terbesar pada tahun {T} adalah dibawah ini ")
st.markdown(negara)
st.markdown(country_codes)
st.markdown(region)
st.markdown(subregion)
st.markdown(f"dengan produksi sebanyak {produksi_total}")

produksi_total = df2[:1].iloc[0]['jumlah']
country_codes = df2[:1].iloc[0]['country_code']
negara = ("")
region = ("")
subregion = ("")

for x in range(len(df_json)):
    if list(df_json['alpha-3'])[x] == country_codes:
        negara = list(df_json['name'])[x]
        region = list(df_json['region'])[x]
        subregion = list(df_json['sub-region'])[x]
st.markdown("Negara dengan jumlah produksi minyak terbesar secara keseluruhan adalah dibawah ini ")
st.markdown(negara)
st.markdown(country_codes)
st.markdown(region)
st.markdown(subregion)
st.markdown(f"dengan produksi sebanyak {produksi_total}")

#Terkecil
dfkecil=df1[df1.Production !=0]
dfkecil=dfkecil.sort_values(by=['Production'], ascending= True)

produksi_total=dfkecil[:1].iloc[0]['Production']
country_codes =dfkecil[:1].iloc[0]['country_code']
negara = ("")
region = ("")
subregion = ('')

for x in range(len(df_json)):
    if list(df_json['alpha-3'])[x] == country_codes:
        negara = list(df_json['name'])[x]
        region = list(df_json['region'])[x]
        subregion = list(df_json['sub-region'])[x]

st.markdown(f"Negara dengan total jumlah produksi terkecil pada tahun {T} adalah dibawah ini ")
st.markdown(f"   {negara}")
st.markdown(country_codes)
st.markdown(region)
st.markdown(subregion)
st.markdown(f"dengan produksi sebanyak {produksi_total}")

dfjumlahkecil=df2[df2.jumlah !=0]
dfjumlahkecil=dfjumlahkecil.sort_values(by=['jumlah'], ascending= True)

produksi_total=dfjumlahkecil[:1].iloc[0]['jumlah']
country_codes =dfjumlahkecil[:1].iloc[0]['country_code']
negara = ("")
region = ("")
subregion = ('')

for x in range(len(df_json)):
    if list(df_json['alpha-3'])[x] == country_codes:
        negara = list(df_json['name'])[x]
        region = list(df_json['region'])[x]
        subregion = list(df_json['sub-region'])[x]

st.markdown("Negara dengan jumlah produksi minyak terkecil secara keseluruhan adalah dibawah ini ")
st.markdown(negara)
st.markdown(country_codes)
st.markdown(region)
st.markdown(subregion)
st.markdown(f"dengan produksi sebanyak {produksi_total}")

#terakhiran
negaranol =[]
regionol = []
subregionol =[]
dfnol= df1[df1.Production ==0]
for x in range (len(dfnol)):
    for y in range(len(df_json)):
        if list(dfnol['country_code'])[x] == list(df_json['alpha-3'])[y] :
            negaranol.append(list(df_json['name'])[y])
            regionol.append(list(df_json['region'])[y])
            subregionol.append(list(df_json['sub-region'])[y])
dfnol['country'] = negaranol
dfnol['region'] = regionol
dfnol['sub-region'] = subregionol
dftotalnol= df2[df2.jumlah ==0]
totalnegaranol =[]
totalregionol = []
totalsubregionol =[]
for x in range (len(dftotalnol)):
    for y in range(len(df_json)):
        if list(dftotalnol['country_code'])[x] == list(df_json['alpha-3'])[y] :
            totalnegaranol.append(list(df_json['name'])[y])
            totalregionol.append(list(df_json['region'])[y])
            totalsubregionol.append(list(df_json['sub-region'])[y])
st.dataframe(dfnol)
st.dataframe(dftotalnol)
st.set_option('deprecation.showPyplotGlobalUse', False)
