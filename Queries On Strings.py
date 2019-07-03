from collections import OrderedDict


def queries_on_strings(no_of_test_cases, string, no_of_queries, queries):
    answer = ""
    answer_list = ""
    k = 0
    start = 0
    count = 0
    if no_of_test_cases == 1:
        for x in range(len(queries)):
            if queries[x] == " ":
                count += 1
                if count == 1:
                    m = x
                    query_1 = int(queries[start:m])
                    continue
                elif count == 2:
                    n = m + 1
                    query_2 = int(queries[n:x])
                    query_string = ""

                    for j in range((query_1 - 1), query_2):
                        query_string += string[j]
                        continue
                    dict = OrderedDict.fromkeys(query_string)
                    distinct_string = ''.join(dict)
                    no_of_distinct_string = len(distinct_string)
                    no_of_distinct_string = str(no_of_distinct_string)
                    answer += no_of_distinct_string + " "
                    query_string = ""
                count = 0
                start = x
        n = m + 1
        query_2 = int(queries[n:])
        query_string = ""

        for j in range((query_1 - 1), query_2):
            query_string += string[j]
            continue
        dict = OrderedDict.fromkeys(query_string)
        distinct_string = ''.join(dict)
        no_of_distinct_string = len(distinct_string)
        no_of_distinct_string = str(no_of_distinct_string)
        answer += no_of_distinct_string + " "
        return answer

    else:
        for query in queries:
            if k < no_of_test_cases:
                for x in range(len(query)):
                    if query[x] == " ":
                        count += 1
                        if count == 1:
                            m = x
                            query_1 = int(query[start:m])
                            continue
                        elif count == 2:
                            n = m + 1
                            query_2 = int(query[n:x])
                            query_string = ""
                            for j in range((query_1 - 1), query_2):
                                query_string += string[k][j]
                                continue
                            dict = OrderedDict.fromkeys(query_string)
                            distinct_string = ''.join(dict)
                            no_of_distinct_string = len(distinct_string)
                            no_of_distinct_string = str(no_of_distinct_string)
                            answer += no_of_distinct_string + " "
                            query_string = ""
                        count = 0
                        start = x
                n = m + 1
                query_2 = int(query[n:])
                query_string = ""
                for j in range((query_1 - 1), query_2):
                    query_string += string[k][j]
                    continue
                dict = OrderedDict.fromkeys(query_string)
                distinct_string = ''.join(dict)
                no_of_distinct_string = len(distinct_string)
                no_of_distinct_string = str(no_of_distinct_string)
                answer += no_of_distinct_string + " "
                count = 0
                start = 0
                k += 1
            answer_list += answer + "\n"
            answer = ""
        return answer_list


no_of_test_cases = 2
string = "abcbaed", "geeksforgeeks"
no_of_queries = 3, 3
queries = "1 4 2 4 1 7", "1 13 2 10 4 6"
print(queries_on_strings(no_of_test_cases, string, no_of_queries, queries))
