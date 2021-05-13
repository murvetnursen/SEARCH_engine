import io
import re
import requests
import operator
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from bs4 import BeautifulSoup,Comment
from nltk.tokenize import word_tokenize 


def scrape_url(url):
    def sozlukolustur(tumkelimeler):
        kelimesayisi = {}  # sozluk yapisi kullanildi
        for kelime in tumkelimeler:
            if kelime in kelimesayisi:
                kelimesayisi[kelime] += 1
            else:
                kelimesayisi[kelime] = 1
        return kelimesayisi


    def sembolleritemizle(tumkelimeler):
        sembolsuzkelimeler = []
        semboller = "1234567890!@$#%^*()_+{}\"<>?,./;'[]|-–©=Â´`⋅·:°•" + chr(775)  # sayilari da ek olarak cikardim
        for kelime in tumkelimeler:
            for sembol in semboller:
                if sembol in kelime:
                    kelime = kelime.replace(sembol, "")
            if (len(kelime) > 0):
                sembolsuzkelimeler.append(kelime)
        return sembolsuzkelimeler

    tumkelimeler = []
    try: 
        r = requests.get(url)
    except:
        return False

    soup = BeautifulSoup(r.content, "lxml")
    all_text = soup.find("body").text.split(" ")

    for kelimegruplari in all_text:
        #print(kelimegruplari)
        # p etiketine sahip tum kelime gruplarÄ±nÄ± aliyoruz
        icerik = kelimegruplari
        kelimeler = icerik.lower().split()  # lower ile kucuk harfe cevirdik split ile bosluklara gore ayirdik
        en_stops = set(stopwords.words('english'))
        for kelime in kelimeler:
            if kelime not in en_stops:
                tumkelimeler.append(kelime)

    tumkelimeler = sembolleritemizle(tumkelimeler)

    #for kelime in tumkelimeler:
        #print(kelime)  # anahtar kelime oluÅŸturmak iÃ§in

    kelimesayisi = sozlukolustur(tumkelimeler)

    sorted_dict = dict(sorted(kelimesayisi.items(), key=lambda item: item[1], reverse=True))
    first_five_keyword = {keyword: sorted_dict[keyword] for keyword in list(sorted_dict.keys())[:15]} 
    """for key in sorted_dict:
        print(key + ":" + str(sorted_dict[key])) """
    print(first_five_keyword) 
    return sorted_dict

def scrape_url2(url):
    def sozlukolustur(tumkelimeler):
        kelimesayisi = {}  # sozluk yapisi kullanildi
        for kelime in tumkelimeler:
            if kelime in kelimesayisi:
                kelimesayisi[kelime] += 1
            else:
                kelimesayisi[kelime] = 1
        return kelimesayisi


    def sembolleritemizle(tumkelimeler):
        sembolsuzkelimeler = []
        semboller = "1234567890!@$#%^*()_+{}\"<>?,./;'[]|-–©=Â´`⋅·:°•" + chr(775)  # sayilari da ek olarak cikardim
        for kelime in tumkelimeler:
            for sembol in semboller:
                if sembol in kelime:
                    kelime = kelime.replace(sembol, "")
            if (len(kelime) > 0):
                sembolsuzkelimeler.append(kelime)
        return sembolsuzkelimeler

    tumkelimeler = []
     
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    all_text = soup.find("body").text.split(" ")

    for kelimegruplari in all_text:
        #print(kelimegruplari)
        # p etiketine sahip tum kelime gruplarÄ±nÄ± aliyoruz
        icerik = kelimegruplari
        kelimeler = icerik.lower().split()  # lower ile kucuk harfe cevirdik split ile bosluklara gore ayirdik
        en_stops = set(stopwords.words('english'))
        for kelime in kelimeler:
            if kelime not in en_stops:
                tumkelimeler.append(kelime)

    tumkelimeler = sembolleritemizle(tumkelimeler)

    #for kelime in tumkelimeler:
        #print(kelime)  # anahtar kelime oluÅŸturmak iÃ§in

    kelimesayisi = sozlukolustur(tumkelimeler)

    sorted_dict = dict(sorted(kelimesayisi.items(), key=lambda item: item[1], reverse=True))
    first_five_keyword = {keyword: sorted_dict[keyword] for keyword in list(sorted_dict.keys())[:15]} 
    """for key in sorted_dict:
        print(key + ":" + str(sorted_dict[key])) """
    print(first_five_keyword) 
    return first_five_keyword

def scrape_url3(url):
    def sozlukolustur(tumkelimeler):
        kelimesayisi = {}  # sozluk yapisi kullanildi
        for kelime in tumkelimeler:
            if kelime in kelimesayisi:
                kelimesayisi[kelime] += 1
            else:
                kelimesayisi[kelime] = 1
        return kelimesayisi


    def sembolleritemizle(tumkelimeler):
        sembolsuzkelimeler = []
        semboller = "1234567890!@$#%^*()_+{}\"<>?,./;'[]|-–©=Â´`⋅·:°•" + chr(775)  # sayilari da ek olarak cikardim
        for kelime in tumkelimeler:
            for sembol in semboller:
                if sembol in kelime:
                    kelime = kelime.replace(sembol, "")
            if (len(kelime) > 0):
                sembolsuzkelimeler.append(kelime)
        return sembolsuzkelimeler

    tumkelimeler = []
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print("---- ERROR -----")
            print(f"---- ${url} : This Web Site is Not Available  -----")
            return {"soup": False, "sorted_dict": False}
    except:
        return {"soup": False, "sorted_dict": False}

    soup = BeautifulSoup(r.content, "lxml")
    all_text = soup.find("body").text.split(" ")

    for kelimegruplari in all_text:
        #print(kelimegruplari)
        # p etiketine sahip tum kelime gruplarÄ±nÄ± aliyoruz
        icerik = kelimegruplari
        kelimeler = icerik.lower().split()  # lower ile kucuk harfe cevirdik split ile bosluklara gore ayirdik
        en_stops = set(stopwords.words('english'))
        for kelime in kelimeler:
            if kelime not in en_stops:
                tumkelimeler.append(kelime)

    tumkelimeler = sembolleritemizle(tumkelimeler)

    #for kelime in tumkelimeler:
        #print(kelime)  # anahtar kelime oluÅŸturmak iÃ§in

    kelimesayisi = sozlukolustur(tumkelimeler)

    sorted_dict = dict(sorted(kelimesayisi.items(), key=lambda item: item[1], reverse=True))
    first_five_keyword = {keyword: sorted_dict[keyword] for keyword in list(sorted_dict.keys())[:15]}
    """for key in sorted_dict:
        print(key + ":" + str(sorted_dict[key])) """
    print(first_five_keyword)
    return {"soup": soup, "sorted_dict": sorted_dict}

recursive_counter = 1
sorted_dict_list = []


def create_nested_list(limit):
    nested_list = []
    for i in range(limit):
        nested_list.append([])
    return nested_list

def get_all_links(soup, current_url):
    all_links = []
    for a_item in soup.find_all('a', href=True):
        link = a_item["href"]
        if link.startswith("http") and current_url[:15] not in link:
            all_links.append(link)
    return all_links


def recursive_scrapper(input_url_list):
    layer_limit = 3
    layer = 0
    url_nested_list = create_nested_list(layer_limit)
    url_nested_list[0] = input_url_list

    data_dict = {}
    for url_list in url_nested_list:
        if layer == layer_limit:
            break
        for url in url_list:
            scrape_url_response = scrape_url3(url)
            if not scrape_url_response.get("sorted_dict"):
               continue 
            word_list = list(scrape_url_response.get("sorted_dict").keys())
            data_dict[url] = word_list
            if not layer == layer_limit-1:
                url_nested_list[layer+1] += get_all_links(scrape_url_response.get("soup"), url)[:3] #1 siteden 3 link donuyor

        layer += 1

    return data_dict



def semantik(first_url,second_url):
    semantik_first_list = list(scrape_url2(first_url).keys())
    semantik_second_list =list(scrape_url2(second_url).keys())
    return find_similarity(semantik_first_list,semantik_second_list)


def find_similarity(first_list, second_list):
    similar_dict = {}
    for first_word in first_list:
        for second_word in second_list:
            word_from_first_list = wordnet.synsets(first_word)
            word_from_second_list = wordnet.synsets(second_word)
            if word_from_first_list and word_from_second_list:
                similarity_rate = word_from_first_list[0].wup_similarity(word_from_second_list[0])
                if similarity_rate and similarity_rate > 0.65:
                    if similar_dict.get(first_word):
                        similar_dict[first_word].append(second_word)
                    else:
                        similar_dict[first_word] = [second_word]
    print(similar_dict)
    return similar_dict
