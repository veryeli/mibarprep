case_codes = {
    'Cole': """Cole v Cole, 289 Mich 202 (1939)""",
    'Grosberg': """Grosberg v Michigan Nat Bank Oakland, 113 Mich App 610 (1982)""",
    'Falkner': """Falkner v Falkner, 24 Mich App 633 (1970)""",
    'Lobato': """Lobato v Paulino, 304 Mich 668 (1943)""",
    'Byker': """Byker v Mannes, 465 Mich 637 (2002)"""
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
        "449.7(4)"),
    ("""However, the statute also lays out several exceptions to the "prima facie evidence" rule.
        It states that no inference of partnership is drawn if the profits were received
        if in payment "[a]s a debt by installments or otherwise,".""", "MCL 449.7(4)(a)")

    ],
 }