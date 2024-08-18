#prices = [0.36, 0.32, 0.21,0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.30, 0.29, 0.34, 0.41, 0.32, 0.34, 0.35, 0.20, 0.36, 0.32, 0.21, 0.34, 0.32, 0.32, 0.43, 0.34, 0.35, 0.45, 0.32, 0.34, 0.22, 0.33, 0.02]
prices = [54990.01, 54990.01, 54990.01, 54984.41, 54984.41, 54975.37, 54975.01, 54975.01, 54975.01, 54975.01, 54975.01, 54975.01, 54958.4, 54948.99, 54940.33, 54938.78, 54931.88, 54931.89, 54931.7, 54926.96, 54932.13, 54933.17, 54935.13, 54935.48, 54931.99, 54926.95, 54935.14, 54926.95, 54926.95, 54960.53, 54960.51, 54960.52, 54960.53, 54969.79, 54986.97, 54995.53, 54997.98, 54999.52, 55000.0, 55000.0, 54999.99, 54999.99, 54991.4, 54973.98, 54978.73, 54976.61, 54984.57, 54989.05, 54994.88, 54999.98, 55000.0, 55007.87, 55011.36, 55018.45, 55018.44, 55018.51, 55022.86, 55029.64, 55028.57, 55029.64, 55029.64, 55029.64, 55029.64, 55029.63, 55029.63, 55043.1, 55043.1, 55043.1, 55057.34, 55057.78, 55059.3, 55059.3, 55063.5, 55070.74, 55070.74, 55073.49, 55076.99, 55076.28, 55076.28, 55059.29, 55036.65, 55029.65, 55016.84, 55024.62, 55012.96, 55021.54, 55025.87, 55025.87, 55021.82]
def Math_RSI(prices):    
    upward_move = []
    downward_move = []
    
    up_avg_list = []
    down_avg_list = []
    
    rs = []
    rsi = []
    
    # while True:
    
    #     try:
    #         p = int(input("How many closing prices would you like to take into consideration before the bot will begin to interact with the live market?\n"))
    #         break
    #     except ValueError:
    #         pass
    
    p=12
    
    i=0
    for x in prices:
        if i==0:
            pass
            
        else:
            if(prices[i] > prices[i-1]):
                newprice = prices[i] - prices[i-1]
                upward_move.append(newprice)
                downward_move.append(0)
                
            elif(prices[i] == prices[i-1]):
                downward_move.append(0)
                upward_move.append(0)
                
            else:
                newprice = prices[i-1]-prices[i]
                downward_move.append(newprice)
                upward_move.append(0)
                
        i+=1
                
    # print(upward_move)
    # print(downward_move)
    
    # print(len(upward_move))
    # print(len(downward_move))
            
    
    # def up_down_list_create(original_list, up_list, down_list):
    #     for 
    up_avg = (sum(upward_move[:p]))/len(upward_move[:p])
    up_avg_list.append(up_avg)
    down_avg = (sum(downward_move[:p]))/len(downward_move[:p])
    down_avg_list.append(down_avg)
    y=0
    for i in upward_move[p:]:
        if y==0:
            continue_up_avg = ((up_avg*(len(upward_move[:p])-1))+i)/len(upward_move[:p])
            up_avg_list.append(continue_up_avg)
        else:
            continue_up_avg = ((up_avg_list[-1]*(len(upward_move[:p])-1))+i)/len(upward_move[:p])
            up_avg_list.append(continue_up_avg)
        y+=1
    l=0    
    for i in downward_move[p:]:
        if l==0:
            continue_down_avg = ((down_avg*(len(downward_move[:p])-1))+i)/len(downward_move[:p])
            down_avg_list.append(continue_down_avg)
        else:
            continue_down_avg = ((down_avg_list[-1]*(len(upward_move[:p])-1))+i)/len(upward_move[:p])
            down_avg_list.append(continue_down_avg)
        l+=1
        
    for i, x in zip(up_avg_list, down_avg_list):
        rs_val = i/x
        rs.append(rs_val)
        
    for i in rs:
        rsi_val = (100-(100/(i+1)))
        rsi.append(rsi_val)
        
    # print('\n\n\n\n\n\n', up_avg_list, '\n\n\n\n\n\n')
    
    # print('\n\n\n\n\n\n', down_avg_list, '\n\n\n\n\n\n')
        
    
    #print(rsi)
    return rsi
       
    #print(prices[p:])
    # print(up_avg_list, '\n\n')
    # print(down_avg_list)
    
    
    #print(len(downward_move[:p]))
    
    
    #first_avg = (sum(prices[:p]))/len(prices[:p])
    

#Math_RSI(prices)
    
    
    










