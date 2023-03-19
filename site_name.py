def link(url):
    return url[8:len(url)-5]

site_list=[
    "https://example.org/",
    "https://duckduckgo.com/",  
    "https://facebook.com/"
]
 
for site_url in site_list:
    print(f"{link(site_url)} : {site_url}")



