# File: chaos.py
#A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x= eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()


#In the original chaos program with a value of '3.9' the output values
#were varied within the range of 0 and 1. The outputs of the altered
#chaos program where the value was changed to '2.0' were much more close
#in value, most only varying by hundredths.

#This program illustrates a chaotic function
#Enter a number between 0 and 1: .7
#How many numbers should I print? 100
#0.8190000000000001
#0.5781320999999998
#0.9511919623034011
#0.18106067129594453
#0.5782830479626452
#0.951099881166545
#0.18138469912496308
#0.5790887311884079
#0.9506053931361303
#0.1831236407388703
#0.5833985544715047
#0.9478742563370475
#0.1926937369910931
#0.6066951567904522
#0.9306029597180973
#0.2518662552198574
#0.7348756143353938
#0.7598504385832282
#0.7116632233156054
#0.8002748515930279
#0.6233565526530618
#0.9156543275784544
#0.30120277186468125
#0.8208706821342847
#0.5734638208520474
#0.9539519614006914
#0.17131770528781426
#0.5536750016566543
#0.9637640773689169
#0.13619923411441334
#0.45883111069013616
#0.9683899779566695
#0.11938223134402765
#0.41000744531505995
#0.9434152263949845
#0.20819345430422997
#0.6429108655674997
#0.8953482895607173
#0.3654289467715193
#0.904373463368612
#0.33728019828076783
#0.8717368379009698
#0.43606572105481367
#0.9590583911054604
#0.1531350348670979
#0.5057703142570674
#0.9748701435461612
#0.09554355239694821
#0.3370184297700473
#0.871404330284978
#0.43702941143771123
#0.9595353494068638
#0.15142632431749523
#0.5011359312226331
#0.974994967675004
#0.09508114466534527
#0.33555881031844453
#0.8695404710308472
#0.44241537705416834
#0.962067643680727
#0.14232462138702895
#0.4760664617828645
#0.9727660244187948
#0.10331991600546539
#0.36131515275214693
#0.8999894012609746
#0.3510330676276595
#0.8884545269323407
#0.38650201397250833
#0.9247610079540427
#0.2713545358752761
#0.7711128817672394
#0.6883414408254652
#0.8366572565043723
#0.5329813774075022
#0.9707576921027853
#0.11071006177163091
#0.38396804157719505
#0.9224926800358169
#0.2788497477329962
#0.7842610070967383
#0.6598631513929576
#0.8753307140241781
#0.4255947349293926
#0.9534090404661133
#0.17323894389203387
#0.5585861276237057
#0.9616138960352295
#0.14395918284998765
#0.48061625244029077
#0.9735346542891116
#0.1004832316304372
#0.3525067719870103
#0.890158415992202
#0.38132800067877776
#0.9200761306507048
#0.2867905733843747
#0.7977127875687214
#0.6293316748604392
#0.9097659397233953