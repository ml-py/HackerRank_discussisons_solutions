"""     Squares of 11…1 (where length is smaller than 10) are called Demlo numbers.
A demlo number is number which consist of 1, 2, 3….n, n-1, n-2, …..1. """
""" Repunit - Wikipedia    https://en.wikipedia.org/
In recreational mathematics, 
a repunit is a number like 11, 111, or 1111 that contains only the digit 1 — a more specific type of repdigit. 
The term stands for repeated unit and was coined in 1966 by Albert H. Beiler in his book Recreations in the Theory of Numbers. """

'''
for i in range(   1,  int(  input()  )+1   ):
    print(   int( 0.123456789 * 10**i )    * 10**(i-1)         +         87654321    % 10**(i-1)   )
    '''


from math import ceil
from functools import reduce
from decimal import Decimal

def Demlo_numbers( number: int )  ->  None :

    ''' File helping underetanding answers in discusiion about HackerRank task on
    https://www.hackerrank.com/challenges/triangle-quest-2/forum
    A method/function containing modified examples examples from the duscusion '''

    ''' jonmcclung 4 years ago    Brute force: '''
    for i in range(  1,  int( number )+1  ):
        print(    1 if i == 1
                  else 121 if i == 2
                         else 12321 if i == 3
                                  else 1234321 if i == 4
                                             else 123454321 if i == 5
                                                          else 12345654321 if i == 6
                                                                         else 1234567654321 if i == 7
                                                                                          else 123456787654321 if i == 8
                                                                                                             else 12345678987654321   , end=" ")  ;  ''' 
    for i in range(  1,  int( number )   ):
    12345678987654321 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 '''
    print()
    ''' mvincent7891 3 years ago:) How does this work? Shame on the designer of this problem. '''
    for i in range(  0,  int( number )    ):
        print(   [  1, 121, 12321, 1234321, 123454321, 12345654321,
                    1234567654321, 123456787654321, 12345678987654321  ][ i ], end=" ")
    print()
    # print("\n==========>\n")
    ''' Issei_Kumagai 2 months ago '''
    for i in range(  1,  int( number )+1   ):
        print(   [ 'nothing==justAnything. Can be int: 0 ',
                    1, 121, 12321, 1234321, 123454321, 12345654321,
                    1234567654321, 123456787654321, 12345678987654321  ][ i ], end=" ")
    print()
    for i in range(  1,  int( number )+1  ):
        print(   [  1, 121, 12321, 1234321, 123454321, 12345654321,
                    1234567654321, 123456787654321, 12345678987654321  ][i-1], end=" ")
    print()
    for i in range(  1,  int( number )+1  ):
        print(   [  1,
                    121,
                    12321,
                    1234321,
                    123454321,
                    12345654321,
                    1234567654321,
                    123456787654321,
                    12345678987654321  ][i-1], end=" ");
    print()
    for i in range(      int( number )    ):
        print(   [  1,
                    121,
                    12321,
                    1234321,
                    123454321,
                    12345654321,
                    1234567654321,
                    123456787654321,
                    12345678987654321  ][ i ], end=" ")
    print()
    ''' flea2310 2 years ago    Two statements on one line also work. :) '''
    for _ in range(   number   ):
        k = [  1, 121, 12321, 1234321, 123454321, 12345654321,
               1234567654321, 123456787654321, 12345678987654321  ] ; print(  k[_]  ,  end=" "  )
    print()

    # print("\n==========>\n")
    ''' aronquemarr 2 months ago    Here's what I thought of: '''
    for n in range(  1,  int( number )+1  ):
        print(   (    n   *     10**  n
                  + (n-1) * int(10**(n-1)) * (10**2  + 1)
                  + (n-2) * int(10**(n-2)) * (10**4  + 1)
                  + (n-3) * int(10**(n-3)) * (10**6  + 1)
                  + (n-4) * int(10**(n-4)) * (10**8  + 1)
                  + (n-5) * int(10**(n-5)) * (10**10 + 1)
                  + (n-6) * int(10**(n-6)) * (10**12 + 1)
                  + (n-7) * int(10**(n-7)) * (10**14 + 1)
                  + (n-8) * int(10**(n-8)) * (10**16 + 1)   )//10  ,  end=" "  )
    print()
    # print("\n==========>\n")
    ''' Cirn3co 1 year ago    works but it looks so dumb... '''
    for i in range(   1,  int(( number ))+1   ):
        print(   sum(   [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000][:i]   ) ** 2   ,  end=" "  )
    print()
    # print("\n==========>\n")
    ''' quachtridat 5 months ago    Not much different from yours lmao. / johnmarston1729 3 years ago '''
    for i, j in zip(   range(int( number )),
                       [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 13131313131313131313]   ):
        print(   j**2   ,  end=" "  )
    print()
    # print("\n==========>\n")
    ''' Ts_jr 11 months ago    A different approach '''
    arr = (  1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 111111111, 1111111111  )
    # n = int( number )
    # for i in range(n)                    :        print(   arr[i  ] **2   ,   end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321                   '''
    # for i in range(1,  int( number )+1  ):        print(   arr[i  ] **2   ,   end=" "   )
    '''   121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 12345678987654321 '''
    # for i in range(    int( number )    ):        print(   arr[i  ] **2   ,   end=" "   )
    for i in range(  1,  int( number )+1  ):        print(   arr[i-1] **2   ,   end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321                   '''
    print()
    # print("\n==========>\n")
    ''' Noctsol 1 year ago    You thought you had to have elegant code. Yout THOUGHT WRONG. I BEAT IT. 
    Dang, someone had a similar solution to mine. No special   snowflake   points for me. 
    Mines smilar but still pretty different though. ''' ''' devenderreddyma1 '''
    for i in range(  1,  int( number )+1  ):
        print(   [  1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 111111111, 1111111111  ][i-1] **2   ,   end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321                   '''
    print()
    # print("\n==========>\n")
    ''' mujiatong 2 weeks ago '''
    myDict = {  1:1,  2:11,  3:111,  4:1111,  5:11111,  6:111111,  7:1111111,  8:11111111,  9:111111111  }
    for i in range(  1,  int( number )+1  ):
        print(   '{}'.format(  myDict[i] * myDict[i]  )   ,   end=" "   )
    print()


    # print( "\n==========>\n==========>\n")
    ''' gy2224 2 years ago    Come up with a different method, though not as efficient: '''
    for i in range(   1,  int(( number ))+1   ):
        print(   round(   111111111 /(10**(9-i))   )**2     ,  end=" "  )
    print()
    ''' master8282 3 years ago ''' ''' samo_chlebo 3 years ago '''
    for i in range(   1,  int(( number ))+1   ):
        print(   (   111111111//(10**(9-i))   )**2     ,  end=" "  )
    print()
    ''' [+++] '''
    for i in range(   1,  int(( number ))+1   ):
        print(   (   111111111//(10**(9-i))   )        ,  end=" "  ) # 1 11 111 1111 11111 111111 1111111 11111111 111111111
    print()
    for i in range(   1,  int(( number ))+1   ):
        print(   (   111111111 /(10**(9-i))   )        ,  end=" "  )
    print() # 1.11111111 11.1111111 111.111111 1111.11111 11111.1111 111111.111 1111111.11 11111111.1 111111111.0
    for i in range(   1,  int(( number ))+1   ):
        print(   (               10**(9-i)    )        ,  end=" "  ) # 100000000 10000000 1000000 100000 10000 1000 100 10 1
    print()

    # print("\n==========>\n")
    ''' jeremyephron 6 months ago    A more math-y solution (in Python3): ''' ''' alekospagon 12 months ago     mod gives you 1,11,111,1111,... so rise to 2nd power'''
    for i in range(   1,  int(( number ))+1   ):
        print(   (   11111111111111 %( 10**i )  )**2   ,  end=" "  ) # 111111111
    # print()
    for i in range(   1,  int(( number ))+1   ):
        # print(     11111111111111 /( 10**i )         ,  end=" "  )
        ''' 1111111111111.1 111111111111.11 11111111111.111 1111111111.1111 111111111.11111 11111111.111111 1111111.1111111 111111.11111111 11111.111111111 '''
        # print(     11111111111111 %( 10**i )         ,  end=" "  )
        '''               1              11             111            1111           11111          111111         1111111        11111111       111111111 '''
    print()
    # print("\n==========>\n")
    ''' zhihongwen 7 months ago '''    ''' julo4925 2 years ago    How's this? 
        I used the fact that int() would erase any unnecessary decimal points to get the necessary value lol '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   0.11111111111 * (10**i)   )**2   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' yosefvb 3 years ago    I'm sure there's a cleaner looking math solution. '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   10.0  /  9  *  10**(i-1)   )
               * int(   10.0  /  9  *  10**(i-1)   )   ,  end=" "   )
    # print(            10    /  9                                  )   #  1.1111111111111112
    '''                             =>  1.1111111111111112                  '''
    print()

    # print("\n==========>\n")
    ''' jeremyephron 6 months ago    A more math-y solution (in Python3): ''' ''' excalibur_kvrv 1 year ago ''' ''' ... '''
    for i in range(   1,  int(( number ))+1   ):
        print(   int(   1/9  *  10**i   )**2   ,  end=" "  )
    print()
    # print("\n==========>\n")
    ''' CollinRoess 2 years ago         print(   int(round(   float(1/9)   (10 *i),  0   ))**2   )'''
    for i in range(   1,  int(( number ))+1   ):
        # print( int(round(   float(1/9) * (10 *i),  0   ))**2   ,  end=" "  )
        ''' 1 4 9 16 36 49 64 81 100 '''
        print(   int(round(   float(1/9) * (10**i),  0   ))**2   ,  end=" "  )
        # print(              float(1/9) * (10**i)               ,  end=" "  )
        ''' 1.1111111111111112 11.11111111111111 111.1111111111111 1111.111111111111 11111.111111111111 111111.11111111111 1111111.111111111 11111111.11111111 111111111.1111111 '''
    print()



    # print("\n==========>\n")

    """ u mnie nie działa """
    ''' rme_academia 6 months ago '''
    # for i in range(   1,  int(( number ))+1   ):
    #     # print(   (123456789//(10**(10-i-1)))  (10*(i-1)) + (987654321%(10**(i-1)))   ,  end=" "  )
    #     ''' TypeError: 'int' object is not callable                         '''
    #     # print(   (123456789//(10**(10-i-1))) *(10*(i-1)) + (987654321%(10**(i-1)))   ,  end=" "  )
    #     ''' 0 121 2481 37341 498121 6227121 74728341 871851781 9964197441   '''
    #     # print(   (123456789//(10**(10-i-1)))**(10*(i-1)) + (987654321%(10**(i-1)))   ,  end=" "  )
    #     ''' 1 61917364225 628206215175202159781085149496179361969222 ...    '''
    #     # print(   (123456789//(10**(10-i-1)))//(10*(i-1)) + (987654321%(10**(i-1)))   ,  end=" "  )
    #     ''' ZeroDivisionError: integer division or modulo by zero           '''

    # print("\n==========>\n")
    """ [+++++] może to wysłać --- w końcu tyle tego szukałem """
    ''' skele 6 months ago    another cute solution '''
    for i in range(   1,  int(( number ))+1   ):
        print(   int( 0.123456789 * 10**i )   *   10**(i-1)
               +                 87654321     %   10**(i-1)   ,  end=" "  ) ; pass ; pass ; pass ; pass
    print();    ''' roopeshkom 2 years ago    Using only math, with 0 loops: '''
    for i in range(   1,  int(( number ))+1   ):
        print(   10**(i-1) * int(10**i * .123456789)
               +                                  987654321 % 10**(i-1)   ,  end=" "  )
    print()


    # print("\n==========>\n")
    """ [+++++] ciekawe """
    for i in range(   1,  int(( number ))+1   ):
        print(   round(   10**(  i+0.045757490560241 -1 )   )**2   ,  end=" "  )
    ''' gudkov_m_22 9 months ago    meh... ugly but it works... '''
    # for i in range( 1,  int(( number ))+1   ):
    #     print( round(   10**(  i+0.045757490560241    )   )**2   ,  end=" "  )
    '''   121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 1234567900987654321 '''
    print()
    # print("\n==========>\n")
    for i in range(       int(( number ))     ):
        print(   round(   10**(  i+0.045757490560241    )   )**2   ,  end=" "  ) # 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321
    print()
    # print("\n==========>\n")
    for i in range(       int(( number ))     ):
        print(   round(   10**(  i+0.045757490560241    )   )      ,  end=" "  ) # 1 11 111 1111 11111 111111 1111111 11111111 111111111
    print()
    # print("\n==========>\n")
    for i in range(       int(( number ))     ):
        print(            10**(  i+0.045757490560241    )          ,  end=" "  )
    ''' 1.1111111111100005 11.111111111100003 111.11111111100003 1111.1111111100001 11111.111111100014 
        111111.11111100014 1111111.1111100013 11111111.111100014 111111111.11100014                                 '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.04575749056069    )          ,  end=" "  )
    ''' 1.1111111111111491 11.111111111111489 111.1111111111149  1111.1111111111488 11111.11111111149 
        111111.1111111149  1111111.111111149  11111111.111111488 111111111.11111511                                 '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_560_675_687    )          ,  end=" "  )
    ''' 1.1111111111111125 11.111111111111125 111.11111111111126 1111.1111111111125 11111.111111111126 
        111111.11111111126 1111111.1111111126 11111111.111111125 111111111.11111103                                 '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_560_675_688    )          ,  end=" "  )
    ''' 1.1111111111111125 11.111111111111125 111.11111111111126 1111.1111111111125 11111.111111111126 
        111111.11111111126 1111111.1111111126 11111111.111111125 111111111.11111148                                 '''
    # print("\n\n==========>")
    print()
    for i in range(       int(( number ))     ):
        print(            10**(  i+0.045757491_000000    )          ,  end=" "  )
    ''' 1.111111112235092  11.111111122350922 111.11111122350917 1111.1111122350917 11111.111122350916 
        111111.11122350917 1111111.1122350916 11111111.122350916 111111111.22350916                                 '''

    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_126_381_3   )          ,  end=" "  )
    ''' 1.1111111100000017 11.111111100000016 111.11111100000016 1111.1111100000016 11111.111100000016 
        111111.11100000016 1111111.1100000017 11111111.100000016 111111110.99999994                                 '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_126_381_4   )          ,  end=" "  )
    ''' 1.111111110000002  11.111111100000016 111.11111100000016 1111.1111100000016 11111.111100000016 
        111111.11100000016 1111111.1100000017 11111111.100000016 111111111.0000004                                  '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_126_38    )          ,  end=" "  )
    ''' 1.1111111099999984 11.111111099999983 111.11111099999982 1111.1111099999982 11111.111099999995 
        111111.11099999995 1111111.1099999994 11111111.099999994 111111110.99999994                                  '''
    # print()
    # for i in range(       int(( number ))     ):
    #     print(            10**(  i+0.045_757_490_126_383    )          ,  end=" "  )
    ''' 1.111111110000006  11.111111100000063 111.11111100000062 1111.1111100000062 11111.111100000062 
        111111.11100000063 1111111.1100000062 11111111.100000063 111111111.0000004                                   '''
    # print("\n\n==========>")
    print()
    for i in range(       int(( number ))     ):
        print(   round(   10**(  i+0.045757490560241 -1 )   )**2   ,  end=" "  )
    ''' 0 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321                                   '''


    # print("\n\n==========>")
    print()
    """ [+++++] ciekawe """
    ''' satcos 9 months ago    How about this? '''
    for i in range(   1,  int(( number ))+1   ):
        print(   int(round(   0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   ),   0 ))**2   ,  end=" "  )
    print() # 1   121   12321   1234321   123454321   12345654321   1234567654321   123456787654321   12345678987654321
    for i in range(   1,  int(( number ))+1   ):
        print(       round(   0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   ),   0 ) **2   ,  end=" "  )
    print() # 1.0 121.0 12321.0 1234321.0 123454321.0 12345654321.0 1234567654321.0 123456787654321.0 1.234567898765432e+16
    """ [+] """
    for i in range(   1,  int(( number ))+1   ):
        print(       round(   0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   )      ) **2   ,  end=" "  )
    print() # 1   121   12321   1234321   123454321   12345654321   1234567654321   123456787654321   12345678987654321
    # for i in range( 1,  int(( number ))+1   ):
    #     print(              0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   )        **2   ,  end=" "  )
    # print()#11.11111111124342 1111.1111111375733 111111.11111508054 11111111.111640355 1111111111.1772656 111111111119.04996 11111111112037.26 1111111111216960.0 1.1111111112301941e+17
    for i in range(   1,  int(( number ))+1   ):
        print(       round(   0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   )      )       ,  end=" "  )
    print() # 1                  11                111                1111               11111              111111             1111111            11111111           111111111
    for i in range(   1,  int(( number ))+1   ):
        print(               0.1111111111111111*(   2.71828182845904523536028747 **(  2.302585093*i  )   )               ,  end=" "  )
    print() # 1.1111111111177265 11.11111111124342 111.11111111309583 1111.1111111375733 11111.111111441884 111111.11111508054 1111111.1111574185 11111111.111640355 111111111.11706525
    for i in range(   1,  int(( number ))+1   ):
        print(                                      2.71828182845904523536028747 **(  2.302585093*i  )                   ,  end=" "  )
    print() # 10.00000000005954  100.0000000011908 1000.0000000178625 10000.00000023816  100000.00000297696 1000000.0000357248 10000000.000416767 100000000.0047632 1000000000.0535873
    for i in range(   1,  int(( number ))+1   ):
        print(                                                                        2.302585093*i                      ,  end=" "  )
    print() #  2.302585093       4.605170186       6.907755279        9.210340372        11.512925464999999 13.815510558       16.118095650999997 18.420680744      20.723265837

    # print("\n\n==========>")
    print()
    ''' proefje2 11 months ago    anyone else sweating on this for hours and coming up with an overly complicated solution? 
                                  Still got some experience with lambda out of it though. '''
    for i in range(   1,  int(( number ))+1   ):
        print(   sum(map(   lambda n:   1 if n==1
                                        else 10**(n-1) * 2 * int(  6.11111111111 * 10**(n-2)   )
                          , range(1, i+1)                                                          ))   ,  end=" "  )



    ''' sidputul1997 4 months ago   
    very manipulative answer by seeing all the testcases and then manipulating answer according to that... '''
    ''' aishwaryakulkar3 4 months ago    Time to leave this planet :D '''




    ''' leo_kamwathi 11 months ago    Solving using math. (python3) 
    HINT 1:	1^2 = 1 		11^2 = 121 		111^2 = 12321 		1111^2 = 1234321	..etc 
    HINT 2:	1/9 = 0.1111 	10/9=1.11111 	100/9=11.1111				..etc 
    HINT 3:	10//9 = 11 		100//9 = 111 	1000//9 = 1111 				See below for solution if you still can't solve. '''
    # print("\n\n==========>\n==========>")
    print("\n")
    ''' somendrakumar 1 year ago    just use math's trick:    
    pow(1,2)=1 pow(11,2)=121 pow(111,2)=12321 pow(1111,2)=1234321 and so on code will be :: '''
    for i in range(  1,  int( number )+1  ):
        print(   pow(   (  pow(10,i) -1  )//9   ,2   )   ,  end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(          (  pow(10,i) -1  )//9            ,  end=" "   ) # 1 11 111 1111 11111 111111 1111111 11111111 111111111
    print()
    for i in range(  1,  int( number )+1  ):
        print(             pow(10,i) -1                  ,  end=" "   ) # 9 99 999 9999 99999 999999 9999999 99999999 999999999
    print()

    # print("\n==========>\n")
    ''' triii_10 11 months ago    Each line of the pattern is the square of 1 repeated i times (like 1,11,111.. and so on) 
    These terms are basically the sum of a geometric series with i terms having a = 1 and r = 10. 
    We could have achieved so by "1"*i but using strings isn't allowed.     So the print statement becomes: '''
    for i in range(  1,  int( number )+1  ):
        print(            (   ( 10**i -1 )//(10-1)   )**2       ,  end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(            (   ( 10**i -1 )//  9      )**2       ,  end=" "   )
    # print()
    # for i in range(1,  int( number )+1  ):
    #     print(          (   ( 10**i -1 ) /  9      )**2 )#    ,  end=" "   )
    ''' 1.0                 ... 1234321.0               ... 1234567654321.0
        121.0                   123454321.0                 123456787654321.0
        12321.0 ...             12345654321.0 ...           1.234567898765432e+16 '''
    print()
    # print("\n==========>\n")
    ''' d0m00re 2 years ago    I fail at 9, any idea?    I begin this number form : 1, 111 ,..., 11111    Then : 111 ** 2 '''
    for i in range(  1,  int( number )+1  ):
        # print( int( pow( (pow(10.0,i) - 1.0)   /9.0   ,  2.0    ) ) ,  end=" "   )
        # print( int(    (   (  10.0**i - 1.0  ) /9.0   )**2.0    )   ,  end=" "   ) # ... 12345678987654320
        print(   int(    (   (  10.0**i - 1.0  )//9.0   )**2.0    )   ,  end=" "   ) # ... 12345678987654320
    print()

    # print("\n==========>\n")
    """ [+++] on the left side of the math ;) _ _ _ and int() after squaring _ _ _ had to add slash """
    ''' hoangthinh379902 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        # print( int(     (   ( 1 -10**i ) /(1-10)   )**2   )   ,  end=" "   ) # ! ... 12345678987654320 !
        print(   int(     (   ( 1 -10**i )//(1-10)   )**2   )   ,  end=" "   ) #   ... 12345678987654321
        # print(          (   ( 10**i -1 )//(10-1)   )**2       ,  end=" "   )
    print(); """ the same """
    # print("\n==========>\n")
    ''' satapathykbichi1 2 years   1 = 1^2   121 = 11^2   12321 = 111^2   So on...
    So basically we need to find       1^2,   11^2,         111^2,              1111^2,  11111^2.
    Now if we check similarity between 1,     11,           111,                1111, 11111,... Each number follows a equation.
    i.e.  1 + x^2 + x^3 + x^4+... ...x^n-1.   11 = 1+10^2   111 = 1+10^2+10^3   1111 = 1+10^2+10^3+10^4 so on.
    Now summation of this equation = (1-10^(n+1))/1-10 This is a case of geometric progression problem. Equation: 1 + '''
    for i in range(  1,  int( number )+1  ):
        # print(          (   ( 1-(10**(i)))//(-9)   )**2   )
        print(            (   (  1 -10**i  )// -9    )**2       ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' Abhxz 2 years ago '''
    for i in range(  0,  int( number )    ):
        print(            (   (  10**i       )
                            + (  10**i  //9  )   )**2   ,  end=" "   )
    print()
    ''' liamroche 2 years ago
        print(   (   10**(i-1)  +  (10**(i-1)-1) /9   )**2   ,  end=" "   )
            0.0 1.0 121.0 12321.0 1234321.0 123454321.0 12345654321.0 1234567654321.0 123456787654321.0
        print(   (   10**(i  )  +  (10**(i  )-1)//9   )**2   ,  end=" "   ) '''


    # print("\n==========>\n")
    ''' umberto_griffo 1 year ago    If you look at this pattern:    << picture link >>    
    the pattern is:    '''
    # a(i)   =    (   i*(  (10^n) //9  )   )^2      // ( i^2 )
    '''    for example, given i = 2 '''
    # a(2)   =    (   2*(  (10^2) //9  )   )^2      // ( 2^2 )
    #        =    (   2*(   11         )   )^2      // (  4  )
    #        =     22*22 //4   =   484 //4   =   121
    for i in range(  1,  int( number )+1  ):
        print(    (   i*(   10**i //9  )   )**2     //   i**2   ,  end=" "   )
    print()

    ''' unpacking '''
    # print("\n==========>\n")
    ''' malrefai 3 years ago '''
    # print(   *map(   lambda i:   ((10**(i+1) - 1)//9)**2
    #                , range(int( number .strip()))           ), sep='\n')
    ''' AttributeError: 'int' object has no attribute 'strip' '''
    print()

    # print("\n==========>\n")
    ''' abhimanyuisqwer1 1 year ago    some what this is suppose to be solution 
    but don't know why not working for last number in case of n=9......... '''
    for i in range(  1,  int( number )+1  ):
        print(   int(               (  100**i -1  )  /99
                      + ( 2/9 )*(   (  100**i -1  )  /99
                                  - (   10**i -1  )  / 9
                                 )                        )   ,  end=" "   ) # !      ... 12345678987654320 !
    print() ; ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654320 '''
    ''' ( 2//9 )  1 101 10101 1010101 101010101 10101010101 1010101010101 101010101010101 10101010101010101 '''




    ''' Chessifer 4 years ago    ( There is no max int limits in python. ) 
    The reason is cause if you don't use integer division you're squaring float numbers, 
    and that returns float numbers. Example
        With float division:        ((10^2-1) /9)^2  =  ((99) /9)^2  =  11.0^2  =  121.0
        With integer division:      ((10^2-1)//9)^2  =  ((99)//9)^2  =  11  ^2  =  121
    This only happens in Python 3 
    cause in Python 2 the default behaviour for / operator was integer division 
    (Unless you imported division from __future__ module). 
    In Python 3 the behaviour for / is float division and integer division is // '''
    # print()
    # for i in range(  1,  Decimal( str( number ) )+1  ):
    #     print(               (( 10**i -1 )//9)**2        ,  end=" "   )

    # print("\n\n==========>")
    # print()
    # ''' pruthiviraj784 1 month ago    my solution : '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   (   10**(i) //9   )**2   ,  end=" "   )          #  (i)





    # print("\n==========>\n")
    ''' EvenParity 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        h = 1  if  i == 1    else    h*10 + 1         ;            print(   h**2   ,  end=" "   )
    print()


    # print("\n==========>\n")
    ''' TiGaDeveloper 2 years ago    REPAIRED '''
    for i in range(   1,  int(( number ))+1   ):
        print(   int( (    (  10**(float(i)) -1  )**2    )/81   )
               +    ( (    (  10**(float(i)) -1  )**2    )%81>0 )   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' vivekraja98 1 year ago    This series is called Demlo number : Refer : http://mathworld.wolfram.com/DemloNumber.html '''
    for i in range(  1,  int( number )+1  ):
        # print( int((   (  10 **i    -1  )**2   ) /81)  ,  end=" "   ) # ! ... 12345678987654320 !
        print(   int((   (  10 **i    -1  )**2   )//81)  ,  end=" "   ) #   ... 12345678987654321
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 '''
    print()

    # print("\n==========>\n")
    """ zrobiłem z przepisu """
    ''' husoski 10 months ago    I did something similar, 
    but simplified it a bit by squaring (10 * * ( i+1) - 1) and dividing just once by 81. 
    The (i+1) is because I looped over range(int(input)).
        Thumbs up for actually using some math on a math problem! 
    I'm sure you're going to mystify the crowd that still thinks 0.999... is less than 1. :^) '''
    for i in range(  1,  int( number )    ):
        print(          (( 10**(i+1) -1 ))**2      ,  end="  \t"   )
    ''' 801  	998001  	99980001  	9999800001  	999998000001  	99999980000001  	9999999800000001  	999999998000000001      '''
    print()
    for i in range(  1,  int( number )    ):
        print(          (( 10**(i+1) -1 ))**2  /81    ,  end=" \t"   )
    ''' 121.0 	12321.0 	1234321.0 	123454321.0 	12345654321.0 	1234567654321.0 	123456787654321.0 	1.234567898765432e+16   '''
    print()
    # print("\n==========>\n")
    list_of_desired = []
    for i in range(  1,  int( number )    ):
        print(   int(   (( 10**(i+1) -1 ))**2  /81)    ,  end="   \t"   )
        ''' 121   	12321   	1234321   	123454321   	12345654321   	1234567654321   	123456787654321   	12345678987654320       '''
        list_of_desired.append(   int(   (( 10**(i+1) -1 ))**2  /81)    ) # o
    print()
    for i in list_of_desired: print(  i*81    ,  end="   \t"   )
    '''     9801   	998001   	99980001   	9999800001   	999998000001   	99999980000001   	9999999800000001   	999999997999999920      '''

    # print("\n==========>\n")

    print("\n    int(     10**i *( 10**i -2 )   /81   +1  )                ")
    for i in range(  1,  int( number )+1  ):
        print(   int(     10**i *( 10**i -2 )   /81   +1  )    ,  end=" "   )
    print("\n             10**i *( 10**i -2 )   /81                        ")
    for i in range(  1,  int( number )+1  ):
        print(            10**i *( 10**i -2 )   /81            ,  end=" "   )
    ''' 0.9876543209876543 120.98765432098766 12320.987654320988 1234320.987654321  123454320.98765433 
                           12345654320.987654 1234567654320.9875 123456787654320.98 1.234567898765432e+16 '''
    print("\n    ceil(    10**i *( 10**i -2 )   /81       )                ")
    for i in range(  1,  int( number )+1  ):
        print(   ceil(    10**i *( 10**i -2 )   /81       )    ,  end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654320 '''

    # print("\n==========>\n")
    print("\n\n\tint(     10**i *( 10**i -2 )  //81   +1  )                ")
    """ work [++-] """
    ''' ~~ tommasodelorenzo 1 day ago '''
    for i in range(  1,  int( number )+1  ):
        print(   int(     10**i *( 10**i -2 )  //81   +1  )    ,  end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 '''
    print("\n    int(     10**i *( 10**i -2 )  //81       )                ")
    for i in range(  1,  int( number )+1  ):
        print(   int(     10**i *( 10**i -2 )  //81       )    ,  end=" "   )
    ''' 0 120 12320 1234320 123454320 12345654320 1234567654320 123456787654320 12345678987654320 '''
    print("\n             10**i *( 10**i -2 )  //81                        ")
    for i in range(  1,  int( number )+1  ):
        print(            10**i *( 10**i -2 )  //81            ,  end=" "   )
    ''' 0 120 12320 1234320 123454320 12345654320 1234567654320 123456787654320 12345678987654320 '''
    # print("\n\n==========>")
    print("\n             10**i *( 10**i -2 )                              ")
    for i in range(  1,  int( number )+1  ):
        print(            10**i *( 10**i -2 )                  ,  end=" "   )
    ''' 80 9800 998000 99980000 9999800000 999998000000 99999980000000 9999999800000000 999999998000000000 '''
    print("\n             10^i                                             ")
    for i in range(  1,  int( number )+1  ):
        print(            10**i                                ,  end="\t"  )
    ''' 0	100	1000	10000	100000	1000000	10000000	100000000	1000000000	'''
    print("\n                      10^i - 2                                ")
    for i in range(  1,  int( number )+1  ):
        print(                   ( 10**i -2 )                  ,  end="\t " )
    ''' 8	 98	 998	 9998	 99998	 999998	 9999998	 99999998	 999999998	'''

    # print("\n\n==========>")
    print()
    ''' anandsingh9123 3 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   (   pow(100,i)  -  2*pow(10,i)  +  1   )//81  ,  end=" "   )
    print() # ''' anandsingh9123 ... M O D I F I E D '''
    for i in range(  1,  int( number )+1  ):
        print(   (      100**i   -   2* 10**i   +   1   )//81  ,  end=" "   )
    # print()
    # for i in range(  1,  int( number )+1  ):
    #     print(       100**i   -   2* 10**i   +   1           ,   end=" "   )
    ''' 81 9801 998001 99980001 9999800001 999998000001 99999980000001 9999999800000001 999999998000000001 '''
    # print()
    # for i in range(  1,  int( number )+1  ):
    #     print(   f"{ 100**i } - { 2* 10**i } +   1          ",   end="\n"  )
    ''' 100 - 20 +   1          
        10000 - 200 +   1          
        1000000 - 2000 +   1          
        100000000 - 20000 +   1          
        10000000000 - 200000 +   1          
        1000000000000 - 2000000 +   1          
        100000000000000 - 20000000 +   1          
        10000000000000000 - 200000000 +   1          
        1000000000000000000 - 2000000000 +   1   '''








    # print("\n\n==========>")
    print() ;    """  V E R Y   M U L T I L I N E   - - -   K I N D   O F  """
    """ [+++] """
    ''' olaf_nielsen 1 year ago    Another solution :    for n in range (1, 1+int(input())): print(pow(1 + sum(10 ** i for i in range(1, n)), 2))
    ... but not accepted by hackerrank, because it has two for loops.    Uglier version, with only one for loop (compressed to 2 lines):
    n = 1; last_n = int(input()) while n <= last_n : print(pow(1 + sum(10 ** i for i in range(1, n)), 2)); n += 1 '''
    n = 1   ;   last_n = int( number )
    while                              n <= last_n : print(pow(1 + sum(10 ** i for i in range(1, n)), 2)   ,  end=" "   ); n += 1
    print()
    n = 1   ;   last_n = int( number )
    while n <= last_n :    print(   (   sum(  10 **i   for i in range(1, n)  )+1   )**2   ,  end=" "   )   ;   n += 1
    print() ;    """  V E R Y   M U L T I L I N E   - - -   K I N D   O F  """

    # print("\n==========>\n")
    ''' ispulkit 3 years ago '''
    for i in range(   1,  int( number )+1   ):
        print(   sum(   10**j for j in range(  i-1,  -1,  -1  )   )**2   ,  end=" "   )
    print()
    for i in range(   9,         10         ):
        print(      [   10**j for j in range(  i-1,  -1,  -1  )   ]      ,  end=" "   )
    print(); ''' [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1] '''

    # print("\n==========>\n")
    ''' svc007 1 month ago '''
    n = 1
    for i in range(   1,  int( number )+1   ):        print(   n*n   ,  end=" "   )   ;       n  =  10**i + n
    print()
    ''' d355587 1 month ago ''' ''' rangithkumar98 2 months ago '''
    b = 0
    for i in range(       int( number )     ):        b  =  10*b + 1        ;    print(   b*b   ,  end=" "   )
    print()

    # print("\n==========>\n")
    """ after adaptation for python 3 it is working, but I'm not sure if I wont to understand it """
    ''' mahesh_waikar 3 years ago ''' """ big respect ! """ """ no strings """
    N = int( number )
    for i in range(  1,  N+1  ):
        size = i

        size = ( size*2 ) -1
        i = 0
        j = size - 1
        k = 1

        a = [0] * size

        mid = size / 2

        if size % 2 != 0:
            while   i < mid   and   j > mid   :
                a[i] = k
                a[j] = k
                i += 1
                j -= 1
                k += 1
            a[int(mid)] = k
        else:
            while i < j:
                a[i] = k
                a[j] = k
                i += 1
                j -= 1
                k += 1

        str1 = "".join(  [  str(x) for x in a  ]  )
        print(   str1   ,  end=" "   )
    print() ;    """  A   L I T T L E   B I T   M U L T I L I N E  """

    # print("\n==========>\n")
    ''' harsimransingh31 3 years ago '''
    m = 0
    for i in range(  1,  int( number )+1  ):
        for j in range(   1,  i+1      ):                 m =   m  +  j * 10**(j-1)
        j += 1 # indent deeper do the same work ;)      # m =   m + j*pow( 10, j-1  )
        for k in range(  i-1,  0,  -1  ):                 m =   m  +  k * 10**(j-1);            j += 1
        print(   m    ,   end=' '   )                   # m =   m + k*pow( 10, j-1  )
        m = 0
    print()

    # print("\n==========>\n")
    ''' nasirkhancse 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        k = i
        for j in range(  1, i  ):            print(  j,  end=''  )
        while  k > 0            :            print(  k,  end=''  )    ;            k -= 1
        # print(   '\n',   end=''   )
        print(             end=" "  )
    print()

    # print("\n==========>\n")
    ''' romarioagros66 3 years ago '''
    m = []
    for i in range(  1,  int( number )+1  ):
        m.append(str(i))
        if   i==1:      print(   int(   "".join( m )             )       ,   end=' '   )
        elif i==2:      print(   int(   "".join( m )   +   "1"   )       ,   end=' '   )
        else     :      print(   int( ( "".join( m )
                                       +"".join( m[ -2 : : -1 ]  ) ) )   ,   end=' '   )
    print() ;    """  V E R Y   M U L T I L I N E  """

    # print("\n==========>\n")
    ''' remainer00 2 years ago    i don't know which part in my code is problem.. '''
    N =                  int( number )
    L = list(range(  1, N+1  ))
    for i in range(  N  ):
        a = L[ :i]  +  L[i::-1]                     #;        print( '\n', a , end='    <--  ' )
        b = [  str(x) for x in a  ]                 #;        print(       i             )
        print(   ''.join(b)   ,   end=' '   )
    ''' print( a ) --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1] '''
    ''' print( b ) --> ['1', '2', '3', '4', '5', '6', '7', '8', '9', '8', '7', '6', '5', '4', '3', '2', '1'] '''
    print    (   )

    N =                  int( number )
    L = list(range(  1, N+1  ))
    for i in range(  N  ):
        a = L[ :i]  +  L[i::-1]                     #;        print( '\n', a , end='    -join->   ' )
        # print(   ''.join(str(a))   ,   end=' '   ) # nie joinuje
        '''  [1, 2, 3, 4, 5, 4, 3, 2, 1]    <--  [1, 2, 3, 4, 5, 4, 3, 2, 1] '''
        print(   ''.join( [  str(x) for x in a  ] )   ,   end=' '   )
    print(   )

    # print("\n==========>")
    print() ;    """  V E R Y   M U L T I L I N E  """
    """ [+++] """
    ''' harryluke 9 months ago    Pretty ugly but it works haha '''
    # for _ in range(  0,  int( number )    ):
    S = int( number )
    x = 1   ;   y = 1
    while(  x <= S  ):
        while(  y < x  ):            print(   y,   end=""   );            y += 1
        while(  y > 0  ):            print(   y,   end=""   );            y -= 1
        y += 1   ;    x += 1
        print(   end=" "   )
    print() ;    """  V E R Y   M U L T I L I N E  """

    # print("\n==========>\n")
    ''' mohdzabeerali 2 months ago '''
    # for _ in range(  1,  int( number )+1  ):
    ''' 121 12321 1234321 ... 12345678987654321 1234567900987654321 '''
    for _ in range(  0,  int( number )    ):
        val = 0
        i   = 0
        while(  i <= _  ): #    while  i <= _  :     # nawiasy można pominąć
            val += 10**i
            i   += 1
        print(   val**2   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' rockershah45 11 months ago    i Solved this problem. it is a basic problem of power 
    but i am unable to short it into 2 lines because my grip on logic is a little loose right now. '''
    temp1 = 0
    temp2 = 1
    for i in range(   1,  int(( number ))+1   ):
        # print(   f"\t  temp1 = {temp1}\ttemp2 = {temp2} "   ,  end=" "  )
        temp2 += temp1
        print(   temp2**2   ,  end=" "  )
        temp1 = 10**i
        # print()
        '''  ~	  temp1 = 0			temp2 = 1  1							temp1 = 0	temp2 = 1  1 
                  temp1 = 10		temp2 = 1  121 							temp1 = 10	temp2 = 1  121 
                  temp1 = 100		temp2 = 11  12321 						temp1 = 100	temp2 = 11  12321 
                  temp1 = 1000		temp2 = 111  1234321 					temp1 = 1000	temp2 = 111  1234321 
                  temp1 = 10000		temp2 = 1111  123454321 				temp1 = 10000	temp2 = 1111  123454321 
                  temp1 = 100000	temp2 = 11111  12345654321 				temp1 = 100000	temp2 = 11111  12345654321 
                  temp1 = 1000000	temp2 = 111111  1234567654321 			temp1 = 1000000	temp2 = 111111  1234567654321 
                  temp1 = 10000000	temp2 = 1111111  123456787654321 		temp1 = 10000000	temp2 = 1111111  123456787654321 
                  temp1 = 100000000	temp2 = 11111111  12345678987654321 	temp1 = 100000000	temp2 = 11111111  12345678987654321  '''
    print()

    # print("\n==========>\n")
    ''' Prg_NIT 1 year ago '''
    for i in range(   1,  int(( number ))+1   ):
        s = 0                                                  # ; print(   '\n'   )
        for j in range(  i, 0, -1  ):
            # print(   f's = {s}    j = {j}    10**(j-1) = {10**(j-1)}'   )#,   end='    ')
            s =  s  +  10**(j-1)                               # ; print(   '   ',  s   )
        print(   s*s   ,   end=" "   )
    ''' s = 0       j = 3    10**(j-1) = 100
            1100
        s = 1100    j = 2    10**(j-1) = 10
            1110
        s = 1110    j = 1    10**(j-1) = 1
            1111                                    12321 '''
    print(); ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 '''

    # print("\n==========>\n")
    ''' qiz2161 2 years ago    k = i*(10**(i-1));    for j in range(1,i):        k += (j*(10**(i+(i-j)-1)) + (j*(10**(i-(i-j)-1))));    print(k)'''
    for i in range(   1,  int(( number ))+1   ):
        k =  i*(  10**( i-1 )  )
        for j in range( 1,i ):            k  +=          j*(  10**(  i +(i-j) -1  ))      \
                                                   + (   j*(  10**(  i -(i-j) -1  ))   )
        print(k   ,   end=" "   )
      # k =  i*(  10**( i-1 )  )    #;    print(  )
      # for j in range( 1,i ):
      #     # print( k , end='  +  ' ); # 900000000
      #     # print(   f'i{  i  } j{  j  }  {            j*(  10**(  i +(i-j) -1  ))  } '
      #     #          f'+ {                             j*(  10**(  i -(i-j) -1  ))  } '      )
      #     k                                +=          j*(  10**(  i +(i-j) -1  ))      \
      #                                            + (   j*(  10**(  i -(i-j) -1  ))   )
      # print(k   ,   end=" "   )   #;    print()
    ''' 10000000900000001        i9 j1  10000000000000000 + 1  +  900000000
        12000000900000021        i9 j2  2000000000000000 + 20  +  900000000
        12300000900000321        i9 j3  300000000000000 + 300  +  900000000
        12340000900004321        i9 j4  40000000000000 + 4000  +  900000000
        12345000900054321        i9 j5  5000000000000 + 50000  +  900000000
        12345600900654321        i9 j6  600000000000 + 600000  +  900000000
        12345670907654321        i9 j7  70000000000 + 7000000  +  900000000
        12345678987654321        i9 j8  8000000000 + 80000000  +  900000000 '''
    print()

    # print("\n==========>\n")
    ''' shironyasha 2 years ago    Spent 3 hours to write this: '''
    for i in range(   1,  int(( number ))+1   ):
        print(   sum(      j* 10**(j-1)
                      +(   j* 10**(i-j)   *   10**(i-1)   )      for j in range(1,i)   )
               + i* 10**(i-1)                                                              ,   end=" "   )
        # print()
        # for j in range(1,i):
        #   print(   f'{   j* 10**(j-1)  } '
        #         f'+ ( {  j* 10**(i-j)  }*{  10**(i-1) } )'     ),
        # print(  f'+ {i* 10**(i-1)  }\n\n'                                                ,   end=" "   )
        '''  12345678987654321 
            1 + ( 100000000*100000000 )
            20 + ( 20000000*100000000 )
            300 + ( 3000000*100000000 )
            4000 + ( 400000*100000000 )
            50000 + ( 50000*100000000 )
            600000 + ( 6000*100000000 )
            7000000 + ( 700*100000000 )
            80000000 + ( 80*100000000 )
            + 900000000                 '''
    print()

    # print("\n==========>\n")
    ''' be149 2 years ago    The following code was graded as incorrect, despite producing seemingly-correct output: '''
    for i in range(   1,  int(( number ))+1   ):
        print (  sum(  [   x* 10**(x-1)
                         +(x* 10**(  2*y -x -1  )     if x<y    else   0   )
                         for x in range(  1, y+1  )                           ]  )   ,   end=" "   )
        ''' 1 1 1 1 1 1 1 1 1 '''
    print()


    # print("\n==========>\n")
    ''' kalidindi_rajeev 2 years ago    Bit lengthy but: '''
    ''' liamroche 2 years ago   I suggest you read the comment in your code! (From the problem) '''
    count = 1
    count_prev = 0
    string1 = ''
    string2 = ''
    for i in range(      int( number )    ): # More than 2 lines will result in 0 score. Do not leave a blank line also
        string1 = string1 + str(count)

        print(   f'count_prev:{ count_prev }'   ,  end='  '      )
        print(   f'count:{      count      }'   ,  end='\t   '   )
        print(   f'string1:{    string1    }'   ,  end='  '      )
        print(   f'string2:{    string2    }'   ,  end='  '      )
        # print(        string1  +  string2[::-1]           ,   end=" "    )
        print(   f'"{   string1  +  string2[::-1]   }"'   )#,   end='\t   ')

        count_prev = count        #  ;       print(   f'count_prev:{ count_prev }'   ,  end='\t   '   )
        count = count + 1         #  ;       print(   f'count:{      count      }'   ,  end='\t   '   )
        if count != 1:
            string2 = string2 + str(count_prev)
    '''        count_prev:0  count:1	   string1:1  string2:  "1"
               count_prev:1  count:2	   string1:12  string2:1  "121"
               count_prev:2  count:3	   string1:123  string2:12  "12321"
               count_prev:3  count:4	   string1:1234  string2:123  "1234321"
               count_prev:4  count:5	   string1:12345  string2:1234  "123454321"
               count_prev:5  count:6	   string1:123456  string2:12345  "12345654321"
               count_prev:6  count:7	   string1:1234567  string2:123456  "1234567654321"
               count_prev:7  count:8	   string1:12345678  string2:1234567  "123456787654321"
               count_prev:8  count:9	   string1:123456789  string2:12345678  "12345678987654321" '''

    # print("\n==========>\n")
    ''' sanjanasuresh241 2 years ago '''
    for counter in range(   1,  int(( number ))+1   ):
        for counter__UP in range(        1        ,   counter+1       ):    print(   counter__UP,   end = ''   )
        for counterDOWN in range(  counter__UP-1  ,       0      ,-1  ):    print(   counterDOWN,   end = ''   )
        print(   ' ',   end=''   )
    print()
    # print("\n==========>\n")
    ''' Tomash '''
    list_BIG = []
    for counter in range(   1,  int(( number ))+1   ):
        list_small = []
        for counter__UP in range(        1        ,   counter+1       ):    list_small.append(  counter__UP  )
        for counterDOWN in range(  counter__UP-1  ,       0      ,-1  ):    list_small.append(  counterDOWN  )
        list_BIG.append(  list_small  )    #;    print(   list_small   )
    # print(   list_BIG   )
    for elem in list_BIG:
        for elemencik in elem:    print(   elemencik   ,   end=''   )#   ,   sep=''   ,   end=''   )
        print(   ''   ,   end=' '   )
    print()

    # print("\n==========>\n")
    ''' pycops 2 years ago '''
    def make_triangle( n ):
        for i in range(  1, 2*int(n)  ):
            total_num = ''
            if i % 2 != 0:
                for text      in range(    1 ,  i//2  +2  ):            total_num += str(text)
                for remaining in range(  i//2,    0,  -1  ):            total_num += str(remaining)
                print(   int(total_num)   ,  end=" "   )
    make_triangle( number )
    print()
    for i in range(  1, 2*int(number)  ):
        total_num = ''
        if i % 2 != 0:
            for text      in range(    1 ,  i//2  +2  ):                total_num += str(text)
            for remaining in range(  i//2,    0,  -1  ):                total_num += str(remaining)
            print(   int(total_num)   ,  end=" "   )
    print()

    # print("\n==========>\n")
    """  V E R Y   M U L T I L I N E  """
    ''' ram9151 9 months ago '''
    # list = []
    # for i in range(      int( number )+1  ):
    #     list.append(i)
    #     x = list[1:]
    #     if len(x)==1:            print(   *x   )
    #     else        :            print(   *x + x[  len(x)-2  :  : -1  ]   ,  sep=''   ,  end=" "   )
    ''' TypeError: 'list' object is not callable '''




    # print("\n==========>\n")
    """  O N E   L I N E   [++++] to im wyślę ... a nie można, bo tam już jest pierwsza linijka :\ """
    """ Generator moze drukować _ _ _ list  L I S T  literal """
    ''' jmw1906 4 months ago    Why using two lines if one is enough (python3)? '''
    # [ print(   (10**i//9)**2               )    for i in range(  1,  int( number )+1  )   ]
    [   print(   (10**i//9)**2  ,  end=" "   )    for i in range(  1,  int( number )+1  )   ]
    print()
    # print("\n==========>\n")
    ''' ravi5197 1 year ago '''
    print(  *[  ((10**i-1)//9)**2                 for i in range(  1,  int( number )+1  )   ]  ,   sep='\n'
            ,  end=" "   )  ;  '''  ,  end=" "   ) --- doesn't work here                                            '''
    print()

    # print("\n==========>\n")
    ''' Odiumediae 4 years ago    Weirdly enough, this:    """ [++ ] """
    print(  *[   int( i* '1' )**2                 for i in range(  1,  int( number )+1  )   ]  ,   sep="\n"  )      '''
    print(  *[   int( i* '1' )**2                 for i in range(  1,  int( number )+1  )   ]  ,   sep=' '   ) # , sep="\n")
    print()

    # print("\n==========>\n")
    ''' sanoj_mv_93 3 months ago '''
    # b = int(input())
    # for i in range(  1, b+1  ):
    for i in range(  1,  int( number )+1  ):
        g = '1'*i
        h = int( g ) **2
        print(   h   ,  end=" "   )
    print()







    print("\n USING STRINGS:\n")

    # print("\n==========>\n")
    ''' Tomash '''
    for i in range(  1,  int( number )+1  ):
        if i == 1  :    print(   i                                                                 ,  end=" "   )
        else       :    print(   '12345678987654321'[ : i ]  +  '12345678987654321'[-1*(i-1) : ]   ,  end=" "   )
    print()
    ''' Tomash '''
    for i in range(  1,  int( number )+1  ):
        if i == 1  :    print(   i                                                                 ,  end=" "   )
        else       :    print(   '12345678987654321'[ : i ]  +  '12345678987654321'[-   i+1  : ]   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' vahram_son 2 years ago    WHYYYY? DON'T WORK '''
    for i in range(  1,  int( number )+1  ):
        # print( "{}{}".format(   '123456789'[:i],   '987654321'[10-i:]   )   ,  end=" "   )
        print(   "{}{}".format(   '123456789'[:i],   '_87654321'[10-i:]   )   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' mtscampagnolo 2 years ago ''' """[!!!]"""
    for i in range(  1,  int( number )+1  ):
        print(                    '123456789'[:i]  + '12345678_'[:i-1][::-1]  ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' sherhy 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        # print(  "123456789"[  0  : i-1       ]
        #      +  "123456789"[ i-1             ]
        #      + "0123456789"[ i-1 :  0  : -1  ]   ,  end=" "   )
        print(    "123456789"[     :  i        ]
               #+ "123456789"[ i-1             ]
               + "0123456789"[ i-1 :  0  : -1  ]  ,  end=" "   ) # that zero is crucial
    print()


    # print("\n==========>\n")
    """UP"""
    ''' 14ravisoni 8 months ago '''
    e = '11111111111111111111111111111111111111111111111111'
    for i in range(  1,  int( number )+1  ):
        print(   (int(  e[:i]  )**2  )    ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' ezzobad 4 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   int( '1' * i )   *   int( '1' * i   )   )   ,  end=" "   )
        # print(        int( '1' * i )   *   int( '1' * i   )       ,  end=" "   ) # works the same
    print()
    # print("\n==========>\n")
    ''' drPY3 9 months ago '''
    # print(  [   int(   '1' (i+1)   )**2
    #             for i in range(      int( number )    ) if True   ],   sep="\n"   )
    ''' TypeError: 'str' object is not callable '''
    ''' [1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321] '''
    # print( *[   int(   '1'*(i+1)   )**2
    #             for i in range(      int( number )    ) if True   ],   sep="\n"   )
    print(   *[   int(   '1'*(i+1)   )**2
                  for i in range(      int( number )    ) if True   ]               )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321                     '''
    print(   *[   int(   '1'*(i+1)   )**2
                  for i in range(  1,  int( number )+1  ) if True   ]               )
    '''   121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 1234567900987654321 '''
    print()
    # print("\n==========>\n")
    ''' brianlin091994 4 weeks ago    Hi, there. I tried to use below code which is similar to yours 
    but comes out with error "invalid string literal found". Do you have any idea with it?  '''
    for i in range(  1,  int( number )+1  ):
        print(   pow(  int('1'*i), 2  )   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' krishnan_ashwin 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   str(1)*i   )**2   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' sanoj_mv_93 1 week ago '''
    for i in range(  1,  int( number )+1  ):
        g = '1'*i        ;        h = int(g) ** 2        ;        print(   h   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' Kjagadishreddy 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   ''.ljust(  i, '1'  )   )**2   ,  end=" "   )
    """ ljust    Return a left-justified string of length width.    Padding is done using the specified fill character (default is a space). """
    print()

    # print("\n==========>\n")
    ''' zackushka 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(    12345678987654321
                % eval(  '1'*10  +  '1'*(i-1) )
               // eval(  '1'     +  '0'*(9-i) )   ,  end=" "   )
        """        Evaluate the given source in the context of globals and locals.
        The source may be a string representing a Python expression    or a code object as returned by compile().
        The globals must be a dictionary and locals can be any mapping,  defaulting to the current globals and locals.
        If only globals is given, locals defaults to it.                                                            """
    print()

    # print("\n==========>\n")
    ''' ayus097836 3 years ago '''
    # print( "\n".join(  [  str(int(str(1)*i)*int(str(1)*i)) for i in range(  1,  int( number )+1  )  ]  )   ,  end=" "   )
    print(    " ".join(  [  str(   int( str(1)*i )**2   )    for i in range(  1,  int( number )+1  )  ]  )   ,  end=""   )
    print(); """ end=' ' is not workink here due to '\n' """

    # print("\n==========>\n")
    # ''' venkatasiva_pan1 2 years ago    Solution using strings: ''' ''' Python2 '''
    # n = int( number )
    # S = (string.digits)[1:n+1]
    # ''' NameError: name 'string' is not defined '''
    # for i in range(0,n):
    #     print(   S[0:i] + S[-n+i::-1]   ,  end=" "   )
    # print()

    # print("\n==========>\n")
    ''' nldrgomeser48 3 years ago    This gives correct output but doesn't pass the test case. Don't know why!! '''
    """ not for me """
    for i in range(  1,  int( number )+1  ):
        # print( ( '{}'*(  2*i -1  ) ).format(   (   list(range(  1,  i+1    ))
        #                                          + list(range( i-1,  0, -1 ))   )   )   )
        ''' IndexError: tuple index out of range '''
        # print(   '{}'               .format(   (   list(range(  1,  i+1    ))
        #                                          + list(range( i-1,  0, -1 ))   )   )   ,  end="   "   )
        ''' [1]   [1, 2, 1]   [1, 2, 3, 2, 1]   [1, 2, 3, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]   '''

    # print("\n==========>\n")
    ''' Baaaba 2 years ago _ _ _ MODIFIED '''
    y = ''
    for i in range(  1,  int( number )+1  ):
        # y += str(i);        print('{}'.format(y[::-1][1:])   ,  end=" "   )
        ''' 1 21 321 4321 54321 654321 7654321 87654321 '''
        y += str(i);
        # print( f'{  y  }',   f'{  y[:           :-1]  }',   sep=''   ,  end=" "   ) # 11 1221 123321 12344321 1234554321 123456654321 12345677654321 1234567887654321 123456789987654321
        # print( f'{  y  }',   f'{  y[:len(y)     :-1]  }',   sep=''   ,  end=" "   ) # 1 12 123 1234 12345 123456 1234567 12345678 123456789
        print(   f'{  y  }',   f'{  y[:len(y)-1][::-1]  }',   sep=''   ,  end=" "   )
    print()
    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i);
        # print( f'{  y  }',   f'{  y[ :  -1      :-1]  }',   sep=''   ,  end=" "   ) # 1 12 123 1234 12345 123456 1234567 12345678 123456789
        print(   f'{  y  }',   f'{  y[  : -1   ][::-1]  }',   sep=''   ,  end=" "   )
    print()

    ''' Tomash '''
    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i);
        z = ''.join(reversed(y))
        print(   f'{  y  }',   f'{  z[1:]               }',   sep=''   ,  end=" "   )
    print()

    # print("\n==========>\n")
    y = ''
    for i in range(  1,  int( number )+1  ):
        z = ''.join(reversed(y))
        y += str(i)
        print(   f'{  y  }',   ''.join(str(i)),   ''.join(reversed(y)),   sep=''   ,   end=" "   )
    print(); ''' 111 12221 1233321 123444321 12345554321 1234566654321 123456777654321 12345678887654321 1234567899987654321  '''
    ''' Tomash '''
    y = ''
    for i in range(  1,  int( number )+1  ):
        print(   f'{  y  }'   +   f'{  str(i)  }'   +   f'{  y[::-1]  }'           ,   end=" "   )
        y += str(i)
    print()

    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i)     ; z1 = y                    ; z2 = y[:-1]
        # print(y)      ; print(z1)                 ; print(z2)
        print(   f'{  z1  }',   f'{  "".join(reversed(z2))       }',   sep=''   ,   end=" "   )
    print()

    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i) ; z1 = y;                         z2 = y[:-1]
        print(   f'{  z1  }',   f'{  "".join(         z2[::-1])  }',   sep=''   ,   end=" "   )
    print()

    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i) ; z1 = y  ;                       z2 = y[:-1]
        print(   f'{  z1  }'  + f'{  "".join(         z2[::-1])  }'             ,   end=" "   )
    print()

    y = ''
    for i in range(  1,  int( number )+1  ):
        y += str(i) ; z1 = y  ;                       z2 = y[:-1]
        print(   f'{  z1      +      "".join(         z2[::-1])  }'             ,   end=" "   )
    print()

    # print("\n==========>\n")
    """ uses string & double 'for' """
    ''' Vedant1734810113 4 months ago    in case if you want a answer in more than one line(i know its more than one line just giving logic ) '''
    x,  z   =   int( number ),  ''
    for x in range(  1,  x+1  ):
        for j in range(  x,  x+1  ):
            z =  z + '' .join(str(1))
            #z=  z +('' .join(str(1))  ) # same effect
            #z= (z + '').join(str(1))    # =>   1 1 1 1 1 1 1 1 1
        print(   int(z) * int(z)   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' Harrison_Shen 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   ''.join(   list(map(   str,   [            k for k in range(  1,  i+1  )  ]
                                             + sorted(   [  m for m in range(  1,  i+1  )  ]
                                                       , reverse = True                        )[1:]   ))   ),   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   ''.join(        map(   str,   [            k for k in range(  1,  i+1  )  ] # list( ) can be omitted
                                             + sorted(   [  m for m in range(  1,  i+1  )  ]
                                                       , reverse = True                        )[1:]   )    ),   end=" "   )
    print()
    # print("\n==========>\n")
    ''' mushki 4 years ago    To change it to the desired output (you're printing a list of integers), 
    you should convert the list to a list of strings and then concatenate the whole into a single string. '''
    list_of_integers = [1,2,3]
    print(       ''.join(        map(   str,   list_of_integers   )   )  );     '''123'''
    ''' or, using list comprehension, '''
    print(       ''.join(   [  str(i) for i in list_of_integers  ]   )   );     '''123'''


    # print("\n==========>\n")
    ''' harryToHell 2 years ago '''
    for i in range(  1,  int( number )+1  ):
    #   a  =   [  str(x) for x in   (        range(1,i+1)    +         range(1,i)[::-1]    )  ] # Python 2 (?)
        ''' TypeError: unsupported operand type(s) for +: 'range' and 'range' '''
        a  =                [  str(x) for x in   (  list( range(1,i+1) )  +   list( range(1,i)[::-1] )  )  ]
        print(   ''.join(a)   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   ''.join(   [  str(x) for x in   (  list( range(1,i+1) )  +   list( range(1,i)[::-1] )  )  ]   )   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' RohanGautam 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   "".join(   [  str(x) for x in   (   [  x for x in range(  1,  i      )  ]
                                                   + [  y for y in range(  i,  0, -1  )  ]   )  ]   )   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' hafizimtiaz 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        # print( ''.join(   [  str(k) for k in            range( 1, i+1    )  ]
        #                 + [  str(k) for k in            range(i-1, 0, -1 )  ]   )   ,   end=" "   )
        print(   ''.join(   [  str(k) for k in            range( 1,  i     )  ]
                          + [  str(k) for k in            range( i,  0, -1 )  ]   )   ,   end=" "   )
    print(); """ similar ↓ ↓ ↓ somewhere down there ↓ ↓ ↓ """

    # print("\n==========>\n")
    ''' sankalp_jain2016 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(  ''.join(   map(  str,  (list(  list(   j for j in range(  1 , i+1      )   )
                                              +list(   k for k in range( i-1,  0 , -1  )   )   ))   ))   ,   end=" "   )
        # print(''.join(   map(  str,   list(  list(   j for j in range(  1 ,  i       )   )             # works the same
        #                                     +list(   k for k in range(  i ,  0 , -1  )   )   )    ))   ,   end=" "   )
        # print(''.join(   map(  str,          list(   j for j in range(  1 ,  i       )   )             # works the same
        #                                     +list(   k for k in range(  i ,  0 , -1  )   )        ))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    # ''' piotr1212 3 years ago '''
    for i in range(  1,  int( number         )+1  ):
        print(   str(   ''.join(   map(  str,  list(range(  1 ,   i      ))  )   )) # str() & list() are to omit
               + str(   ''.join(   map(  str,  list(range(  i ,   0, -1  ))  )   ))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' shantanu1395 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(          "".join(   map(  str,       range(  1 ,  i+1     )   )   )
                      + "".join(   map(  str,       range( i-1,   0, -1  )   )   )   ,   end=" "   )
        ''' dathu 2 years ago '''
        # print(        ''.join(   map(  str,       range(  1 ,   i      )   )   )
        #             + ''.join(   map(  str,       range(  i ,   0, -1  )   )   )   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' ObaidGill 2 years ago ''' """ added list() """
    # for i in range(1,  int( number.strip() )+1  ): # not definied
    for i in range(  1,  int( number )+1  ):
        print(          ''.join(   map(  str,  list(range(  1,  i+1      ))
                                              +list(range(  1,   i       ))[::-1]  )   )   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' piotr1212 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(          ''.join(   map(  str,  list(         range(  1,  i+1  ))   )   )
                      + ''.join(   map(  str,  list(reversed(range(  1,   i   )))  )   )   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' josericardopere1 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(          "".join(   map(  str,  [   x   for x in range(  1,  i+1  )  ]  )   )
                      + "".join(   map(  str,  [  i-x  for x in range(  1,   i   )  ]  )   )       ,   end=" "   )
    print();  #  print("\n==========>\n")
    ''' kylezs 2 years ago    Same for me. Though my approach was a little different:
        The      int()     isn't really necessary '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   "".join(   [  str(j) for j in range( 1, i     )  ]   )       #             int() isn't necessary
                      + "".join(   [  str(k) for k in range( i, 0, -1 )  ]   )   )   ,   end=" "   )
        # print(        "".join(   [  str(j) for j in range( 1, i     )  ]   )
        #             + "".join(   [  str(k) for k in range( i, 0, -1 )  ]   )       ,   end=" "   ) # works the same
    print(); ''' ericmuccino 2 years ago ''' ; #    print("\n==========>\n")
    for i in range(  1,  int( number )+1  ):
        print(          "".join(   [  str(j) for j in range( 1, i+1   )  ]
                                 + [  str(j) for j in range( 1, i     )  ][::-1] )   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' hedleypanama 4 years ago '''
    for i in range(  1,  int( number )+1  ): # i in range is allways int
        # print(        "".join(   [  str(j) for j in range( 1, i+1          )  ]   )
        #             + "".join(   [  str(j) for j in range( 1,  int( i )+1  )  ]   )[::-1][1:]   ,   end=" "   )
        print(          "".join(   [  str(j) for j in range( 1, i+1          )  ]   )
                      + "".join(   [  str(j) for j in range( 1, i+1          )  ]   )[::-1][1:]   ,   end=" "   )
        #             + "".join(   [  str(j) for j in range( 1, i+1          )  ][::-1][1:]   )   ,   end=" "   )
        #             + "".join(   [  str(j) for j in range( 1, i+1          )[::-1][1:]  ]   )   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' calmwmcauliffe 2 years ago    I have a working solution (py2), but fails on compile?? '''
    for i in range(  1,  int( number )+1  ):
        print(          ''.join(   [  str(j) for j in range( 0, i,  1 )  if j!=0  ]   )
                      + ''.join(   [  str(j) for j in range( i, 0, -1 )  if j!=0  ]   ),   end=" "   )
    print()
    # print("\n==========>\n")
    ''' ganeshkamath89 3 years ago '''
    # for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for i in range(  1,  int( number )+1  ):
        # print(        "".join(   [  str(j) for j in range( 1, i+1   )                 ]   )
        #             + "".join(   [ str(i-k)for k in range( 1, i+1   )  if (i-k != 0)  ]   ),   end=" "   )
        print(          "".join(      str(j) for j in range( 1, i+1   )                     )
                      + "".join(     str(i-k)for k in range( 1, i+1   )  if (i-k != 0)      ),   end=" "   )
    print()

    # print("\n==========>\n")
    ''' ganesh_dreamer 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        print(          "".join(      str(x) for x in range( 1, i     )      ), end=""             )
        print(          "".join(      str(x) for x in range( i, 0, -1 )      )       ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' aviralbansal29 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(          "".join(    str(x+1) for x in range(    i       )    )
                      + "".join(    str( x ) for x in range( i-1, 0, -1 )    )       ,   end=" "   )
    print()

    # print("\n==========>\n")
    """ add strip maybe - because it doesn't work for me """
    ''' mayel_espino 2 years ago    s1 = "".join([str(j) for j in range(1,i)]); s2 = "".join([str(j) for j in range(i-2,0,-1)]);print("{}{}".format(s1,s2))'''
    for i in range(  1,  int( number )+1  ):
        s1 =            "".join(   [  str(j) for j in range(  1,  i     )  ]   );
        # s2 =          "".join(   [  str(j) for j in range( i-2, 0, -1 )  ]   );   # StartingFromSpace
        '''  1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 '''
        # s2 =            "".join(   [  str(j) for j in range( i-1, 0, -1 )  ]   );
        '''  11 1221 123321 12344321 1234554321 123456654321 12345677654321 1234567887654321 '''
        # print(   "{}{}".format(  s1, s2  )   ,   end=" "   )
    print()


    ''' phanttan 6 months ago '''
    # for i in range(      int( number )    ):
    #     print(   ''.join(   [   str(j) for j in (   [  range( 1, i+2    )  ]
    #                                               + [  range( i,  0, -1 )  ]   )   ]   )   ,  end=" "   )
    ''' range(1, 2)range(0, 0, -1) range(1, 3)range(1, 0, -1) range(1, 4)range(2, 0, -1) range(1, 5)range(3, 0, -1) range(1, 6)range(4, 0, -1) range(1, 7)range(5, 0, -1) range(1, 8)range(6, 0, -1) range(1, 9)range(7, 0, -1) range(1, 10)range(8, 0, -1) '''



    print(   ''' UNPACKINEG '''   )
    # print("\n==========>\n")
    ''' ytian3 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   *(   list(range(  1, i+1  )                     )
                    + list(range(  1,  11  )     [:i-1]  [::-1]  )   ),   sep=''   ,  end=" "   )
                  # + list(range(  1,  11  )  )  [:i-1]  [::-1]      ),   sep=''   ,  end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   *(   list(range(  1,  10  )     [: i ]          )
                    + list(range(  1,   9  )     [:i-1]  [::-1]  )   ),   sep=''   ,  end=" "   )
                  # + list(range(  1,   9  )  )  [:i-1]  [::-1]      ),   sep=''   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' lyapinaalexander 8 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   *range(1, i+1),            *range(1,i)[::-1],   sep=''   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' shyamkatta 3 years ago    I can see below code, works in https://repl.it/languages/python3,  ''' ''' g_karanikas 1 month ago ''' ''' broook2025 8 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   *range(1, i+1),   *reversed(range(1,i))     ,   sep=''   ,  end=" "   )
        ''' 1 121 12321 1234321 123454321 ... 12345678987654321                         '''
        # print( *range(1, i+1),   *range(  i+1, 0, -1  ),   sep=''   ,  end=" "   )
        '''   121 12321 1234321 123454321 ... 12345678987654321 12345678910987654321    '''
        '''                        *range(  i+1, 0, -1  )                               '''
        # print( *range(1, i+1),   *range(  i , -1, -1  ),   sep=''   ,  end=" "   )
        '''   110 12210 1233210 123443210 12345543210 1234566543210 123456776543210 12345678876543210 1234567899876543210 '''
    print()
    """ ! czemu działają tak samo - jeszcze przemyśleć _ HA HA wiem - bo inkluzif ;) """     ''' goodmajo 2 years ago '''
    ''' shashankvyas 6 days ago ''' ''' r82941037 1 year ago    this took me a fucking hour and its unacceptable '''
    for i in range(  1,  int( number )+1  ):
        print(   *range(  1,  i   ),            *range(   i,  0, -1  ),   sep=''   ,   end=" "   )
    print()
    ''' foreverbabykid 2 years ago ''' ''' pinosh 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        # print( *range(  1, i+1  ),            *range(  i-2, 0, -1  ),   sep=''   ,   end=" "   )
        ''' 1   12   123 1   1234 21   12345 321   123456 4321   1234567 54321   12345678 654321   123456789 7654321 '''
        print(   *range(  1, i+1  ),            *range(  i-1, 0, -1  ),   sep=''   ,   end=" "   )
    print()


    # # ''' jshwright 4 years ago '''
    # # # for i in range(  1,  int( number )+1  ):
    # # #     # print(   "".join([str(i)]*i)   ,  end=" "   )

    # print("\n==========>\n")
    ''' IshanRastogi 3 months ago '''    ''' So You can make it longer '''
    for i in range(  1,  int( number )+1  ):
        print(   *range( 1, i ),   *[  y for y in range(i,0,-1)  ],   sep=""   ,   end=" "   )
    # print("\n\n==========>")
    print()
    ''' dylanmendonca 7 months ago '''
    for i in range(  1,  int( number )+1  ):
        normal =    [    [ z+1 for z in range(   i            ) ]
                       , [ z   for z in range(  i-1,  0,  -1  ) ]    ]
        print(    int("".join(map(   str
                                   , [  y for x in normal for y in x  ]   )))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' abhisheksaitwal 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(        "".join(map(   str,     list(  range(  1,  i      )  )
                                            + list(  range(  i,  0, -1  )  )   ))   ,   end=" "   )
    print()


    # print("\n==========>\n")
    ''' prabhjotsingh876 3 days ago    print(*final_list,sep='') returns error but runs fine everywhere else '''
    for i in range(  1,  int( number )+1  ):
        final_list =    list(range(  1,  i+1     ))   \
                      + list(range( i-1,  0 , -1 ))
        print(   *final_list                               ,   sep=''   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' vinay_deshmukh 1 year ago ''' ''' jeremyarr '''
    for i in range(  1,  int( number )+1  ):
        print(   *(     list(range(  1,  i+1     ))
                      + list(range( i-1,  0 , -1 ))       ),   sep=''   ,   end=" "   )
    print()
    ''' akash_exe 5 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   *(     list(range(  1,  i+1  ))
                      + list(range(  1,  i    ))[::-1]    ),   sep=''   ,   end=" "   )
    #   print(          list(range(  1,  i+1  ))
    #                 + list(range(  1,  i    ))[::-1]     ,   sep=''   ,   end="   " )
    ''' [1]   [1, 2, 1]   [1, 2, 3, 2, 1]   [1, 2, 3, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 4, 3, 2, 1]   
    [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]   
    [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]   '''
    print()
    """                             ! ! ! M A G I C ! ! !                 /[0.0]\                 ! ! ! M A G I C ! ! !
                                                                      nnn   [0]   nnn                                           """
    ''' richardwang96 1 year ago    A shorter solution without any use of str: '''
    for i in range(  1,  int( number )+1  ):
        print(   *(     list(range(  1,  i+1  ))
                      + list(range(  1,  i    ))[::-1]    ),   sep=dir()[0][0:0]   ,   end=" "   )
    """ If called without an argument, return the names in the current scope. """
    print()



    # print("\n==========>\n")
    ''' jessielingiraffe 10 months ago    More than 2 lines but it does work: '''
    for i in range(  1,  int( number )+1  ):
        k = 0
        for j in range(i):
            m = 10**j+10**(2*i-2-j)
            if (2*i-2-j) < 0:
                m = 0
                k += (j+1)*m
                k -= i*10**(i-1)
            print(k,   end=" "   )
            ''' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 '''
    print()

    # print("\n==========>\n")
    """ BUT FOR WHAT? - interesujące lecz u mnie nie działa - ta końcówka robi niewłaściwe rzeczy rzeczy """
    ''' xbhavyatomar 1 month ago
        1^2=1                           i k**2
        11^2=121                        0 1**2
        111^2=12321                     1 11**2
        1111^2=1234321                  2 111**2
                                        3 1111**2           '''
    k = 0
    n = int( number )
    for i in range(  1,  int( number )    ):
        # for i in range(0,n):
        k =   k  +  10**i
        print(   k**2   ,   end = (  '  '  if  i!= (n-1)  else  ''  )    )
        ''' 100  12100  1232100  123432100  12345432100  1234565432100  123456765432100  12345678765432100 '''
        # print(   k**2  )# ,   end = (  '\n'  if  i!= (n-1)  else  ''  )    )

    # print("\n\n==========>")
    print()
    ''' kiru24121996 2 months ago '''
    r = 0 # musi istnieć bo =>   UnboundLocalError: local variable 'r' referenced before assignment ;)
    for i in range(  1,  int( number )+1  ):
        #print(                                                                f"{ r}  <=   r_old"               )
        r = r*10 + i                                       # ;        print(   f"{ r } <=   r = r*10 + i"        )
        print(   str(r) + str(r)[-2::-1]    ,  end=" "   ) # ;        print(   f"\n{r} <=   r_after__the_same"   )
        int(r)                                             # ;        print(   f"{ r } <=   int( r )\n"          )
    print()

    # print("\n==========>\n")
    """ posprzątałem odrobinkę """
    ''' rathourabhishek1 2 months ago     please tell me problem in this ''' ''' naneethc003 1 year ago '''
    """ Well, the problem in this is:
            from readability point of view = brothel-snafu-mess
            from task        point of view = double loop and strings
            from program     point of view = it's interesting and I'll do it later """
    for i in range(  1,  int( number )+1  ):
        for j in range(  1,  i*2  ):
            # print(   f'\n\ni={i}  j={j}   '     ,   end=''   )
            if   j <= i  :    print(        j   ,   end=''   )
            else         :    print(   i*2 -j   ,   end=''   )
            # print(   ' ', end='') # daje wszystko luzem
            # print(   '\r'       ) # daje wszystko w pionie
        print(   ' ',   end=''   )



    # print("\n\n==========>")
    print()
    ''' raghuweer23 5 months ago '''
    # def pat(num):
    #     for i in range(     1,  num+1  ):
    #         for j in range(    1 ,   i+1        ):        print(  j,  end=""  )
    #         for j in range(   i-1,    0,   -1   ):        print(  j,  end=""  )
    #         print(   "\r"   )                                             # drukuje trójkąt
    #         # print( "\r"   ,   end=''   )                                # drukuje ostatnią linijkę 12345678987654321
    #         print(   ""     ,   end=''   )                                # drukuje trójkąt
    # nmbr = int( number )
    # pat( nmbr )
    # print()
    def pat(num):
        for i in range(     1,  num+1  ):
            # for j in range(    1 ,   i+1        ):        print(  j,  end=""  )
            for j in range  (    1 ,    i         ):        print(  j,  end=""  )
            # for j in range(   i-1,    0,   -1   ):        print(  j,  end=""  )
            for j in range  (    i ,    0,   -1   ):        print(  j,  end=""  )
            print(   " "   ,   end=''   )
    nmbr = int( number )
    pat( nmbr )
    print()
    # print("\n==========>\n")
    ''' rishab_sharma 2 years ago '''    # n=int( number )
    def palimd( i ):
        if i==1:                                            print(  1,  end=''  )
        else   :
            # for j in range(    1 ,   i+1        ):        print(  j,  end=''  )
            for j in range  (    1 ,    i         ):        print(  j,  end=''  )
            # for k in range(   i-1,    0,   -1   ):        print(  k,  end=''  )
            for k in range  (    i ,    0,   -1   ):        print(  k,  end=''  )
    for i in range(  1,  int( number )+1  ):
        palimd( i )  #;        print()
        print(   ""   ,  end=" "   )
    print()






    # print("\n==========>\n")



    print("\n\n F U N C T I O N A L :\n")
    """UP"""
    ''' pmadeo 7 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   list(map(   lambda x:   x*x,
                             [1,11,111,1111,11111,111111,1111111,11111111,111111111]
                          )).pop(i-1)   ,  end=" "   )
    print()

    ''' JTBoi 1 month ago    Two Liner :p XD  '''
    """ ... wygląda na łan lajner, bo dał średnik ;) """
    """ baaardzo intreresujące """
    f = lambda x:   x   and     [  f(x-1),    print( ( 10**x //9 )**2 ,end=" " ),    range(1, x+1)  ];
    f(int(( number )))
    print()


    # print("\n==========>\n")
    """ HA! import can be inside while loop """
    ''' jay_s_livingston 1 year ago    I wanted to share my "creative" solution. '''
    ''' i = 1  ;  k = int(input())
        while i < k+1:   from functools import reduce  ;  print((   reduce((lambda x, y: x + y)
                                                                  , [10**(j) for j in range(0,i)]))**2)  ;   i = i+1 '''
    i = 1
    while   i   <   int( number )+1   :
        from functools import reduce
        print(   (reduce(   lambda x, y:   x + y
                          , [   10**j  for j in range(0,i)   ]   ))**2   ,   end=" "   )
        i = i+1
    print(   '\n',          [   10**j  for j in range(0,i)   ]           ,   end=" "   )
    print(); '''  [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000] '''
    # print("\n==========>\n")
    ''' husainzafar 4 years ago ''' """ lista Michał """
    for i in range(  1,  int( number )+1  ):
        print(   reduce(   lambda x, y:   10*x + y
                         , [   1 for j in range(i)   ]
                        )**2   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        # print(           [   1 for j in range(i)   ]   ,   end=" "   )
        ''' [1] [1, 1] [1, 1, 1] [1, 1, 1, 1] [1, 1, 1, 1, 1] [1, 1, 1, 1, 1, 1] [1, 1, 1, 1, 1, 1, 1] [1, 1, 1, 1, 1, 1, 1, 1] [1, 1, 1, 1, 1, 1, 1, 1, 1] '''

    # print("\n==========>\n")
    ''' do późniejszego tłumaczenia - ni to pospacjowałem, lecz nic mi po tym 
    - niby trochę kumam, lecz jakby kto o tym poopowiadał trochę to by było coś '''
    ''' tsarevich 1 year ago    Very smart, fast, small and concise :)     This is my ugly one in functional style: '''
    for i in range(  1,  int( number )+1  ):
        print(   reduce(   (   lambda a, v:   a*10 +v   )
                         , map(   lambda x:   -1 * abs(x-i)   +  i,   range(1, 2*i)   )
                         , 0
                           )   ,  end=" "   )
    print()

    # print("\n==========>\n")
    """ magic """
    ''' MadhuRanjanKumar 1 year ago    similarly, incorrect check is failing this: Wrong Answer only 1 for is allowed '''
    for i in range(  1,  int( number )+1  ):
        lista  =       list("\n") * (  i != 1  )                \
                     + (  list(range(   1 ,  i+1       ))  )    \
                     + (  list(range(  i-1,   0 ,  -1  ))  )
        for j in range(len(  lista  )):
            print(   lista[j]   ,   end=f"{ (j-3)*' ' }"   )  ;''' , end="" ) --- musi być, bo inaczej się rozłazi '''
    print()
    # print("\n==========>\n")
    for i in range(  1,  int( number )+1  ):
        print(              list(range(   1 ,  i+1       ))     ,  sep="    "   ,   end="  "   )
    print() ; ''' [1]  [1, 2]  [1, 2, 3]  [1, 2, 3, 4]  [1, 2, 3, 4, 5]  [1, 2, 3, 4, 5, 6]  [1, 2, 3, 4, 5, 6, 7]  [1, 2, 3, 4, 5, 6, 7, 8]  [1, 2, 3, 4, 5, 6, 7, 8, 9] '''
    for i in range(  1,  int( number )+1  ):
        print(           (  list(range(   1 ,  i+1       ))  )  ,  sep=""       ,   end="  "   )
    print() ; ''' [1]  [1, 2]  [1, 2, 3]  [1, 2, 3, 4]  [1, 2, 3, 4, 5]  [1, 2, 3, 4, 5, 6]  [1, 2, 3, 4, 5, 6, 7]  [1, 2, 3, 4, 5, 6, 7, 8]  [1, 2, 3, 4, 5, 6, 7, 8, 9] '''
    for i in range(  1,  int( number )+1  ):
        print(              list(range(  i-1,   0 ,  -1  ))     ,  sep=""       ,   end="  "   )
    print() ; '''   []    [1]     [2, 1]     [3, 2, 1]     [4, 3, 2, 1]     [5, 4, 3, 2, 1]     [6, 5, 4, 3, 2, 1]     [7, 6, 5, 4, 3, 2, 1]     [8, 7, 6, 5, 4, 3, 2, 1] '''
    # lista =                    range(   1 ,  i+1       )             \
    #                  +         range(  i-1,   0 ,  -1  )
    ''' TypeError: unsupported operand type(s) for +: 'range' and 'range' '''
    ''' MadhuRanjanKumar 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        lista =          (  list(range(   1 ,  i+1       ))  ) \
                       + (  list(range(  i-1,   0 ,  -1  ))  )
        # lista =           list(range(   1 ,  i+1       ))            \ # bez nawiasów też działa
        #              +    list(range(  i-1,   0 ,  -1  ))              # bez nawiasów też działa
        print(  *lista  ,  sep=""                                           ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' mling 3 years ago    I used the built-in function reduce ''' ''' sanjaychandak '''
    for i in range(  1,  int( number )+1  ):
        print(   reduce(    lambda a, b:  10*a + b,
                            list(range(   1 ,  i+1       ))
                          + list(range(  i-1,   0 ,  -1  ))  ,   0    )   ,  end=" "   )
    #                       list(range(   1 ,   i        ))
    #                     + list(range(   i ,   0 ,  -1  ))           )   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' wenyizaidao_ww 4 years ago ''' """ the same but with brackets """ """ MMMMMCCLXXVII 3 years ago """
    for i in range(  1,  int( number )+1  ):
        print(   reduce(    lambda x, y:  x*10 + y
                          , (   list(range(   1 ,  i+1       ))
                              + list(range(   1 ,  i         ))[::-1]    ))   ,  end=" "   )
        #                 ,     list(range(   1 ,  i+1       ))
        #                     + list(range(   1 ,  i         ))[::-1]     )   ,  end=" "   ) # bez nawiasów też działa
    ''' rajeevbhatt595 4 years ago    can you please explain? what are x and y?
        wenyizaidao_ww 4 years ago:
    x and y is two elements in the list.    Such as:
    reduce(   lambda x, y:  x*10+y   ,   [1,2,3,4]   )
        means:
    (   (1*10 + 2)  *  10+3   )*10 + 4
    This is my understanding, I wish it could help you. '''
    print()
    """     reduce(function, sequence, initial=None):  # real signature unknown; restored from __doc__
            reduce(function, sequence[, initial]) -> value -------------------------------------------
                Apply a function of two arguments cumulatively to the items of a sequence,
            from left to right, so as to reduce the sequence to a single value.
            For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
                If initial is present, it is placed   before the items of the sequence in the calculation, 
            and serves as a default when the   sequence is empty.    """
    ''' unpacking '''
    # print("\n==========>\n")
    ''' akash_exe 5 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   *(     list(range(  1,  i+1  ))
                      + list(range(  1,  i    ))[::-1]    ),   sep=''   ,   end=" "   )
    #   print(          list(range(  1,  i+1  ))
    #                 + list(range(  1,  i    ))[::-1]     ,   sep=''   ,   end="   " )
    ''' [1]   [1, 2, 1]   [1, 2, 3, 2, 1]   [1, 2, 3, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 4, 3, 2, 1]
    [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]   [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]   '''
    print()
    # print("\n==========>\n")
    ''' saurabhsinghr 3 years ago    please help with this logic '''
    for i in range(  1,  int( number )+1  ):
        # print(      [  l for l in range(  1,  i+1      )  ]
        #           + [  j for j in range( i-1,  0,  -1  )  ]                 ,   end=" "   )
        ''' -//-//-//-//- '''
        print(   *(   [  l for l in range(  1,   i       )  ]
                    + [  j for j in range(  i,   0,  -1  )  ]   )   ,   sep='',   end=" "   )
    print()

    # print("\n==========>\n")
    ''' MohammedShoaib 5 months ago    Using reduce in Python 2: No more than 2 lines    We can't post the same solution 
    in Python 3 since reduce has been moved to functools. Importing functools causes an additional line. '''
    for i in range(  1,  int( number )+1  ):
        print(   reduce(    lambda x, y:  x*10 + y,    [1]*i    )**2   ,  end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(                                         [1]*i           ,  end="   " )
        ''' [1]   [1, 1]   [1, 1, 1]   [1, 1, 1, 1]   [1, 1, 1, 1, 1]   [1, 1, 1, 1, 1, 1]   [1, 1, 1, 1, 1, 1, 1]   [1, 1, 1, 1, 1, 1, 1, 1]   [1, 1, 1, 1, 1, 1, 1, 1, 1] '''
    print()



    # print("\n==========>\n")
    ''' fluffydogcatrat 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        # print( reduce(    lambda a, b:  (10*a + b)
        #                 , map(   lambda x :   ( 2*i -x )   if   x > i   else (x)
        #                        , range(  1,  2*i  )   )                            )   ,  end=" "   )
        print(   reduce(    lambda a, b:   10*a + b
                          , map(   lambda x :     2*i -x     if   x > i   else  x
                                 , range(  1,  2*i  )   )                            )   ,  end=" "   ) # can omit some brackets
    print()

    # print("\n==========>\n")
    ''' scottmcghee 3 years ago    Overly complicated, but: '''
    for i in range(  1,  int( number )+1  ):
        # print( reduce(    lambda x, y:  (x*10)+ y,   range(   1,  i+1    )) * pow(10, i-1)) \
        #      +(reduce(    lambda x, y:  (x*10)+ y,   range(  i-1,  0,  -1)) if i > 1 else 0)
        ''' TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' '''
        print(   reduce(    lambda x, y:   x*10 + y
                          , range(   1,  i+1      )    )
               * 10**( i-1 )
               +(reduce(    lambda x, y:   x*10 + y
                          , range(  i-1,  0,  -1  )    )    if i > 1 else 0   )   ,  end=" "   )
    # print()
    for i in range(  1,  int( number )+1  ):
    #     print(   reduce(    lambda x, y:   x*10 + y
    #                       , range(   1,  i+1      )    )                                          , '*'
    #            , 10**( i-1 )                                                                      , ' + '
    #            ,(reduce(    lambda x, y:   x*10 + y
    #                       , range(  i-1,  0,  -1  )    )    if i > 1 else 0   )   ,  end="\t  "   , sep=''   )
        ''' 1*1 + 0	  12*10 + 1	  123*100 + 21	  1234*1000 + 321	  12345*10000 + 4321	  123456*100000 + 54321	  
        1234567*1000000 + 654321	  12345678*10000000 + 7654321	  123456789*100000000 + 87654321	  '''
    print()

    # print("\n==========>\n")
    ''' niilz 3 months ago    I think I've really work to hard here. But the following does the job aswell:
    it woul have been easier with functools.reduce but that would have required an extra line, which was not allowed. '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(  map(   lambda x:  x * 10**(i-x),       list(range(1, i+1))   )  )* 10**(i-1)
               + sum(  map(   lambda y:  y * 10**(y-1),   reversed(range(1, i  ))   )  )             ,   end=" "   )
        # print()
        # for i in range(  1,  int( number )+1  ):
        #     print( sum(map(   lambda x:  x * 10**(i-x),       list(range(1, i+1))   )) * 10**(i-1)
        #          , sum(map(   lambda y:  y * 10**(y-1),   reversed(range(1, i  ))   ))             )#,   end=" "   )
        ''' 1 0
            120 1
            12300 21
            1234000 321
            123450000 4321
            12345600000 54321
            1234567000000 654321
            123456780000000 7654321
            12345678900000000 87654321 '''
        # print()
        # for i in range(  1,  int( number )+1  ):
        #     print(       map(   lambda x: x * 10**(i-x),       list(range(1, i+1))   )
        #            ,     map(   lambda y: y * 10**(y-1),   reversed(range(1, i  ))   )              )#,   end=" "   )
        ''' <map object at 0x0000000002A46B38> <map object at 0x0000000002A46BE0> ... ... ... '''
        # print()
        # for i in range(  1,  int( number )+1  ):
        #     for elem in  map(   lambda x: x * 10**(i-x),       list(range(1, i+1))   ):
        #         print(   elem   ,   end="   "   )
        #     print()
        ''' 1   
            10   2   
            100   20   3   
            1000   200   30   4   
            10000   2000   300   40   5   
            100000   20000   3000   400   50   6   
            1000000   200000   30000   4000   500   60   7   
            10000000   2000000   300000   40000   5000   600   70   8   
            100000000   20000000   3000000   400000   50000   6000   700   80   9    '''
        # print()
        # for i in range(  1,  int( number )+1  ):
        #     for elem in  map(   lambda y: y * 10**(y-1),   reversed(range(1, i  ))   ):
        #         print(   elem   ,   end="   "   )
        #     print()
        ''' 1   
            20   1   
            300   20   1   
            4000   300   20   1   
            50000   4000   300   20   1   
            600000   50000   4000   300   20   1   
            7000000   600000   50000   4000   300   20   1   
            80000000   7000000   600000   50000   4000   300   20   1    '''

    print()
    # print("\n==========>\n")
    ''' D O U B L E   for()   L O O P ''' ''' a_nichochlain '''
    ''' stevehopkinson 4 years ago    Any reason why my answer is being failed? '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(   10**x  for  x  in range(i)   )**2    ,   end=" "   )
        # print( sum( [ 10**x  for  x  in range(i) ] )**2                 ,   end=" "   ) # Cirn3co 1 year ago
        # print( sum(   10**j  for  j  in range( i-1, -1, -1  )   )**2    ,   end=" "   ) # ispulkit 3 years ago
    print()
    # print("\n==========>\n")
    ''' S I N G L E   for()   L O O P '''
    ''' jjvanhan 4 years ago    the instructions forbid the use of another for loop. I used map to get around this: '''
    for i in range(  1,  int( number )+1  ):
        print(       sum(map(    lambda x:   10**x ,      range( i )   ))      **2   ,   end=" "   )
        ''' m_osiak46 1 year ago '''
        # print(     sum(map(    lambda x:   10**x , list(range(0,i))  ))      **2   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' charlesartbr 3 years ago    Another solution:   '''
    for i in range(  1,  int( number )+1  ):
        print(   (   sum(map(    lambda x:  (10**x),      range(1,i)   ))+1   )**2   ,   end=" "   )
        # print( (   sum(map(    lambda x:   10**x ,      range(1,i)   ))+1   )**2   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' jacekffid 1 year ago    pretty straight-forward, but maps aren't forbidden '''
    for i in range(  1,  int( number )+1  ):
        print(       sum(map(   lambda a:     a    *  pow(  10,       a -1  )
                                           + (a-1) *  pow(  10,  2*i -a     )
                              , range(  1,  i+1  )                                  ))   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(       sum(map(   lambda a:     a    * 10**(            a -1  )
                                           + (a-1) * 10**(       2*i -a     )
                              , range(  1,  i+1  )                                  ))   ,   end=" "   )
    print()

    # print("\n==========>\n")
    """ [++++] """
    ''' mamunovalisher 1 month ago    This is how I did it legally without hacking ;)
        So many constraints, but It stimulates for creativity.    This is how i did it without hacking. '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda x:  pow(10,x[0]) * x[1]
                          , enumerate(   [*range(1, i)]  +  [*range(i, 0, -1)]   )   ))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' polipiper 1 year ago    So there is a really simple mathematical way to solve this 
    which is appears in the dscussion below,    but you'd really have to be a math wiz to come up with that 
    if you haven't seen it before,    so that isn't really fair in a Python programming problem.
        But in Python there is a way to do this using iteration without any more "for" loops... 
        and that's very "Pythonic", and so really much more appropriate here, even if less mathematically elegant. '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda t:  t[1] * (10**t[0])
                          , zip(   range(  i*2 -2,  -2,  -1  )
                                 , list(range( 1, i ))  +  list(range( i, 0, -1 ))   )   ))   ,   end=" "   )
    ''' Explanation: We use range() to construct two lists, 
        one with the palindrome of digits    and one with the appropriate powers of 10, 
    then zip() them together and use map to apply the necessary power of 10 to each digit, 
    then sum the whole thing for the final result... 
    i.e. for i=2 that would be [ 2 1 0 ] and [1 2 1], 
    then zip for [ (2, 1), (1, 2), (0, 1)], 
    now use map() to apply the power of 10 to get [ 100, 20, 1 ]    then sum() to get 121.'''
    print(   '\n',        range(  i*2 -2,  -2,  -1  )    )
    '''                   range(      16,  -2,  -1  )                   '''
    print(           list(range(  i*2 -2,  -2,  -1  ))   )
    '''  [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1] '''
    print(                         list(range( 1, i ))  +  list(range( i, 0, -1 ))                          )
    '''  [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1] '''
    # print(                zip(   range(  i*2 -2,  -2,  -1  )
    #                            , list(range( 1, i ))  +  list(range( i, 0, -1 ))   )                      )
    ''' <zip object at 0x00000000023B7F08> '''
    print(             list(zip(   range(  i*2 -2,  -2,  -1  )
                                 , list(range( 1, i ))  +  list(range( i, 0, -1 ))   ))                     )
    ''' [(16, 1), (15, 2), (14, 3), (13, 4), (12, 5), (11, 6), (10, 7), (9, 8), (8, 9), (7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)] '''
    print()

    # print("\n==========>\n")
    ''' działa lecz nie wiem dlaczego '''
    ''' krell1 3 months ago    Straightforward mapping: '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda k:   min(  (k+1) *10**k,  (2*i-1-k) *10**k  )
                          , range(  2*i -1 )                                      ))   ,   end=" "   )
    # for i in range(1,  int( number )+1  ):
    #     print(     map(   lambda k:   min(  (k+1) *10**k,  (2*i-1-k) *10**k  )
    #                     , range(  2*i -1 )                                      )    ,   end=" "   )
    ''' <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70> <map object at 0x0000000002A66B70>  '''
    # print()
    # for i in range(  1,  int( number )+1  ):
    #     # print(              lambda k:   min(  (k+1) *10**k,  (2*i-1-k) *10**k  )       ,   end=" "   )
    #     ''' <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A60F28> '''
    #     # print(              range(  2*i -1 )                                           ,   end=" "   )
    #     ''' range(0, 1) range(0, 3) range(0, 5) range(0, 7) range(0, 9) range(0, 11) range(0, 13) range(0, 15) range(0, 17) '''
    #     # print(   f" i={i}                   { (k+1) *10**k} {(2*i-1-k) *10**k  }"          ,   end=" "   )
    #     ''' jakaś infinite loop '''
    #     # print(   f" i={i                }   { (i+1) *10**i} {(2*i-1-i) *10**i  }"          ,   end="\n"   )
    #     '''  i=1   20 0
    #          i=2   300 100
    #          i=3   4000 2000
    #          i=4   50000 30000
    #          i=5   600000 400000
    #          i=6   7000000 5000000
    #          i=7   80000000 60000000
    #          i=8   900000000 700000000
    #          i=9   10000000000 8000000000 '''

    # print("\n==========>\n")
    # """ podobna matematyka _ _ _ nie działa """
    ''' srikv 3 months ago '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   sum(map(   lambda x:   (x if x <= i else 2*i-x)(10*(2*i-1-x)) ,range(1,2*i)))   ,   end='\n'   )
    ''' TypeError: 'int' object is not callable '''
    print()

    # print("\n==========>\n")
    ''' ghaderi_amin 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(  [         10**(2*i-j-2)  *  (    j+1)   if j<i
                            else 10**(2*i-j-2)  *  (2*i-1-j)
                                 for j in range(    2*i-1    )                  ]  )   ,   end=' '   )
    print()
    # for i in range(  1,  int( number )+1  ):
        # for j in range(    2*i-1    ):
        #                     if j<i: print(   sum(  [         10**(2*i-j-2)  *  (    j+1)  ]  )   ,   end=' '   )
        #                     else:   print(   sum(  [         10**(2*i-j-2)  *  (2*i-1-j)  ]  )   ,   end=' '   )
    ''' 1   100 20 1   10000 2000 300 20 1   1000000 200000 30000 4000 300 20 1   100000000 ... '''
    # print("\n==========>\n")
    ''' bvermeulen 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda j:   int(   (j+1) * 10**(2*i-j-2)
                                             +  j    * 10**(    j-1)   )
                          , range(i)                                        ))   ,   end=' '   )
    print()

    # print("\n==========>\n")
    ''' kamanashisroy 2 years ago
    The following will work for big numbers as long as it is smaller than equals to maximum number allowed as integer ! '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda x:     x   *  10**(  i-x-1  )
                          , range(i)                              ))
               * 10**i
               + sum(map(   lambda x:   (x+1) *  10**x
                          , range(i)                              ))   ,   end=' '   )
    # for i in range(  1,  int(   23   )+1  ):
    ''' ... 12345679 012345679 01234 5 432 0 98765432 0 987654321 '''
    print()







    # print("\n==========>\n")
    print(   '\n S U M   L I S T   M A P   sum(list(map(   lambda x:   10**x ,  range( i )   ))) **2   :'   )
    ''' viswanathan_p202 4 months ago '''    ''' yishanxu0806 12 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(    sum(list(map(   lambda x:  (10**x),       range( i )    ))) **2    ,    end=" "    )
        # print( (sum(list(map(   lambda j:   10**j ,       range(0,i)    ))))**2    ,    end=" "    ) # the same effect
        # print(  sum(     map(   lambda x:   10**x ,       range( i )    ) ) **2    ,    end=" "    ) # works the same
        ''' Vendett2 1 week ago '''
        # print(  sum(list(map(   lambda x:   10**x ,  list(range(0,i))   ))) **2    ,    end=" "    )
        ''' andrew_ocallagh1 2 years ago    Map function is an easy way to get around 'for' clause. 
        Not as cheeky as the lookup table, not as simple as ((10^i-1)/9)^2, but just another way of solving the problem. '''
    print()

    # print("\n==========>\n")
    """ u mnie nie działa """
    ''' dharmateja_k30 8 months ago    The below statement will give the desired output. '''
    # for i in range(  1,  int( number )+1  ):    # well great! But How?!
    #     # print(sum(list(map(lambda x: int(x * 10 ** (i + i - 1 - x) + (i - x)    10 * (i - 1 - x)), range(1, i + 1)))))
    #     # print(sum(list(map(lambda x: int(x * 10 ** (i + i - 1 - x) + (i - x)  * 10 * (i - 1 - x)), range(1, i + 1)))))
    #     print(    sum(list(map(   lambda x:  int(      x *10**(  i+i-1-x  )
    #                                               + (i-x)*10*(     i-1-x  )   )
    #                             ,         range(1,i+1)               )))      ,   end=" "   )

    # print("\n==========>\n")
    ''' shivam_hackgod 3 months ago    A little complex but can take n>10. '''
    for i in range(  1,  int( number )+1  ):
        print(   (sum(list(map(   lambda x:   1* 10**(i-x)
                                , list(   range(1,i+1)   )          ))))**2   ,   end=" "   )
    # for i in range(1,  int(   23   )+1  ):
    #     print( (sum(list(map(   lambda x:   1* 10**(i-x)
    #                           , list(   range(1,i+1)   )          ))))**2   ,   end=" "   )
    """ but working with n>10 a little bit """
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 
    12345679 00 987654321    12345679 0120 987654321   12345679 012320 987654321 ... 
                                            ... 12345679 012345679 01234 5 432 0 98765432 0 987654321 '''


    print()
    # print("\n==========>\n")
    """ jak oni to wymyślają ???    # 10^16 !!!   --- my logic is saying - it shouldn't work ;) """
    ''' [deleted] 7 months ago    This is my code: '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(list(map(   lambda a,b:   a*b,
                                 list( range(1, i+1) )   +   list( reversed(list( range(1, i) )) ),
                                 list(map(   lambda x:  pow(10, x)      # 10^16 !!!
                                           , list( range(0, i*2-1) )
                                             ))                                                       )))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' donkeyh 3 years ago    How about that: ''' """ redone from Pythona2 but ... """
    # for i in range(  1,  int( number )+1  ):
    #     print(   sum(map(   lambda i, el:  pow(   10,   len(   list(range(   1 ,  j+1,   1  ))
    #                                                          + list(range(  j-1,   0 ,  -1  ))   ) -i -1   )
    #                                        *el
    #                       , enumerate(   list(range(   1 ,  j+1,   1  ))
    #                                    + list(range(  j-1,   0 ,  -1  ))   )))   ,   end=" "   )
    ''' TypeError: <lambda>() missing 1 required positional argument: 'el' '''





    print("\n==========>\n")
    ''' pshaikh 3 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(list(map(   lambda z:        z[1]*(  10**z[0][0] + 10**z[0][1]  )    if z[0][0] != z[0][1]
                                             else z[1]*   10**z[0][0]
                               , zip(   zip(            range(  2*i -1  )
                                             , reversed(range(  2*i -1  )))
                                      , range(  1,  i+1  )   )                                        )))   ,   end=" "   )
    print()
    # for i in range(  1,  int( number )+1  ):
    #     for elem in        list(                      range(  2*i -1  )   ):       print(  elem, end='\t'  )
    #     print(  )
    #     for elem in        list(             reversed(range(  2*i -1  ))  ):       print(  elem, end='\t'  )
    #     print(  )
    #     for elem in        list(      range(  1,  i+1  )                  ):       print(  elem, end='\t'  )
    #     print( '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' )
    ''' 0	
        0	
        1	
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        0	1	2	
        2	1	0	
        1	2	
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        0	1	2	3	4	
        4	3	2	1	0	
        1	2	3	
        ...
        ...	
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	
        16	15	14	13	12	11	10	9	8	7	6	5	4	3	2	1	0	
        1	2	3	4	5	6	7	8	9	
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''


    # print("\n==========>\n")
    ''' lkform 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(list(map(   lambda x, y:   x * 10**y
                               , [1]*i
                               , list(range(0,i))            ))    )**2   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   sum(     map(   lambda x, y:   x * 10**y                                    # works the same
                               , [1]*i
                               , list(range(0,i))             )    )**2   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' yuyliu 3 years ago    This is gonna trick the system while I'm actually doing a loop but not using "for" statement '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(     map(   lambda x:   x[0]**x[1]
                               , zip(  [10]*i,  range(i)  )   )    )**2   ,   end=" "   )
    print()


    # print("\n==========>\n")
    ''' aneesh_chopra 3 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   pow( sum(list(map(   pow,   [10]*(i),   list(range(0,i))   ))) , 2 )   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(        sum(list(map(   pow,   [10]* i ,   list(range(0,i))   )))         ,   end=" "   )
        # print(      sum(list(map(   pow,    10 * i ,   list(range(0,i))   )))         ,   end=" "   )
        ''' TypeError: 'int' object is not iterable '''
    print()
    for i in range(  1,  int( number )+1  ):
        print(            list(map(   pow,   [10]* i ,   list(range(0,i))   ))          ,   end=" "   )
        ''' [1] [1, 10] [1, 10, 100] [1, 10, 100, 1000] [1, 10, 100, 1000, 10000] [1, 10, 100, 1000, 10000, 100000] [1, 10, 100, 1000, 10000, 100000, 1000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000] '''
        # for i in range(1,  int( number )+1  ):
        #     print(               map(   pow,   [10]* i ,   list(range(0,i))   )           ,   end=" "   )
        ''' <map object at 0x0000000002A36B70> <map object at 0x0000000002A36C18> <map object at ... '''
    print()
    for i in range(  1,  int( number )+1  ):
        print(                               [10]* i,'\t\t\t',list(range(0,i))          ,   end="\n"   )
        ''' [10] 			 [0]
            [10, 10] 			 [0, 1]
            [10, 10, 10] 			 [0, 1, 2]
            [10, 10, 10, 10] 			 [0, 1, 2, 3]
            [10, 10, 10, 10, 10] 			 [0, 1, 2, 3, 4]
            [10, 10, 10, 10, 10, 10] 			 [0, 1, 2, 3, 4, 5]
            [10, 10, 10, 10, 10, 10, 10] 			 [0, 1, 2, 3, 4, 5, 6]
            [10, 10, 10, 10, 10, 10, 10, 10] 			 [0, 1, 2, 3, 4, 5, 6, 7]
            [10, 10, 10, 10, 10, 10, 10, 10, 10] 			 [0, 1, 2, 3, 4, 5, 6, 7, 8] '''
        ''' [10]    
             [0]
            [10, 10]    
             [0, 1]
            [10, 10, 10]    
             [0, 1, 2]
            [10, 10, 10, 10]    
             [0, 1, 2, 3]
            [10, 10, 10, 10, 10]    
             [0, 1, 2, 3, 4]
            [10, 10, 10, 10, 10, 10]    
             [0, 1, 2, 3, 4, 5]
            [10, 10, 10, 10, 10, 10, 10]    
             [0, 1, 2, 3, 4, 5, 6]
            [10, 10, 10, 10, 10, 10, 10, 10]    
             [0, 1, 2, 3, 4, 5, 6, 7]
            [10, 10, 10, 10, 10, 10, 10, 10, 10]    
             [0, 1, 2, 3, 4, 5, 6, 7, 8]            '''
    print()
    # print("\n==========>\n")
    ''' imsaravana369 6 months ago  '''
    for i in range(  1,  int( number )+1  ):
        a =   list( range(   1 , i+1       ) ) \
            + list( range(  i-1,  0  , -1  ) )
        b = [   10**i    for i in range(   len(a)-1,  -1,  -1   )   ]
        print(   sum(list(map(    lambda x:  x[0]*x[1],    zip(a,b)    )))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' dmytro_y_solovei 6 months ago    How about this? It's somewhat clumsy at the part in which the two lists 
    are created but besides that... Also .enumerate() might be a good solution 
    in situations where you need to use the item's index without running a for-loop '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(list(map(    lambda x:  10**x[0] * x[1]
                                , enumerate(      list(         range(  1,  i+1  ))
                                                + list(reversed(range(  1,   i   )))      )     )))   ,   end=" "   )
        # print( sum(list(map(    lambda i:  10**i[0] * i[1]
        #                       , enumerate(  (   list(         range(  1,  i+1  ))
        #                                       + list(reversed(range(  1,   i   )))   )  )     )))   ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' hannesRSA 1 year ago    Without math knowledge: '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(     map(    lambda x:  int(  10**x[0] * x[1] )
                                , enumerate(      list(range(  1,  i       ))
                                                + list(range(  i,  0,  -1  ))      )   )     )   ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' npsmith79 9 months ago    Here is what I did:  '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(   list(map(    lambda x:   x  *  pow(  10  ,  2*len(list(range(1,i)))  -x+1  )
                                   , list(range(1,i   ))                                             ))
                      + list(map(    lambda x:   x  *  pow(  10  ,                            x-1  )
                                   , list(range(i,0,-1))                                             ))  ),  end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(                                                      2*len(list(range(1,i)))  -x+1         ,  end="\t\t"   )
    print() ; '''		-8		-6		-4		-2		0		2		4		6		8				'''
    for i in range(  1,  int( number )+1  ):
        print(                                         pow(  10  ,  2*len(list(range(1,i)))  -x+1  )      ,  end="\t"     )
    print() ; '''		1e-08	1e-06	0.0001	0.01	1		100		10000	1000000	100000000		'''
    # print(                     lambda x:   x  *  pow(  10  ,  2*len(list(range(1,i)))  -x+1  )      ,  end="\t"     )
    ''' <function Demlo_numbers.<locals>.<lambda> at 0x0000000002A842F0>		<function Demlo_numbers.<locals>.<lambda> at 0x0000000002A842F0>	...		'''

    # for i in range(  1,  int( number )+1  ):
    #     print(        list(map(    lambda x:   x  *  pow(  10  ,  2*len(list(range(1,i)))  -x+1  )
    #                              , list(range(1,i   ))                                             ))   ,  end="\t\t"   )
    ''' []	[100]			[10000, 2000]				[1000000, 200000, 30000]					[100000000, 20000000, 3000000, 400000]								[10000000000, 2000000000, 300000000, 40000000, 5000000]											[1000000000000, 200000000000, 30000000000, 4000000000, 500000000, 60000000]	[100000000000000, 20000000000000, 3000000000000, 400000000000, 50000000000, 6000000000, 700000000]	[10000000000000000, 2000000000000000, 300000000000000, 40000000000000, 5000000000000, 600000000000, 70000000000, 8000000000]		'''
    # print()
    # for i in range(  1,  int( number )+1  ):
    #     print(        list(map(    lambda x:   x  *  pow(  10  ,                            x-1  )
    #                              , list(range(i,0,-1))                                             ))   ,  end="\t\t"   )
    ''' [1]	[20, 1]			[300, 20, 1]				[4000, 300, 20, 1]							[50000, 4000, 300, 20, 1]											[600000, 50000, 4000, 300, 20, 1]																[7000000, 600000, 50000, 4000, 300, 20, 1]		[80000000, 7000000, 600000, 50000, 4000, 300, 20, 1]		[900000000, 80000000, 7000000, 600000, 50000, 4000, 300, 20, 1]		'''
    # print()
    for i in range(  1,  int( number )+1  ):
        print(          list(map(    lambda x:   x  *  pow(  10  ,  2*len(list(range(1,i)))  -x+1  )
                                   , list(range(1,i   ))                                             ))
                      + list(map(    lambda x:   x  *  pow(  10  ,                            x-1  )
                                   , list(range(i,0,-1))                                             ))   ,  end="\t\t"   )
    print() ; ''' [1]	[100, 20, 1]	[10000, 2000, 300, 20, 1]	[1000000, 200000, 30000, 4000, 300, 20, 1]	[100000000, 20000000, 3000000, 400000, 50000, 4000, 300, 20, 1]		[10000000000, 2000000000, 300000000, 40000000, 5000000, 600000, 50000, 4000, 300, 20, 1]		[1000000000000, 200000000000, 30000000000, 4000000000, 500000000, 60000000, 7000000, 600000, 50000, 4000, 300, 20, 1]		[100000000000000, 20000000000000, 3000000000000, 400000000000, 50000000000, 6000000000, 700000000, 80000000, 7000000, 600000, 50000, 4000, 300, 20, 1]		[10000000000000000, 2000000000000000, 300000000000000, 40000000000000, 5000000000000, 600000000000, 70000000000, 8000000000, 900000000, 80000000, 7000000, 600000, 50000, 4000, 300, 20, 1]		'''







    """ UNPACKING """

    print("\n\n Czemu ten rozdzielnik rozdziela tam, a indziej-tam nie???")
    ''' do późniejszego tłumaczenia - ni to pospacjowałem, lecz nic mi po tym '''
    ''' tsarevich 1 year ago    Very smart, fast, small and concise :) 
    This is my ugly one in functional style: '''
    for i in range(  1,  int( number )+1  ):
        print(   *list(map(    lambda x:  i-abs(x-i),      range(  1, i*2  )    ))             , sep='-' ,  end=" "   )
    ''' 1 1-2-1 1-2-3-2-1 1-2-3-4-3-2-1 1-2-3-4-5-4-3-2-1 1-2-3-4-5-6-5-4-3-2-1 1-2-3-4-5-6-7-6-5-4-3-2-1 1-2-3-4-5-6-7-8-7-6-5-4-3-2-1 1-2-3-4-5-6-7-8-9-8-7-6-5-4-3-2-1  '''
    print()
    for i in range(  1,  int( number )+1  ):
        print(   *list(map(    lambda x:  i-abs(x-i),      range(  1, i*2  )    ))                       ,  end=" "   )
    ''' 1 1 2 1 1 2 3 2 1 1 2 3 4 3 2 1 1 2 3 4 5 4 3 2 1 1 2 3 4 5 6 5 4 3 2 1 1 2 3 4 5 6 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1  '''
    print()
    for i in range(  1,  int( number )+1  ):
        print(   *list(map(    lambda x:  i-abs(x-i),      range(  1, i*2  )    ))             , sep=''  ,  end=" "   )
    ''' 1 121 12321 1234321 123454321 12345654321 1234567654321 123456787654321 12345678987654321 '''
    print()
    # print("\n==========>\n")
    ''' ZanderWang 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   ''.join(   [   str(  i -abs(j-i)  )              for j in range(  1, i*2  )   ]   )   ,  end=" "   )
    print()
    # print("\n==========>\n")
    ''' kcalderhead 1 month ago    Having read plenty of comments using the squaring trick (which ended up being my final solution), 
    I stumbled across this when a comment inadvertently tripped the "no string methods" warning:
    The general idea is the get a formula for the digits and use powers of 10 to move them to the right location. '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(       [      (  i -abs(i-j)  )* 10**(j-1)   for j in range(  1, 2*i  )   ]   )   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' tsarevich 1 year ago '''
    for i in range(  1,  int( number )+1  ):
        print(   ''.join(map(   str,   (map(   lambda x:   i - abs(x-i),  range(1, i*2)   ))    ))  ,  end=" "   )
    print()



    print(   '\n UNPACKINEG ~ ~ ~  F U N C T I O N A L :'   )
    # print("\n==========>\n")
    """ [+++] """
    ''' nirino 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        # print(           *[            i-abs(n) for n in range(  1-i, i  )  ],   sep = ''   ,  end=" "   )
        print(             *[            i-abs(n) for n in range( -i+1, i  )  ],   sep = ''   ,  end=" "   )
    print()

    # print("\n==========>\n")
    ''' iangagn 10 months ago    You can use the asterisk operator to unpack an iterable made up of concatenated lists 
    and remove the separator : '''
    for i in range(  1,  int( number )+1  ):
        print(   *(   list(range(   1 ,  i+1       ))
                    + list(range(  i-1,   0  , -1  ))   )  ,  sep=""  ,  end=" "    )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   *(   list(range(   1 ,  i+1       ))
                    + list(range(  i-1,   0  , -1  ))   )  ,  sep=None,  end="\t"   )
    print();''' 1	1 2 1	1 2 3 2 1	1 2 3 4 3 2 1	1 2 3 4 5 4 3 2 1	1 2 3 4 5 6 5 4 3 2 1	1 2 3 4 5 6 7 6 5 4 3 2 1	1 2 3 4 5 6 7 8 7 6 5 4 3 2 1	1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1	'''
    # print("\n==========>\n")
    ''' moth_atham 2 years ago    I tried this but it didn't work because of the separator (even though it gives the same answer) '''
    for i in range(  1,  int( number )+1  ):
        print(            *range(   1 ,  i+1       )
                        , *range(   1 ,   i        )[::-1] ,  sep=""  ,  end=" "    )
                      # , *range(  i-1,   0  , -1  )       ,  sep=""  ,  end=" "    ) # the same effect
    print()
    # print("\n==========>\n")
    ''' Tomash '''
    for i in range(  1,  int( number )+1  ):
        print(            *range(   1 ,   i        )
                        , *range(   i ,   0  , -1  )       ,  sep=""  ,  end=" "    )
    print()
    # print("\n==========>\n")
    ''' hossain_al_tomal 3 years ago ''' """ changed """
    for i in range(  1,  int( number )+1  ):
        print(            *range(   1 ,   i        )   ,   sep=""
                        , *range(   i ,   0  , -1  )   ,   end=" "    )
    print()
    for i in range(  1,  int( number )+1  ):
        print(            sep=""
                        , end=" "
                        , *range(   1 ,   i        )
                        , *range(   i ,   0  , -1  )                  )
    print()

    # print("\n==========>\n")
    ''' prayagdesai24 2 years ago    what can I do to remove blank spaces from each lines generated 
    from the following code?   The code works correctly but there are spaces between each numbers in each line '''
    for i in range(  1,  int( number )+2  ):
        # print( strip((   *range(   1 ,   i        )
        #                , *range(  i-2,   0  , -1  )   )) )
        ''' NameError: name 'strip' is not defined ''' #      ,  sep=""  ,  end=" "    )
    print()











    print(   ' S U M '   )
    # print("\n==========>\n")
    ''' mikuo0628 2 months ago    Mathematically: '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   (  10**(i) //9  )**2   ,   end=" "   )
    '''                           Pythonically:   '''
    for i in range(  1,  int( number )+1  ):
        print(    sum(    [   10**i  //9   *   10**j  for j in range(i)   ]   )   ,   end=" "    )
        # print(  sum(    [   10**i  //9   *   10**i  //9                 ]   )   ,   end=" "    )
    ''' 1 122 12333 1234444 123455555 12345666666 1234567777777 123456788888888 12345679000000000 '''

    print()
    ''' s_c_z 2 years ago    double for statement   lecz ciekawe i uczy czegoś '''
    for i in range(  1,  int( number )+1  ):
        print(   (sum(    [  10**j  for j in  range(0,i)  ]    )   )**2   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(    sum(    [  10**j  for j in  range(0,i)  ]    )    **2   ,   end=" "   ) # bez nawiasów też zadziała
    print()
    for i in range(  1,  int( number )+1  ):
        print(    sum(    [  10**j  for j in  range(0,i)  ]    )          ,   end=" "   )
    # print()
    # for i in range(  1,  int( number )+1  ):
    #     print(          [  10**j  for j in  range(0,i)  ]               ,   end=" "   )
    ''' [1] [1, 10] [1, 10, 100] [1, 10, 100, 1000] [1, 10, 100, 1000, 10000] [1, 10, 100, 1000, 10000, 100000] [1, 10, 100, 1000, 10000, 100000, 1000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]  '''
    # for i in range(  1,  int( number )+1  ):
    #     print(          (  10**j  for j in  range(0,i)  )               ,   end=" "   )
    ''' <generator object Demlo_numbers.<locals>.<genexpr> at 0x0000000002A52C00> '''
    print()
    ''' [++++] '''
    for i in range(  1,  int( number )+1  ):
        print(        list(  10**j  for j in  range(0,i)  )               ,   end=" "   )
    ''' [1] [1, 10] [1, 10, 100] [1, 10, 100, 1000] [1, 10, 100, 1000, 10000] [1, 10, 100, 1000, 10000, 100000] [1, 10, 100, 1000, 10000, 100000, 1000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000] [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000] '''
    for i in range(  1,  int(   22   )+1  ):
        print(    sum(    [  10**j  for j in  range(0,i)  ]    )    **2   ,   end=" "   )
    print('\n\t', sum(    [  10**j  for j in  range(0,23) ]    )    **2                 )
    ''' 12345679 01 2345679 01   234 5 432    0 98765432  0 987654321 '''
    print()
    # print("\n==========>\n")
    ''' GopalKrish23 2 years ago    Hi, '''
    for i in range(      int( number )    ):
        # print(  sum(      (10**j) for j in range(  int(i), -1, -1  )      )**2   ,   end=" "   )
        print(    sum(       10**j  for j in range(      i , -1, -1  )      )**2   ,   end=" "   ) # works the same
    print()
    # print("\n==========>\n")
    ''' pj_debarros 3 years ago    I don't understand what I am doing wrong here.    
    There are only two total lines (the for and the print). I don't think I used any string operations. '''
    for i in range(  1,  int( number )+1  ):
        print(    sum(    [  x * (10**y)  for (x,y) in zip(   list(         range(  1, i+1      ))
                                                            + list(reversed(range(  1,  i       )))
                                                            , list(reversed(range(  0, 2*i -1   )))   )  ]   )   ,   end=" "   )
    print()
    # for elem in                                         (   list(         range(  1, i+1      ))
    #                                                       + list(reversed(range(  1,  i       )))   ):
    #     print(   elem,   end='\t'   )
    # print();
    ''' 1	2	3	4	5	6	7	8	9	8	7	6	5	4	3	2	1	'''
    # for elem in                                             list(reversed(range(  0, 2*i -1   )))    :
    #     print(   elem,   end='\t'   )
    # print();
    ''' 16	15	14	13	12	11	10	9	8	7	6	5	4	3	2	1	0	'''



    # print("\n==========>\n")
    ''' lianzitong 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(  [   j*(  10**(  i+( i-j )-1  )  )
        # print( sum(  [   j*(  10**(  i+  i-j  -1  )  )                               # works the same ;)
                         + j*(  10**(  j-1  )          )   for j in range(1,i)   ]  )
               + i*(  10**(  i-1  )  )                                                ,   end=" "   )
    print()
    # print("\n==========>\n")
    ''' raghav_batta 3 months ago '''
    for i in range(  1,  int( number )+1  ):
        # print( sum(  [   j*( 10**(    j-1    ))  for j in range(   1 , i+1      )   ]
        print(   sum(  [   j*  10**(    j-1    )   for j in range(   1 ,  i       )   ]
        #            + [   k*( 10**( 2*i -1 -k ))  for k in range(  i-1,  0,  -1  )   ]   )   ,   end=" "   )
                     + [   k*  10**( 2*i -1 -k )   for k in range(   i ,  0,  -1  )   ]   )   ,   end=" "   )
    print()
    # print("\n==========>\n")





    print(   '\n S U M   M A P   sum(map(   lambda x:   ... )   )   + '   )
    # print("\n==========>\n")
    ''' adityaso 1 year ago    Highly irritating problem, but a good mental exercise. solution: '''
    for i in range(  1,  int( number )+1  ):
        print(   pow(   sum(map(   lambda x:  pow(10,x)  ,  range(i)   ))   ,2)   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(          sum(map(   lambda x:      10**x  ,  range(i)   ))**2      ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' tushar8998 10 months ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda n:   n*10**(       n -1  )
                                      + n*10**(  2*i -n -1  )
                          , range(1,i)                         ))
               +   i* 10**(i-1)                                        ,   end=" "   )
    print()

    # print("\n==========>\n")
    ''' agrigorcea 2 years ago '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda k:   k*pow(10, i-k)
                          , range(   1,  i+1     )       ))  *  pow(10, i-1)
               + sum(map(   lambda j:   j*pow(10, j-1)
                          , range(  i-1,  0, -1  )       ))                    ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda k:   10**(i-k) *k
                          , range(   1,  i+1     )       ))  *  10**(i-1)
               + sum(map(   lambda j:   10**(j-1) *j
                          , range(  i-1,  0, -1  )       ))                    ,   end=" "   )
    print()

    # print("\n==========>\n")
    """  I N T E R E S T I N G  =>  :->  """
    ''' a_idris 1 month ago    Here's some ugly horseshit that works. 
    It seems that the problem setter doesn't know the one about Einstein and the speed of light. '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(map(   lambda j:         j * 10**(       j -1 )    if  i==1  or  j==i
                                       else   j * 10**(       j -1 )
                                            + j * 10**( i +i -j -1 )
                          , range( 1, i+1 )                                                  ))   ,   end=" "   )
    print()

    # print("\n==========>\n")
    print(   '''\n sum(   F I L T E R (  lambda, range  )   )  '''   )
    ''' patrickvonglehn 5 months ago   Not as elegant as some other solutions, but here is my approach (python3): '''
    for i in range(  1,  int( number )+1  ):
        print(   sum(filter(   lambda y: y > 0,
                               map(   lambda x:           (i-x)  *  10**(i-(x+1))
                                                  +    (i-(x+1)) *  10**(i+x)     ,
                                      range(0,10))
                               ))   ,   end=" "   )
    # print()





    # print("\n==========>\n")
    ''' zhumorgan88 3 years ago    # i think this is easy to memory '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   reduce(   lambda x,y:   10*x+y,   range(1,i)  +  range(i,0,-1)   )   )
    ''' TypeError: unsupported operand type(s) for +: 'range' and 'range' '''


    # print("\n\n==========>\n==========>")
    ''' souravkundu27 3 years ago       why fail ?    '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   ''.join(map(   str,   range(1, i + 1)   +   range(i - 1, 0, -1)          ))    ,  end=" "   )
    ''' TypeError: unsupported operand type(s) for +: 'range' and 'range' '''
    ''' Zip może zadziała - na przyszłość '''

    # print("\n==========>\n")
    print("\n\n bin() BINARY: ")
    ''' RosieJunghwa 2 years ago    Used binary to make consecutive '1's.
        1 = bin(2 ** 1 - 1)		            1     =     1 ** 2
       11 = bin(2 ** 2 - 1)	               121    =    11 ** 2
      111 = bin(2 ** 3 - 1)	              12321   =   111 ** 2
     1111 = bin(2 ** 4 - 1)	             1234321  =  1111 ** 2
    11111 = bin(2 ** 5 - 1)	            123454321 = 11111 ** 2 '''
    ''' krishnansr_siva 2 months ago ''' ''' vikramlance 3 years ago ''' ''' gabrielle_992 1 week ago '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   bin(2**i-1)[2:]   )**2   ,   end=" "   )
    print()
    for i in range(  1,  int( number )+1  ):
        print(          bin(2**i-1)[2:]          ,   end=" "   )
    print() ;   '''   1    11    111    1111    11111    111111    1111111    11111111    111111111  '''

    # print("\n==========>\n")
    for i in range(  1,  int( number )+1  ):
        print(              2**i-1               ,   end=" "   ) # 1 3 7 15 31 63 127 255 511
    print()
    for i in range(  1,  int( number )+1  ):
        print(          bin(2**i-1)[ :]          ,   end=" "   )
    print() ;   ''' 0b1  0b11  0b111  0b1111  0b11111  0b111111  0b1111111  0b11111111  0b111111111  '''

    for i in range(  1,  int( number )+1  ):
        print(              2**i                 ,   end=" "   ) # 2 4 8 16 32 64 128 256 512
    print()
    for i in range(  1,  int( number )+1  ):
        print(          bin(2**i  )[ :]          ,   end=" "   )
    print() ;   ''' 0b10 0b100 0b1000 0b10000 0b100000 0b1000000 0b10000000 0b100000000 0b1000000000  '''

    for i in range(  1,  int( number )+1  ):
        print(              2**i-2               ,   end=" "   ) # 0 2 6 14 30 62 126 254 510
    print()
    for i in range(  1,  int( number )+1  ):
        print(          bin(2**i-2)[ :]          ,   end=" "   )
    print() ;   ''' 0b0  0b10  0b110  0b1110  0b11110  0b111110  0b1111110  0b11111110  0b111111110   '''

    for i in range(  1,  int( number )+1  ):
        print(              2**i-3               ,   end=" "   ) # -1 1 5 13 29 61 125 253 509
    print()
    for i in range(  1,  int( number )+1  ):
        print(          bin(2**i-3)[ :]          ,   end=" "   )
    print("\n");'''-0b1  0b1   0b101  0b1101  0b11101  0b111101  0b1111101  0b11111101  0b111111101   '''

    for i in range(20):
        print(       i     ,   end="\t\t"   )
    print("\n     "    ,   end=" "   )
    for i in range(20):
        print(   bin(i)    ,   end="\t"   )
    '''	0		1		2		3		4		5		6		7		8		9		10		11		12		13		14		15		16		17		18		19		
		0b0		0b1		0b10	0b11	0b100	0b101	0b110	0b111	0b1000	0b1001	0b1010	0b1011	0b1100	0b1101	0b1110	0b1111	0b10000	0b10001	0b10010	0b10011	'''

    print('\n                                                    ')
    # print('\n(   int(   bin(   (1 << i) - 1   )[2:]   )**2   ):')
    ''' trianman 2 years ago    Also works cause bin is not threated as a string function '''
    for i in range(  1,  int( number )+1  ):
        print(   int(   bin(   (1 << i) - 1   )[2:]   )**2,   end=" "   )
    """  x << y    Returns x with the bits shifted to the left by y places 
                  (and new bits on the right-hand-side are zeros).       This is the same as multiplying x by 2**y. """
    """ 12 << 2    48    Actual binary value of 12 is "00 1100"   when we execute the above statement Left shift  
        ( 2 places shifted left)        returns the value 48 its binary value is "11 0000".                         """





    print("\n")
    ''' za wiele linii, chyba printuje stringa... lecz po co - niepotrzebnie  '''
    ''' mr_boombastic 5 days ago '''
    n=1
    for i in range(  1,  int( number )+1  ):
        print(   f"{ n**2 }"   ,   end=" "   )
        n  =  n*10 + 1


    print("\n")
    ''' ctinterim 4 years ago    My stupid answer... but works! '''
    # for i in range(  1,  int( number )+1  ):
    #     print(   ( 12345678900000000//(10*(16-i+1)))   (10*(i-1))   +   (87654321%(10*(i-1)))   ,   end=" "   )
    #     ''' TypeError: 'int' object is not callable '''
    #     print(   ( 12345678900000000//(10*(16-i+1))) * (10*(i-1))   +   (87654321%(10*(i-1)))   ,   end=" "   )
    ''' ZeroDivisionError: integer division or modulo by zero '''
    print()



    # print("\n==========>\n")
    ''' Tomash '''
    for i in range(  1,  int( number )+1  ):
        if i == 1  :    print(   [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1][     i-1     ]    ,  end=" "   )
        else       :    print(   [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1][         : i ]
                               + [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1][-   i+1  :   ]    ,  end=" "   )
    ''' 1 [1, 2, 1] [1, 2, 3, 2, 1] [1, 2, 3, 4, 3, 2, 1] [1, 2, 3, 4, 5, 4, 3, 2, 1] [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1] [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1] [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1] [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1] '''
    print()
    # print("\n==========>\n")
    # for i in range(  1,  int( number )+1  ):
    #     j = 0
    #     while j < i :
    #         j =+ 1
    #         print(   [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1][         : j ]
    #                + [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1][-   j+1  :   ]    ,  end=" "   )
    # print()

    # print("\n==========>\n")
    ''' Tomash '''
        # string = i
        # for el in '987654321'[i-1: ]:
        # while el in reversed(i)  >  1 :
        #     i -= 1
        #     string.insert(el).append(el)
    for i in range(  1,  int( number )+1  ):
        j = i
        line_list = [j]     #;       print(   line_list   )
        while j > 1:        # while j != 1:
            # print(   line_list   )
            j -= 1
            line_list.append(      j  )
            line_list.insert(  0,  j  )
        print(   *line_list   ,   sep=''   ,   end=" "   )
    print()


    print("\n==========>\n")

    ''' Tomash 
        string = i 
        for el in '987654321'[i-1: ]:
        while el in reversed(i)  >  1 :
            i -= 1
            string.insert(el).append(el) '''
    ''' Tomash '''
    for el in '987654321': print(   f"'{el}',"   ,   end=" "   )
    ''' '9', '8', '7', '6', '5', '4', '3', '2', '1', '''
    full_listOfStrings_987654321 = [ '9', '8', '7', '6', '5', '4', '3', '2', '1' ]
    print()
    for el in '123456789': print(   f"'{el}',"   ,   end=" "   )
    ''' '1', '2', '3', '4', '5', '6', '7', '8', '9', '''
    full_listOfStrings_123456789 = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    print()

    print("\n==========>\n")
    for i in range(  1,  int( number )+1  ):
        line_tmp_str = ""

        line_tmp_str = "".join(   full_listOfStrings_123456789[i]   )
        for j in range(  i,  0,  -1  ):
            line_tmp_str = (     "".join(  full_listOfStrings_123456789[j]  )
                             +   "".join(  line_tmp_str                     )
                             +   "".join(  full_listOfStrings_123456789[j]  )      )
        print(line_tmp_str)
    print()


    def add_in_Front_recursively(  goal,  sliced,  slicer_starter   ):
        TODO


Demlo_numbers(9)

''' prathameshtatar 4 months ago
    when i == 3
1234321
ie
    (111000-111)//9
ie
    (((10^(i)-1)//9 x 10^i) - ((10^(i)-1)   //9 ) //9
ie
             (10^(i) -1) x (10^(i) -1)      //9   //9
ie
    general ((10^(i) -1)^2                  //9^2     )
code:
for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)                '''

''' vishwanatham 5 months ago
n=int(input()) for i in range(2,n+2): print((''.join(map(int,(list(range(1,i))+list(range(1,i-1)[::-1])))))) 
TypeError: sequence item 0: expected str instance, int found 
what is the problem i am not able to figure it out '''

''' mmcss 6 months ago   I found this challenge to be frustrating, but I got some practice using reduce(). 
Ironically, I had to revert to Python2. 
Python3 required me to add "from functools import reduce," which violated the "only two lines" constraint . 
I can't imagine a RW case where only arithmetic operations are allowed to solve a problem like this. '''