# SolarEdge performance data parameters

# event data interpretation
#
#   timeStamp = devData[0]
#   Type = devData[1] # 0 or 1
#   timeStamp = devData[2] # event start time
#   timeStamp = devData[3] # event end time (Type == 0) or tzOffset (Type == 1)
#   timeStamp = devData[4] # 0 (Type == 0) or event end time (Type == 1)
#   data5 = devData[5] # 0
#   data6 = devData[6] # 0

# format string used to unpack input data
eventInFmt = "<LLLlLLL"
# length of data that will be unpacked
eventInFmtLen = (len(eventInFmt)-1)*4
# mapping of input data to device data items
eventIdx = [0,1,2,3,4]
# device data item names
eventItems = ["Date", "Time", "ID", "Type", "Event1", "Event2", "Event3"]

# inverter data interpretation
#
#   timeStamp = devData[0]
#   Uptime = devData[1] # uptime (secs) ?
#   Interval = devData[2] # time in last interval (secs) ?
#   Temp = devData[3] # temperature (C)
#   Eday = devData[4] # energy produced today (Wh)
#   Eac = devData[5] # energy produced in last interval (Wh)
#   Vac = devData[6] # AC volts
#   Iac = devData[7] # AC current
#   freq = devData[8] # frequency (Hz)
#   data9 = devData[9] # 0xff7fffff
#   data10 = devData[10] # 0xff7fffff
#   Vdc = devData[11] # DC volts
#   data12 = devData[12] # 0xff7fffff
#   Etot = devData[13] # total energy produced (Wh)
#   data14 = devData[14] # ?
#   data15 = devData[15] # 0xff7fffff
#   data16 = devData[16] # 0.0
#   data17 = devData[17] # 0.0
#   Pmax = devData[18] # max power (W) = 5000
#   data19 = devData[19] # 0.0
#   data20 = devData[20] # ?
#   data21 = devData[21] # 0xff7fffff
#   data22 = devData[22] # 0xff7fffff
#   Pac = devData[23] # AC power (W)
#   data24 = devData[24] # ?
#   data25 = devData[25] # 0xff7fffff
    
# format string used to unpack input data
invInFmt = "<LLLffffffLLfLffLfffffLLffL"
# length of data that will be unpacked
invInFmtLen = (len(invInFmt)-1)*4
# mapping of input data to device data items
invIdx = [0,1,2,3,4,5,6,7,8,11,13,18,23]
# device data item names
invItems = ["Date", "Time", "ID", "Uptime", "Interval", "Temp",
            "Eday", "Eac", "Vac", "Iac", "Freq", "Vdc",
            "Etot", "Pmax", "Pac"]
# device data output file format strings
invOutFmt = ["%s", "%s", "%s", "%d", "%d", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f"]


# 3 phase inverter data interpretation
#
#   timeStamp = devData[0]
#   Uptime = devData[1] # uptime (secs) (confirmed)
#   Interval = devData[2] # time in last interval (secs) (confirmed)
#   Temp = devData[3] # temperature (C) (confirmed)
#   Eday = devData[4] # energy produced today (Wh) (probably right)
#   Eac = devData[5] # energy produced in last interval (Wh) (probably right)
#   Vac1 = devData[6] # AC volts (confirmed)
#   Vac2 = devData[7] # AC volts (confirmed)
#   Vac3 = devData[8] # AC volts (confirmed)
#   Iac1 = devData[9] # AC current (confirmed)
#   Iac2 = devData[10] # AC current (confirmed)
#   Iac3 = devData[11] # AC current (confirmed)
#   freq1 = devData[12] # frequency (Hz) (confirmed)
#   freq2 = devData[13] # frequency (Hz) (confirmed)
#   freq3 = devData[14] # frequency (Hz) (confirmed)
#   data15 = devData[15] # 0xff7fffff
#   data16 = devData[16] # 0xff7fffff
#   Vdc = devData[17] # DC volts (confirmed)
#   data18 = devData[18] # 0xff7fffff
#   Etot = devData[19] # total energy produced (Wh) (confirmed)
#   data20 = devData[20] # ?
#   data21 = devData[21] # 0xff7fffff
#   data22 = devData[22] # 0.0
#   data23 = devData[23] # 0.0
#   Pmax = devData[24] # max power (W) = 5000 (wrong, always shows 1)
#   data25 = devData[25] # 0.0
#   data26 = devData[26] # ?
#   data27 = devData[27] # 0xff7fffff
#   data28 = devData[28] # 0xff7fffff
#   Pac = devData[29] # AC power (W) (wrong, always 100 or 0)
#   data30 = devData[30] # ?
#   data31 = devData[31] # 0xff7fffff
    
# format string used to unpack input data
inv3PhInFmt = "<LLLffffffffffffLLfLffLfffffLLffL"
# length of data that will be unpacked
inv3PhInFmtLen = (len(inv3PhInFmt)-1)*4
# mapping of input data to device data items
#inv3PhIdx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,19,24,29]
inv3PhIdx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
# device data item names
inv3PhItems = ["Date", "Time", "ID", "Uptime", "Interval", "Temp",
	"Eday", "Eac", "Vac1", "Vac2", "Vac3", "Iac1",
   "Iac2", "Iac3", "Freq1", "Freq2", "Freq3", "data15", "data16", "Vdc", "data18",
   "Etot", "data20", "data21", "data22", "data23", "Pmax", "data25", "data26", "data27", "data28", "Pac", "data30", "data31"]
# device data output file format strings
#inv3PhOutFmt = ["%s", "%s", "%s", "%d", "%d", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f"]
inv3PhOutFmt = ["%s", "%s", "%s", "%d", "%d", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%f", "%d", "%d", "%f", "%d", "%f", "%f", "%d", "%f", "%f", "%f", "%f", "%f", "%d", "%d", "%f", "%f", "%d"]

# optimizer data interpretation
#
#   timeStamp = devData[0]
#   inverter = devData[1] & 0xff7fffff
#   Uptime = devData[3] # uptime (secs) ?
#   Vmod = devData[4] # module voltage
#   Vopt = devData[5] # optimizer voltage
#   Imod = devData[6] # module current
#   Eday = devData[7] # energy produced today (Wh)
#   Temp = devData[8] # temperature (C)

# format string used to unpack input data
optInFmt = "<LLLLfffff"
# length of data that will be unpacked
optInFmtLen = (len(optInFmt)-1)*4
# mapping of input data to device data items
optIdx = [0,1,3,4,5,6,7,8]
# device data item names
optItems = ["Date", "Time", "ID", "Inverter", "Uptime",
            "Vmod", "Vopt", "Imod", "Eday", "Temp"]
# device data output file format strings
optOutFmt = ["%s", "%s", "%s", "%s", "%d", "%f", "%f", "%f", "%f", "%f"]

# Decode optimiser data in packet type 0x0080
#  (into same order as original data)
#
# Byte index (in reverse order):
# 
# 0c 0b 0a 09 08 07 06 05 04 03 02 01 00
# Tt Ee ee Cc cO o# pp Uu uu Dd dd dd dd 
#  # = oo|Pp
#
#  Temp, 8bit (1.6 degC)  Signed?, 1.6 is best guess at factor
#  Energy in day, 16bit (1/4 Wh)
#  Current (panel), 12 bit (1/160 Amp)
#  voltage Output, 10 bit (1/8 v)
#  voltage Panel, 10 bit (1/8 v)
#  Uptime of optimiser, 16 bit (secs)
#  DateTime, 32 bit (secs)
#

