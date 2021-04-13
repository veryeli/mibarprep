from jinja2 import Environment, FileSystemLoader
from rules import case_codes, rules_from_essays
from collections import Counter, defaultdict
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('index_generator.html')


coded = [
{"Agency": ['F2014', 'F1602', 'F1910', 'J1602', 'J1815']},
{"Civ Pro": ['J1512',
 'J1603',
 'F1603',
 'F1808',
 'F1903',
 'F2004',
 'J1912',
 'J2004',
 'J1805',
 'F1715',
 'J1715',
 'F1502']},
{"Negotiable Instruments": ["J1907"]},
{"Choice of Law": ['F1805', 'J1809', 'J1908', 'F1605', 'F1703']},
{"Con Law": ['J1914',
 'F1507',
 'F1712',
 'J1508',
 'J1614',
 'F1905',
 'F1611',
 'F1813',
 'F2009',
 'J1810',
 'J2003']},
{"Contracts": ['F1505',
 'J1504',
 'F1707',
 'J1703',
 'F1607',
 'F1801',
 'F1911',
 'F2013',
 'J1604',
 'J1814',
 'J1904',
 'J2014']},
{"Corporations": ['F1503',
 'F1809',
 'F1902',
 'F2005',
 'J1511',
 'J1714',
 'J1804',
 'J1910',
 'J2010']
},
{"Creditors' Rights": ['F1708', 'F1802', 'J1701', 'J1905']},
{"Criminal Law": ['F1508',
 'F1610',
 'F1710',
 'F1814',
 'F1906',
 'F2008',
 'J1507',
 'J1706',
 'J1811',
 'J1915',
 'J2015']},
{"Crim Pro": ['F1612',
 'F1815',
 'F1904',
 'F2007',
 'J1615',
 'J1812',
 'J1913',
 'J2012',
 'J1704', 'F1509', 'F1711', 'J1509', 'J1613']},
{"Domestic Relations": ['F1514',
 'F1606',
 'F1701',
 'J1515',
 'F1915',
 'F2001',
 'J1909',
 'J2009',
 'F1806',
 'J1712',
 'J1808',
 'J1607']},
{"Equity": ['J1609', 'F1913', 'F2002', 'J1710', 'J2001']},
{"Evidence": ['F1709',
 'F1506',
 'F1609',
 'F1803',
 'F1912',
 'F2015',
 'J1505',
 'J1606',
 'J1702',
 'J1813',
 'J1906',
 'J2011']},
{"No-Fault": ["J1705", "J1601"]},
{"Partnership": ["F1713"]},
{"Personal Property": ['J1610',
 'F1511',
 'F1615',
 'F1704',
 'J1501',
 'J1707',
 'F1810',
 'F1907',
 'F2011',
 'J1803',
 'J1901',
 'J2006']},
{"Prof Responsibility": ['F1504', 'F1608', 'J1506', 'J1605']},
{"Real Property": ['F1512',
 'F1613',
 'F1706',
 'J1503',
 'J1709',
 'F1811',
 'F1909',
 'F2012',
 'J1802',
 'J2002',
 'J1902',
 'J1612']},
{"Sales": ['F1513', 'J1514', 'J1608', 'J1807', 'J2005']},
{"Secured Trans": ["F1604", "J1711"]},
{"Torts": ['J1510',
 'F1501',
 'F1601',
 'F1714',
 'F1515',
 'F1807',
 'F1901',
 'F2006',
 'J1713',
 'J1806',
 'J1911',
 'J2007']},
{"Trusts": ['J1502', 'J2008', 'F1812']},
{"Wills": ['F1614',
 'F1510',
 'F1705',
 'F1908',
 'F2010',
 'J1611',
 'J1708',
 'J1801',
 'J1903']},
{"Workers' Comp": [
    "J1513",
    "F1804",
    "F1702",
    "F1914",
    "F2003",
    "J2013",
]},
]


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
    } for r in rules]
    numbers = [(v, k) for k, v in source_numberer.items()]
    numbers.sort()
    numbers = [{'slug': 'num%03d' % _[0], 'text': _[1], 'num': _[0]} for _ in numbers]

    output_from_parsed_template = template.render(
        topic=topic, rules=rules, sources=numbers,
        coded_so_far=coded_so_far)
    with open(slugs[topic] + '.html', 'w') as fh:
        fh.write(output_from_parsed_template)





# for each topic
# for each case in rules
# if the case is in the topic
# count the number of time each rule occurs
# for each number in the count
#
#
