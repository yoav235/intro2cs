import copy
import pickle
import sys
import urllib.parse
import bs4
import requests


if sys.argv[1] == "crawl":
    BASE_URL = sys.argv[2]
    INDEX_FILE = sys.argv[3]
    OUT_FILE = sys.argv[4]
elif sys.argv[1] == "page_rank":
    ITERATIONS = sys.argv[2]
    DICT_FILE = sys.argv[3]
    OUT_FILE =  sys.argv[4]
if sys.argv[1] =="words_dict":
    BASE_URL =  sys.argv[2]
    INDEX_FILE = sys.argv[3]
    OUT_FILE = sys.argv[4]
elif sys.argv[1] == "search":
    QUERY = sys.argv[2]
    RANKING_DICT_FILE = sys.argv[3]
    WORDS_DICT_FILE = sys.argv[4]
    MAX_RESULTS = sys.argv[5]



def index_extractor(INDEX_FILE):
    """
    :param INDEX_FILE:
    :return: list of str from the index file
    """
    f = open(INDEX_FILE, "r")
    lst = []
    for line in f:
        strip = line.strip()
        list_strip = strip.split()
        lst.append(list_strip)
    return lst


def html_extractor(url):
    """
    :param url:
    :return: list of all of the links in the url
    """
    href = []
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all('p'):
        for link in p.find_all('a'):
            x = link.get('href')
            href.append(x)
    return href
# ----supporting functions----


def dictionary_constructor(lst_of_keys):
    """
    :param lst_of_keys:
    :return: a dictionary with all of the keys from the list assigned with the default value of 0
    """
    dict = {}
    for key in lst_of_keys:
        dict[key[0]] = 0
    return dict


def num_of_connections_dict(url):
    """
    :param url:
    :return: a dictionary with the keys as names from the index file and the value as number of links referred to every
    name in the index list
    """
    lst = index_extractor(INDEX_FILE)
    dict = dictionary_constructor(lst)
    html = html_extractor(url)
    for target in dict:
        for hit in html:
            if target == hit:
                dict[target] += 1
    return dict


def make_traffic_dict():
    """
    :return: a dictionary with keys as web pages and values as dictionaries of number of references to every name
     in the index file in the key web page
    """
    traffic_dict = {}
    html = html_extractor(BASE_URL)
    index_lst = index_extractor(INDEX_FILE)
    for index in index_lst:
        full_url = urllib.parse.urljoin(BASE_URL, index[0])
        traffic_dict[index[0]] = num_of_connections_dict(full_url)
    return traffic_dict


def reference_removel(traffic_dict):
    copy_dict = copy.deepcopy(traffic_dict)
    for key in traffic_dict:
        for sub_key in traffic_dict[key]:
            if traffic_dict[key][sub_key] == 0:
                copy_dict[key].pop(sub_key)
    return copy_dict


def crawl():
    traffic_dict = make_traffic_dict()
    traffic_dict = reference_removel(traffic_dict)
    with open(OUT_FILE, 'wb') as f:
        pickle.dump(traffic_dict, f)
# ----phase a----


def page_rank():
    traffic_dict = {}
    with open(DICT_FILE, "rb") as f:
        traffic_dict = pickle.load(f)
    dict_points = first_rank_dictionary(traffic_dict, 1)
    dict_defaulet = first_rank_dictionary(traffic_dict, 0)
    for loop in range(int(ITERATIONS)):
        dict_points = iterations(traffic_dict,dict_defaulet,dict_points)
    with open(OUT_FILE, "wb") as f:
        pickle.dump(dict_points, f)


def iterations(traffic_dict, dict_defaulet, point_dict):
    copy_default = copy.deepcopy(dict_defaulet)
    for name in point_dict:
        for page in traffic_dict[name]:
            if not(is_name_there(traffic_dict[page], name)):
                continue
            link_num = sum(traffic_dict[page].values())
            add_points = point_dict[page]*(traffic_dict[page][name]/link_num)
            copy_default[name] += add_points
    return copy_default


def is_name_there(dict, name):
    for key in dict:
        if name == key:
            return True
    return False


def total_num_of_links(traffic_dict, page):
    sum_of_links = 0
    for link in traffic_dict[page]:
        sum_of_links += traffic_dict[page][link]
    return sum_of_links


def first_rank_dictionary(key_list, value):
    return_dict = {}
    for key in key_list:
        return_dict[key] = float(value)
    return return_dict
# ----phase b----


def text_extractor(url):
    text = ""
    full_url = urllib.parse.urljoin(BASE_URL, url)
    response = requests.get(full_url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all('p'):
        text += (p.get_text())
    return text


def words_dict_constructor():
    url_list = dictionary_constructor(index_extractor(INDEX_FILE))
    dict_word = {}
    for page in url_list:
        dict_word[page] = 0
    return dict_word



def total_dict():
    dict_words = words_dict_constructor()
    page_lst = index_extractor(INDEX_FILE)
    dict_total = {}
    for page in page_lst:
        full_url = urllib.parse.urljoin(BASE_URL, page[0])
        for word in text_extractor(full_url).split():
            dict_total[word] = how_much_words(index_extractor(INDEX_FILE), dict_words, word)
    with open(OUT_FILE, "wb") as f:
        pickle.dump(dict_total, f)


def how_much_words(pages, word_dict, word):
    for page in pages:
        html_text = text_extractor(page[0])
        if html_text.count(word) > 0:
            word_dict[page[0]] = html_text.count(word)
    return word_dict
# ----phase c----


def pages_with_query(query):
    query_list = query.split()
    pages_dict = load_pickle(WORDS_DICT_FILE)
    rank_dict = load_pickle(RANKING_DICT_FILE)
    sorted_rank_dict = sort_query(rank_dict, rank_dict)
    page_list = {}
    for page in sorted_rank_dict:
        for q in query_list:
            for word in pages_dict[page]:
                if word == q:
                    page_list[page] = pages_dict[page]
                    break
        if len(page_list) >= int(MAX_RESULTS):
            break
    return page_list


def summed_up_rank(rank_dict, word_dict, query):
    summed_up_rank = {}
    for key in word_dict:
        word = smallest_query(query, key)
        summed_up_rank[key] = rank_dict[key]*word_dict[key][word]
    summed_up_rank = sort_query(summed_up_rank, summed_up_rank)
    return summed_up_rank


def text_storing(dict):
    file = open("results.txt", "a")
    for key, value in dict.items():
        file.write(key + " " + str(value) + "\n")
    file.write("**********\n")
    file.close()





def smallest_query(query, key):
    list_query = query.split()
    dict_word = pages_with_query(query)
    for word in list_query:
        if is_query_in_dict(word, dict_word[key]):
            small_query = word
    for word in list_query:
        if is_query_in_dict(word,dict_word[key]):
            if dict_word[key][word] > dict_word[key][small_query]:
                small_query = word
    return small_query

def is_query_in_dict(word,dict):
    for key in dict:
        if word == key:
            return True
    return False



def sort_query(lst, dict=None):
    return_dict = {}
    sort_lst = sorted(lst, key=lst.get, reverse=True)
    if dict == None:
        for element in sort_lst:
            return_dict[element] = 0
    else:
        for element in sort_lst:
            return_dict[element] = dict[element]
    return return_dict




def query_remover(query):
    query_list = query.split()
    all_words = load_pickle(WORDS_DICT_FILE)
    for q in query_list:
        for key in all_words.values():
            is_there = False
            if is_there:
                break
            for word in key.keys():
                if q == word:
                    is_there = True
                    break
        query_list.remove(q)
    return query_list


def load_pickle(pickl):
    with open(pickl, "rb") as f:
        return pickle.load(f)



if __name__ == "__main__":
    if sys.argv[1] == "crawl":
        crawl()
    elif sys.argv[1] == "page_rank":
        page_rank()
    elif sys.argv[1] == "words_dict":
        total_dict()
    elif sys.argv[1] == "search":
        dict = summed_up_rank(load_pickle(RANKING_DICT_FILE), pages_with_query(QUERY), QUERY)
    #     text_storing(dict)
    # RANKING_DICT_FILE = "page_rank.pickle"
    # QUERY = "Pensieve McGonagall"
    # summed_up_rank(load_pickle(RANKING_DICT_FILE), pages_with_query(QUERY), QUERY)








