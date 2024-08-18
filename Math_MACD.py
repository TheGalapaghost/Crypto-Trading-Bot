prices = [53679.65, 53674.41, 53682.8, 53682.79, 53695.91, 53702.05, 53697.06, 53711.28, 53721.77, 53742.93, 53744.42, 53738.12, 53738.24, 53707.22, 53676.93, 53658.76, 53653.51, 53666.11, 53675.3, 53692.24, 53713.8, 53737.42, 53746.56, 53734.97, 53746.56, 53779.94, 53794.62, 53794.63, 53794.87, 53800.18, 53803.87, 53807.47, 53805.82, 53811.45, 53805.82, 53805.82, 53789.71, 53781.72, 53791.81, 53803.83, 53792.34, 53750.0, 53727.85, 53734.21, 53739.19, 53722.24, 53759.54, 53777.55, 53772.57, 53785.12, 53800.0, 53811.65, 53805.44, 53812.0, 53812.0, 53812.0, 53812.0, 53819.15, 53845.49, 53850.0, 53849.99, 53850.0, 53841.46, 53825.34, 53825.34, 53824.32, 53816.32, 53805.35, 53808.53, 53810.5, 53845.32, 53836.1, 53846.15, 53855.02, 53875.3, 53884.6, 53888.0, 53888.0, 53895.1, 53922.67, 53919.53, 53939.12, 53903.03, 53921.19, 53906.07, 53900.0, 53879.73, 53875.64, 53838.14, 53833.2, 53840.41, 53833.18, 53822.87, 53822.86, 53822.87, 53822.87, 53843.94, 53860.79, 53876.0, 53843.42, 53850.01, 53850.47, 53823.48, 53833.2, 53844.97, 53854.41, 53854.41, 53878.4, 53870.19, 53849.56, 53817.88, 53831.35]
#prices = [53349.0, 53341.25, 53319.24, 53306.7, 53337.91, 53341.64, 53330.49, 53324.75, 53337.19, 53351.0, 53380.78, 53362.69, 53343.87, 53356.29, 53342.37, 53361.07, 53387.42, 53371.2, 53371.2, 53389.87, 53399.98, 53424.0, 53447.71, 53457.29, 53472.42, 53456.11, 53448.69, 53434.37, 53449.74, 53449.53, 53448.71, 53463.6, 53470.89, 53467.43, 53469.76, 53447.8, 53441.92, 53459.52, 53501.12, 53515.13, 53549.99, 53540.08, 53540.14, 53500.0, 53499.99, 53455.66, 53458.78, 53490.32, 53522.62, 53522.0, 53529.29, 53527.24, 53531.8, 53535.9, 53549.99, 53560.0, 53560.0]
#prices = [54123.14, 54057.94, 54126.26, 53986.14, 53973.47, 53945.32, 53978.81, 54163.71, 54073.21, 54071.59, 53869.45, 53797.55, 53833.92, 53999.45, 54049.97, 54186.13, 54209.35, 54276.63, 54297.77, 54231.79, 54238.58, 54156.39, 54109.21, 54059.77, 54047.38, 54109.22, 54171.43, 54149.1, 54043.85, 54023.31, 54070.6, 54053.18, 53960.11, 53974.46, 54028.72, 54191.61, 54220.91, 54227.85, 54075.94, 54059.46, 54053.11, 54013.14, 53912.57, 53904.01, 53876.34, 53856.75, 53793.1, 53788.39, 53716.27, 53656.81, 53750.07, 53744.25, 53715.36, 53811.61, 53927.68, 53887.54, 53731.71, 53676.21, 53646.06, 53699.99, 53848.0, 53906.44, 53749.97, 53803.02, 53897.47, 53975.75, 53954.81, 54029.05]
#prices = [0.36, 0.32, 0.21,0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.30, 0.29, 0.34, 0.41, 0.32, 0.34, 0.35, 0.20, 0.36, 0.32, 0.21, 0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.02, 0.36, 0.32, 0.21,0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.30, 0.36, 0.32, 0.21,0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.30]
def Math_MACD(prices):
    first_avg = []
    second_avg = []
    
    MACD = []
    signal_line = []
    final_verd = []
    
    initial_avg = (sum(prices[:12]))/len(prices[:12])
    first_avg.append(initial_avg)
    
    time_p = 9
    
    x=0
    for i in prices[12:]:
        #print(i)
        if x==0:
            continue_avg = ((i*(2/((len(prices[:12]))+1)))+(initial_avg)*(1-(2/((len(prices[:12]))+1))))
            first_avg.append(continue_avg)
            
        else:
            continue_avg = ((i*(2/((len(prices[:12]))+1)))+(first_avg[-1])*(1-(2/((len(prices[:12]))+1))))
            first_avg.append(continue_avg)
        x+=1
        
    second_initial_avg = (sum(prices[:26]))/len(prices[:26])
    second_avg.append(second_initial_avg)
    y=0
    for i in prices[26:]:
        if y==0:
            continue_avg = ((i*(2/((len(prices[:26]))+1)))+(second_initial_avg)*(1-(2/((len(prices[:26]))+1))))
            second_avg.append(continue_avg)
            
        else:
            continue_avg = ((i*(2/((len(prices[:26]))+1)))+(second_avg[-1])*(1-(2/((len(prices[:26]))+1))))
            second_avg.append(continue_avg)
        y+=1
        
    for i, x in zip(first_avg[26-12:], second_avg):
        macd_val = i-x
        MACD.append(macd_val)
    
    MACD_avg = (sum(MACD[:time_p]))/len(MACD[:time_p])
    signal_line.append(MACD_avg)
    
    k=0
    for i in MACD[time_p:]:
        if k==0:
            continue_avg = ((i*(2/((len(MACD[:time_p]))+1)))+MACD_avg*(1-(2/((len(MACD[:time_p]))+1))))
            signal_line.append(continue_avg)
            
        else:
            continue_avg = ((i*(2/((len(MACD[:time_p]))+1)))+(signal_line[-1])*(1-(2/((len(MACD[:time_p]))+1))))
            signal_line.append(continue_avg)
        k+=1
        
    
    # print('\n\n\n\n\n', len(MACD[time_p-1:]), '\n\n\n\n\n')
    
    # print('\n\n\n\n\n', len(signal_line), '\n\n\n\n\n')
    
    # print(len(prices))
    # print(67-34)
    t=0
    for mac, sig in zip(MACD[time_p-1:], signal_line):
        try:
            if mac > sig:
                if MACD[time_p+t] < sig:
                    # print('-'*20,"\n\nIntersection occured {Bearish Outlook}, advice is to SELL",'-'*20)
                    # print("Initial Point: " + str(mac))
                    # print("End Point: " + str(MACD[time_p+t]))
                    # print("Current Signal Line: " + str(sig))
                    bot_trans = -1
                    final_verd.append(bot_trans)
                    #return bot_trans
                    #print(bot_trans)
                    
                else:
                    #print('-'*20, "\n\nIntersection did not occur {Neutral Outlook}, advice is to HOLD", '-'*20)
                    bot_trans = 0
                    final_verd.append(bot_trans)
                    #print(bot_trans)
                    #return bot_trans
                    
                    
            elif mac < sig:
                if MACD[time_p+t] > sig:
                    # print('-'*20,"\n\nIntersection occured {Bullish Outlook}, advice is to BUY",'-'*20)
                    # print("Initial Point: " + str(mac))
                    # print("End Point: " + str(MACD[time_p+t]))
                    # print("Current Signal Line: " + str(sig))
                    bot_trans = 1
                    final_verd.append(bot_trans)
                    #print(bot_trans)
                    #return bot_trans
                else:
                    #print('-'*20, "\n\nIntersection did not occur {Neutral Outlook}, advice is to HOLD", '-'*20)
                    bot_trans = 0
                    final_verd.append(bot_trans)
                    #print(bot_trans)
                    #return bot_trans
                    
        except:
            pass
                
        t+=1
        
    return final_verd
        
        
#print(Math_MACD(prices))

#[0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0]
#[0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0]
#[0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0]
















    