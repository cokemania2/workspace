class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a = set()
        for email in emails:
            email = email.split('@')
            localname = ''.join(email[0].split('+')[0].split('.'))
            domain = email[1]
            a.add(localname+'@'+domain)
        return len(a)
            