case_codes = {
    'Allard': """Allard v Allard, 318 Mich App 583 (2017)""",
    'Byker': """Byker v Mannes, 465 Mich 637 (2002)""",
    'Central Wholesale': """Central Wholesale Co v Sefa, 351 Mich 17 (1957)""",
    'Cole': """Cole v Cole, 289 Mich 202 (1939)""",
    'Dumas': """Dumas v Auto Club Ins Ass’n, 437 Mich 521 (1991)""",
    'Eastman': """Eastman v Univ of Mich, 30 F3d 670 (CA 6, 1994)""",
    'Falkner': """Falkner v Falkner, 24 Mich App 633 (1970)""",
    'Farm Bureau': """Farm Bureau Ins Co v TNT Equip, Inc, 328 Mich App 667 (2019)""",
    'Grosberg': """Grosberg v Michigan Nat Bank Oakland, 113 Mich App 610 (1982)""",
    'Hertz': """Hertz Corp v Friend, 559 US 77 (2010)""",
    'Ingham': """Co of Ingham v Mich Co Rd Comm’n Self-Insurance Pool, 329 Mich App 295, ___ (2019)""",
    'Kisiel': """Kisiel v Holz, 272 Mich App 168 (2006)""",
    'Krause': """Krause v Boraks, 341 Mich 149 (1954)""",
    'Koenig': """Koenig v City of South Haven, 460 Mich 667 (1999)""",
    'LeBlanc': """LeBlanc v Cleveland, 248 F3d 95 (CA 2, 2001).""",
    'Lobato': """Lobato v Paulino, 304 Mich 668 (1943)""",
    'Logan': """Logan v Manpower of Lansing, Inc, 304 Mich App 550 (2014)""",
    'Maids': """Maids Int’l, Inc v Saunders, Inc, 224 Mich App 508 (1997)""",
    'Meretta': """ Meretta v Peach, 195 Mich App 695 (1992)""",
    'Mitchell': """Mitchell v US, 88 US 350 (1874)""",
    'Peeples': """Peeples v City of Detroit, 99 Mich App 285 (1980)""",
    'Rehab': """Prof Rehab Assocs v State Farm Mut Auto Ins Co, Mich App 167 (1998)""",
    'Rory': """Rory v Continental Ins Co, 473 Mich 457 (2005)""",
    'Schmalfeldt': """Schmalfeldt v North Pointe Ins Co, 469 Mich 422 (2003)""",
    'Shay': """Shay v Aldrich, 487 Mich 648 (2010)""",
    'St Paul': """St Paul Mercury Indemnity Co v Red Cab Co, 303 US 283 (1938)""",
    'Von Dunser': """Von Dunser v Aronoff, 915 F2d 1071 (CA 6, 1990)""",
}


rules_from_essays = {
 'F1713': [
    ("""A partnership is an association of two or more persons to be the co-owners of a business for profit.""",
        "MCL 449.6(1)"),
    ("""In determining whether a partnership exists, the primary question is "whether the parties intentionally acted as co-owners of a business for
    profit, and not on whether they consciously intended to create the legal relationship of 'partner-ship.'" """,
        "Byker"),
    ("""The burden of proof to show a partnership is on the party alleging the partnership.""",
        'Grosberg', 'Falkner'),
    ("""Generally, the party alleging the partnership is required to prove that a partnership exists by a preponderance of the evidence.""",
        'Lobato'),
    ("""Where the alleged partners are <b>relatives</b> the party alleging the partnership is required to prove the existence of the partnership by clear and convincing evidence.""",
        'Grosberg',
        'Falkner',
        'Cole'
        ),
    ("""MCL 449.7 lays out specific rules for determining the existence of partnership.""", "MCL 449.7"),
    ("""The receipt by a person of a share of the profits of a business is prima facie evidence that he is a partner in the business""",
        "MCL 449.7(4)"),
    ("""MCL 449.7(4) lays out several exceptions to the "prima facie evidence" rule.
        It states that no inference of partnership is drawn if the profits were received
        if in payment "[a]s a debt by installments or otherwise,".""", "MCL 449.7(4)(a)")

    ],
    # contracts
    'J2014': [
        ("""Neither law nor
equity will enforce a contract that is in violation of public
policy. Contracts in violation of public policy are void and unenforceable.""", "Krause", "Allard", 'Peeples'),
        ("""Public policy is be found in statutes and when they have not directly spoken, then in the
decisions of the courts and in constitutions""", 'Maids', 'Rory'),
        (""" Under
the doctrine of severability, “[a]n unlawful term in a contract is
severable from the whole unless that term is central to the
parties’ agreement. Hence, the failure of a distinct part of a
contract does not void valid, severable provisions.”""", 'Ingham', 'Rehab'
),
        ("""As a general rule, a contract is entire when, by its
terms, nature and purpose, it contemplates that each and
all of its parts are interdependent and common to one another and to the consideration, and is severable when,
in its nature and purpose, it is susceptible of division
and apportionment.

The singleness or apportionability of the consideration
appears to be the principal test. The question is
ordinarily determined by inquiring whether the contract
embraces one or more subject matters, whether the
obligation is due at the same time to the same person,
and whether the consideration is entire or apportioned.""", 'Dumas'),

        ("""“When the price is expressly
apportioned by the contract . . . to each item to be performed,
the contract will generally be held to be severable.""", 'Dumas'),
        ("""In Michigan, a person who is a nonparty to a contract may
be entitled to sue to enforce the contract as a third-party
beneficiary.""", 'Farm Bureau'),
        ("""Any person for whose benefit a promise is made by way of
contract . . . has the same right to enforce said promise
that he would have had if the said promise had been made
directly to him as the promisee. (1) A promise shall be construed to have been made for
the benefit of a person whenever the promisor of said
promise had undertaken to give or to do or refrain from
doing something directly to or for said person.""", " MCL 600.1405"),
        ("""Not just any person who benefits
from a contract may enforce it. Rather, it states that a person is
a third-party beneficiary of a contract only when the promisor
undertakes an obligation ‘directly’ to or for the person.""", 'Shay', 'Koenig'
),
        ("""Contracting parties must be “clearly
aware that the scope of their contractual undertakings encompasses
a third party, directly referred to in the contract, before the
third party is able to enforce the contract.”""", 'Shay'),
        ("""The standard for
determining whether a person is a third-party beneficiary is an
objective standard and must be determined from the language of the
contract only.""", 'Shay'),
        ("""Only intended beneficiaries, not incidental
beneficiaries, may enforce a contract under 1405. A third person cannot
maintain an action on a simple contract merely because he or she
would receive a benefit from its performance or would be injured
by its breach.""", 'Schmalfeldt', 'Kisiel'),

    ],

    'F2014': [
        (""". An agency is
“a fiduciary relationship created by express or implied contract
or by law, in which one party (the agent) may act on behalf of
another party (the principal) and bind that other party by words
or actions.”""", 'Logan'),
        ("""An agent’s authority to act may be either actual or apparent/ostensible.""",
          'Meretta'),
        (""" “Actual authority may be express or
implied. Implied authority is the authority which an agent believes
he possesses.”""", 'Meretta'),
        ("""Apparent authority may be found “when acts and
appearances lead a third person reasonably to believe that an
agency relationship exists.” While “all
surrounding facts and circumstances” must be considered in
determining whether an agent has apparent authority to engage in
an act that binds the principal, “[a]pparent authority must be
traceable to the principal and cannot be established by the acts
and conduct of the agent.”""", 'Meretta'),
        ("""A  principal
can be estopped from challenging the authority of an agent
[w]henever a principal has placed an agent in such a
situation that a person of ordinary prudence, conversant
with business usages and the nature of the particular
business, is justified in assuming that such agent is
authorized to perform in behalf of the principal the
particular act, and such particular act has been
performed . . . """, 'Meretta', 'Central Wholesale')

    ],
    'J2004': [
        ("""Federal courts are courts of limited
jurisdiction, meaning they can only hear actions authorized by the
United States Constitution or federal statutes."""),
        ("""The two primary
categories of federal subject matter jurisdiction are when (1)
there is a either a federal question asserted in a well-pleaded
complaint that seeks a remedy based on the federal question or (2)
there is complete diversity of jurisdiction, which requires that
the action be between citizens of different states and the amount
in controversy exceeds $75,000. For “complete diversity” to exist,
no plaintiff can be a citizen of the same state of any defendant. """, "28 USC § 1332"),
        ("""When determining an individual’s citizenship, a court will
look to the person’s domicile at the time the action was filed."""),
        (""" A
person can have only one domicile for purposes of diversity
jurisdiction.""", 'Eastman'),
        ("""A previous domicile cannot be lost until another is adequately
established""", 'Mitchell'),
        ("""Establishment
of a new domicile, for diversity jurisdiction purposes, is
determined by two factors: (1) residence in the new domicile, and
(2) intention to remain there.""", 'Von Dunser'),
        ("""Diversity is determined at the time that the action is filed, and
based on the residency of the parties at that time. A change in
domicile by a party after that date does not destroy diversity. """,
'LeBlanc'),
        ("""Unlike an individual, a corporation is a citizen where it is
incorporated and where it has its principal place of business. """, '28 USC § 1332(c)(1)'),
        (""" A corporation’s
“principal place of business” for purposes of federal diversity
jurisdiction refers to “the place where the corporation’s highlevel officers direct, control, and coordinate the corporation’s
activities.” """, 'Hertz'),
        ("""In determining the
amount in controversy, courts will accept the plaintiff’s good
faith allegations as to damages unless it appears to a legal
certainty that the plaintiff cannot recover that amount.""", 'St Paul'),
        (""" Federal courts have
subject matter jurisdiction to hear claims that “arise under” the
Constitution or other federal laws.""", '28 USC § 1331')
    ],





 }