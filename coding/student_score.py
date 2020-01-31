def print_score(score_of_nlg, score_of_math, score_of_social):
    """
    Calculate the scores
    """
    score_length = len(score_of_nlg)
    print " No.  score_of_nlg   score_of_math   score social"
    lang_score_sum = 0
    math_score_sum = 0
    social_score_sum = 0
    # calculate social social_score in dictionary - key student id and value is social_score
    social_score_dict = {}
    for i in range(len(score_of_social)):
        nlg_tuple = score_of_social[i]
        # social_score_dict key is student id and value is social value marks, [(3, 80)]
        social_score_dict[nlg_tuple[0]] = nlg_tuple[1]

    for i in range(score_length):
        score_of_nlg_tuple = score_of_nlg[i]
        student_id = score_of_nlg_tuple[0]
        score_of_math_tuple = score_of_math[i]
        # check if social social_score exists for this student id
        if student_id in social_score_dict:
            print score_of_nlg_tuple[0]
            print score_of_nlg_tuple[1]
            print score_of_math_tuple[1]
            print score_of_nlg_tuple[1]
            # calculating the sum of social_score
            lang_score_sum = lang_score_sum + score_of_nlg_tuple[1]
            math_score_sum = math_score_sum + score_of_math_tuple[1]
            social_score_sum = social_score_sum + social_score_dict[student_id]
        else:  # calculate scores when social social_score is not available
            print score_of_nlg_tuple[0]
            print score_of_nlg_tuple[1]
            print score_of_math_tuple[1]
            social_score = ((score_of_nlg_tuple[1] + score_of_math_tuple[1]) / 2) * 80 / 100
            print str(social_score)
            # calculating the sum of social_score
            lang_score_sum = lang_score_sum + score_of_nlg_tuple[1]
            math_score_sum = math_score_sum + score_of_math_tuple[1]
            social_score_sum = social_score_sum + social_score

        print ""

    #  calculating the average of scores
    print "Averages: "
    print lang_score_sum / score_length
    print math_score_sum / score_length
    print social_score_sum / score_length


print_score([(1, 80), (2, 70), (3, 80)], [(1, 60), (2, 90), (3, 100)], [(3, 80)])
