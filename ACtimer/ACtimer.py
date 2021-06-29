from AClocalTime import *

GREET = '''

     **         ******            **********   **   ****     ****   ********
    ****       **////**          /////**///   /**  /**/**   **/**  /**///// 
   **//**     **    //               /**      /**  /**//** ** /**  /**      
  **  //**   /**                     /**      /**  /** //***  /**  /******* 
 **********  /**                     /**      /**  /**  //*   /**  /**////  
/**//////**  //**    **              /**      /**  /**   /    /**  /**      
/**     /**   //******    *****      /**      /**  /**        /**  /********
//      //     //////    /////       //       //   //         //   ////////

WELCOME to the ACtimer to track your time usage~
Be effective and have fun!
It's a beginner's work.
=======================
     VERSION: 1.0.1
  DEVELOPER: Elichika
email: test@outlook.com
=======================
'''
def main():
    swi = True
    print(GREET)
    Dict = {}
    while swi:
        temp = input('\n======\n# input "start" + [name] to start recording time on something\n# input "conclude" to see your results\n# input "quit" to exit the program\n======\n\n$ ')
        if temp == 'quit':
            prtConclu(Dict)
            return None
        if len(temp) < 3 and temp[0:3] != 'con' and temp[0:3] != 'sta':
            print('please try again\n')
            pass
        if temp[0:8] == 'continue':
            Dict = contin(temp[9:],Dict)
        elif temp == 'conclude':
            prtConclu(Dict)
        elif temp[0:5] == 'start':
            Dict = start(temp[6:],Dict)
        
        
def contin(str,Dict):
    print('Now continuing %s' % str)
    swi = True
    startTime = sec()
    a = input("Let's WORK!\nClick anything to continue & and this period")
    endTime = sec()
    period = diff(startTime,endTime)
    Dict[str] += period
    period = fom(period)
    print('This time peroid last for %s hrs, %s min, %s sec' % (period[0],period[1],period[2]))
    return Dict

def start(str,Dict):
    
    for x in Dict:
        if x == str:
            Dict = contin(str,Dict)
            return Dict
    print('element [%s] is created' % str)
    Dict[str] = 0
    Dict = contin(str,Dict)
    return Dict

def prtConclu(Dict):
    print('====CONCLUSION====')
    timeList = []
    for e in Dict:
        timeList.append(e)
    for i in range(len(Dict)):
        print('%s. %s --> %s hrs, %s minute, %s sec' % (i+1,timeList[i],fom(Dict[timeList[i]])[0],fom(Dict[timeList[i]])[1],fom(Dict[timeList[i]])[2]))

    a = input('Enter Anything to continue......')
        
        

if __name__ == '__main__':
    main()
