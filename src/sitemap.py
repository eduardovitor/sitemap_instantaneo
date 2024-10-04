from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET


def check_associated_pages(text_link):
    if text_link.find("https")!=-1 or text_link.find("http")!=-1:
        return True
    return False


def scrapy_subpages(target_url):
    doc_html = requests.get(target_url)
    soup_html = BeautifulSoup(doc_html.content, "html.parser")
    links = soup_html.find_all("a")
    links_indesejados = ["","/","#"]
    links_finais = []
    for link in links:
        if link.get("href") is not None: 
            if link.get("href") not in links_indesejados and not check_associated_pages(link.get("href")):
                links_finais.append(link.get("href"))
    return set(links_finais)


def add_first_link(target_url):
    url = ET.Element("url")
    loc = ET.SubElement(url,"loc")
    loc.text = target_url
    return url


def generate_xml(filename, links, target_url):
    root = ET.Element("urlset")
    root.set("xmlns","http://www.sitemaps.org/schemas/sitemap/0.9")
    root.append(add_first_link(target_url))
    for link in links:
        url = ET.Element("url")
        loc = ET.SubElement(url,"loc")
        loc.text = f"{target_url[0:-1]}{link}"
        root.append(url)
    tree = ET.ElementTree(root)
    with open(filename,"wb") as file:
        tree.write(file,encoding="utf-8",xml_declaration=True)
