# D0rkFind3r
D0rkFind3r is a tool designed to automate web reconnaissance tasks through open-source intelligence (OSINT) searches. With it, we can obtain fast and reliable results, as it verifies whether the website we are searching for is functional before returning a result.

To use the tool, we will need a Google API_KEY and a custom search engine to prevent Google from blocking us if we make too many requests.

In the "dorks" file, there are some entries already created, but it can be extended as long as "target.com" (with the quotes) appears, as the script will replace that with the URL you provide when prompted by the script.

Additionally, we can populate the "dorks" file with custom searches by simply changing the "target.com" attribute.

# Screenshots of the tool

![image](https://github.com/user-attachments/assets/02ebb69d-7673-4a95-9a87-d9f78a25c830)

# ________________________________________________________________________

![image](https://github.com/user-attachments/assets/3384ff7e-dd6a-435c-9117-855bf1cd7687)

# How to use it

**- The first step is to execute the script**
`python3 d0rkfind3r.py`

**- Later, the script, will ask you what is the file where the dorks are located**
`Write the file name .txt (add the path if necesarry): dorks.txt`

**- Finally, you have to write the url that you want to search**
`Enter a URL that will replace 'target.com': url.com`


