import pymem
import pymem.process

dwEntityList = 0x4E051DC
dwGlowObjectManager = 0x535FCB8
m_iGlowIndex = 0x10488
m_iTeamNum = 0xF4


def main():

    print("glow aktif")

    oyun = pymem.Pymem("csgo.exe")

    sunucu = pymem.process.module_from_name(oyun.process_handle, "client.dll").lpBaseOfDll    

    while True:
        glow = oyun.read_int(sunucu + dwGlowObjectManager)
        for i in range(1, 32):  
            entity = oyun.read_int(sunucu + dwEntityList + i * 0x10)
            if entity:
                entity_team_id = oyun.read_int(entity + m_iTeamNum)
                entity_glow = oyun.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2:  
                    oyun.write_float(glow + entity_glow * 0x38 + 0x8, float(1))   
                    oyun.write_float(glow + entity_glow * 0x38 + 0xC, float(0))   
                    oyun.write_float(glow + entity_glow * 0x38 + 0x10, float(0))  
                    oyun.write_float(glow + entity_glow * 0x38 + 0x14, float(1))  
                    oyun.write_int(glow + entity_glow * 0x38 + 0x28, 1)           
                elif entity_team_id == 3:  
                    oyun.write_float(glow + entity_glow * 0x38 + 0x8, float(0))  
                    oyun.write_float(glow + entity_glow * 0x38 + 0xC, float(0))   
                    oyun.write_float(glow + entity_glow * 0x38 + 0x10, float(1)) 
                    oyun.write_float(glow + entity_glow * 0x38 + 0x14, float(1)) 
                    oyun.write_int(glow + entity_glow * 0x38 + 0x28, 1)          

if __name__ == '__main__':
    main() 
