from jinja2 import Environment, FileSystemLoader
from rules import case_codes, rules_from_essays
from collections import Counter, defaultdict
from jinja_markdown import MarkdownExtension


env = Environment(loader=FileSystemLoader(''))
env.add_extension(MarkdownExtension)
template = env.get_template('index_generator.html')


coded = [
    {'Agency': ['F1910', 'J1815', 'F2014', 'J1602', 'F1602']}, 
    {'Choice of Law': ['F1605', 'J1908', 'J1809', 'F1703', 'F1805']}, 
    {'Civ Pro': ['F1603', 'J1212', 'J2004', 'F1411', 'J1512', 'F1502', 'J1805', 'J1414', 'J0902', 'F0902', 'F1303', 'J1715', 'J1001', 'F1903', 'F1808', 'F1001', 'F1715', 'F1103', 'F2004', 'J1912', 'F1207', 'J1603', 'J1302']}, 
    {'Con Law': ['J1508', 'F1712', 'J1406', 'F1013', 'J2003', 'J1914', 'J1112', 'F1310', 'F1611', 'J1208', 'J0905', 'F1905', 'F1406', 'J1312', 'F1214', 'J1006', 'J1614', 'F2009', 'J1810', 'F1813', 'F1507', 'F1105']}, 
    {'Contracts': ['F1801', 'F1211', 'J1904', 'F1114', 'F1911', 'F1006', 'F1607', 'J1703', 'F0914', 'F2013', 'F1505', 'F1306', 'J1814', 'J1504', 'F1404', 'J1404', 'J2014', 'J1015', 'J1204', 'J1104', 'J1306', 'J1604', 'F1707']}, 
    {'Corporations': ['F1412', 'F1902', 'F1809', 'J1910', 'F2005', 'J1102', 'F1302', 'J1511', 'F1102', 'F1209', 'J1008', 'J1210', 'J1413', 'J2010', 'F0913', 'J0912', 'J1303', 'J1714', 'J1804', 'F1503', 'F1003']}, 
    {"Creditors' Rights": ['F1708', 'F1802', 'J1701', 'J1905']}, 
    {'Crim Pro': ['F1015', 'J1812', 'F1509', 'J1310', 'J1913', 'F1215', 'F1612', 'J0906', 'J1613', 'F2007', 'J1509', 'J1403', 'J1004', 'F1403', 'F1815', 'J1209', 'J2012', 'F1106', 'F0905', 'F1304', 'J1111', 'F1711', 'J1704', 'F1904']}, 
    {'Criminal Law': ['F0906', 'F1104', 'F1401', 'F1710', 'J1207', 'J1615', 'J1915', 'F1610', 'J1401', 'J0904', 'F2008', 'J1706', 'J1311', 'F1906', 'J1110', 'J1507', 'F1213', 'F1508', 'F1311', 'J2015', 'F1814', 'J1005', 'F1014', 'J1811']}, 
    {'Domestic Relations': ['J1407', 'F2001', 'J1607', 'J1011', 'J1515', 'F1413', 'F1806', 'F1701', 'J1712', 'J1114', 'F1112', 'F1204', 'F1315', 'F1514', 'J1808', 'F1606', 'J0909', 'F1915', 'J1909', 'J1213', 'F0907', 'J2009', 'J1315']}, 
    {'Equity': ['F2002', 'F1913', 'F1008', 'J1209', 'J1609', 'J2001', 'J1710']}, 
    {'Evidence': ['F1115', 'J1702', 'F0904', 'F1402', 'J1505', 'J1813', 'J1606', 'F1212', 'F1912', 'F1609', 'F2015', 'F1312', 'J1305', 'F1803', 'J2011', 'J1106', 'F1506', 'J0901', 'J1402', 'J1906', 'J1014', 'F0901', 'J1206', 'F1709', 'F1005']}, 
    {'Negotiable Instruments': ['J1907', 'F1009']}, 
    {'No-Fault': ['F1002', 'J1103', 'J1705', 'J1601', 'J1415']}, 
    {'Partnership': ['F1713', 'J1101']}, 
    {'Personal Property': ['F1407', 'F1309', 'F2011', 'J1707', 'J1410', 'J1501', 'F1615', 'J1308', 'J2006', 'F1511', 'F1907', 'F1201', 'F1810', 'J1107', 'J1803', 'J1610', 'F1012', 'F1109', 'J1009', 'J0914', 'J1202', 'F0910', 'F1704', 'J1901']}, 
    {'Prof Responsibility': ['F1608', 'J1405', 'F1004', 'F1305', 'J1605', 'J0910', 'J1013', 'J1304', 'F1405', 'J1506', 'F1504', 'F0915', 'F1210', 'F1113', 'J1105', 'J1205']}, 
    {'Real Property': ['J0915', 'J1412', 'F1811', 'F1107', 'F0911', 'J1503', 'J1007', 'J2002', 'J1307', 'J1109', 'J1802', 'J1902', 'J1203', 'F1011', 'F1307', 'J1709', 'F1706', 'F1202', 'F1512', 'F1909', 'F1408', 'J1612', 'F1613', 'F2012']}, 
    {'Sales': ['J1113', 'J1807', 'F1513', 'J1514', 'F1111', 'J0911', 'J1314', 'J2005', 'J1214', 'J1608']}, 
    {'Secured Trans': ['F1205', 'F1314', 'F1414', 'F1604', 'F0908', 'J1711']}, 
    {'Torts': ['F1515', 'J1510', 'J1911', 'J1301', 'J1713', 'F1501', 'J1211', 'F1101', 'J2007', 'F1714', 'F1807', 'F1301', 'F1901', 'J1806', 'F1410', 'J1002', 'F0903', 'F2006', 'F1601']}, 
    {'Trusts': ['F1409', 'J1502', 'J1201', 'F1308', 'F1812', 'J2008', 'F1203', 'F1108', 'J1309', 'F1208', 'J1409',]}, 
    {'Wills': ['F1614', 'F1705', 'F1510', 'J1708', 'J1903', 'J1003', 'J0913', 'J1611', 'J1108', 'F2010', 'J1411', 'F1010', 'F0912', 'F1908', 'J1801']}, 
    {"Workers' Comp": ['F1804', 'F1415', 'J1513', 'F0909', 'F1702', 'F1313', 'J1010', 'J1408', 'J2013', 'J1215', 'J1313', 'F1110', 'F1007', 'F1914', 'J0908', 'J1115', 'F1206', 'F2003']}]


slugs = {k[0]: k[0].lower().replace(' ', '-').replace("'", '') for k in [[_ for _ in _.keys()] for _ in coded]}

def url_for(essay):
    return 'pdfs/' + essay + '.pdf'

def name_of(essay):
    month = 'Feb' if essay[0] == 'F' else 'Jul'
    year = '20' + essay[1:3]
    return month + ' ' + year

def sort_key(essay):
    month = 'Feb' if essay[0] == 'F' else 'Jul'
    year = '20' + essay[1:3]
    return year + ('2' if month == 'Feb' else '7')

def get_render_info(item):
    res = {}
    res['link'] = url_for(item)
    res['analysis'] = 'pdfs/' + item + 'A.pdf'
    res['test_name'] = name_of(item)
    res['sortkey'] = sort_key(item)
    return res



topics = []
for item in coded:
    for k, v in item.items():
        topic = {}
        topic['topic'] = k
        topic['slug'] = slugs[k]
        topic['links'] = []
        for item in v:
            topic['links'].append(get_render_info(item))
        topic['links'].sort(key=lambda x: x['sortkey'])
    topics.append(topic)



output_from_parsed_template = template.render(topics=topics)

# to save the results
with open("index.html", "w") as fh:
    fh.write(output_from_parsed_template)

topic_render = {}
for item in coded:
    topic = [_ for _ in item.keys()][0]
    tests = item[topic]
    topic_render['topic'] = topic


    # assemble rules
    rules = []
    coded_so_far = []
    source_accumulator = defaultdict(set)
    source_numberer = {}
    numbers = []
    for essay in rules_from_essays:
        if essay in tests:
            coded_so_far.append({'test': name_of(essay), 'url': url_for(essay)})
            rules += rules_from_essays[essay]
            rule_accumulator = Counter([_[0] if type(_) == tuple else _ for _ in rules])
            for rule in rules:
                if type(rule) == str:
                    continue
                for source in rule[1:]:
                    source = case_codes.get(source, source)
                    if source not in source_numberer:
                        source_numberer[source] = len(source_numberer)
                    source_accumulator[rule[0]].add(source_numberer[source])

    template = env.get_template('topic_generator.html')
    rules = [{'rule': r[0],
            'sources': [
            {
                'num': _,
                'slug': '#num%03d' % _
            }
            for _ in
            source_accumulator[r[0]]
            ]
    } if type(r) == tuple else

    {
        'rule': r,
        'sources': []
    }
    for r in rules]
    numbers = [(v, k) for k, v in source_numberer.items()]
    numbers.sort()
    numbers = [{'slug': 'num%03d' % _[0], 'text': _[1], 'num': _[0]} for _ in numbers]

    # get outlines
    try:
        with open("%s-outline.html" % slugs[topic]) as f:
            print("Found: %s-outline.html" % slugs[topic])
            outline = f.read()
    except IOError:
        try:
            with open("%s-outline.md" % slugs[topic]) as f:
                outline = f.read() 
                print("Found: %s-outline.md" % slugs[topic])   
        except IOError:    
            print("File not accessible: %s-outline.md" % slugs[topic])
            outline = ""


    output_from_parsed_template = template.render(
        topic=topic, outline=outline, rules=rules, sources=numbers,
        coded_so_far=coded_so_far)
    with open(slugs[topic] + '.html', 'w') as fh:
        fh.write(output_from_parsed_template)

