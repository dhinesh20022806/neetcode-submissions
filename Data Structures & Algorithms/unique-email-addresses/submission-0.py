class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        uniqueEmails = set()


        for email in emails:
            localName, domainName = email.split('@')
            splitPlus = localName.split('+')
            cleanedLocalName = "".join(splitPlus[0].split('.'))
            uniqueEmails.add(cleanedLocalName + "@" + domainName)

        return len(uniqueEmails)