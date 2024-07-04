from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import urllib

listUrl = "https://openphish.com/feed.txt"
misp_key='Wiz6zuvjSkq7LsyouGqhgzb8qRAv82fja5MNiKmD'
misp_url='https://localhost'
misp_verify_cert = False
list = urllib.request.urlopen(listUrl)


misp = ExpandedPyMISP(misp_url, misp_key, misp_verify_cert)
event = MISPEvent()
event.info = "Feed urls OpenPhish"
event.analysis = "1"
event.threat_level_id = "1"
event.distribution = "0"
event.add_tag('tlp:amber')
event.add_tag('admiralty-scale:source-reliability="a"')
event.add_tag('admiralty-scale:information-credibility="1"')
event.add_tag('CERT-XLM:information-gathering="social-engineering"')
event.add_tag('CERT-XLM:fraud="phishing"')
event.add_tag('phishing:techniques="fake-website"')
event.add_tag('circl:incident-classification="phishing"')



for i in list:  
    url = str(i.decode("utf-8").replace('\n', ''))


    event.add_attribute('url', str(url), comment="Feed Urls", disable_correlation=False, to_id=True)
event.published = True
event = misp.add_event(event)
