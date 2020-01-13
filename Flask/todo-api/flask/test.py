def updateVehicleYawRollRate():
    input_value = 4000
    canData = []

    canData.append(int('0xE1',16))

    # NOTE: Multiplier below (10) does not match latest CAN msg version in VNSM, but this is what StarFire team wants for UltimateData.
    # This equates to 0.1 mile/bit, instead of 0.2 km/bit

    rtkRoverRelativeDistance = int('0xFF', 16)
    vehicleYawRate = hex(input_value)

    if 0 < input_value < 256:
        vehicleYawRateByte1 = int(vehicleYawRate[2:], 16) # append 00 
        vehicleYawRateByte2 = int('0', 16)
    elif 255 < input_value < 4096:
        vehicleYawRateByte1 = int(vehicleYawRate[3:], 16) # append 00
        vehicleYawRateByte2 = int(vehicleYawRate[2:3], 16) # 7d
    elif input_value > 4095:
        vehicleYawRateByte1 = int(vehicleYawRate[4:], 16) # 01
        vehicleYawRateByte2 = int(vehicleYawRate[2:4], 16) # 7d

    # if rtkRoverRelativeDistance <= 25:
    #     rtkRoverRelativeDistance = rtkRoverRelativeDistance * 10
    # else:
    #     rtkRoverRelativeDistance = 255

    # Bytes 2-6 & 8: Don't care
    canData += [0x00, 0x00, 0x00, vehicleYawRateByte1, vehicleYawRateByte2, rtkRoverRelativeDistance, 0x00]
    print(canData)

    # self.canDataArrays['VehicleRollYawRate']['DataArray'] = canData

updateVehicleYawRollRate()