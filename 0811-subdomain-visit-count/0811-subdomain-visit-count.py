class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        site_visits = {}

        for domain in cpdomains:
            hits_and_domain = domain.split()
            hits = int(hits_and_domain[0])
            domain_name = hits_and_domain[1].split(".")

            website = ""
            while domain_name:
                if website:
                    website = "." + website

                sub_domain = domain_name.pop()
                website = sub_domain + website

                site_visits[website] = site_visits.get(website, 0) + hits

        ans = []
        for domain, hits in site_visits.items():
            cpdomain_str = f"{hits} {domain}"
            ans.append(cpdomain_str)

        return ans
