start  
Declarations  
    num mortgagePayment  
    num utilities  
    num taxes  
    num upkeep  
    num total  

startUp()  
while mortgagePayment not equal to 0 do  
    mainLoop()  
endwhile  
finishUp()  
stop  

startUp()  
    output "Enter your mortgage payment or 0 to quit"  
    input mortgagePayment  
    return  

mainLoop()  
    output "Enter utilities"  
    input utilities  
    output "Enter taxes"  
    input taxes  
    output "Enter amount for upkeep"  
    input upkeep  
    
    total = mortgagePayment + utilities + taxes + upkeep  
    output "Total is ", total  
    return  

finishUp()  
    output "End of program"  
    return
