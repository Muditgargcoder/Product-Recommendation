import pandas as pd
import json
import math
import tkinter as tk



print("loading data")
with open('ProductTree.json') as f:
    data = json.load(f)
with open('productId.json') as f:
    products = json.load(f)


print("loaded")

print("Press q to quit anytime :) \n")

requiredRecommendations = int(
    input(("Enter Required recommendations(less than 100): ")))
# df = pd.read_excel(r'./ecommerce_sample_dataset.xlsx')
# # dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
# #         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
# #         'score':[90, 40, 80, 98],
# #         'test' : {
# #                 'age' : 3,
# #                 'price' : [1,2,4]

# #             }
# #         }

# limit = 1000
# data = {}
# products = {}
# # df = pd.DataFrame(dict)
# t = 0
# for i in df.itertuples():
#     if(t == 5):
#         break
#     # tree = i.product_category_tree[2:-2].split(" >> ")
#     # print(i)
#     t += 1

# t = 0
# for i in df.itertuples():
#     #uniq_id, crawl_timestamp, product_url, product_name, product_category_tree, pid, retail_price, discounted_price, image,
#     #is_FK_Advantage_product, description, product_rating, overall_rating, brand, product_specifications
#     # if(t == limit):
#     #     break
#     tree = i.product_category_tree[2:-2].split(" >> ")
#     d = data
#     for x in range(len(tree) - 1):
#         if(not d.__contains__(tree[x])):
#             d[tree[x]] = {}

#         d = d[tree[x]]

#     if(not d.__contains__("products")):
#         d["products"] = []
#         d["count"] = 0
#     productData = [i.pid, i.product_name, i.discounted_price, i.brand]
#     j = 0

#     if(str(i.discounted_price) != 'nan'):
#         while(j < d["count"]):
#             if str(i.discounted_price) != 'nan':
#                 j += 1
#                 continue
#             if(i.discounted_price > int(d["products"][j][2])):
#                 j += 1
#             else:
#                 break

#     d["products"] = d["products"][:j] + [productData] + d["products"][j:]
#     d["count"] += 1
#     products[i.pid] = i
#     t += 1


def main():
    def getProducts(direc, x):
        p = []
        stack = [direc[x]]

        while(len(stack) > 0):
            t = stack.pop()
            if(type(t) is int):
                continue
            if(type(t) is list):
                p = p + t
            elif(t.__contains__("products")):
                p = p + t["products"]
            else:

                for x in t.keys():
                    stack.append(t[x])
        return p

    def word2vec(word):
        from collections import Counter
        # count the characters in word
        cw = Counter(word)
        # precomputes a set of the different characters
        sw = set(cw)
        # precomputes the "length" of the word vector
        lw = math.sqrt(sum(c*c for c in cw.values()))
        # return a tuple
        return cw, sw, lw

    # id = 'SRTEH2FVVKRBAXHB'
    while(True):
        id = input("Enter a Product Id: ")
        if(id == "q"):
            exit()
        if(not products.__contains__(id)):
            print("Invalid Id, Enter Again ")
        else:
            product = products[id]
            # print(product)
            # product is a tuple
            brand = product[14]
            price = product[8]
            name = product[4]
            print("Product: ", [brand, name, price, ], "\n")
            print("Recommendations: \n")
            tree = product[5][2:-2].split(" >> ")
            direc = data
            t = len(tree)
            totalProductsGot = 0
            RecommendedProducts = []
            for x in range(t - 1):
                direc = direc[tree[x]]
            RecommendedProducts = RecommendedProducts + direc['products']
            totalProductsGot = direc['count']
            searched = direc
            if(not totalProductsGot >= 50):
                stack = []
                while(True):
                    t -= 1
                    direc = data
                    for x in range(t - 1):
                        direc = direc[tree[x]]

                    # direc = stack.pop()
                    for x in direc.keys():
                        if(direc[x] != searched):
                            # stack.push(direc[x])
                            RecommendedProducts = RecommendedProducts + \
                                getProducts(direc, x)
                    if(len(RecommendedProducts) >= requiredRecommendations*2):
                        break
                    searched = direc

            # Product example
            #   "NKCDWBPZTRZJTVR2": [
            #     4093,
            #     "4bd90b580784743d95f93d764036e0f0",
            #     "2015-12-01 12:40:44 +0000",
            #     "http://www.flipkart.com/voylla-metal-alloy-necklace/p/itmdwbpze8y2gdwe?pid=NKCDWBPZTRZJTVR2",
            #     "Voylla Metal, Alloy Necklace",
            #     "[\"Jewellery >> Necklaces & Chains >> Necklaces\"]",
            #     "NKCDWBPZTRZJTVR2",
            #     360.0,
            #     360.0,
            #     "[\"http://img5a.flixcart.com/image/necklace-chain/v/r/2/dadel20184-voylla-necklace-original-imadwbtxuseu9hay.jpeg\", \"http://img5a.flixcart.com/image/necklace-chain/v/r/2/dadel20184-voylla-necklace-original-imadwbtyqe8fr6xx.jpeg\"]",
            #     false,
            #     "Voylla Metal, Alloy Necklace - Buy Voylla Metal, Alloy Necklace only for Rs. 360 from Flipkart.com. Only Genuine Products. 30 Day Replacement Guarantee. Free Shipping. Cash On Delivery!",
            #     "No rating available",
            #     "No rating available",
            #     "Voylla",
            #     "{\"product_specification\"=>[{\"key\"=>\"Brand\", \"value\"=>\"Voylla\"}, {\"key\"=>\"Collection\", \"value\"=>\"Ethnic\"}, {\"key\"=>\"Model Number\", \"value\"=>\"DADEL20184\"}, {\"key\"=>\"Precious/Artificial Jewellery\", \"value\"=>\"Fashion Jewellery\"}, {\"key\"=>\"Type\", \"value\"=>\"Necklace\"}, {\"key\"=>\"Ideal For\", \"value\"=>\"Women\"}, {\"key\"=>\"Occasion\", \"value\"=>\"Everyday\"}, {\"key\"=>\"Color\", \"value\"=>\"Gold, Pink\"}, {\"key\"=>\"Weight\", \"value\"=>\"75.56 g\"}, {\"key\"=>\"Base Material\", \"value\"=>\"Metal, Alloy\"}, {\"key\"=>\"Sales Package\", \"value\"=>\"1 Necklace\"}, {\"key\"=>\"Pack of\", \"value\"=>\"1\"}]}"
            # ]
            
            def sorting(product):
                
                # which characters are common to the two words?
                v1 = word2vec(name[-20:][::-1])
                v2 = word2vec(product[1][-20:][::-1])
                common = v1[1].intersection(v2[1])

                # by definition of cosine distance we have
                wordSimilarity = sum(v1[0][ch]*v2[0][ch]
                                     for ch in common)/v1[2]/v2[2]
                if(product[2] != "Nan"):
                    difference_between_price = abs(
                        int(price) - int(product[2]))
                else:
                    difference_between_price = price*1.5

                combine_WordSimilarity_DifferenceBetweenPrice = (
                    -(wordSimilarity*10000) + difference_between_price)/2
                Samebrand = brand == product[3]
                # return (not Samebrand, -wordSimilarity, difference_between_price)
                return (not Samebrand, combine_WordSimilarity_DifferenceBetweenPrice)

            import copy
            temp = copy.deepcopy(RecommendedProducts)
            for x in range(len(RecommendedProducts)):
                if(RecommendedProducts[x][3] == 'Nan'):
                    temp.remove(RecommendedProducts[x])

            FinalRecommendation = sorted(temp, key=sorting)
            FinalRecommendation.pop(0)
            for x in range(requiredRecommendations):
                print
                (FinalRecommendation[x])
            print()


main()


# print(d)

# SAVE JSON

# print("Printing data")
# with open('ProductTree.json', 'w') as fp:
#     json.dump(data, fp)

# with open('productId.json', 'w') as fp:
#     json.dump(products, fp)

# print(data)
