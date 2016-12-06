"""
///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.        //
//                           oscar.riveros@peqnp.com                         //
//                                                                           //
//    without any restriction, Oscar Riveros reserved rights, patents and    //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
"""

# http://www.sfu.ca/~ssurjano/shubert.html

import math


def shubert3D(a, b, c):
    A = sum([i * math.cos((i + 1) * a + i) for i in range(1, 5 + 1)])
    B = sum([i * math.cos((i + 1) * b + i) for i in range(1, 5 + 1)])
    C = sum([i * math.cos((i + 1) * c + i) for i in range(1, 5 + 1)])
    return A * B * C


def shubert4D(a, b, c, d):
    A = sum([i * math.cos((i + 1) * a + i) for i in range(1, 5 + 1)])
    B = sum([i * math.cos((i + 1) * b + i) for i in range(1, 5 + 1)])
    C = sum([i * math.cos((i + 1) * c + i) for i in range(1, 5 + 1)])
    D = sum([i * math.cos((i + 1) * d + i) for i in range(1, 5 + 1)])
    return A * B * C * D


def shubertND(xx):
    from operator import mul
    from functools import reduce
    return reduce(mul, [sum([i * math.cos((i + 1) * x + i) for i in range(1, 5 + 1)]) for x in xx])


if __name__ == '__main__':
    print(shubert3D(-1.421147908477072, -0.78039983023680781, -0.88836581242904256))
    print(shubertND([-1.421147908477072, -0.78039983023680781, -0.88836581242904256]))
    print(shubert4D(3.7373135646577724, 5.4901983164977732, 5.4717277747047222, -0.75216047020846366))
    print(shubertND([3.7373135646577724, 5.4901983164977732, 5.4717277747047222, -0.75216047020846366]))
    print(shubertND([-6.3126570443303089, 15.317522747245699, -4.5911555683817058, 30.46217702719618, 6.2547143986253193, 8.3888749104648053, 45.586964863240958, -3.6435057184276616, -21.99883939703599, -10.767469472368763, 22.938090589528183, 30.801179157208793, -32.456504668826454, 16.923566846903523, 21.947309198125794, 7.2970487033859417, -10.366528436660479, 0.34157914962592306, 23.639240752023113, 8.6352003848510481, -6.0020408589788419, -22.484435508144252, -0.68466461704944948, -22.485901091770302, 30.904468209118527, -2.0846742276174011, 43.453931405535911, -6.290926541149422, 3.6381564745657631, -5.3405289354580319, 4.4893795687997509, -4.261454625137338, -2.6925516769844244, -7.7343242496991014, 21.098545590072707, -3.5249993119979948, 26.93244704826353, -28.724746191298347, 2.754652135166769, 13.037843409093263, -15.571815577758942, 4.2087810893103033, -1.1105404046355092, 10.553142727810854, -9.052831028569944, 19.872639184088946, 11.313565297210356, 9.4447167185273209, 2.6440410747811072, 2.9820629023472245, 20.547338556133063, 10.336211228758707, -1.5259794571976684, -4.4567790963772804, -2.095257305765859, 3.8683473706988574, 0.73577151349607839, -9.4935088433486818, 32.188026958117533, 4.3957939885194337, 30.594152435792715, -7.1018146602138561, 14.95851068010411, 7.9829502203781306, -13.044341646516781, -10.954409263310984, -31.268269562736329, 18.75180721268265, 43.979230033925539, 29.882739108626897, 3.4661167032667919, -17.785155341039818, -5.9274971849139568, -10.989575683431113, -10.569812861442351, 21.938799362676249, -4.4087607691002875, -13.450219944280734, -1.2636474790202274, -9.7666957917149251, -11.818521417683359, -32.32144218417605, 11.456198390771309, 5.1133732937680234, -10.494546773257404, -21.278465190128696, -16.089173598641548, -23.312481777075007, 3.9432051323978099, 12.742732391075494, -0.59836405414966665, -19.41531878941381, -9.0635923268751952, 5.7592572558975137, 15.539938044766281, 10.236277878557093, -33.980887837435667, -17.73140595048406, 30.179425571157253, -1.3961337190493557]))
