def solution(id_list, report, k):
    answer = []
    report_dict = {}
    for r in report:
        name = r.split()[0]
        target = r.split()[1]
        report_list = report_dict.get(name, [])
        report_list.append(target)
        report_dict[name] = report_list
    
    reported = {}
    
    for r in report:
        name = r.split()[0]
        target = r.split()[1]
        report_list = reported.get(target, [])
        report_list.append(name)
        reported[target] = report_list
        
    #print(reported)
    '''
    frodo : muzi, apeach o
    neo : muzi, frodo o 
    muzi : apeach x
    apeach : x x 

    [frodo, neo]

    muzi - 2 [frodo, neo]
    frodo - 1 [neo]
    apeach - 1 [muzi, frodo]
    neo - 0 [x]
    
    '''
    stopped = []
    for name in reported:
        if len(set(reported[name])) >= k:
            stopped.append(name)
    #print(stopped)
    
    for _id in id_list:
        cnt=0
        for rd in set(report_dict.get(_id, [])):
            if rd in stopped:
                cnt += 1
        answer.append(cnt)
    
    return answer