from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import urllib

listIP = "https://s3.i02.estaleiro.serpro.gov.br/blocklist/blocklist.txt"
misp_key='Wiz6zuvjSkq7LsyouGqhgzb8qRAv82fja5MNiKmD'
misp_url='https://localhost'
misp_verify_cert = False
list = urllib.request.urlopen(listIP)


misp = ExpandedPyMISP(misp_url, misp_key, misp_verify_cert)
event = MISPEvent()
event.info = "BlockList do  Serpro"
event.analysis = "1"
event.threat_level_id = "1"
event.distribution = "0"
event.add_tag('tlp:amber')
event.add_tag('osint:source-type="block-or-filter-list"')
event.add_tag('admiralty-scale:source-reliability="a"')
event.add_tag('admiralty-scale:information-credibility="1"')




for i in list:  
    ip = str(i.decode("utf-8").replace('\n', ''))


    event.add_attribute('ip-dst', str(ip), comment="Lista de Bloqueio", disable_correlation=False, to_id=True)
event.published = True
event = misp.add_event(event)
