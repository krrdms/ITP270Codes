import re

emailHeaders_ = ["X-Sieve: CMU Sieve 2.3",
                 "X-DSPAM-Result: Innocent \n",
                 "X-DSPAM-Confidence: 0.8475 \n",
                 "X-Content-Type-Message-Body: text/plain \n"]

matchPatterns_ = ["^X.*", "^X.\S*", "^X-DSPAM.\S+"]


def slide1012(matchPatterns, emailHeaders):
    for mP in matchPatterns:
        print("MP:", mP)
        for header in emailHeaders:
            hits = re.findall(mP, header)
            for hit in hits:
                print(hits)
        print("-------")
    return hits


def main():
    slide1012(matchPatterns_, emailHeaders_)


if __name__ == '__main__':
    main()
