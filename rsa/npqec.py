#!/usr/bin/env python3
# coding:utf-8
#power by jedi

import gmpy2
import binascii

n = 966808932627497190635859236054960349099463975227350564265384373280336699853387254070662881265937565163000758606154308757944030571837175048514574473061401566330836334647176655282619268592560172726526643074499534129878217409046045533656897050117438496357231575999185527675071002803951800635220029015932007465117818739948903750200830856115668691007706836952244842719419452946259275251773298338162389930518838272704908887016474007051397194588396039111216708866214614779627566959335170676055025850932631053641576566165694121420546081043285806783239296799795655191121966377590175780618944910532816988143056757054052679968538901460893571204904394975714081055455240523895653305315517745729334114549756695334171142876080477105070409544777981602152762154610738540163796164295222810243309051503090866674634440359226192530724635477051576515179864461174911975667162597286769079380660782647952944808596310476973939156187472076952935728249061137481887589103973591082872988641958270285169650803792395556363304056290077801453980822097583574309682935697260204862756923865556397686696854239564541407185709940107806536773160263764483443859425726953142964148216209968437587044617613518058779287167853349364533716458676066734216877566181514607693882375533
# p 和 q通过在线网站http://factordb.com/index.php分解
p = gmpy2.mpz(31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928797450473)
q = gmpy2.mpz(31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928997877221)
e = gmpy2.mpz(65537)
phi_n = (p-1)*(q-1)
d = gmpy2.invert(e, phi_n)
c = gmpy2.mpz(168502910088858295634315070244377409556567637139736308082186369003227771936407321783557795624279162162305200436446903976385948677897665466290852769877562167487142385308027341639816401055081820497002018908896202860342391029082581621987305533097386652183849657065952062433988387640990383623264405525144003500286531262674315900537001845043225363148359766771033899680111076181672797077410584747509581932045540801777738548872747597899965366950827505529432483779821158152928899947837196391555666165486441878183288008753561108995715961920472927844877569855940505148843530998878113722830427807926679324241141182238903567682042410145345551889442158895157875798990903715105782682083886461661307063583447696168828687126956147955886493383805513557604179029050981678755054945607866353195793654108403939242723861651919152369923904002966873994811826391080318146260416978499377182540684409790357257490816203138499369634490897553227763563553981246891677613446390134477832143175248992161641698011195968792105201847976082322786623390242470226740685822218140263182024226228692159380557661591633072091945077334191987860262448385123599459647228562137369178069072804498049463136233856337817385977990145571042231795332995523988174895432819872832170029690848)

m = pow(c, d, n)
print("十进制:\n%s"%m)
m_hex = hex(m)[2:]
print("十六进制:\n%s"%(m_hex,))
#print("ascII:\n%s"%((binascii.b2a_hex(hex(m)[2:])).decode('hex'),))
print("ascii:\n%s"%(binascii.a2b_hex(m_hex).decode("utf8"),))
