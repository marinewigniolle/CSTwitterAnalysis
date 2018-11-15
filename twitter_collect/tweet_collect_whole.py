def get_candidate_queries(num_candidate, file_path,type):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        L = []
        path = type + '_'+ file_path+ '_' + num_candidate + '.txt'
        with open(path) as csvfile:
            for line in csvfile
            L.append(line)
        return L
    except IOError:
        print (' erreur dans la fonction')

