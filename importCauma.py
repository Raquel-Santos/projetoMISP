from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import urllib

listUrl = "https://cauma.pop-ba.rnp.br/feed/txt"
misp_key='<misp_key>'
misp_url='<misp_url>'
misp_verify_cert = False
list = urllib.request.urlopen(listUrl)


misp = ExpandedPyMISP(misp_url, misp_key, misp_verify_cert)
event = MISPEvent()
event.info = "Feed urls CAUMA"
event.analysis = "1"
event.threat_level_id = "1"
event.distribution = "0"
event.add_tag('tlp:amber')
event.add_tag('admiralty-scale:source-reliability="a"')
event.add_tag('admiralty-scale:information-credibility="1"')
event.add_tag('CERT-XLM:information-gathering="social-engineering"')
event.add_tag('CERT-XLM:fraud="phishing"')
event.add_tag('CERT-XLM:malicious-code="virus"')
event.add_tag('CERT-XLM:malicious-code="trojan-malware"')
event.add_tag('phishing:techniques="fake-website"')
event.add_tag('phishing:techniques="email-spoofing"')
event.add_tag('malware_classification:malware-category="Virus"')
event.add_tag('malware_classification:malware-category="Trojan"')
event.add_tag('circl:incident-classification="phishing"')
event.add_tag('circl:incident-classification="malware"')


for i in list:  
    url = str(i.decode("utf-8").replace('\n', ''))


    event.add_attribute('url', str(url), comment="Feed Urls", disable_correlation=False, to_id=True)
event.published = True
event = misp.add_event(event)
