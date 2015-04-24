'''
legisletters: collect, archive, and make searchable legislators' letters
'''

import re

ES_INDEX_NAME = 'legisletters'
ES_LETTER_DOC_TYPE = 'letter'
ES_RAW_DOC_TYPE = 'raw_letter'
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'
}
LETTER_IDENTIFIERS = [
    'full text of the letter',
    'full text is below',
    'text of the full letter'
]
END_RECIPIENTS_RE = re.compile(r'(>dear[^:,<]+[^:<]|>to the[^:,<]+[^:<])', re.IGNORECASE)
END_TEXT_RE = re.compile(r'(sincerely|thank you[\w\s]*for your|look forward to[\w\s]*reply|respectfully yours)([^:,<]*)', re.IGNORECASE)
END_SIGNATURES_RE = re.compile(r'###|<footer|<script|-\d+-', re.IGNORECASE)
