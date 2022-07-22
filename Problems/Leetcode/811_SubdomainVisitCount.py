import collections


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        Time complexity:
            - We need to process each domain in cpdomains => O(N)
                - All the splitting and framenting of each domain in cpdomains
                is a constant operation. As lenth of a fragmented domain is
                atmost 3  (per description)
            - Total: O(N) * O(1) => O(N)

        Space complexity:
            - Counts dictionary has cpdomains input => O(N)
                - Even though we are splitting every domain in cpdomains, the
                maximum pieces we can split is atmost 3
            - Total: O(N * 3) => O(N)
        """

        counts = collections.defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            fragments = domain.split('.')
            for i in range(len(fragments)):
                counts['.'.join(fragments[i:])] += count
        return [" ".join((str(count), domain)) for domain, count in counts.items()]
