
#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = pd.read_csv("persona.csv")

df.head()
df.info()
df.size
df.describe().T
df.shape

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].value_counts()
df["PRICE"].nunique()

df["PRICE"].sort_values(ascending=False).head()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()
#ikinci olarak
df.groupby("COUNTRY").agg({"PRICE": "count"})

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY").agg({"PRICE": "sum"})
#veya ikinci yol
df["COUNTRY"].value_counts()

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?

df.groupby("SOURCE").agg({"PRICE": "count"})
#veya ikinci yol
df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg({"PRICE": "mean"})


# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})


# Bonus- Visualization Barplots

fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(11, 9))

sns.barplot(x='SEX', y='PRICE', hue='SOURCE', data=df, ax=axis1)
axis1.set_title('Sex vs Price Source Comparison')

sns.barplot(x='SEX', y='PRICE', hue='COUNTRY', data=df, ax=axis2)
axis2.set_title('Sex vs Price Country Comparison')

plt.show(block=True)

fig, qaxis = plt.subplots(1, 2, figsize=(11, 9))

sns.barplot(x = 'SEX', y = 'PRICE', hue = 'COUNTRY', data=df, ax = qaxis[0])
qaxis[0].set_title('Sex vs Price Country Comparison')

sns.barplot(x = 'SEX', y = 'PRICE', hue = 'AGE_CAT', data=df, ax  = qaxis[1])
qaxis[1].set_title('Sex vs Price Age_Cat Comparison')
plt.show(block=True)

fig, (axis1, axis2, axis3) = plt.subplots(1, 3, figsize=(11, 9))

sns.barplot(x='SEX', y='PRICE', hue='SOURCE', data=df, ax=axis1)
axis1.set_title('Sex vs Price Source Comparison')

sns.barplot(x='SEX', y='PRICE', hue='COUNTRY', data=df, ax=axis2)
axis2.set_title('Sex vs Price Country Comparison')

sns.barplot(x="SEX", y="PRICE", hue="AGE_CAT", data=df, ax=axis3)
axis3.set_title("Sex vs Price Age_Cat Comparison")

plt.show(block=True)


#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})


#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

selected = ["COUNTRY", "SOURCE", "SEX", "AGE"]
new_df = df.groupby(selected).agg({"PRICE": "mean"})
agg_df = new_df.sort_values(by="PRICE", ascending=False)


#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df.reset_index(inplace=True)

#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

agg_df["AGE_CAT"] = pd.cut(df["AGE"], [0, 18, 23, 30, 40, 70], labels=['0_18', '19_23', '24_30', '31_40', '41_70'])


#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df["customer_level_based"] = [(country + "_" + source + "_" + sex + "_" + age_cat).upper() for country, source, sex, age_cat in zip(agg_df["COUNTRY"], agg_df["SOURCE"], agg_df["SEX"], agg_df["AGE_CAT"])]
agg_df.apply(lambda x: x.astype(str).str.upper())
df["AGE"] = df["AGE"].astype(str)
df["AGE"].dtype
df["AGE"].astype(str).str.upper()
agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})
agg_df.reset_index(inplace=True)
agg_df.head()

#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user]

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

new_user_2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customer_level_based"] == new_user_2]