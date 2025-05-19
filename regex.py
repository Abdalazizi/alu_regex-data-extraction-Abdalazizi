import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'(?:\(\d{3}\)\s?|\d{3}[.-])\d{3}[.-]\d{4}'
    return re.findall(pattern, text)

def extract_credit_card_numbers(text):
    pattern = r'(?:\d{4}[- ]?){3}\d{4}'
    return re.findall(pattern, text)

def extract_time_formats(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)
sample_text = '''
user@example.com
firstname.lastname@company.co.uk
URLs:
https://www.example.comLinks to an external site.
https://subdomain.example.org/pageLinks to an external site.
Phone numbers (various formats):
(123) 456-7890
123-456-7890
123.456.7890
Credit card numbers:
1234 5678 9012 3456
1234-5678-9012-3456
Time:
14:30 (24-hour format)
2:30 PM (12-hour format)
HTML tags:
<p>
<div class="example">
<img src="image.jpg" alt="description">
Hashtags:
#example
#ThisIsAHashtag
Currency amounts:
$19.99
$1,234.56
'''

emails = extract_emails(sample_text)
print("-----Emails-----")
for email in emails:
    print(email)
urls = extract_urls(sample_text)
print("-----Urls-----")
for url in urls:
    print(url)
phone_numbers = extract_phone_numbers(sample_text)
print("-----Phone numbers-----")
for number in phone_numbers:
    print(number)
credit_cards = extract_credit_card_numbers(sample_text)
print("-----Credit Card-----")
for cc in credit_cards:
    print(cc)
times = extract_time_formats(sample_text)
print("-----time-----")
for time in times:
    print(time)
html = extract_html_tags(sample_text)
print("-----Tags-----")
for tag in html:
    print(tag)
hash_tags = extract_hashtags(sample_text)
print("-----Hash Tags-----")
for tag in hash_tags:
    print(tag)
currencies = extract_currency_amounts(sample_text)
print("-----Curency-----")
for curreny in currencies:
    print(curreny)
