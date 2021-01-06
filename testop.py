import crcmod
from opendbc.can.packer import CANPacker


hyundai_checksum = crcmod.mkCrcFun(0x11D, initCrc=0xFD, rev=False, xorOut=0xdf)
dbc_name = 'hyundai_kia_generic'

packer = CANPacker(dbc_name)
values = {
  "CF_Spas_Stat": 5,
  "CF_Spas_TestMode": 0,
  "CR_Spas_StrAngCmd": 18.5,
  "CF_Spas_BeepAlarm": 0,
  "CF_Spas_Mode_Seq": 2,
  "CF_Spas_AliveCnt": 205,
  "CF_Spas_Chksum": 0,
  "CF_Spas_PasVol": 0
}
dat = packer.make_can_msg("SPAS11", 0, values)[2]
print(dat)
crc = hyundai_checksum(dat)

values["CF_Spas_Chksum"] = sum(dat[:6]) % 256

#dat = dat[:6]
cs6b = (sum(dat[:6]) % 256)
#cs7b = ((sum(dat[:6]) + dat[7]) % 256)

print(dat)
print(crc)
print(cs6b)
print(values["CF_Spas_Chksum"])

"""

BO_ 809 ACC: 8 XXX
    SG_ ACC_ACTIVE : 30|1@0+ (1,0) [0|1] "" XXX
    SG_ THROTTLE_POS_SENSE : 47|8@0+ (1,0) [0|255] "" XXX
    SG_ BRAKE_ACTIVE_DRIVER : 32|2@1+ (1,0) [0|3] "" XXX
    SG_ GAS_PEDAL_POSITION : 55|8@0+ (1,0) [0|255] "" XXX

BO_ 870 366_EMS: 8 EMS
    SG_ VS : 40|8@1+ (1,0) [0|255] "km/h" MDPS

BO_ 914 S_MDPS11: 8 XXX
    SG_ CR_Mdps_StrAng : 24|16@1- (1,0) [0|65535] "" XXX
    SG_ CF_Mdps_Stat : 0|4@1+ (1,0) [0|15] "" XXX
    SG_ CF_Mdps_AliveCnt : 47|8@0+ (1,0) [0|255] "" XXX
    SG_ CF_Mdps_Chksum : 63|8@0+ (1,0) [0|255] "" XXX
    SG_ CR_Mdps_DrvTq : 8|12@1+ (1,0) [0|15] "" XXX

"""
