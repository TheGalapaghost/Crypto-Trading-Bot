close = [200,195,190,192,193,194,192,193,196,200,201,202,203,205,199,198,207,209,210,220,217,214,210,205,200,192,185,172,210,220,217,214,210,205,200,192,185,172]
lows =  [189,184,182,185,182,189,170,185,185,190,191,181,194,185,180,182,190,192,193,200,201,199,189,192,191,172,165,143,193,200,201,199,189,192,191,172,165,143]
highs = [202,199,195,194,197,195,199,195,196,202,206,208,210,207,202,200,208,210,211,220,219,225,215,209,202,197,189,187,211,220,219,225,215,209,202,197,189,187]

def stochastic(highs, lows, close, period=13, K_avg=3):
    percent_K_list = []
    numerator_list = []
    denominator_list = []
    slow_stochastic = []
    signal_line = []
    x=0
    for y in close:
        try:
            numerator = ((close[period+x])-(min(lows[x:(period+1)+x])))
            numerator_list.append(numerator)
            denominator = ((max(highs[x:(period+1)+x]))-(min(lows[x:(period+1)+x])))
            denominator_list.append(denominator)
            percent_K = numerator/denominator
            #print(lows[x:(period+1)+x])
            #print(close[period+x])
            percent_K_list.append(percent_K)
            #print(x)
            x+=1
        except Exception as e:
            break
    x=0
    for i in percent_K_list:
        slow = (sum(numerator_list[x:K_avg+x]))/(sum(denominator_list[x:K_avg+x]))
        if len(numerator_list[x:K_avg+x]) < K_avg:
            break
        slow_stochastic.append(slow*100)
        x+=1
    
    x=0
    for i in slow_stochastic:
        signal = sum(slow_stochastic[x:K_avg+x])/len(slow_stochastic[x:K_avg+x])
        if len(slow_stochastic[x:K_avg+x]) < K_avg:
           break
        signal_line.append(signal)
        x+=1
        
    #print(slow_stochastic[-1])
    #print(signal_line[-1])
        
    if slow_stochastic[-1] > 80 and signal_line[-1] > 80:
        return -4
    elif slow_stochastic[-1] > 80 and signal_line[-1] < 80:
        return -1
    elif slow_stochastic[-1] < 80 and signal_line[-1] > 80:
        return -1
    elif slow_stochastic[-1] < 20 and signal_line[-1] < 20:
        return 4
    elif slow_stochastic[-1] < 20 and signal_line[-1] > 20:
        return 1
    elif slow_stochastic[-1] > 20 and signal_line[-1] < 20:
        return 1
    else:
        return 0

