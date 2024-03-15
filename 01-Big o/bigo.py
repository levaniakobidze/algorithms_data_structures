def print_items(n):
    for i in range(n):
        print(i)
  
print_items(10)

# ამ ფუნქციის time complexity არის O(n). ფუნქციის შესრულების დრო პროპორციულად იზრდება ინფუთის ზრდასთან ერთად.

# ////////////////////

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
  
print_items(10)

# ამ ფუნქციაში ყოველი i - ს დატირალებისას j - n - ჯერ მეორდება ანუ ამ შემთხვევაში 10 - ჯერ. საერთო ჯამში 10 * 10.
# გამეორება მოხდება ანუ სულ 100 - ი.
# შიგნითა ლუპის გამეორებების რაოდენობა იქნება n * n რაც ნიშნავს n². ანუ ამ ფუნქციის დროითი კომპლექსურობა
# time complexity იქნება O(n²)


def print_items(n):
    print(n + n)
  
print_items(10)
# ამ ფუნქციის time complexity არის O(1)
