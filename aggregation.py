from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["PracticeDB"]
collection = db["PracticeCollection"]

# a = collection.aggregate([
#     {"$match": {"center_id": {"$eq": 11}}},{"$count": "totalrows"},])

# b = collection.aggregate([
#     {
#         "$match": {"center_id": {"$gt": 20, "$lt": 100}}
#     },
#     {
#         "$group": {
#             "_id": "$center_id", "Number_of_orders": {
#                 "$avg": "$num_orders"
#             }}}
#
# ])
#
# for i in b:
#     pprint(i)

# c = collection.aggregate([{"$group": {"_id": "$center_id", "Number_of_orders": {"$avg": "$num_orders"}}}])
# pprint(list(c))


new_dict = [{"author": "dave", "score": [80, 90, 100], "views": 100},
            {"author": "dave", "score": [85, 40, 80], "views": 521},
            {"author": "ahn", "score": [60, 94, 91], "views": 1000},
            {"author": "li", "score": [55, 49, 100], "views": 5000},
            {"author": "annT", "score": [60, 78, 98], "views": 50},
            {"author": "li", "score": [94, 78, 59], "views": 999},
            {"author": "ty", "score": [95, 80, 65], "views": 1000}]

# a = collection.insert_many(new_dict)
# for i in new_dict:
# print(i)

b = collection.aggregate([{"$match": {"author": "dave"}}])
# pprint(list(b))


# c = collection.aggregate([{"$match": {"$or": [{"score": {"$gt": 70, "$lt": 90}}, {"views": {"$gte": 1000}}]}},
#                           {"$group": {"_id": "$author", "count": {"$sum": 1}}}])
# pprint(list(c))

# d = collection.aggregate([{"$addFields": {"total_score": {"$sum": "$score"}}},
#                           {"$addFields": {"score_and_views": {"$sum": ["$total_score", "$views"]}}},
#                           {"$addFields": {"quality": "1080p"}},
#                           {"$addFields": {"score": {"$concatArrays": ["$score", [95]]}}}])
# pprint((list(d)))


# print(list(e))
# f = collection.find_one({"quality": "1080p"}, {"_id": 0})


dict1 = [
    {
        "_id": 1,
        "name": "Alice",
        "department": "HR",
        "salary": 50000,
        "age": 30
    },
    {
        "_id": 2,
        "name": "Bob",
        "department": "IT",
        "salary": 60000,
        "age": 28
    },
    {
        "_id": 3,
        "name": "Charlie",
        "department": "IT",
        "salary": 55000,
        "age": 35
    },
    {
        "_id": 4,
        "name": "David",
        "department": "HR",
        "salary": 52000,
        "age": 32
    }
]

# one = collection.insert_many(dict1)
a = collection.aggregate([{"$group": {"_id": "salary",
                                      "average_salary": {"$avg": "$salary"}}}])
# pprint(list(a))

c = collection.aggregate([{"$sort": {"age": -1}},
                          {"$limit": 1},
                          {"$project": {"name": 1, "age": 1, "department": 1, "_id": 0}}])
# pprint(list(c))
d = collection.aggregate([{"$group": {"_id": "$department", "count": {"$sum": 1}}}])
# pprint(list(d))

e = collection.aggregate([{"$match": {"department": "IT"}},
                          {"$project": {"name": 1, "_id": 0}}])

# {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]}, "then": "50k-60k"},

# f = collection.aggregate([{"$group": {"_id":
#     {"$switch":
#         {"branches": [
#             {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]},
#              "then": "50_to_60"},
#             {"case": {"$and": [{"$gte": ["$salary", 60000]}, {"$lt": ["$salary", 70000]}]},
#              "then": "60_to_70"},
#             {"case": {"$gte": ["$salary", 70000]}, "then": "exceeding_70K"}
#         ],
#             "default": "Below_50k"
#         },
#         "count": {"$sum": 1}}}
# }
# ])
# pprint(list(e))

# pipeline = [
#     {
#         "$group": {
#             "_id": {
#                 "$switch": {
#                     "branches": [
#                         {"case": {"$and": [{"$gte": ["$salary", 50000]}, {"$lt": ["$salary", 60000]}]},
#                          "then": "50_to_60"},
#                         {"case": {"$and": [{"$gte": ["$salary", 60000]}, {"$lt": ["$salary", 70000]}]},
#                          "then": "60_to_70"},
#                         {"case": {"$gte": ["$salary", 70000]}, "then": "exceeding_70K"}
#                     ],
#                     "default": "Below_50k"
#                 }
#             },
#             "count": {"$sum": 1}
#         }
#     }
# ]
#
# result = list(collection.aggregate(pipeline))
# print(result)


dict2 = [
    {
        "_id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "rating": 4.5,
        "num_reviews": 100
    },
    {
        "_id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "rating": 4.8,
        "num_reviews": 80
    },
    {
        "_id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "rating": 4.7,
        "num_reviews": 120
    },
    {
        "_id": 4,
        "title": "1984",
        "author": "George Orwell",
        "rating": 4.3,
        "num_reviews": 60
    }
]

# collection.insert_many(dict2)

# ba = collection.aggregate([{"$group": {
#     "_id": {
#         "$cond": {
#             "if": {"$gte": ["$rating", 4.7]},
#             "then": "HighlyRated",
#             "else": {
#                 "$cond": {"if": {"gte": ["$rating", 4.0]},
#                           "then": "ModeratelyRated",
#                           "else": "Lowly Rated"
#                           }}}}, "count": {"$sum": 1}}}])
#
# pprint(list(ba))

# collection.insert_many([
#   {
#     "_id": 1,
#     "title": "Inception",
#     "genre": "Action",
#     "year": 2010,
#     "ratings": [8.8, 9.2, 8.9]
#   },
#   {
#     "_id": 2,
#     "title": "The Shawshank Redemption",
#     "genre": "Drama",
#     "year": 1994,
#     "ratings": [9.3, 9.5, 9.1]
#   },
#   {
#     "_id": 3,
#     "title": "The Dark Knight",
#     "genre": "Action",
#     "year": 2008,
#     "ratings": [9.0, 8.7, 8.9]
#   },
#   {
#     "_id": 4,
#     "title": "Pulp Fiction",
#     "genre": "Crime",
#     "year": 1994,
#     "ratings": [8.9, 9.1, 8.8]
#   }
# ])

nq = collection.aggregate([{"$addFields": {"average_ratings": {"$avg": "$ratings"}}},
                           {"$project": {"title": 1, "year": 1, "average_ratings": 1, "_id": 0}},
                           {"$out": "Average_ratings"}])
print(list(nq))
