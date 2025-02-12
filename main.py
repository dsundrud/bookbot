def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return (file_contents)
def word_count(work):
    x = work.split()
    return len(x)

def char_count(work):
    ans = {}
    for i in work:
        for j in i:
            if j in ans:
                ans[j] += 1
            else:
                ans[j] = 1
    return ans

def report(work):
    for key, value in work.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

work = main()
work2 = work.lower()
sorted= dict(sorted(char_count(work2).items()))

report(sorted)

