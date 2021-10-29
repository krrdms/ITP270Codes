import re

emailHeaders_ = ["X-Sieve: CMU Sieve 2.3",
                 "X-DSPAM-Result: Innocent \n",
                 "X-DSPAM-Confidence: 0.8475 \n",
                 "X-Content-Type-Message-Body: text/plain \n"]

matchPatterns_ = ["^X.*", "^X.\S*", "^X.\S+"]


def altApproach(matchPatterns, emailHeaders):
    # another approach - capture the headers into a dictionary
    headerDict = dict()
    for mP in matchPatterns:
        for header in emailHeaders:
            validHeader = re.match(mP, header)
            if validHeader:
                headerParts = header.split(":")
                headerDict[headerParts[0].strip()] = headerParts[1].strip()

    for key, value in headerDict.items():
        print("[", key, "]", value)
    print("-------")
    return headerDict


def main():
    altApproach(matchPatterns_, emailHeaders_)


if __name__ == '__main__':
    main()
